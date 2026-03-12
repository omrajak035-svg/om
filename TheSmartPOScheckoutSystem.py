coffee_price = 250
tax_rate = 0.05

input_customer = input("enter how many cups of coffee you want to buy: ")
real_price = int(input_customer)
input_primium = input ("are u a currentally the primeum member of our shop YES or NO")
primiun_benifit= str(input_primium)
if primiun_benifit == "yes"  :
    print ("congrase you got 50rs off in your order:",coffee_price-50)
else:
    print("no offer")

    total_price = ( real_price * coffee_price)+(coffee_price*real_price*tax_rate)
    print("total price is " , total_price)

    if real_price >= 5:
        discount = total_price * 0.1
        total_price -= discount
        print("got 10% off" , total_price)

    else:
        print("no discount")







