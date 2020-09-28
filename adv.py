# from room import Room
# from player import Player
# from world import World

# import random
# from ast import literal_eval


# # Load world
# world = World()


# # You may uncomment the smaller graphs for development and testing purposes.
# # map_file = "maps/test_line.txt"
# # map_file = "maps/test_cross.txt"
# # map_file = "maps/test_loop.txt"
# # map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# # Loads the map into a dictionary
# room_graph=literal_eval(open(map_file, "r").read())
# world.load_graph(room_graph)
# print(room_graph)

# # Print an ASCII map
# world.print_rooms()

# player = Player(world.starting_room)
# print("player.current_room: ",player.current_room)
# print("player.current_room.id: ", player.current_room.id) 
# print("player.current_room.get_exits(): ", player.current_room.get_exits()) 
# # print(player.travel('n'))

# # Fill this out with directions to walk
# # traversal_path = ['n', 'n']
# traversal_path = []
# # used to keep track of the direction we have just come from
# back_track = {"n": "s", "s": "n", "e": "w", "w": "e"}
# # keep track of the path we are currently exploring
# cur_path_tracker = []
# # key = current_room.id, value = current_room.get_exits()
# visited = {}

# visited[player.current_room.id] = player.current_room.get_exits()


# while len(visited) < len(room_graph) - 1:

#     if player.current_room.id not in visited:
#         visited[player.current_room.id] = player.current_room.get_exits()
#         # random.shuffle(visited[player.current_room.id])
#         last = cur_path_tracker[-1]
#         # print(last)
#         visited[player.current_room.id].remove(last)
#         # print(visited)

#     # will pop last remaining direction off to travel in that direction
#     while len(visited[player.current_room.id]) < 1:
#         cur_direction = cur_path_tracker.pop()
#         # print(cur_direction, traversal_path)
#         traversal_path.append(cur_direction)
#         player.travel(cur_direction)
    
#     direction = visited[player.current_room.id].pop(0)
#     # traversal_path.append(direction)
#     cur_path_tracker.append(back_track[direction])
#     print(direction, back_track[back_track[direction]])
#     player.travel(direction)

# # print(visited)
# # TRAVERSAL TEST - DO NOT MODIFY
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# # player.current_room.print_room_description(player)
# # while True:
# #     cmds = input("-> ").lower().split(" ")
# #     if cmds[0] in ["n", "s", "e", "w"]:
# #         player.travel(cmds[0], True)
# #     elif cmds[0] == "q":
# #         break
# #     else:
# #         print("I did not understand that command.")

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
print(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print("player.current_room: ",player.current_room)
print("player.current_room.id: ", player.current_room.id) 
print("player.current_room.get_exits(): ", player.current_room.get_exits()) 
# print(player.travel('n'))

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# used to keep track of the direction we have just come from
back_track = {"n": "s", "s": "n", "e": "w", "w": "e"}
# keep track of the path we are currently exploring
cur_path_tracker = []
# key = current_room.id, value = current_room.get_exits()
visited = {}

visited[player.current_room.id] = player.current_room.get_exits()

def get_neighbors():
    return player.current_room.get_exits()

def dft(starting_vertex, visited=set()):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.

    This should be done using recursion.
    """
    path = []
    if starting_vertex in visited:
        return
    else:
        visited.add(starting_vertex)
        path.append(starting_vertex)
        neighbors = get_neighbors()

        if len(neighbors) == 0:
            return None

        for neighbor in get_neighbors():
            dft(neighbor, visited)
    return path

print("skdljfalsjdf: ",get_neighbors())
print("LKSDFJALKSDJF: ", dft(player.current_room.id))

# print(visited)
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
