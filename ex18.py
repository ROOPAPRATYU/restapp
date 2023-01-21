from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,Table,MetaData
import pandas as p

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Satish/Downloads/flask-login-register-form-master/database6.db'
db=SQLAlchemy(app)

class userroopa(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(200))
	add=db.Column(db.String(200))

@app.route('/',methods=['GET','POST'])
def index():
	engine = create_engine('sqlite:////Users/Satish/Downloads/flask-login-register-form-master/database6.db', convert_unicode=True)
	a=engine.execute('select * from userroopa')
	df=p.DataFrame(a)
	return print(df)

while True:
	db.create_all()
	app.run(debug=True)
	