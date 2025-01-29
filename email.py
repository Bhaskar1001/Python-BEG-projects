#email slicer

email = input("enter your email: ")

index = email.index("@") # index for @ symbol

username =  email[:index]
domain = email[index:]

print(f"your username is {username} and domain is {domain}")