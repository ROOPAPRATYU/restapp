import mysql.connector as m
db=m.connect(host='localhost',user='root',passwd='root',database='roopa')
myc=db.cursor()
#myc.execute('CREATE TABLE restr (snum int,rname varchar(200),tablenum int,menu varchar(200))')
q='insert into restr (snum,rname,tablenum,menu) value (%s,%s,%s,%s)'
v=('1','abc','1','a,b,c,d')
#myc.execute(q,v)
db.commit()
