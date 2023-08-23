import psycopg2


def updateTable(publisherId, establishedYear):
	try:
		connection = psycopg2.connect(user="postgres",
									password="postgres",
									host="localhost",
									port="5432",
									database="pythonpostgres")

		cursor = connection.cursor()
		# Update single record now
		sql_update_query = """Update publisher set \
		publisher_estd = %s where publisher_id = %s"""
		cursor.execute(sql_update_query,
					(establishedYear,
						publisherId))
		connection.commit()
		count = cursor.rowcount
		print(count, "Record Updated successfully ")

	except (Exception, psycopg2.Error) as error:
		print("Error in update operation", error)

	finally:
		# closing database connection.
		if connection:
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")


# call the update function
publisherId = 3
establishedYear = 2000
updateTable(publisherId, establishedYear)
