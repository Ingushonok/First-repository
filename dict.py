from pprint import pprint

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}
print(product)
product["memory"] = 256
print(product.get("discount", 0))

del product["stock"]
print(product)

phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
product["recommended"] = phones
print(product)
pprint(product)
product["recommended"].append("iPhone 9")
print(product)

cities = {
    "city": "Москва",
    "temperature": "20"
}
cities["temperature"] = int(cities["temperature"]) - 5
cities["date"] = "27.05.2019"
print(len(cities))