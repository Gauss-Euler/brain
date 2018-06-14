# "brain" is stored as a map/tree of connections between cells
import matplotlib.pyplot as plt
import numpy as np
import time


def ask_for_int(x, y, extra=None):
    """Prompt for integer value. x :: lower bound ~~
    y :: upper bound. ~~ extra :: extra string to add
    in prompt."""

    # Repeatedly prompt if condition not satisfied
    while True:
        if extra is not None:
            print(extra)
        my_var = input("Enter an INTEGER between "
                       "{} and {} inclusive ::: ".format(x, y))
        print("You entered: " + str(my_var))

        # check if my_var condition is satisfied (INT and range)
        if str(my_var).isdigit():
            if int(my_var) in range(x, y + 1):
                my_var = int(my_var)
                # break loop since condition is satisfied
                break
        else:
            pass  # keep the question loop going
    # return the variable, (integer between x and y)
    return my_var


def get_link_from_user(n):
    """ask user for (x,y) link 'n' times"""
    links = []
    for _ in range(0, n):
        # loop till user gives digits.
        while True:
            print("add a link: enter mem_x, mem_y")
            mem_x = input("mem_x = ")
            mem_y = input("mem_y = ")

            if mem_x.isdigit() and mem_y.isdigit():
                break

        link = (int(mem_x), int(mem_y))  # tuple that will be appen to memory map
        links.append(link)
    return links


def add_link_to_map(links, memory_map, p):
    """ adds given links (list of tuples) to main memory map (list)
        print memory map if 'p' argument is True"""

    print("adding links: {} to the memory_map".format(links))
    for _ in links:
        mem_map.append(_)
    # display if p == True
    if p == True:
        print("Memory map: {}".format(mem_map))


def display_network(memory, memory_map):
    # plt.plot([1, 2, 3], [-5, 2, 20], 'ro')
    # plt.plot([1, 1, 1], [-5, 2, 20], 'bo')
    theta = 360 / len(memory)
    mem_pts = {}    # dictionary to link mem cells to points
    fig = plt.figure(figsize=(7, 7))

    # make dictionary linking memory cells and points in a circle
    # keys: memory cells. values: coordinates
    # 1: (1.0,0) 2: (a,b)
    for i in range(0, len(memory)):
        mem_pts[memory[i]] = (np.cos((np.pi / 180) * theta * i),
                              np.sin((np.pi / 180) * theta * i))
    print("mem_pts: {}".format(mem_pts))
    # plot the points of memory.
    for values in mem_pts.values():
        plt.plot(values[0], values[1], 'bo')

    # plot the connections. take link from memory map and plot line segment.
    for link in memory_map:
        m1, m2 = link[0], link[1]
        p1, p2 = mem_pts[m1], mem_pts[m2]

        plt.plot([p1[0], p2[0]], [p1[1], p2[1]])

        print("plotting ({},{})".format((p1[0], p1[1]), (p2[0], p2[1])))

    plt.show()

    # for con in mem_map:
    # link = (2,3)      mem_ptslink[0]


# get memory size using ask_for_int()
mem_size = ask_for_int(1, 50, "For MEMORY size, ")

# create memory list size of mem_size
mem = list(range(1, mem_size + 1))

# show memory ex: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... ]
print("Memory: {}".format(mem))

# links of size 2,3,4.. are distinct but the link (1,2,3) should
# be related to (1,2)
# input should be only I or O

mem_map = []  # map of the memory with links

num_links = ask_for_int(1, 100, "For NUMBER OF LINKS, ")
user_links = get_link_from_user(int(num_links))

add_link_to_map(user_links, mem_map, True)

display_network(mem, mem_map)

# inp = input("Give Input ::: ")
# print(inp)
