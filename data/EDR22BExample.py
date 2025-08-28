import json
import matplotlib.pyplot as plt

# Load the JSON data
with open("grasshopperboardapp-locations.json", "r") as f:  # update filename if needed
    data = json.load(f)

# Extract latitudes and longitudes
lats = [gym["latitude"] for gym in data["gyms"]]
lons = [gym["longitude"] for gym in data["gyms"]]
names = [gym["name"] for gym in data["gyms"]]  # optional, for labels

# Create scatter plot
plt.figure(figsize=(8,6))
plt.scatter(lons, lats, c="blue", marker="o")

# Add labels for each point
for lon, lat, name in zip(lons, lats, names):
    plt.text(lon, lat, name, fontsize=8, ha="right")

# Axis labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Gym Locations (Lat vs Long)")

plt.show()
