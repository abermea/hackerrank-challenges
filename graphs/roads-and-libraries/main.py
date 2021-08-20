#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return c_lib * n

    graph = generateGraph(cities)
    
    clusters, traversed = findClusters(graph)
    orphans = 0

    if len(traversed) < n:
        orphans = n - len(traversed)
    
    cluster_roads = list(map(lambda x: (len(x) - 1) * c_road, clusters))
    
    return sum(cluster_roads) + ((len(cluster_roads) + orphans) * c_lib)

def generateGraph(cities):
    graph = dict()
    
    for city in cities:
        graph[city[0]] = graph.get(city[0], []) + [city[1]]
        graph[city[1]] = graph.get(city[1], []) + [city[0]]
    
    return graph

def findClusters(graph):
    traversed = set()
    clusters = []

    for city in graph:
        if city not in traversed:
            cluster = findCluster(graph, city, set())
            traversed.update(cluster)
            clusters = clusters + [cluster]
    
    return clusters, traversed

def findCluster(graph, node, cluster):
    if node not in cluster:
        paths = graph[node]
        cluster.add(node)
        for city in paths:
            cluster = findCluster(graph, city, cluster)
    return cluster

