import random
import turtle


def random_walk(n):
    x=0
    y=0
    for i in range(n):
        step=random.choice(["N","S","E","W"])
        if step=="N":
            y=y+1
        elif step=="S":
            y=y-1
        elif step=="E":
            x=x+1
        else:
            x=x-1
    return x,y




def max_min_steps(number_of_walks,steps_taken):
    """Takes number of walks with a fixed steps taken and returns longest and shortest walk"""
    distances_walked=set()
    for i in range(number_of_walks):
        walk=random_walk(steps_taken)
        print(f"Observation: {i+1}, Cordinates: {walk}, Distance from home: {abs(walk[0])+abs(walk[1])}")
        distance_walked= abs(walk[0])+abs(walk[1])
        distances_walked.add(distance_walked)
    print(f"Min absolute distance walked:{min(distances_walked)}")
    print(f"Max absolute distance walked:{max(distances_walked)}")




def walk_loop(number_of_walks,walk_lenghts_range,distance_limit):
    """Determins how often you'll need a transport from the walk,
    it will be needed always once absolute distance is bigger than distance_limit variable"""
    for walk_length in range(1,walk_lenghts_range+1):
        no_transport=0
        for i in range(number_of_walks):
            (x,y)=random_walk(walk_length)
            distance=abs(x)+abs(y)
            if distance<=distance_limit:
                no_transport+=1
        no_transport_percantage= float(no_transport)/ number_of_walks
        print(f"Walk size = {walk_length}, % of no transport = {100*no_transport_percantage}")




def draw_random_walk(n,forward,pointer,speed):
    """Draws a random walk"""
    make = turtle.Turtle()
    x = 0
    y = 0
    make.dot(pointer,'red')
    make.speed(speed)
    for i in range(n):
        step = random.choice(["N", "S", "E", "W"])
        if step == "N":
            y = y + 1
            make.setheading(90)  # UP
            make.forward(forward)
        elif step == "S":
            y = y - 1
            make.setheading(270)  # DOWN
            make.forward(forward)
        elif step == "E":
            x = x + 1
            make.setheading(0)  # RIGHT
            make.forward(forward)
        else:
            x = x - 1
            make.setheading(180)  # LEFT
            make.forward(forward)
    make.dot(pointer, 'blue')
    make.end_fill()
    turtle.done()
    print(f"({x},{y}), Distance from home: {abs(x) + abs(y)}")
    return x, y

#####--------- draw_random_walk(steps,line length for each step,point size for start and end,speed)
#Function to draw random walk in turtle module below:
# draw_random_walk(100,50,5,6)



number_of_walks=1000
# for each walk_length in walk_lengts_range, the number of walks will be executed
walk_lengths_range=100
# start from one and goes to walk_lengt_range
distance_limit=10
# once the distance limit is surpassed at the end of each walk, you need a transport back to start point
#####--------- walk_loop(number_of_walks,walk_lengts_range,distance_limit)
# walk_loop(number_of_walks,walk_lengths_range,distance_limit)


#####--------- x,y=random_walk(steps_to_take)
# x,y = random_walk(100)
# print(f"({x},{y}), Distance from home: {abs(x) + abs(y)}")


#####--------- max_min_steps(number_of_walks,steps_taken)
# max_min_steps(100,100000)

