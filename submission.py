import csv
from queue import PriorityQueue
import os.path
from os import path


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


class FileNotFoundError(Exception):
    def __init__(self, data):
        print("%s does not exist" % data)


# Implement this function to read data into an appropriate data structure.
def build_graph(path):
    dict = {}
    with open(path) as f:
        next(f)
        for line in f.read().splitlines():
            city1, city2, distance = line.split(',')

            if not city1 in dict:
                dict[city1] = {}
            dict[city1][city2] = int(distance)

            if not city2 in dict:
                dict[city2] = {}
            dict[city2][city1] = int(distance)

    return dict


# Implement this function to perform uniform cost search on the graph.
def uniform_cost_search(graph, start, end):
    visited = []

    queue = PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()
        node_name = node[1][-1]
        node_distance = node[0]

        if node_name == end:
            # print(node_distance)
            print("Path : " + str(node[1]) + " ; Cost : " + str(node_distance))
            exit()

        visited.append(node_name)

        for each in graph[node_name]:
            if each not in visited:
                distance = node_distance + graph[node_name][each]
                queue.put((distance, node[1] + [each]))


def take_start_city():
    start = input("Please enter start city : ")
    while True:
        try:
            if start not in graph:
                raise CityNotFoundError(start)
            break
        except CityNotFoundError:
            start = input("Please enter valid city!")
    return start


def take_end_city():
    end = input("Please enter end city : ")
    while True:
        try:
            if end not in graph:
                raise CityNotFoundError(end)
            break
        except CityNotFoundError:
            end = input("Please enter valid city!")
    return end


def take_data():
    data = input("Please enter data path : ")
    while True:
        try:
            if not (path.isfile(data)):
                raise FileNotFoundError(data)
            break
        except FileNotFoundError:
            data = input("Please enter valid file path! : ")
    return data


# Implement main to call functions with appropriate try-except blocks
if __name__ == "__main__":
    # take_data()
    graph = build_graph(take_data())
    uniform_cost_search(graph, take_start_city(), take_end_city())
