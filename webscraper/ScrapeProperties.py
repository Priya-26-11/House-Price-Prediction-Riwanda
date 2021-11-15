from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

#chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-gpu")

#chrome_options.add_argument("--headless")

webdriver = "C:/Users/Matt Murtagh/Google Drive/ODI/Projects/Web Scraping/chromedriver"

driver = Chrome(webdriver,port=8082, options=chrome_options)

pagesToScrape = 2000
startPage = 127600


Links = []
Prices = []
Locations = []
Descriptions = []
Rows = []

for i in range(startPage, (startPage - pagesToScrape), -1):
    
    
    pageNumber = str(i)
 
    url = ("https://www.imali.biz/announce-24-" + pageNumber + ".html")
    driver.get(url)
    print(i)
    
    try:
    
        driver.get(url)

        print(url)

        price = driver.find_element_by_class_name("Price").text

        Prices.append(price)

        location = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[1]/div[2]/ul/li[1]").text

        Locations.append(location)
        
        description = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[1]/div[6]").text
    
        Descriptions.append(description)
        
        date = driver.find_element_by_class_name("Posted_date").text
        
        title = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[1]/span[2]/span[1]").text
        
        
        
    except:
        continue
        
    print(location)
    
    print(price)
    
    print(description)
    
    Rows.append((title,price,location,description, date))
  
    #time.sleep(30)
    
    
    
#Links = list(dict.fromkeys(Links)) 
df = pd.DataFrame(Rows,columns=['Title','Price','Location','Description', 'Date'])
df.to_csv('PropertyPrices.csv')