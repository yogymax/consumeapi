import requests
from consumer.Beans import *

BASE_URI = "http://localhost:8000/api/vendor/"

def getVendorInfo():
    response = requests.get(BASE_URI)
    listOfVendors = []
    for vendor in response.json():
        listOfProducts = []
        for product in vendor['products']:
                listOfProducts.append(Product(name=product['productName'],price=product['productPrice'],qty=product['productQty'],cat=product['productCat'],customer=Customer(name=product['customer']['custName'],age=product['customer']['custAge'],balance=product['customer']['custBalance'])))
        listOfVendors.append(Vendor(products=listOfProducts,address=Address(city=vendor['address_id']['city'],state=vendor['address_id']['state'],pin=vendor['address_id']['pincode'])))
    return listOfVendors

if __name__ == '__main__':
    listOfV = getVendorInfo()
    print(listOfV)