# trDate_list = ['24','02','2021']

# for i in range(1,31):
#     if (trDate_list[0] <= "30"):
#         trDate_list[0]=str(int(trDate_list[0])+1)
#         print(trDate_list)
#     else:
#         if(trDate_list[1]=="12"):
#             trDate_list[2]=str(int(trDate_list[2])+1)
#             trDate_list[0]="01"
#             trDate_list[1]="01"
#         else:
#             trDate_list[0]="01"
#             trDate_list[1]=str(int(trDate_list[1])+1)
#         print(trDate_list)
# trDate=f"{trDate_list[0]}/+{trDate_list[1]}/{trDate_list[2]}"
# print(trDate)

import datetime
count=0
start = datetime.datetime.strptime("21-06-2021", "%d-%m-%Y")
end = datetime.datetime.strptime("21-07-2021", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    print (date.strftime("%d/%m/%Y"))
    count+=1
print(count)