from geopy.distance import geodesic

def haversine_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def build_distance_matrix(places):
    n = len(places)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                coord1 = (places[i].lat, places[i].lon)
                coord2 = (places[j].lat, places[j].lon)
                dist_matrix[i][j] = haversine_distance(coord1, coord2)
    return dist_matrix
