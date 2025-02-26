import re 

def check_password_Strength(password):
    if len(password)<8:
        return "Password is very weak.Should be at least 8 characters long"
    if not any(char.isdigit() for char in password):
        return "Password is weak.Should be at least one number in password"
    if not any(char.isupper() for char in password):
        return "Password is weak.Should be at least contain one uppercase letter"
    if not any(char.islower() for char in password):
        return "Password is weak.Should be at least contain one lowercase letter "
    if not re.search(r'[!@#$%^&*(),.?":;{}|<>]',password):
        return "Password is medium.Add special characters to make password strong"
    return "Password is very STRONG"

def password_checker():
    print("Welcome to password strength checker")
    while True:
        password=input()
        if password.lower()=="exit":
            print("Thanks for using password strength checker.GoodBye!")
            break
        result=check_password_Strength(password)
        print(result)
if __name__=="__main__":
    password_checker()