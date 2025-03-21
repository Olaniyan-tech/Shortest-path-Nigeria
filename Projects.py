import heapq

class Country:

    def __init__(self):
        self.adj_list = {}
        self.country = {}

    def add_time(self, country1, country2, time):
        if country1 not in self.adj_list:
            self.adj_list[country1] = []
        if country2 not in self.adj_list:
            self.adj_list[country2] = []

        self.adj_list[country1].append((country2, time))
        self.adj_list[country2].append((country1, time))

    def add_country(self, index, country):
        self.country[index] = country
        self.adj_list[index] = []

    def get_country(self, data):
        for country, country_data in self.country.items():
            if country_data == data:
                return country
        return None

    def shortest_distance(self, start_data):
        start = self.get_country(start_data)

        if start is None:
            print("Invalid start country")
            return None, None

        distances = {country : float('inf') for country in self.adj_list}
        predecessors = {country : None for country in self.adj_list}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_country = heapq.heappop(pq)

            for neighbour, weight in self.adj_list[current_country]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    predecessors[neighbour] = current_country
                    heapq.heappush(pq, (new_distance, neighbour))

        return distances, predecessors

    def get_path(self, predecessors, end_country):
        path = []
        while end_country is not None:
            path.append(self.country[end_country])
            end_country = predecessors[end_country]

        path.reverse()
        return ' -> '.join(path)


my_country = Country()

my_country.add_country(0, 'Germany')
my_country.add_country(1, 'Nigeria')
my_country.add_country(2, 'England')
my_country.add_country(3, 'Dubai')
my_country.add_country(4, 'France')
my_country.add_country(5, 'Spain')
my_country.add_country(6, 'USA')

my_country.add_time(2, 0, 2)
my_country.add_time(3, 4, 10)
my_country.add_time(1, 4, 8)
my_country.add_time(4, 0, 2)
my_country.add_time(2, 5, 3)
my_country.add_time(5, 0, 3)
my_country.add_time(5, 1, 7)
my_country.add_time(6, 5, 10)

print("Shortest distance from 'Nigeria' to other countries: ")
distances, predecessors = my_country.shortest_distance('Nigeria')

start = my_country.get_country('Nigeria')

if start is None:
    print("Invalid start country")

else:
    for country_index in my_country.adj_list:
        if country_index == start:
            continue
        path = my_country.get_path(predecessors, country_index)
        print(f"Shortest distance to {my_country.country[country_index]} : {path}, Distance : {distances[country_index]}")

