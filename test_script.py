#packages
import osmnx as ox
import folium

# import the data for high tension power lines in Finistère with osmnx. 
# the data comes from openstreetmap APIs, and is stored in a GeoDataFrame named 'power'. Each row is a power line segment.
# It is open source and contribution-based hence the sparse network.
power = ox.features_from_place("Quimper, France", tags={"power": "line"})

#create the openstreetmap leaflet centered on [LOCATION]. the object is an html map
m = folium.Map(location=[48.0, -2.9], #currently somewhere around Pontivy
               zoom_start=9,
               tiles="CartoDB Positron") 

# draw the power lines contained in GeoDF 'power' onto the map 'm'.
power.explore(m=m)

#save 'm' in an html file
m.save("lignes.html")