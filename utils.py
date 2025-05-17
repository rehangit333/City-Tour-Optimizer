import csv
from collections import namedtuple

Place = namedtuple("Place", ["name", "lat", "lon"])

def read_places(filename):
    places = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            places.append(Place(row['Name'], float(row['Lat']), float(row['Lon'])))
    return places

def find_place_index(places, name):
    for i, place in enumerate(places):
        if place.name.lower() == name.lower():
            return i
    raise ValueError(f"Place '{name}' not found in CSV.")
