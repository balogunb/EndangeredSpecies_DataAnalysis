#!/usr/bin/python

# Database login details
hostname = 'localhost'
username = 'balogunb'
password = ''
database = 'balogunb'
port     = '5432'




# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute( "SELECT family, Abundance FROM flora_fauna" )
    for family, Abundance  in cur.fetchall() :
        print (family, Abundance)




#Gets all unique categories and call splitDataByCategory on each of them
def getCategories(conn):
	cur = conn.cursor()
	cur.execute( "SELECT DISTINCT category FROM flora_fauna")
	data = cur.fetchall()
	print(len(data))

	for category in data:
		cat = ''.join(category)
		splitDataByCategory(conn,cat)


#Creates a csv file based on the category name and populates it with cleaned data
def splitDataByCategory(conn, categoryName):
	name = "Categories/" +categoryName.replace("/", "_").replace(' ','_') + ".csv"
	file = open(name, "w")
	file.writelines(["abundance,","acres,","state,","latitude,","longitude\n"])
	cur = conn.cursor()
	cur.execute("SELECT flora_fauna.category, flora_fauna.abundance, parks.acres, parks.state, parks.latitude, parks.longitude FROM flora_fauna INNER JOIN parks ON flora_fauna.park_name = parks.name and flora_fauna.occurrence = 'Present' and flora_fauna.abundance != '' and flora_fauna.abundance != 'Unknown'")
	


	list = ['Rare', 'Uncommon','Occasional','Common','Abundant']
	for  category, abundance,  acres, state, latitude, longitude in cur.fetchall():
		if(category == categoryName):

			abundanceVal = list.index(abundance) + 1
			st = str(abundanceVal) + ","  +str(acres) + "," + state.replace(',',' ') + ","+str(latitude) + "," +str(longitude) + "\n"
			file.write(st)
	file.close()




import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, port = port, dbname=database )



#---------- Queries ----------#
getCategories(myConnection)
myConnection.close()
