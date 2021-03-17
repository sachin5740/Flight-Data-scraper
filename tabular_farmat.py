# import pandas as pd

# data=pd.read_csv("FlightsData_1BOM-DEL-10-03-2021.csv")
# print(data.to_sql())

import pandas as pd
from glob import glob

path=r'C:\Users\kapil\OneDrive\Desktop\Test-code' 
filesname = glob (path + "/*.csv")
print(filesname)

files = [filesname]
#print(files)
concat_files = pd.DataFrame()
#print(concat_files)

for file_path in files:
    for path_of_file in file_path:
        #print(type(path_of_file[-14:-4]))
        
        df = pd.read_csv(path_of_file)
        #print(df)
        # concat_files = pd.concat()
        df.set_index('flight_name', inplace=True)
        #total indexs
        index = df.index
        # Declare a list that is to be converted into a column 
        date_of_flight = [path_of_file[-14:-4] for i in range(len(index)) ]
        # print(date_of_flight)
        df['Date_of_flight'] = date_of_flight
        concat_files = concat_files.append(df)
    concat_files.to_csv('combined_csv_data.csv')
    print(concat_files)
