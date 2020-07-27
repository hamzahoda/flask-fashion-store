from flask import Flask, request, render_template,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import json




with open('config.json','r') as c:
    params=json.load(c)["params"]

local_server=True


app = Flask(__name__)


if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI']=params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI']=params['prod_uri']   

app.secret_key='super_secret_key'
    
db=SQLAlchemy(app)



class Contacts(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(20),nullable=False)
    phone=db.Column(db.String(20),nullable=False)
    message=db.Column(db.String(120),nullable=False)


class Cosmetics(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  

class Dresses(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20))
    image2=db.Column(db.String(20))
    image3=db.Column(db.String(20))
    title=db.Column(db.String(20))
    details=db.Column(db.String(50))
    discountprice=db.Column(db.Integer)    
    actualprice=db.Column(db.Integer)   
    tag=db.Column(db.String(10))  
 


class Jeans(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  

class Jewellery(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  

class Salwars(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False) 

class Sandals(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  

class Heels(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False) 

class Boots(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False) 

class Flats(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)              

class Sarees(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  

class Shirts(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  

class SinglePage(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  

class Skirts(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  

class Sweaters(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  


class Watches(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    image1=db.Column(db.String(20),nullable=False)
    image2=db.Column(db.String(20),nullable=False)
    image3=db.Column(db.String(20),nullable=False)
    title=db.Column(db.String(20),nullable=False)
    details=db.Column(db.String(50),nullable=False)
    discountprice=db.Column(db.Integer,nullable=False)
    actualprice=db.Column(db.Integer,nullable=False)
    tag=db.Column(db.String(10),nullable=False)  


class Checkout(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    product=db.Column(db.String(20),nullable=True)
    productname=db.Column(db.String(20))
    price=db.Column(db.Integer)























@app.route("/", methods=["GET", "POST"])
def home():
    shirts=Shirts.query.all()
    skirts=Skirts.query.all()
    watches=Watches.query.all()
    sandals=Sandals.query.all()
    jewellery=Jewellery.query.all()
    sarees=Sarees.query.all()
    cosmetics=Cosmetics.query.all()
    dresses=Dresses.query.all()
    jeans=Jeans.query.all()
    return render_template("index.html",jeans=jeans,shirts=shirts,skirts=skirts,watches=watches,sandals=sandals,jewellery=jewellery,sarees=sarees,cosmetics=cosmetics,dresses=dresses)


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        entry=Contacts(name=name,email=email,phone=phone,message=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("mail.html")









@app.route("/products", methods=["GET", "POST"])
def products():
    return render_template("products.html")


@app.route("/cosmetics", methods=["GET", "POST"])
def cosmetics():
    cosmetics=Cosmetics.query.all()
    return render_template("cosmetics.html",cosmetics=cosmetics)

@app.route("/cosmeticdetail/<string:sno>",methods=["GET","POST"])
def cosmeticdetail(sno):
    cosmeticdetail=Cosmetics.query.filter_by(sno=sno).first()
    return render_template("cosmeticdetail.html",cosmeticdetail=cosmeticdetail)




   
   
@app.route("/watches", methods=["GET", "POST"])
def watches():
    watches=Watches.query.all()
    return render_template("watches.html",watches=watches)
   

@app.route("/watchdetail/<string:sno>",methods=["GET","POST"])
def watchdetail(sno):
    watchdetail=Watches.query.filter_by(sno=sno).first()
    return render_template("watchdetail.html",watchdetail=watchdetail)





@app.route("/jewellery", methods=["GET", "POST"])
def jewellery():
    jewellery=Jewellery.query.all()
    return render_template("jewellery.html",jewellery=jewellery)


@app.route("/jewellerydetail/<string:sno>",methods=["GET","POST"])
def jewellerydetail(sno):
    jewellerydetail=Jewellery.query.filter_by(sno=sno).first()
    return render_template("jewellerydetail.html",jewellerydetail=jewellerydetail)









@app.route("/dresses", methods=["GET", "POST"])
def dresses():
    dresses=Dresses.query.all()
    return render_template("dresses.html",dresses=dresses)


@app.route("/dressdetail/<string:sno>",methods=["GET","POST"])
def dressdetail(sno):
    dressdetail=Dresses.query.filter_by(sno=sno).first()
    return render_template("dressdetail.html",dressdetail=dressdetail)




@app.route("/jeans", methods=["GET", "POST"])
def jeans():
    jeans=Jeans.query.all()
    return render_template("jeans.html",jeans=jeans)

@app.route("/jeansdetail/<string:sno>",methods=["GET","POST"])
def jeansdetail(sno):
    jeansdetail=Jeans.query.filter_by(sno=sno).first()
    return render_template("jeansdetail.html",jeansdetail=jeansdetail)





@app.route("/salwars", methods=["GET", "POST"])
def salwars():
    salwars=Salwars.query.all()
    return render_template("salwars.html",salwars=salwars)

@app.route("/salwardetail/<string:sno>",methods=["GET","POST"])
def salwardetail(sno):
    salwardetail=Salwars.query.filter_by(sno=sno).first()
    return render_template("salwardetail.html",salwardetail=salwardetail)



@app.route("/sarees", methods=["GET", "POST"])
def sarees():
    sarees=Sarees.query.all()
    return render_template("sarees.html",sarees=sarees)

@app.route("/sareedetail/<string:sno>",methods=["GET","POST"])
def sareedetail(sno):
    sareedetail=Sarees.query.filter_by(sno=sno).first()
    return render_template("sareedetail.html",sareedetail=sareedetail)








@app.route("/shirts", methods=["GET", "POST"])
def shirts():
    shirts=Shirts.query.all()
    return render_template("shirts.html",shirts=shirts)

@app.route("/shirtdetail/<string:sno>",methods=["GET","POST"])
def shirtdetail(sno):
    shirtdetail=Shirts.query.filter_by(sno=sno).first()
    return render_template("shirtdetail.html",shirtdetail=shirtdetail)










@app.route("/skirts", methods=["GET", "POST"])
def skirts():
    skirts=Skirts.query.all()
    return render_template("skirts.html",skirts=skirts)

@app.route("/skirtdetail/<string:sno>",methods=["GET","POST"])
def skirtdetail(sno):
    skirtdetail=Skirts.query.filter_by(sno=sno).first()
    return render_template("skirtdetail.html",skirtdetail=skirtdetail)








@app.route("/sweaters", methods=["GET", "POST"])
def sweaters():
    sweaters=Sweaters.query.all()
    return render_template("sweaters.html",sweaters=sweaters)    


@app.route("/sweaterdetail/<string:sno>",methods=["GET","POST"])
def sweaterdetail(sno):
    sweaterdetail=Sweaters.query.filter_by(sno=sno).first()
    return render_template("sweaterdetail.html",sweaterdetail=sweaterdetail)





@app.route("/single", methods=["GET", "POST"])
def single():
    return render_template("single.html")    






@app.route("/sandals", methods=["GET", "POST"])
def sandals():
    sandals=Sandals.query.all()
    return render_template("sandals.html",sandals=sandals)    

@app.route("/sandaldetail/<string:sno>",methods=["GET","POST"])
def sandaldetail(sno):
    sandaldetail=Sandals.query.filter_by(sno=sno).first()
    return render_template("sandaldetail.html",sandaldetail=sandaldetail)


@app.route("/heels", methods=["GET", "POST"])
def heels():
    heels=Heels.query.all()
    return render_template("heels.html",heels=heels)   

@app.route("/heeldetail/<string:sno>",methods=["GET","POST"])
def heeldetail(sno):
    heeldetail=Heels.query.filter_by(sno=sno).first()
    return render_template("heeldetail.html",heeldetail=heeldetail)


@app.route("/boots", methods=["GET", "POST"])
def boots():
    boots=Boots.query.all()
    return render_template("boots.html",boots=boots)   

@app.route("/bootdetail/<string:sno>",methods=["GET","POST"])
def bootdetail(sno):
    bootdetail=Boots.query.filter_by(sno=sno).first()
    return render_template("bootdetail.html",bootdetail=bootdetail)


@app.route("/flats", methods=["GET", "POST"])
def flats():
    flats=Flats.query.all()
    return render_template("flats.html",flats=flats)             

@app.route("/flatdetail/<string:sno>",methods=["GET","POST"])
def flatdetail(sno):
    flatdetail=Flats.query.filter_by(sno=sno).first()
    return render_template("flatdetail.html",flatdetail=flatdetail)    





# @app.route("/cardbootstrap",methods=["GET","POST"])
# def bootstrap():
#     return render_template("cardbootstrap.html")

# @app.route("/tryindex",methods=["GET","POST"])
# def tryindex():
#     dresses=Dresses.query.all()
#     return render_template("tryindex.html",dresses=dresses)


# @app.route("/anothertryindex",methods=["GET","POST"])
# def anothertryindex():
#     dresses=Dresses.query.all()
#     return render_template("anothertryindex.html",dresses=dresses)

# @app.route("/finalother",methods=["GET","POST"])
# def finalother():
#     dresses=Dresses.query.all()
#     return render_template("finalother.html",dresses=dresses)    

# @app.route("/hovercard",methods=["GET","POST"])
# def hovercard():
#     dresses=Dresses.query.all()
#     return render_template("hovercard.html",dresses=dresses)  






# HOME PAGE PAR ADD TO CART TAMAM SEPERATE CHEEZEIN 
@app.route("/homeaddshirttocart",methods=["GET","POST"])
def homeaddshirttocart():
    sno=request.form.get('sno')
    shirts=Shirts.query.filter_by(sno=sno).first()
    value=Checkout(product=shirts.image1,price=shirts.discountprice,productname=shirts.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/")

@app.route("/homeaddskirttocart",methods=["GET","POST"])
def homeaddskirttocart():
    sno=request.form.get('sno')
    skirts=Skirts.query.filter_by(sno=sno).first()
    value=Checkout(product=skirts.image1,price=skirts.discountprice,productname=skirts.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/")

@app.route("/homeaddwatchtocart",methods=["GET","POST"])
def homeaddwatchtocart():
    sno=request.form.get('sno')
    watches=Watches.query.filter_by(sno=sno).first()
    value=Checkout(product=watches.image1,price=watches.discountprice,productname=watches.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/")

@app.route("/homeaddsandaltocart",methods=["GET","POST"])
def homeaddsandaltocart():
    sno=request.form.get('sno')
    sandals=Sandals.query.filter_by(sno=sno).first()
    value=Checkout(product=sandals.image1,price=sandals.discountprice,productname=sandals.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/")

@app.route("/homeaddjewellerytocart",methods=["GET","POST"])
def homeaddjewellerytocart():
    sno=request.form.get('sno')
    jewellery=Jewellery.query.filter_by(sno=sno).first()
    value=Checkout(product=jewellery.image1,price=jewellery.discountprice,productname=jewellery.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/")        

@app.route("/homeaddsareetocart",methods=["GET","POST"])
def homeaddsareetocart():
    sno=request.form.get('sno')
    sarees=Sarees.query.filter_by(sno=sno).first()
    value=Checkout(product=sarees.image1,price=sarees.discountprice,productname=sarees.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/")   

@app.route("/homeaddcosmetictocart",methods=["GET","POST"])
def homeaddcosmetictocart():
    sno=request.form.get('sno')
    cosmetics=Cosmetics.query.filter_by(sno=sno).first()
    value=Checkout(product=cosmetics.image1,price=cosmetics.discountprice,productname=cosmetics.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/")   

@app.route("/homeadddresstocart",methods=["GET","POST"])
def homeadddresstocart():
    sno=request.form.get('sno')
    dresses=Dresses.query.filter_by(sno=sno).first()
    value=Checkout(product=dresses.image1,price=dresses.discountprice,productname=dresses.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/")   

@app.route("/homeaddjeantocart",methods=["GET","POST"])
def homeaddjeantocart():
    sno=request.form.get('sno')
    jeans=Jeans.query.filter_by(sno=sno).first()
    value=Checkout(product=jeans.image1,price=jeans.discountprice,productname=jeans.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/")   







































# SEPERATE PAGES ADD TO CART


@app.route("/addflattocart",methods=["GET","POST"])
def addflattocart():
    sno=request.form.get('sno')
    flats=Flats.query.filter_by(sno=sno).first()
    value=Checkout(product=flats.image1,price=flats.discountprice,productname=flats.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/flats")


@app.route("/addboottocart",methods=["GET","POST"])
def addboottocart():
    sno=request.form.get('sno')
    boots=Boots.query.filter_by(sno=sno).first()
    value=Checkout(product=boots.image1,price=boots.discountprice,productname=boots.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/boots")



@app.route("/addsandaltocart",methods=["GET","POST"])
def addsandaltocart():
    sno=request.form.get('sno')
    sandals=Sandals.query.filter_by(sno=sno).first()
    value=Checkout(product=sandals.image1,price=sandals.discountprice,productname=sandals.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/sandals")


@app.route("/addheeltocart",methods=["GET","POST"])
def addheeltocart():
    sno=request.form.get('sno')
    heels=Heels.query.filter_by(sno=sno).first()
    value=Checkout(product=heels.image1,price=heels.discountprice,productname=heels.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/heels")




@app.route("/addwatchtocart",methods=["GET","POST"])
def addwatchtocart():
    sno=request.form.get('sno')
    watches=Watches.query.filter_by(sno=sno).first()
    value=Checkout(product=watches.image1,price=watches.discountprice,productname=watches.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/watches")


@app.route("/addjewellerytocart",methods=["GET","POST"])
def addjewellerytocart():
    sno=request.form.get('sno')
    jewellery=Jewellery.query.filter_by(sno=sno).first()
    value=Checkout(product=jewellery.image1,price=jewellery.discountprice,productname=jewellery.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/jewellery")



@app.route("/addcosmetictocart",methods=["GET","POST"])
def addcosmetictocart():
    sno=request.form.get('sno')
    cosmetics=Cosmetics.query.filter_by(sno=sno).first()
    value=Checkout(product=cosmetics.image1,price=cosmetics.discountprice,productname=cosmetics.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/cosmetics")


@app.route("/addsareetocart",methods=["GET","POST"])
def addsareetocart():
    sno=request.form.get('sno')
    sarees=Sarees.query.filter_by(sno=sno).first()
    value=Checkout(product=sarees.image1,price=sarees.discountprice,productname=sarees.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/sarees")


@app.route("/addsalwartocart",methods=["GET","POST"])
def addsalwartocart():
    sno=request.form.get('sno')
    salwars=Salwars.query.filter_by(sno=sno).first()
    value=Checkout(product=salwars.image1,price=salwars.discountprice,productname=salwars.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/salwars")


@app.route("/addsweatertocart",methods=["GET","POST"])
def addsweatertocart():
    sno=request.form.get('sno')
    sweaters=Sweaters.query.filter_by(sno=sno).first()
    value=Checkout(product=sweaters.image1,price=sweaters.discountprice,productname=sweaters.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/sweaters")



@app.route("/addskirttocart",methods=["GET","POST"])
def addskirttocart():
    sno=request.form.get('sno')
    skirts=Skirts.query.filter_by(sno=sno).first()
    value=Checkout(product=skirts.image1,price=skirts.discountprice,productname=skirts.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/skirts")



@app.route("/addshirttocart",methods=["GET","POST"])
def addshirttocart():
    sno=request.form.get('sno')
    shirts=Shirts.query.filter_by(sno=sno).first()
    value=Checkout(product=shirts.image1,price=shirts.discountprice,productname=shirts.title)
    db.session.add(value)
    db.session.commit()
    return redirect("/shirts")




@app.route("/adddresstocart",methods=["GET","POST"])
def adddresstocart():
    sno=request.form.get('sno')
    dresses=Dresses.query.filter_by(sno=sno).first()
    value=Checkout(product=dresses.image1,price=dresses.discountprice,productname=dresses.title)
    db.session.add(value)
    db.session.commit()
    flash("Item successfully added to cart")
    return redirect("/dresses")



@app.route("/deleteproduct/<string:sno>",methods=["GET","POST"])
def deleteproduct(sno):
    # sno=request.form.get('sno')
    checkout=Checkout.query.filter_by(sno=sno).first()
    db.session.delete(checkout)
    db.session.commit()
    return redirect("/checkout")













@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    checkout=Checkout.query.all()
    return render_template("checkout.html",checkout=checkout)













app.run(debug=True)
