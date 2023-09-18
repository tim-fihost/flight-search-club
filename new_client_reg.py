from sheety import Users 
#==============================================
print("Welcome to Timur's Travel Agency!")
print("We will find best flight deals for you!")
user_name_v = input("What is your name: ")
user_last_name_v = input("What is your last name: ")
user_email_v = "orginal"
re_check_email =  "for_verification"

while user_email_v != re_check_email:
    user_email_v = input("What is your email? ")
    if user_email_v.lower() == "quit" \
            or user_email_v.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if re_check_email.lower() == "quit" \
            or re_check_email.lower() == "exit":
        exit()

print("OK. You're in the club!")

user_info = Users(user_name=user_name_v,user_last_name=user_last_name_v,user_email=user_email_v)
user_info.load_info()
