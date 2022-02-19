import csv
import numpy as np

file=open("Student Marks vs Days Present.csv")
data=csv.reader(file)
file_data=list(data)

file_data.pop(0)

RollList=[]
PersentageList=[]

for i in range(len(file_data)):
    Roll=file_data[i][0]
    Persentage=file_data[i][1]

    RollList.append(float(Roll))
    PersentageList.append(float(Persentage))
coeffiect=np.corrcoef(RollList, PersentageList)
print(coeffiect[0,1])    