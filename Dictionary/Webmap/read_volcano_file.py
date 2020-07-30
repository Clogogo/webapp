import pandas as pd
import folium

maps = folium.Map(zoom_start=5, tiles='Stamen Terrain')

data = pd.read_csv(open("original.txt"))
print(data)

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "red"
    else:
        return "orange"


fgv = folium.FeatureGroup(name="Volcanoes")
for nm, lt, ln, el in zip(name, lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, fill=True, popup=nm + " " + str(el),
                                      fill_color=color_producer(el), color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(open("/Users/Lucky/PycharmProjects/Udemy/venv/Dictionary/Webmap_with_Folium/world.json",
                                  "r", encoding='utf-8-sig').read(), style_function=lambda x: {"fillColor": "green"
if x['properties']
   ['POP2005']
   < 10000000 else "orange" if 100000000 <= x["properties"]["POP2005"] < 2000000 else "red"}))

maps.add_child(fgv)
maps.add_child(fgp)
maps.add_child(folium.LayerControl())

maps.save("map1.html")
