import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# print(visits.head(10))
# print(cart.head(10))
# print(checkout.head(10))
# print(purchase.head(10))

# print(len(visits))

visit_cart = pd.merge(visits, cart, how='left')
visit_cart_row = len(visit_cart)
print(visit_cart_row)

null_cart_times = len(visit_cart[visit_cart.cart_time.isnull()])
print(float(null_cart_times) / visit_cart_row)

checkout_cart = pd.merge(cart, checkout, how='left')
checkout_cart_row = len(checkout_cart)
print(checkout_cart_row)

null_checkout_times = len(checkout_cart[checkout_cart.checkout_time.isnull()])
print(float(null_checkout_times) / checkout_cart_row)

all_data = visits.merge(cart, how='left') \
                .merge(checkout, how='left') \
                .merge(purchase, how='left')
# print(all_data.head())

checkout_purchase = checkout.merge(purchase, how='left')
checkout_purchase_row = len(checkout_purchase)
print(checkout_purchase_row)

null_checkout_purchase = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
print(float(null_checkout_purchase) / checkout_purchase_row)

# 0.805068226121
# 0.209302325581
# 0.16889632107
# The first step of the funnel is weakeset. They have to change the process or encourage customer's motivation to put their item into the cart

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
# print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
