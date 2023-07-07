def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price - price * discount
        return price
        
        

    apply_discount()
    return price

price = int(input('Enter price '))
discount = float(input('Enter discount '))
print(discount_price(price, discount))