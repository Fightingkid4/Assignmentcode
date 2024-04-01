size = int(input("Size: "))
shape = input("Shape: ")
string = input("String: ")

def square(size, my_string):
    while len(my_string) > size or len(my_string) < size:
        print(f"You must enter a string of length {size}!")
        my_string = input("String: ")
        len(my_string)
            
    else:
        i = 0
        while i < size:
            print(my_string)
            i = i + 1
            
        
        
def ltriangle(size, my_string):
    while len(my_string) > size or len(my_string) < size:
        print(f"You must enter a string of length {size}!")
        my_string = input("String: ")
        len(my_string)
    else:
        
        i = 0
        while i < size:
            print(my_string[0:i + 1])
            i = i + 1

def step(size, my_string):
    while len(my_string) > size or len(my_string) < size:
        print(f"You must enter a string of length {size}!")
        my_string = input("String: ")
        len(my_string)
    else:
        space = " "
        i = 0
        while i < size:
            print(space * i, my_string[i])
            i = i + 1

def rtriangle(size, my_string):
    while len(my_string) > size or len(my_string) < size:
        print(f"You must enter a string of length {size}!")
        my_string = input("String: ")
        len(my_string)
    else:
        dist = size - 1
        for i in range(1, size + 1):
            space = " "
            print(space * dist, my_string[-i:])
            dist = dist - 1

while True:
    if shape == "square":
        square(size, string)
        break
    elif shape == "ltriangle":
        ltriangle(size, string)
        break
    elif shape == "step":
        step(size, string)
        break
    elif shape == "rtriangle":
        rtriangle(size, string)
        break
    else:
        print(f"The shape {shape} is not a valid option")
        shape = input("Shape: ")