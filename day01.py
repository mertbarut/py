# ex01

print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')
print('Anothor line\n')

# ex02

print("I could have code like this.") # comment ignored

# print("This won't run.")

print("This will run.\n")

# ex03

print("I will now count my chickens:\n")

print('Hens', 25.0 + 30.0 / 6)
print('Rooster', 100.0 - 25.0 * 3.0 % 4.0, '\n')
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)
print("Is it true that 3 + 2 < 5 - 7?\n")
print(3.0 + 2.0 < 5.0 - 7.0)

print("What is 3 + 2?", 3.0 + 2.0)
print("What is 5 - 7?", 5.0 - 7.0)

print("Oh, that's why it's False.")
print("How about some more.")

print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)

d = 5
print(d * 2 * 3.14)

# ex04

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available") 

#ex04

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny? {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# ex07

print("Mary had a little lamb.")
print("Its fleece was white as {}".format('snow'))
print("And everywhere that Mary went.")
print('.' * 10)

end1 = "Cheese"
end2 = "Burger"

print(end1, end = " ")
print(end2)

# ex08

formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))

# ex09

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, 6.
""")
