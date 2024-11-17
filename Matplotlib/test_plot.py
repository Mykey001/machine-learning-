import matplotlib.pyplot as plt

# importing numpy to get data for our plots

import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)

print(x)
print(y)
print(z)


# Plotting the data

#       Sine wave

plt.plot(x,y)
plt.show()


#       Cosine Wave


plt.plot(x,z)
plt.show()

# Adding title  , x - axis  & y - axis labels 

plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sin value')
plt.title('Sine Wave')
plt.show()

plt.plot(x,z)
plt.xlabel('angle')
plt.ylabel('Cos value')
plt.title('Cosine Wave')
plt.show()


#   Parabola

import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(-10, 10, 20)
y = x**2

# Plot the curve
plt.plot(x, y)
plt.show()

# Plot with red '+' markers
plt.plot(x, y, 'r+')
plt.show()


x = np.linspace(-5,5,50)
plt.plot(x,np.sin(x), 'g--')
plt.plot(x,np.cos(x), 'r+')
plt.show()

# Bar plot

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
languages = ['English', 'French', 'Swahili', 'latin', 'German']
people = [100,50,150,40,70]
ax.bar(languages , people)
plt.xlabel('LANGUAGES')
plt.ylabel('NUMBER OF PEOPLE')
plt.show()