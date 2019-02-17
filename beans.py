
print('added by other developer..!')
class Address:

    def __init__(self,city,state,pin):
        self.city=city
        self.state=state
        self.pincode=pin

    def __str__(self):
        return 'City : {}, State : {}, PinCode : {}'.format(self.city,self.state,self.pincode)

    def __repr__(self):
        return str(self)

class Customer:

    def __init__(self,name,age,balance):
        self.custName=name
        self.custAge=age
        self.custBalance=balance

    def __str__(self):
        return 'CustName : {}, CustAge : {},  CustBalance :{}'.format(self.custName,self.custAge,self.custBalance)

    def __repr__(self):
        return str(self)

class Product:

    def __init__(self,name,price,qty,cat,customer):
        self.productName=name
        self.productPrice=price
        self.productQty=qty
        self.productCat=cat
        self.customer=customer

    def __str__(self):
        return '\n ProdName : {} ProdPrice : {}, ProdCat : {}, ProdQty : {}, Customer :{}'.format(self.productName,self.productPrice,self.productCat,self.productQty,self.customer)

    def __repr__(self):
        return str(self)


class Vendor:

    def __init__(self,products,address):
        self.listOfProducts=products
        self.address=address

    def __str__(self):
        return '\n\n ListOfProducts : {}, Address : {}'.format(self.listOfProducts,self.address)

    def __repr__(self):
        return str(self)
