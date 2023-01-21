import mysql.connector as m
import pandas as p
db2=m.connect(host='localhost',user='root',passwd='root',database='roopa')
myc=db2.cursor()
#myc.execute('CREATE TABLE restr1 (snum int,rname varchar(200),tablenum varchar(200),menu varchar(200))')
q='insert into restr1 (snum,rname,tablenum,menu) value (%s,%s,%s,%s)'
v=('3','abcd1','1,2,3,4,5,6,7,8,9,10','a,b,c,d')
#myc.execute(q,v)
myc.execute('select * from restr1')
data=myc.fetchall()
db2.commit()
df=p.DataFrame(data,columns=('snum','rname','tablenum','menu'))
l=list(df['rname'])
ltable=list(df['tablenum'])
print(ltable)



