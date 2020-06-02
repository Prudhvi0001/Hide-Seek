#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
    moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]
#Give Directions to the path
def directions(x1,y1,x2,y2):
    if x2==x1+1 and y2==y1:
        return 'S'
    elif x2==x1-1 and y2==y1:
        return 'N'
    elif x2==1 and y2==y1-1:
        return 'W'
    elif x2==x1 and y2==y1+1:
        return 'E'
    else:
        return ''
# Perform search on the map
def search1(IUB_map):
    # Find my start position
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    #Create an empty string for generating the path
    path = ''
    fringe=[(you_loc,0,path)]
    #An empty List to Keep Track of the visited moves 
    total_fringe =[]

    while fringe:
        total_fringe += fringe[:]
        (curr_move, curr_dist,curr_path)=fringe.pop(0)
        for move in moves(IUB_map,curr_move[0],curr_move[1]):
            if IUB_map[move[0]][move[1]]=="@":
                return str(curr_dist+1)+' '+curr_path+directions(*curr_move,*move)
            elif move not in (item for sublist in total_fringe for item in sublist):
                fringe.append((move, curr_dist + 1,curr_path+directions(*curr_move,*move)))
                
    return 'Inf'

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    print("Shhhh... quiet while I navigate!")
    solution = search1(IUB_map)
    print("Here's the solution I found:")
    print(solution)