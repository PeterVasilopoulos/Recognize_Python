num1 = 42 # variable declaration, initialize int
num2 = 2.3 # variable declaration, initialize float
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable delcaration, initialize tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access list value
pizza_toppings.append('Mushrooms') # add list value
print(person['name']) # log statement, access dictionary value
person['name'] = 'George' # change dictionary value
person['eye_color'] = 'blue' # append dictionary value
print(fruit[2]) # log statement, access tuple value

if num1 > 45: # if statement
    print("It's greater") # log statement
else: # else statement
    print("It's lower") # log statement

if len(string) < 5: # if statement, string length check
    print("It's a short word!") # log statement
elif len(string) > 15: # else if statement, string length check
    print("It's a long word!") # log statement
else: # else statement
    print("Just right!") # log statement

for x in range(5): # for loop, variable declaration
    print(x) # log statement
for x in range(2,5): # for loop, variable declaration
    print(x) # log statement
for x in range(2,10,3): # for loop, variable declaration
    print(x) # log statement
x = 0 # varaible declaration, initialize int
while(x < 5): # while loop start, while loop stop
    print(x) # log statement
    x += 1 # while loop increment

pizza_toppings.pop() # delete list value
pizza_toppings.pop(1) # delete list value

print(person) # log statement, access dictionary value
person.pop('eye_color') # delete dictionary value
print(person) # log statement, access dictionary value

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # if statement
        continue # if continue statement
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if statement
        break # for loop break

def print_hello_ten_times(): # function declaration
    for num in range(10): # for loop
        print('Hello') # log statement

print_hello_ten_times() # run function

def print_hello_x_times(x): # function declaration, function parameter
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # run function, function argument

def print_hello_x_or_ten_times(x = 10): # function declaration, function parameter
    for num in range(x): # for loop
        print('Hello') # log statment

print_hello_x_or_ten_times() # run function
print_hello_x_or_ten_times(4) # run function, function parameter


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)