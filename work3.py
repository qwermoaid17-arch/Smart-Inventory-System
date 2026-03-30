import json

def append ():
    name=input("Enter the product name : ")
    price=float(input("enter your price : "))
    quantity=int(input("Enter the quantity : "))
    new_herfer={"name" : name, "price" : price, "quantity" : quantity}
    hafer.append(new_herfer)
    with open("data.json", "w") as file:
        json.dump(hafer, file, indent=2)
    

def show_products():

    for i, n in enumerate(hafer):
        print(i,"-", n)

def delete():
    print(hafer)
    delle=int(input("Enter the numer product you want to delete : "))
    hafer.pop(delle)
    with open("data.json", "w") as file:
        json.dump(hafer, file, indent=2)

while True:

    input_message = """
    What Do You Want To Do ?
    "1" => Add New product    
    "2" => Show All product
    "3" => Delete A product
    "4" => Quit The App
    Choose Option:
    """

    print(input_message)

    try:
        user_input = int(input("Enter what you want to do : "))
    except ValueError:
        print("An error occurred. Text is prohibited. : ")
        continue


    with open("data.json", "r") as file:
        hafer = json.load(file)


    if user_input==1:
        append()
    elif user_input==2:
        show_products()
    elif user_input==3:
        delete()
    else:
        n=input("Enter \"Exit\" if you want to exit : ").strip().lower()
        if n=="exit":
            break
        else:
            pass

#good morning