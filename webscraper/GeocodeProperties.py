import pandas as pd
import numpy as np
import re
import geopy
from geopy.geocoders import Nominatim
import time


df = pd.read_csv("PropertyPricesCleaned.csv")

MatchedDistrictsNump = np.asarray(df["MatchedDistricts"])

Lat = [None]*df.shape[0]
Lon = [None]*df.shape[0]



for i in range(0,MatchedDistrictsNump.size):
    
    if isinstance(MatchedDistrictsNump[i], str):
    
        MatchedDistrictsNump[i] = str(MatchedDistrictsNump[i] + ", Rwanda")
        #print(MatchedDistrictsNump[i])
        
    else:
        continue
        
    while True:
        try:
            locator = Nominatim(user_agent = "Rwanda Property Geo")
            print(MatchedDistrictsNump[i])
            location = locator.geocode(MatchedDistrictsNump[i])
            #time.sleep(10)
            break
        except Exception: # Try to catch something more specific
            
            #time.sleep(10)
            pass
    
    
    
    
        
    if location is not None: 
        
        Lat[i] = location.latitude
        Lon[i] = location.longitude
        
        
        
    print(Lat[i])
    print(Lon[i])    

    

    
    


#print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

df.insert(7,"Lat", Lat)
df.insert(8,"Lon", Lon)
df.to_csv('PropertyPricesGeocoded.csv')