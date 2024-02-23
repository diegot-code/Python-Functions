
def beginning():
    print ("Starting intro to Python Functions...")

beginning()

def intro():
    print("Hi, I'm John Doe")

# intro()
    
def givex():
    x = 15 # this is local to the func
    print(x)

# givex()

def displaying_firstname(fname): # 'fname' is a parameter of the function
    print(f'{fname} has entered the chatroom.')

# displaying_firstname("Ezekiel")
# displaying_firstname("Josh")
# displaying_firstname("Rodrick")

def display_full_name(fname, mname, lname):
    print(f'Chatter 143 has registered under {fname} {mname} {lname}')

# display_full_name("Chloe", "Robert", "Williams")

def display_name_age(fname, age):
    print(f'{fname} is {age} years old')

display_name_age("Ava", 31)


