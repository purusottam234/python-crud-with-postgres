from psycopg2 import connect
 
# declare the connection string specifying
# the host name database name
# use name and password
conn_string = "host='localhost' \
dbname='pythonpostgres' user='postgres'\
password='postgres'"
 
# use connect function to establish the connection
conn = connect(conn_string)