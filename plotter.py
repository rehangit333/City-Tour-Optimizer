import matplotlib.pyplot as plt

def plot_route(places, path, title="Optimal TSP Path"):
    # Extract coordinates from places
    coords = [(places[i].lon, places[i].lat) for i in path]

    # Unzip the coordinates for plotting
    lon, lat = zip(*coords)

    # Create a scatter plot of the cities
    plt.figure(figsize=(10, 6))
    plt.scatter(lon, lat, c='blue', label='Cities', s=100)

    # Plot the route with arrows
    for i in range(len(path) - 1):
        plt.annotate('', xy=(lon[i+1], lat[i+1]), xytext=(lon[i], lat[i]),
                     arrowprops=dict(facecolor='red', edgecolor='black', arrowstyle='->', lw=2))

    # Annotate the city names
    for i, place in enumerate(path):
        plt.text(lon[i] + 0.01, lat[i] + 0.01, places[place].name, fontsize=9, ha='left')

    # Plot settings
    plt.title(title)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.legend()
    plt.show()
