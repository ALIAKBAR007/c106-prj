from calendar import week
import csv
import numpy as np

file=open("cups of coffee vs hours of sleep.csv")
data=csv.reader(file)
file_data=list(data)

file_data.pop(0)

weeksList=[]
CupsList=[]

for i in range(len(file_data)):
    weeks=file_data[i][0]
    Cups=file_data[i][1]

    weeksList.append(float(weeks))
    CupsList.append(float(Cups))
coeffiect=np.corrcoef(weeksList, CupsList)
print(coeffiect[0,1])    