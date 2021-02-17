def get_base_price(quantity, item_price):
    base_price = quantity * item_price
    return base_price
def get_discount(base_price):
    discount_factor = 0
    if base_price > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return discount_factor
def get_total(base_price, discount_factor):
    total = base_price * discount_factor
    return total