import argparse
from distance import build_distance_matrix
from tsp_solver import greedy_tsp, total_path_length
from geojson_exporter import export_geojson
from utils import read_places, find_place_index
from plotter import plot_route

def main():
    parser = argparse.ArgumentParser(description="TSP City Tour Optimizer")
    parser.add_argument("--csv", required=True, help="Path to CSV file")
    parser.add_argument("--start", required=True, help="Starting location name")
    parser.add_argument("--return-to-start", action="store_true", help="Return to starting point")
    args = parser.parse_args()

    try:
        places = read_places(args.csv)
        start_index = find_place_index(places, args.start)
        dist_matrix = build_distance_matrix(places)

        path = greedy_tsp(dist_matrix, start_index)
        if not args.return_to_start:
            path.pop()

        print("\nOptimal tour:")
        for i in path:
            print(f"- {places[i].name}")
        distance = total_path_length(path, dist_matrix)
        print(f"\nTotal distance: {distance:.2f} km")

        export_geojson(path, places)
        print("Route written to route.geojson")
        plot_route(places, path)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
