#tuples are immutable
from collections import namedtuple

#color = (55, 155, 255) #tuple
#color = { 'red': 55, 'green': 155, 'blue': 255 } #dictionary

#named Tuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
#color = Color(red = 55, green = 155, blue = 255)
color = Color(55, 155, 255)

print(color[0])
print(color.red)