master_psw = input("Input the master passowrd: ")

def add():
    name = input("Name: ")
    password = input("Password: ")
    
    with open("passwords.txt", "a" ) as f:
        f.write(name + "|" + password + "\n")


def view():
    with open("passwords.txt" , "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ",Password:",  passw) 
            

while True:
    password_prompt = input("Do you want to create a new password or view existing passwords? (create/view or 'q' to quit)").lower()
    if password_prompt == "q":
        break
    if password_prompt == "create":
        add()
    elif password_prompt == "view":
        view()
    else:
        print("Not a valid response.")
        quit()
