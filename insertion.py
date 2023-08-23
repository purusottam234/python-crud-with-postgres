import psycopg2
 
 
try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pythonpostgres")
    cursor = connection.cursor()
 
    postgres_insert_query = """ INSERT INTO publisher(publisher_id,
    publisher_name, publisher_estd, publsiher_location, publsiher_type)
    VALUES (%s,%s,%s,%s,%s)"""
    record_to_insert = [(1, 'Packt', 1950,
                         'chennai', 'books'),
                        (2, 'Springer', 1950,
                         'chennai', 'books'),
                        (3, 'Springer', 1950,
                         'chennai', 'articles'),
                        (4, 'Oxford', 1950,
                         'chennai', 'all'),
                        (5, 'MIT', 1950,
                         'chennai', 'books')]
    for i in record_to_insert:
        cursor.execute(postgres_insert_query, i)
 
        connection.commit()
        count = cursor.rowcount
    print(count, "Record inserted successfully \
    into publisher table")
 
except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into publisher table", error)
 
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")