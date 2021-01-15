#
# Python Ver:   3.9
#
# Author:       Jaimie Bertoli
#
# Purpose:      Create a database and add new data into that database.


import sqlite3

# creating a databas, giving it a name, and a variable 
conn = sqlite3.connect('pythonDatabase.db')


#Createing a table in the database we just created
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_findFile( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_info TEXT \
        )")
    conn.commit()
# close the connection once setting up the table 
conn.close()


fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')



# looping through each object in the tuple to find files that end with .txt and placing in db
conn = sqlite3.connect('pythonDatabase.db')

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # printing the name of the files that end with .txt
            cur.execute("INSERT INTO tbl_findFile (col_info) VALUES (?)", (x,))
            print(x)
conn.close()
            

