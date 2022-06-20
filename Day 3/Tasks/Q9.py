# Q-9  Email and phone validation and meta-characters using regex

import re


def check_mail(email):
    email_regex = r"[a-zA-Z0-9._]+@[a-zA-Z.-]+\.(com|in|edu|gov|org)"
    if (re.fullmatch(email_regex,email)):
        print("Valid Email")
    else:
        print("Invalid Email")
    return

def check_phone(phone):
    phone_regex = r"[0-9]{7,14}"
    if (re.search(phone_regex,phone)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
    return


# Main - Driver code
while True:
    print("\n1) Check Mail")
    print("2) Check Phone")
    print("3) Exit\n")

    choice = int(input("Enter choice: "))
    
    if (choice==1):
        email = input("\nEnter email: ")
        check_mail(email)
    elif (choice==2):
        phone = input("\nEnter phone number: ")
        check_phone(phone)
    elif (choice==3):
        exit()
    else:
        print("\nPlease enter a valid choice !!!")
