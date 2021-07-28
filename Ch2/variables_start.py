# 
# Example file for variables


# Declare a variable and initialize it
#f="Abc"
#print(f)


# re-declaring the variable works
f=0


# ERROR: variables of different types cannot be combined
#print("This is an string " + str(123))


# Global vs. local variables in functions

def someFunctions():
    global f
    f="def"
    print(f)

someFunctions()
print(f)


#del f
#print(f)