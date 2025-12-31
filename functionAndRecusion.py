# def converter(usd_val):
#     inr_val = usd_val * 82.74
#     print(f"INR value is: {inr_val} rs")
#     return inr_val

# usd = float(input("Enter USD value: "))
# inr = converter(usd)

# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)

# show (5)

# def fact(n):
#     if (n == 1 or n == 0):
#         return 1
#     return fact(n-1)+n

# print(" the factorial is this : " ,fact (5) )

def print_list(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list , idx +1)

    fruits = ["alu","mango","banana","apple","papaya"]
    print_list(fruits)
