import mysql.connector as m
import pandas as p
db3=m.connect(host='localhost',user='root',passwd='root',database='roopa')
myc=db3.cursor()
#myc.execute('create table payment4 (cardnum varchar(200),exdate varchar(200),cvv varchar(200))')
q='insert into payment4 (cardnum,exdate,cvv) value (%s,%s,%s)'
v=('2222-2222-1111-2224','08/20','112')
#myc.execute(q,v)
myc.execute('select * from payment4')
data=myc.fetchall()
db3.commit()
df=p.DataFrame(data,columns=('cardnum','expiry date','cvv'))
l1=list(df['cardnum'])
ledate=list(df['expiry date'])
lcvv=list(df['cvv'])
print(lcvv)
