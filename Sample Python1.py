# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red","green")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)



# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

###################################

from prettytable import PrettyTable  

table = PrettyTable()
 
table.add_column("Pokemon name",["Pikachu","Squirtle","Charmender"])
table.add_column("Type",["Electric","Water","Fire"])
table.add_column("Strr",["alpha","beta","gamma"])

table.align = "l"
print(table)

