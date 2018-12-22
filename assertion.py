#learning assert
def apply_discount(product, discount):
  price = int(product['price']*(1-discount))
  assert 0 <= price <= product['price']
  return price

#product is represented in plain dictionaries

shoes ={'name': 'Fancy shoes', 
        'price': 14900}

print(apply_discount(shoes, 0.25))

print(apply_discount(shoes, 2.0))
