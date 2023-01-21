from sqlalchemy import create_engine, MetaData, Table
import pandas as pd
engine = create_engine('sqlite:////Users/Satish/Downloads/flask-login-register-form-master/database.db', convert_unicode=True)
metadata = MetaData(bind=engine)
users = Table('userdetails', metadata, autoload=True)
data=engine.execute('select * from userdetails ')
df4=pd.DataFrame(data,columns=('sn','uname','mobilenum','emailid','date','tablenum'))
l5=list(df4['uname'])
print(l5)
l6=list(df4['date'])
print(l6)
