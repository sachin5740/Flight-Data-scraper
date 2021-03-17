import csv
import datetime
import time
import selenium.webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from prettytable import from_csv

#-----------------------------------------------------------------------------------------------
start = datetime.datetime.strptime("26-02-2021", "%d-%m-%Y")
end = datetime.datetime.strptime("26-03-2021", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

trDate_list=[]
for date in date_generated:
    trDate_list.append(date.strftime("%d/%m/%Y"))

for date in trDate_list:
    trDate=date
    trDate_list.pop(0)
#-------------------------------------------------------------------------------------------------
#SCROLL_PAUSE_TIME=1
    #trDate="25/02/2021"
    origin = "BOM" 
    destin = "DEL" 



    baseDataUrl = "https://www.makemytrip.com/flight/search?itinerary="+ origin +"-"+ destin +"-"+ trDate +"&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng"

    try:
        #driver = selenium.webdriver.Firefox(executable_path='C:\Program Files\Google\Drive/geckodriver.exe')
        driver = selenium.webdriver.Chrome()
        #executable_path='C:\Program Files\Google\Drive/geckodriver.exe'
    
        print ("Requesting URL: " + baseDataUrl)

        driver.get(baseDataUrl)  
        print ("Webpage found ...")


#----------------------------------------------------------------------------------------   
        SCROLL_PAUSE_TIME = 1

# Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
    # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        #sleep for 5 second
        driver.implicitly_wait(10)
    #----------------------------------------------------------------------------------------
    
    
        body = driver.find_element_by_tag_name("body").get_attribute("innerHTML")

        print("Closing Chrome ...") 
        driver.quit()

        # Getting data from DOM ...
        soupBody = BeautifulSoup(body,"html.parser")

        spanFlightName = soupBody.findAll("span",class_="airways-name") 
        pDeptCity = soupBody.findAll("p", class_= "dept-city") 
        pFlightCode = soupBody.findAll("p", class_= "fli-code")
        divDeptTime = soupBody.findAll("div", class_= "dept-time")
        pFlightDuration = soupBody.findAll("p", class_= "fli-duration")
        pArrivalTime = soupBody.findAll("p", class_= "reaching-time append_bottom3") 
        pArrivalCity = soupBody.findAll("p", class_= "arrival-city")
        spanFlightCost = soupBody.findAll("span", class_= "actual-price")
        print(spanFlightName)
        print(pDeptCity)
        #infinite loop for missing data
        if spanFlightName==[]:
                trDate_list.append(trDate)

        else:

#-----------------------------------------------------------------------------------------------------------
                flightsData = [["flight_name", "flight_code", "departure_time", "departure_city", "flight_duration", "arrival_time", "arrival_city", "flight_cost"]]


                for j in range(0, len(spanFlightName)):
                        flightsData.append([spanFlightName[j].text, pFlightCode[j].text, divDeptTime[j].text, pDeptCity[j].text  , pFlightDuration[j].text, pArrivalTime[j].text, pArrivalCity[j].text , spanFlightCost[j].text])

    
    

                outputFile = "FlightsData_1" + origin +"-"+ destin +"-"+ trDate.split("/")[0] + "-" + trDate.split("/")[1] + "-" + trDate.split("/")[2] +  ".csv"
                print(outputFile)
                print("Writing flight data to file: "+ outputFile + " ...")
                with open(outputFile, 'w', encoding="utf-8") as spfile:
                        csv_writer = csv.writer(spfile)
                        csv_writer.writerows(flightsData)
                        print ("Data Extracted and Saved to File. ")
   
                        path = 'C:\\Users\\kapil\\OneDrive\\Desktop\\Test-code\\FlightsData_1BOM-DEL-26-02-2021.csv'
                        c = open(path)
                        x = from_csv(c)
                        print(x)    


        #that is used for a hard reset in the webpage  ----F5
        #driver.execute_script("location.reload()")
        # program sleep for 20 second 

#-----------------------------------------------------------------------------------------------------------
    except Exception as e:
            print (str(e))