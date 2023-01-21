from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from e8 import tm,td,ty
from databases import l,ltable
from databasepayment import l1,ledate,lcvv
from sqlalchemy import create_engine, MetaData, Table
import pandas as pd


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Satish/Downloads/flask-login-register-form-master/database.db'
db = SQLAlchemy(app)

#create table called user
class user(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(200))
    mobile=db.Column(db.Integer)
    email=db.Column(db.String(200))
    password=db.Column(db.String(200))

#create table called userdetails
class userdetails(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(200))
    mobilenum=db.Column(db.Integer)
    email=db.Column(db.String(200))
    hotelname=db.Column(db.String(200))
    dat=db.Column(db.Integer)
    number=db.Column(db.Integer)    


#index page
@app.route('/')
def index1():
    return render_template("index1.html")

@app.route('/show_all')
def show_all(): 
    return render_template("show_all.html", userdetails = userdetails.query.all())

#adminlogin page
@app.route('/adminlogin',methods=['POST','GET'])
def adminlogin():
    if request.method=="POST":
        adminname=request.form['aname']
        passwd=request.form['passw']
        if adminname=='Admin' and passwd=='Admin':
            return redirect(url_for("show_all"))
    return render_template("adminlogin.html")
 

#userlogin page
@app.route('/userlogin',methods=['POST','GET'])
def userlogin(): 
    if request.method=='POST':
        global uname
        uname=request.form['username']
        #request.form.get("username", False)
        passwd=request.form['passwuser']
        login=user.query.filter_by(username=uname,password=passwd).first()
        if login is not None:
            return redirect(url_for("serching"))
    return render_template("userlogin.html")


#signup page
@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        uname = request.form['username']
        mble = request.form['mbln']
        mail = request.form['email']
        passw = request.form['passwd']
        engine = create_engine('sqlite:////Users/Satish/Downloads/flask-login-register-form-master/database.db', convert_unicode=True)
        usertabledata1=engine.execute('select * from user ')
        dfsign=pd.DataFrame(usertabledata1,columns=('sn','username','mobilenum','emial','passwrd'))
        mobilenumber=list(dfsign['mobilenum'])
        
        try:
            if mobilenumber.index(mble)>=0:
                return render_template("a.html")
        except:
            register = user(username = uname, email = mail, mobile =mble,  password = passw)
            db.session.add(register)
            db.session.commit()

        return redirect(url_for("userlogin"))
    return render_template("signup.html")

#lookup page
@app.route('/lookup',methods=['POST','GET'])
def lookup():
    return render_template("lookup.html")

#serching page
@app.route('/serching',methods=['POST','GET'])
def serching():
    if request.method=="POST":
        global serch
        serch=request.form['search1']
        try:
            if l.index(serch)>=0: 
                return redirect(url_for("lookup"))
        except:
            return render_template("serchnot.html")
    return render_template("serching.html")

#cvvv page    
@app.route('/cvvv',methods=['POST','GET'])
def cvvv():
    #collect the table number  and hotelname of perticular hotelname from restr
    m=l.index(serch)
    ltablenum=ltable[m]
    ltablenum1=ltablenum.split(',')
    print(ltablenum1)
    if request.method == "POST":
        #collect data from cvvv form
        hotelname = request.form['hname1']
        sname= request.form['adname']
        date1 = request.form['date']
        tnum = request.form['tablen']
        print(type(tnum))
        print('date is',date1)
        try:
            #collect the user details from user table
            engine = create_engine('sqlite:////Users/Satish/Downloads/flask-login-register-form-master/database.db', convert_unicode=True)
            usertabledata=engine.execute('select * from user ')
            dfuser=pd.DataFrame(usertabledata,columns=('sn','username','mobilenum','emial','passwrd'))
            listuname=list(dfuser['username'])
            listmbl1=list(dfuser['mobilenum'])
            listemail1=list(dfuser['emial'])
            #ref for user table details add to the session
            indexuser=listuname.index(uname)
            unameuser=listuname[indexuser]
            mobilenumber = listmbl1[indexuser]
            emailid = listemail1[indexuser]

           
            #collect data from table userdetails 
            engine = create_engine('sqlite:////Users/Satish/Downloads/flask-login-register-form-master/database.db', convert_unicode=True)
            data=engine.execute('select * from userdetails')
            df4=pd.DataFrame(data,columns=('sn','uname','mobilenum','emailid','hotelname','date','tablenum'))
            datelist=list(df4['date'])
            
        except:
            return render_template("cvvv.html",ltablenum1=ltablenum1) 
            
        try:
            df5=df4
            a=len(df5)
            for i in range(a):
                da=str(datelist[i])
                if date1!=da:
                    df5=df5.drop(i) 
            dlist=list(df5['date'])
            tlist=list(df5['tablenum'])
            hotellist=list(df5['hotelname'])

        except:
            df5=df4

        try: 
            for i in range(len(df5)):
                if hotelname==hotellist[i] and int(tnum)==tlist[i] and date1==str(dlist[i]):
                    result='blocked'
        except:
            result='unblocked'
            
        date1y=date1[0]+date1[1]+date1[2]+date1[3]
        date1m=date1[5]+date1[6]
        date1d=date1[8]+date1[9]
        
        try:
            if result=='blocked':
                return render_template("tablebooked.html")
            
        except:
            if sname==uname and hotelname==serch:
                register1 = userdetails(username = uname, mobilenum = mobilenumber, email = emailid, hotelname = serch, dat = date1, number = tnum)
                db.session.add(register1)
                db.session.commit()
                return redirect(url_for("payment"))
            
            
            

    return render_template("cvvv.html",ltablenum1=ltablenum1)

@app.route('/paymentsuccess',methods=['POST','GET'])
def paymentsuccess():
    return render_template("paymentsuccess.html")
    tm.sleep(3)
    return redirect(url_for("index"))

@app.route('/paymentfail',methods=['POST','GET'])
def paymentfail():
    return render_template("paymentfail.html")

#payment page
@app.route('/payment',methods=['POST','GET'])
def payment():
    if request.method=="POST":
        cnum=request.form['cardNumber']
        date1=request.form['cardExpiry']
        cvvv1=request.form['cardCVV']
        try:
            k=l1.index(cnum)
            if l1[k]==cnum and ledate[k]==date1 and lcvv[k]==cvvv1:
                return redirect(url_for("paymentsuccess"))
                
        except:
            return redirect(url_for("paymentfail"))
        return redirect(url_for("paymentfail"))
    return render_template("payment.html")

while True:
    
    db.create_all()
    app.run(debug='True')

