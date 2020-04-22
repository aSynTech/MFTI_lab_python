import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'DESKTOP-5CMRJE6\SERV' 
database = 'Shak' 
username = 'test' 
password = '123' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

cursor.execute("insert into [Shak].[dbo].[DICES]  select 10,10,10") 
cnxn.commit()
row = cursor.fetchone()

# while row: 
    # print 'Inserted Product key is ' + str(row[0]) 
    # row = cursor.fetchone()