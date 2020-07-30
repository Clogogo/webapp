import folium
import jupyter

cor = [80, -100]

maps = folium.Map(location=cor, zoom_start=8, tiles='Stamen Terrain')

maps.add_child(folium.LatLngPopup())

cor1 = [[60, -147], [34.2, -87.1]]
fg = folium.FeatureGroup(name="My map")

for coordinates in cor1:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi i am marker", icon=folium.Icon(color='blue')))

maps.add_child(fg)
maps.save("map1.html")
print("map created")
