import datetime
import csv
import selenium.webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from prettytable import from_csv


start = datetime.datetime.strptime("25-06-2021", "%d-%m-%Y")
end = datetime.datetime.strptime("25-07-2021", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    trDate=date.strftime("%d/%m/%Y")
    origin = "BOM" 
    destin = "DEL" 
# trDate = '25/02/2021'


    baseDataUrl = "https://www.makemytrip.com/flight/search?itinerary="+ origin +"-"+ destin +"-"+ trDate +"&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng"



# https://www.makemytrip.com/flight/search?itinerary=BOM-DEL-24/02/2021                                   &tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng
    try:
        driver = selenium.webdriver.Firefox(executable_path='C:\Program Files\Google\Drive/geckodriver.exe')
    
        print ("Requesting URL: " + baseDataUrl)

        driver.get(baseDataUrl)  
        print ("Webpage found ...")

        element_xpath = '//*[@id="left-side--wrapper "]'

        element = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

        print ("Scrolling document upto bottom ...")
        for j in range(1, 100):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    
        body = driver.find_element_by_tag_name("body").get_attribute("innerHTML")
    
        print("Closing Chrome ...") 
        driver.quit() 

        print("Getting data from DOM ...")
        soupBody = BeautifulSoup(body) 

    
        spanFlightName = soupBody.findAll("span", {"class": "airways-name"}) 
        pDeptCity = soupBody.findAll("p", {"class": "dept-city"}) 
        pFlightCode = soupBody.findAll("p", {"class": "fli-code"})
        divDeptTime = soupBody.findAll("div", {"class": "dept-time"})
        pFlightDuration = soupBody.findAll("p", {"class": "fli-duration"})
        pArrivalTime = soupBody.findAll("p", {"class": "reaching-time append_bottom3"}) 
        pArrivalCity = soupBody.findAll("p", {"class": "arrival-city"})
        spanFlightCost = soupBody.findAll("span", {"class": "actual-price"})



        flightsData = [["flight_name", "flight_code", "departure_time", "departure_city", "flight_duration", "arrival_time", "arrival_city", "flight_cost"]]


        for j in range(0, len(spanFlightName)):
                flightsData.append([spanFlightName[j].text, pFlightCode[j].text, divDeptTime[j].text, pDeptCity[j].text  , pFlightDuration[j].text, pArrivalTime[j].text, pArrivalCity[j].text , spanFlightCost[j].text])

    
    

        outputFile = "FlightsData_11" + origin +"-"+ destin +"-"+ trDate.split("/")[0] + "-" + trDate.split("/")[1] + "-" + trDate.split("/")[2] +  ".csv"
        print(outputFile)
        print("Writing flight data to file: "+ outputFile + " ...")
        with open(outputFile, 'w', encoding="utf-8") as spfile:
            csv_writer = csv.writer(spfile)
            csv_writer.writerows(flightsData)
            print ("Data Extracted and Saved to File. ")
   
#     path = 'C:/Users/Intel/FlightsData_1BOM-DEL-23-02-2021.csv'
#     c = open(path)
#     x = from_csv(c)
#     print(x)    

    except Exception as e:
        print (str(e))


