# City-Tour Optimizer

A Python-based project to solve the Travelling Salesman Problem (TSP) for city landmarks using real-world geolocation data from a CSV file. The tool computes the shortest possible tour that visits all locations and optionally returns to the start.

## Features

- Parses CSV files containing places with latitude and longitude
- Computes geodesic distance using the Haversine formula
- Implements greedy TSP algorithm and optional 2-opt improvement
- Exports route in GeoJSON format for visualization on Google Maps
- Optional Matplotlib scatter-plot of the tour
- Command-line interface for flexible usage

## Project Structure

```

.
├── distance.py
├── tsp\_solver.py
├── geojson\_exporter.py
├── utils.py
├── plotter.py
├── tsp.py
├── places.csv
├── requirements.txt
└── tests/
└── test\_distance.py

```

## Usage

### 1. Prepare your CSV file

Example `places.csv`:

```

Name,Lat,Lon
Eiffel Tower,48.8584,2.2945
Louvre Museum,48.8606,2.3376
Notre-Dame,48.8530,2.3499
Arc de Triomphe,48.8738,2.2950

````

### 2. Run the program

```bash
python tsp.py --csv places.csv --start "Eiffel Tower" --return
````

* `--csv`: Path to the CSV file with places
* `--start`: Name of the starting place
* `--return`: Optional flag to return to the starting point

### 3. Output

* Prints ordered tour and total distance in kilometers
* Exports `route.geojson` for drag-and-drop into Google Maps
* Displays a scatter plot of the tour with arrows

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Testing

Run unit tests using:

```bash
pytest -q
```

## License

This project is for educational purposes.

```

