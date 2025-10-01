drinks={
    "name": "Brisk",
    "price": 2.50,
    "type": "Iced Tea"
}
chips={
    "name": "Pop Corners",
    "price": 3.00,
    "type": "chips"
}
gum={
    "name": "Watermelon gum",
    "price": 2.00,
    "type": "gum"
}
result=input("welcome, would you like to buy drinks, chips, or gum? ")
if result=="drinks":
    print(drinks["name"])
