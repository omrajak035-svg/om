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

# def print_list(list,idx=0):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list , idx +1)

# fruits = ["alu","mango","banana","apple","papaya"]
# print_list(fruits)



# total_word = 90
# if total_word >100:
#     print("the script is too long")
# else:
#     print("script is okay")

# user_input = input ("enter the length at which you want to make video in minutes if you want to make a short reel enter 1 or less less then 1 min")
# video_length = int(user_input)
# if  video_length<=1:
#     print("short reels charge 200rs")
# elif video_length <= 5:
#     print("middium videos rate is around 500rs")
# elif video_length <=10 :
#     print ("mid long video rate is around 1000rs")
# else:
#     print("long video rate is 2000rs or more depends on the lengthof video ")

# client_list = ["rahul" , "priya", "amit"]
# client_list.append("bheem")
# print(client_list)
# for person in client_list:
#     print("sender final video to :"+person)
#     print("all videos sent")
account_balance = 1000
for balance in account_balance:
    if balance <0:
        print("your account is in negative balance")