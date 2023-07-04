#Task : User Registration System You are tasked with creating a user registration system for a website.
# 1.
users = [] 

def register_user(username, password, email):    
    new_user = {
      "username": username,
      "password": password,
      "email" : email,
        }
    users.append(new_user)

register_user('Jane','12345','j@gmail.com')
register_user("john123", "pass123", "john@example.com")
register_user("emma456", "abc456", "emma@example.com")
register_user("james789", "xyz789", "james@example.com")
print(users)
#-------------------------------------------------------------------------------------------------------
# 2.
def login_user(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Login successful!")
            return
    print("Invalid username or password.")
    return

login_user('Jane','12345')
login_user("john123", "pass123")
login_user("emma456", "wrongpass")
login_user("james789", "xyz789")

#------------------------------------------------------------------------------------------------------
# 3.

def change_password(username, old_password, new_password): 
    for user in users:
        if user['username'] == username and user['password'] == old_password:
            user['password'] = new_password
            print("Password changed successfully!")
            return
        else:
            print("Invalid password.")
            return
change_password('Jane','12345','j@gmail.com')
#change_password("john123", "pass123", "newpass")
change_password("emma456", "wrongpass", "newpass")
#--------------------------------------------------------------------------------------------------------
# 4.





