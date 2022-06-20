# Q-3  GST calculator

def show_all():
    print("""
    1) Grocery - (gst: 5%)
    2) Electronic - (gst: 12%)
    3) Sport - (gst: 18%)
    """)

def get_category():
    choice = int(input("Enter your choice:"))
    return choice

def get_price():
    price = int(input("Enter price:"))
    return price

def get_tax(choice):
    if (choice==1):
        tax = 5
    elif (choice==2):
        tax = 12
    else:
        tax = 18
    return tax
    

def get_items():
    original_amount = 0
    gst_amount = 0
    i = 0
    items = int(input("Enter number of items:"))
    while i<items:
        choice = get_category()
        tax = get_tax(choice)
        price = get_price()
        original_amount += price
        amount = (price*tax)/100
        gst_amount += amount
        i+=1
    print(f"\nOriginal Amount: {original_amount}")
    print(f"GST Amount: {gst_amount}")
    total = original_amount + gst_amount
    print(f"Total Amount: {total}\n")



show_all()
get_items()