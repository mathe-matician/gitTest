import csv
from datetime import datetime
from pprint import pprint

def convert2ampm(time: str):
    return datetime.strptime(time, "%H:%M").strftime("%I:%M%p")

with open("buzzers.csv") as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().title().split(",")
        flights[k] = v

pprint(flights)

flights2 = {}

for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint(flights2)
