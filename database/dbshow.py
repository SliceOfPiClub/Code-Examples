# ==========================================
# dbshow.py
#
# display the records in a SQLite3 database
# from the table Temperature
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 29-June-2015
# ==========================================
#
Import sqlite3 as lite
Import sys

Try:
	#
	# create a connection to the database
	#
	con = lite.connect(‘TemperatureReaddings.db’)

	#
	# create a cursor to all data to be fetched from the database
	#
	cur = con.cusrsor()
	
	#
	# Execute the select command 
	#
	cur.execute(‘Select * from Temperature’);

	#
	# Fetch all the records from the Temperature table
	#
	rows= cur.fetchall()

	#
	# loop through each record and print it
	#
	for row in rows:
        	print "%s %s %s %s" % (row["Id"], row["Device"], row["Date"], row["Value"])


except lite.Error,e
	#
	# the program only comes here if an error occurs
	# display the error and quit
	#
	print "error %s:",% e.args[0]
	sys.exit(1)

finally:
	#
	# always come here, even if an error does or doesn't occur
	#
	# if the connection exists, close it	
	#
	if con:
		con.close()

