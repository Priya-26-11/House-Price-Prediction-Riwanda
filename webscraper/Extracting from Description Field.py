import pandas as pd
import numpy as np
import re

df = pd.read_csv("PropertyPricesGeocoded.csv")
keywordsFile = pd.read_csv("Keywords.csv")

#Create numpy arrays for the rows we need to clean, as they are easier to deal with
Descriptions = np.asarray(df["Description"])
keywords = np.asarray(keywordsFile["keyword"])
types = np.asarray(keywordsFile["type"])
addTo = np.asarray(keywordsFile["addTo"])
beforeAfter =  np.asarray(keywordsFile["after"])

#Create an empty array that can be added on to the data frame
l = [None]*df.shape[0]


#Create an empty array for matched districts that can be filled in later
bedrooms = np.asarray(l)
bathrooms = np.asarray(l)
apartment = np.asarray(l)
waterTank = np.asarray(l)


i = 0 #Description index
j = 0 #Keyword index

for description in Descriptions:

    for keyword in keywords:

        x = re.search(keyword,str(Descriptions[i]))

        if (x is not None):

            if types[j] == "num":

                #print(beforeAfter[j])

                if (addTo[j] == "bedrooms"):

                    bedrooms[i] = None

                    #If traditionally written after in whetever language

                    if (beforeAfter[j] == True):
                    
                        ind = str(Descriptions[i]).index(keyword)
                        entry = (str(Descriptions[i])[ind + len(str(keyword)) :ind + len(str(keyword)) + 4])
                        #print(entry)
                        if (re.search("\d",entry) is not None):
                            
                            entry = int(re.sub("\D","",entry))
                        else:

                            entry = None

                        bedrooms[i] = entry

                    #If number traditionally comes before in the language (ie english)
                    else:

                                            
                        ind = str(Descriptions[i]).index(keyword)
                        entry = (str(Descriptions[i])[ind - 6 :ind + 8])
                        
                        if (re.search("\d",entry) is not None):

                            entry = int(re.sub("\D","",entry))
                            #print(entry)

                        else:

                            entry = None

                        if (entry == ""):
                            entry = None

                        bedrooms[i] = entry
                        #print(entry)


        if (j != len(keywords) - 1):
            j += 1

    i += 1
    j = 0

i = 0


for description in Descriptions:

    for keyword in keywords:

        x = re.search(keyword,str(Descriptions[i]))

        if (x is not None):

            if types[j] == "num":

                #print(beforeAfter[j])

                if (addTo[j] == "bathrooms"):

                    bathrooms[i] = None

                    #If traditionally written after in whetever language

                    if (beforeAfter[j] == True):
                    
                        ind = str(Descriptions[i]).index(keyword)
                        entry = (str(Descriptions[i])[ind + len(str(keyword)) :ind + len(str(keyword)) + 4])
                        #print(entry)
                        if (re.search("\d",entry) is not None):
                            
                            entry = int(re.sub("\D","",entry))
                        else:

                            entry = None

                        bathrooms[i] = entry

                    #If number traditionally comes before in the language (ie english)
                    else:

                                            
                        ind = str(Descriptions[i]).index(keyword)
                        entry = (str(Descriptions[i])[ind - 6 :ind + 8])
                        
                        if (re.search("\d",entry) is not None):

                            entry = int(re.sub("\D","",entry))
                            #print(entry)

                        else:

                            entry = None

                        if (entry == ""):
                            entry = None

                        bathrooms[i] = entry
                        #print(entry)


        if (j != len(keywords) - 1):
            j += 1

    i += 1
    j = 0


i = 0

for description in Descriptions:

    for keyword in keywords:

        if (addTo[j] == "apartment"):
            x = re.search(keyword,str(description))
            print(x)

        if (x is not None):

            if (addTo[j] == "apartment"):
                
                apartment[i] = True
                print("Found Apartment")
        elif apartment[i] is not True:

            apartment[i] = False     
                    

    
        if (j != len(keywords) - 1):
            j += 1

    j = 0

    i += 1



i = 0


for description in Descriptions:

    for keyword in keywords:

        if (addTo[j] == "water tank"):
            x = re.search(keyword,str(description))

        if (x is not None):

            if (addTo[j] == "water tank"):
                
                waterTank[i] = True

        elif waterTank[i] is not True:

            waterTank[i] = False     
                    

    
        if (j != len(keywords) - 1):
            j += 1

    j = 0

    i += 1



i = 0
#print(bedrooms)
df.insert(10,"Bedrooms", bedrooms)
df.insert(11, "Bathrooms", bathrooms)
df.insert(12, "Apartment", apartment)
df.insert(13, "WaterTank", waterTank)
df.to_csv("Description_Extracted.csv")
