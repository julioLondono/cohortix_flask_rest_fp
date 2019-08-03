from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userFirstName = db.Column(db.String(45), nullable=False)
    userLastName = db.Column(db.String(45), nullable=False)
    userName = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.userName

    def serialize(self):
        return {
            "user id" : self.id,
            "userFirstName": self.userFirstName,
            "userLastName": self.userLastName,
            "userName": self.userName,
            "email": self.email,
            "password": self.password
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(45), unique=True, nullable=False)
    productDescription = db.Column(db.String(255), unique=True, nullable=True)
    productPrice = db.Column(db.String(45), unique=False, nullable=False)
    productCategory = db.Column(db.String(45), unique=False, nullable=True)
    productAgeRange = db.Column(db.String(45), unique=False, nullable=True)

    def __repr__(self):
        return '<Product %r>' % self.productName

    def serialize(self):
        return {
            "Product id": self.id,
            "ProductName": self.productName,
            "productDescription": self.productDescription,
            "productPrice": self.productPrice,
            "productCategory": self.productCategory,
            "productAgeRange": self.productAgeRange
        }

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userStreet = db.Column(db.String(45), nullable=False)
    userNumber = db.Column(db.String(45), nullable=False)
    userCity = db.Column(db.String(45), nullable=False)
    userState = db.Column(db.String(45), nullable=False)
    userZipCode = db.Column(db.String(12), nullable=False)



    def __repr__(self):
        return '<Addres %r>' % self.userStreet

    def serialize(self):
        return {
            "User Street": self.userStreet,
            "User Number": self.userNumber,
            "User City": self.userCity,
            "User State": self.userState,
            "User Zip Code": self.userZipCode,

        }

class BillingAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    billingStreet = db.Column(db.String(45), nullable=True)
    billingNumber = db.Column(db.String(45), nullable=True)
    billingCity = db.Column(db.String(45), nullable=True)
    billingState = db.Column(db.String(45), nullable=True)
    billingZipCode = db.Column(db.String(12), nullable=True)

    def __repr__(self):
        return '<BillingAddress %r>' % self.billingStreet

    def serialize(self):
        return {
            "Billing Street": self.billingStreet,
            "Billing Number": self.billingNumber,
            "Billing City": self.billingCity,
            "Billing State": self.billingState,
            "Billing Zip Code": self.billingZipCode,

        }

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_url = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return '<Picture %r>' % self.picture_url

    def serialize(self):
        return {
            "Picture URL": self.picture_url
        }