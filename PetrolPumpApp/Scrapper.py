import pyodbc
from random import randint
from pprint import pprint
from bs4 import BeautifulSoup
from datetime import datetime
import requests
#----- Data Base connection------
print("************** Petrol Price Retrieve Script ********** \n")
print("Petrolium : Database Connection started")
conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-ASHUTOS\SQLEXPRESS2017;''Database=PetrolPump;''Trusted_Connection=yes;',autocommit=True)
cursor = conn.cursor()
print("Petrolium : Database Connected -True")

#------- Start Page Loading-----"https://economictimes.indiatimes.com/wealth/fuel-price/petrol"
try:
    data=[]
    print("Petrolium : Page Loading.....")
    page = requests.get("https://economictimes.indiatimes.com/wealth/fuel-price/petrol")
    print("Petrolium : Page Loaded successfully : "+str(page.status_code)+"\n")
    soup = BeautifulSoup(page.content, 'html.parser')
    tables=soup.find_all('table')
    for row in tables:
        
        for j in row.find_all('tr'):
            datadict={}
            datalist=j.find_all('td')
            if(len(datalist)!=0):
                datadict["City"]=datalist[0].text
                datadict["Price"]=datalist[1].text
                datadict["Change"]=datalist[2].text
            data.append(datadict)
    print(data)
    cursor.execute("truncate table PetrolPumpApp_petrollist")
    print('start')
    if(int(cursor.rowcount)==0):
        for drow in data:
            cityname=""
            price=""
            changes=""
            for dkey,dval in drow.items():
                if(dkey=="City"):
                    cityname=dval;
                elif(dkey=="Price"):
                    price=dval;
                elif(dkey=="Change"):
                    changes=dval;
                else:
                    pass
            #cursor.execute("Update PetrolPumpApp_petrollist set Changes='"+changes+"',Price='"+price+"',City='"+cityname+"',UpdatedOn=GetDate(),FuelType=1 where City='"+cityname+"'")
            cursor.execute("Insert into PetrolPumpApp_petrollist(Changes,City,Price,FuelType,UpdatedOn) Values ('"+changes+"','"+cityname+"','"+price+"','1',GetDate())")
            print(cityname)
    cursor.execute("select * from PetrolPumpApp_petrollist")
    print(cursor.rowcount)
    cursor.close()
    print("Data Updated On : "+str(datetime.now())) 
except Exception as ex:
    print(ex)
    cursor.close()
