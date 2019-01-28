# namedtuple is an object like regular tuple but more readable. for readability we could use dictionaries but in that way we lose the immutability functionality of tuples and also there are lots of typing. so named tuples are a compromise
from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])  # the first value is the name and the second value (list) is the values of the tuples

color = Color(55, 155, 255)  # readable: it is a color!
white = Color(255, 255, 255)
black = Color(red=0, green=0, blue=0)  # defines each argument
gray = Color(green=55, red=55, blue=55)  # defines each argument

print(color.blue)  # more readble: instead of color[0]
