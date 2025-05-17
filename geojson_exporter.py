import json

def export_geojson(path, places, filename='route.geojson'):
    coords = [[places[i].lon, places[i].lat] for i in path]
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": coords
                },
                "properties": {
                    "name": "TSP Route"
                }
            }
        ]
    }
    with open(filename, 'w') as f:
        json.dump(geojson, f, indent=4)
