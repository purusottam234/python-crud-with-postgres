import psycopg2

try:
	connection = psycopg2.connect(user="postgres",
								password="postgres",
								host="localhost",
								port="5432",
								database="pythonpostgres")
	cursor = connection.cursor()
	postgreSQL_select_Query = "select * from publisher"

	cursor.execute(postgreSQL_select_Query)
	print("Selecting rows from publisher table using cursor.fetchall")
	publisher_records = cursor.fetchall()

	print("Print each row and it's columns values")
	for row in publisher_records:
		print("publisher_Id = ", row[0], )
		print("publisher_name = ", row[1])
		print("publisher_estd = ", row[2])
		print("publisher_location = ", row[3])
		print("publisher_type = ", row[4], "\n")
except (Exception, psycopg2.Error) as error:
	print("Error while fetching data from PostgreSQL", error)

finally:
	# closing database connection.
	if connection:
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")
