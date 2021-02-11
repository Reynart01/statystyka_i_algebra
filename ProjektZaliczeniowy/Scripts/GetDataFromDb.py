import cx_Oracle

dsn_tns = cx_Oracle.makedsn('213.184.8.44', '1521', service_name='orac') 
conn = cx_Oracle.connect(user=r'wegrodzki', password='dobrehaslo321', dsn=dsn_tns)

c = conn.cursor()
c.execute('select * from wegrodzki.categories') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
conn.close()