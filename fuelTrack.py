__author__ = "Muser Tomas"

import sqlite3


conn = sqlite3.connect('fuelTrack.db')

c = conn.cursor()

# c.execute("""CREATE TABLE fuelTracktb (
#             entryID INT KEY VALUE AUTOINCREMENT,
#             entryDate INT,
#             qtyOfLiters INT,
#             fuelType TEXT,
#             fuelCostLiter INT,
#             fuelCostTotal INT,
#             priceDiscount INT,
#             gasStation INT
#                 )
#                 """)


# c.execute("INSERT INTO fuelTracktb VALUES (5, 06, 5, 'SUPER', 54, 500, 0, 2)")

c.execute("SELECT * FROM fuelTracktb")
print(c.fetchall())


conn.commit()
conn.close

