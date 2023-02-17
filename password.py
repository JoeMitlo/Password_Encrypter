from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def change(name, old_password, new_password):
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            if (name == user) and (fer.decrypt(passw.encode()).decode() == old_password):
                new_data = name + "|" + fer.encrypt(new_password.encode()).decode() + "\n"
                print("Change successful"+'\n')
                with open('passwords.txt', 'w') as f:
                    f.write(new_data)
                    break
            else:
                print("Something isn't right. Try again")

while True:
    mode = input(
        "Would you like to add a new password, view existing ones, or change a current password (view, add, change), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "change":
        username = input("What is the username of the password you would like to change? ")
        old = input('What is the current password for the account? ')
        new = input('What is the new password for the account? ')
        change(username, old, new)
    else:
        print("Invalid mode.")
        continue