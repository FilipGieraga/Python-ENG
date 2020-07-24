# Random walk with steps program consists of several functions that are related to the random walk concept. Inspired by the Socratica channel on YT

Requirements: Python 3, random module, turtle module

# Random_walk (n):
The random_walk(n) function is the backbone of the program and only retrieves the number of steps from the user.
After performing these steps, it returns us the x and y coordinates and the absolute value of the path traveled.

# max_min_steps (number_of_walks, steps_taken):
The max_min_steps (number_of_walks, steps_taken) function simulates a walk with a fixed number of steps,
given number of times. The distances of individual walks are stored in the variable distances_walked, which is a set.
The program returns us the minimum and maximum absolute value of the distance traveled for the given number of walks.



# walk_loop (number_of_walks, walk_lengths_range, distance_limit):
The walk_loop(number_of_walks, walk_lengths_range, distance_limit) function determines how often it would be needed to take a transport
back home from walked distance. It will be needed whenever the absoulte distance traveled is
longer than distance_limit.
In this function we also have a variable number_of_walks which determines how many times the walks will be performed
for a single walk size.
The variable walk_lengths_range is the length range of our walks from one to the given length. <br>
Example: <br>
number_of_walks = 1000 <br>
walk_lengths_range = 100 <br>
distance_limit = 10 |
For each walk length from 1 to 100 steps, the walks will be simulated 1000 times. If absolute
distance from home is less than or equal 10, the variable no_transport will be incremented, initial
value of no_transport for each walk distance is zero. After the last walk made for a specific amount of
steps, we will be given the percentage of walks from which we do not need a taxi for all walk sizes.


# draw_random_walk (n, forward, pointer, speed):
The draw_random_walk (n, forward, pointer, speed) function is my favorite in this program and it draws us a random walk
based on the adopted parameters. <br>
n- is the number of steps to be drawn <br>
forward- is the length of a single step in pixels <br>
pointer- is the size of the dot that is placed at the beginning (red) and at the end (blue) in pixels <br>
speed- drawing speed

## Disclaimer:
All functions are hashed, to run them, delete # in the right place
