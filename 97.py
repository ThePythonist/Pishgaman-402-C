chances = 3

def signup():
    username = input("Username : ").lower()
    password = input("Password : ")

    open("users.txt", "a").write(username + "\n")
    open("passwords.txt", "a").write(password + "\n")

    print(f"Signed up user {username}")

def signin():
    global chances
    users = [i[:-1] for i in open("users.txt").readlines()]
    passwords = [i[:-1] for i in open("passwords.txt").readlines()]
    accounts = dict(zip(users, passwords))
    # print(accounts)

    if chances > 0 :
        username = input("Username : ").lower()
        password = input("Password : ")
        if username in accounts:
            if password == accounts[username]:
                print("Successfully logged in")
            else:
                print("Password is incorrect")
                chances -= 1
                print(chances)
        else:
            print("Account not found")
    else :
        print("Too many attempts. Try later")
while True:
    operation = input("""
    Choose an operation :
    1 : Register an account
    2 : Sign-in to your account
    """)

    if operation == "1":
        signup()
    elif operation == "2":
        signin()
    else:
        print("Invalid entry. Choose 1 or 2")

