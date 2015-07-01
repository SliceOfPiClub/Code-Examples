# ==========================================
# dbinsert.py
#
# insert a number of records into a SQLite3 database
# the records will be stored in the Temperature table
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 29-June-2015
# ==========================================
#
import sqlite3 as lite
import sys

try:
	#
	# create a connection to the database
	#
	con = lite.connect('TemperatureReadings.db')

	#
	# create a cursor to all data to be fetched from the database
	#
	cur = con.cursor()
	
	#
	# Execute the insert command a number of times
	#
	cur.execute("INSERT INTO Temperature VALUES(null, '28-99983873','30-06-2015 19:20:00',25.000)")
	cur.execute("INSERT INTO Temperature VALUES(null, '28-99983873','30-06-2015 19:21:00',25.500)")
	cur.execute("INSERT INTO Temperature VALUES(null, '28-99983873','30-06-2015 19:22:00',26.000)")
	cur.execute("INSERT INTO Temperature VALUES(null, '28-99983873','30-06-2015 19:23:00',26.250)")
	cur.execute("INSERT INTO Temperature VALUES(null, '28-99983873','30-06-2015 19:24:00',26.500)")

	#
	# print the id of the last record inserted
	#
	lid = cur.lastrowid
	print "The last Id of the inserted row is %d" % lid
	#
	# committhe data to the database
	#
	con.commit()

except lite.DatabaseError, e:
	#
	# the program only comes here if an error occurs
	# display the error and quit
	#
	print "error %s:" % e.args[0]
	sys.exit(1)

finally:
	#
	# always come here, even if an error does or doesn't occur
	#
	# if the connection exists, close it	
	#
	if con:
		con.close()

