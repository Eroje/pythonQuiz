# Test yourself Quiz

# Question 1 - Assigning Variables
x = 10
y = 3
print(x * y)
print(x + y)
print(x - y)
print(x / y)

# Question 2 - Create a list of even numbers from 0 t0 100
my_list = list(range(0, 101, 2))
print(my_list)

print(my_list[0:10]) # Print the first 10 elements of the list

print(len(my_list)) # Finding the length of the list

my_list.append(True) # Append a value to the list
print(my_list)

# Question 3 - Incorporate an If statement to find out if a number is divisible by 5
number = 835892
if number % 5 == 0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 5")

# Question 4 - Print number 0 to 5 Using a For Loop
for i in range(6):
    print(i)

# Question 5 - Draw a pentagon Using Turtle
# import turtle
#
# for i in range(5): # A pentagon has five sides!
#     turtle.right(72) # This is the angle needed to produce a pentagon
#     turtle.forward(200) # This will give the length of the pentagon size
# turtle.done()

# Question 6 - Functions (Create a pythagorean triple)
def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(pythagorean_triple(3, 4, 5))
print(pythagorean_triple(3, 9, 15))

# # Question 7 - Plotting
# import matplotlib.pyplot as plt
# list1 = [1, 6, 13, 16, 24]
# list2 = [3, 7, 17, 28, 30]
# plt.plot(list1, list2, c="blue", linewidth=1, label="A Line!", linestyle="dashed",
#          marker='s', markerfacecolor="purple", markersize=2)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Python Plot of a Line")
# plt.legend()
# plt.show()

import turtle

turtle.bgcolor("grey") # Background colour
turtle.pensize(2) # pen size
turtle.color("red")
turtle.speed(0)

for i in range(12):
    for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(5)
turtle.done()







