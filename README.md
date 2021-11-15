# CS7CS4-Machine-Learning-Group-53

## To run webscraper:

1. Run the scrapeProperties.py file. Change the pagesToScrape variable to whatever amount of pages you want. More will take longer.

2. Run CleanScrapedDataset.py. This will clean some variables, such as the price, by parsing out text. It will also use the disctrictsInKigali.csv to check against the description field and create a location variable.

3. Run GeocodeProperties.py. This will use geopy and Nominatim to provide the coordinates of the properties based on the scraped location data.

4. Finally, run "Extracting from Description Field.py". This will extract the remaining variables from the description field, such as number of bedrooms and bathrooms.

Following this, some manual cleaning might be needed, but the dataset should be around 95% ready.
  
