import pandas as pd
import numpy as np
import re

df = pd.read_csv("PropertyPrices.csv")
Districts = pd.read_csv("Districts in Kigali.csv")

#Remove any price observations that are simply down as "negotiable"
#Mark them as missing values

df[["Price"]] = df[["Price"]].replace("NEGOTIABLE", np.NaN)

#Create numpy arrays for the rows we need to clean, as they are easier to deal with

PricesNump = np.asarray(df["Price"])
LocationNump = np.asarray(df["Location"])
Districts = np.asarray(Districts["Districts"])
Descriptions = np.asarray(df["Description"])

#Create an empty array that can be added on to the data frame

l = [None]*df.shape[0]

#Create an empty array for matched districts that can be filled in later

MatchedDistricts = np.asarray(l)

i = 0

for price in PricesNump:
    
    x = re.search("\$",str(PricesNump[i]))
    
    if (x is not None):
        PricesNump[i] = np.NaN
    
    PricesNump[i] = re.sub("RWF| ","", str(PricesNump[i]))
    #print(PricesNump[i])
    PricesNump[i] = float(str(PricesNump[i]))
    i += 1
    
#print(PricesNump)
#print(np.asarray(prices))

i = 0

for location in LocationNump:
      
    LocationNump[i] = re.sub("CITY: |KIGALI| |\d\dM","", str(LocationNump[i]))
    
    
    for District in Districts:
        x = re.search(District,str(LocationNump[i]))
        MatchedDistricts[i] = None
        
        if x is not None:
            MatchedDistricts[i] = District
            break
    
    i += 1
    




i = 0

for description in Descriptions:
    
    #Check to see if the district is in any of the locations that were not specified previously
    
    if MatchedDistricts[i] is None:
        
        #print(description)
        
        for District in Districts:
            
            x = re.search(District,str(description),flags=re.IGNORECASE)
        
            if x is not None:      
                print(i)
                MatchedDistricts[i] = District
                
    i += 1              


df.insert(3,"MatchedDistricts", MatchedDistricts)
print(np.asarray(df["MatchedDistricts"]))
df.to_csv('PropertyPricesCleaned.csv')



