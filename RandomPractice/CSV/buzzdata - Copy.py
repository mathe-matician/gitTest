import csv
from datetime import datetime
from pprint import pprint

with open("buzzers.csv") as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().title().split(",")
        flights[k] = v

pprint(flights)
