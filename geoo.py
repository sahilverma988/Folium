import folium

# Create a base map centered around India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Sample coordinates (replace with your own)
coordinates = [(28.6139, 77.2090),  # Delhi
               (12.9716, 77.5946),  # Bangalore
               (18.5204, 73.8567),(14.2798, 74.8796),(26.7654, 79.6789)]  # Pune

# Add markers for each coordinate
for coord in coordinates:
    folium.Marker(location=coord, popup=str(coord)).add_to(india_map)

# Save the map to an HTML file
india_map.save("india_map.html")