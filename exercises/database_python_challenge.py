
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.6
#
# Author:       Jaimie Bertoli
#
# Purpose:      Create a database table in RAM named Roster that includes the fields ‘Name’, ‘Species’ and ‘IQ’
# manipulate code with sql syntax




import sqlite3
connection = sqlite3.connect(':memory:')
c = connection.cursor()


c.execute("CREATE TABLE IF NOT EXISTS Roster( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Name TEXT, \
        Species TEXT, \
        IQ INT \
        )")



c.execute("INSERT INTO Roster(Name, Species, IQ) VALUES (?, ?, ?)", ('Jean-Baptiste Zorg', 'Human', '122'))

c.execute("INSERT INTO Roster(Name, Species, IQ) VALUES (?, ?, ?)", ('Korben Dallas', 'Meat Popsicle', '100'))

c.execute("INSERT INTO Roster(Name, Species, IQ) VALUES (?, ?, ?)", ('Aknot', 'Mangalore', '-5'))


c.execute("UPDATE Roster SET Species='Human' WHERE Species='Meat Popsicle'")


"""# This is a query to display the entire Roster table
c.execute("SELECT * from Roster")
for row in c.fetchall():
    print(row)"""


#This is a query to display the names and IQs of everyone in the table who is classified as Human
c.execute("SELECT Name, IQ from Roster WHERE Species = 'Human'")
for row in c.fetchall():
    print(row)
