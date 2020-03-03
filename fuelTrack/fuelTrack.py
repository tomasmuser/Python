__author__ = "Muser Tomas"

import sqlite3
import datetime as dt

conn = sqlite3.connect('fuelTrack.db')
c = conn.cursor()

c.execute("""CREATE TABLE fuelTracktb (
            entryID INTEGER PRIMARY KEY,
            entryDate INTEGER,
            qtyOfLiters REAL,
            fuelType TEXT,
            fuelCostLiter REAL,
            fuelCostTotal REAL
                )""")

            #TODO Two tables for stations and type of "Fuel"
            # gasStation INT FOREING KEY
            # fuelType INT FOREING KEY

def dataCall():
    # SampleData

    entryDate = timeGet()
    qtyOfLiters = 5.6
    fuelType = 'Infinia'
    fuelCostLiter = 68.54
    fuelCostTotal = round(qtyOfLiters * fuelCostLiter, 2)
    return entryDate, qtyOfLiters, fuelType, fuelCostLiter, fuelCostTotal


def timeGet(timeZone=None):
    #TODO get timeZone from somewhere
    currentFullTime = dt.datetime.now(timeZone).strftime('%Y%m%d%H%M%S')
    return currentFullTime
     
def insertData():
    data = dataCall()
    sql = "INSERT INTO fuelTracktb(entryDate, qtyOfLiters, fuelType, fuelCostLiter, fuelCostTotal) VALUES(?, ?, ?, ?, ?)"

    c = conn.cursor()
    c.execute(sql, data)

insertData()
c.execute("SELECT * FROM fuelTracktb")
print(c.fetchall())

conn.commit()
conn.close
