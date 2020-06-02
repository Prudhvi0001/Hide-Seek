####                                             Part - 1 Finding your Way                                                                                   

According to the Given map:

Initial State:
The Starting state of the given map

✔	  ✔	  ✔	  ✔	 🕍	🕍   🕍

✔	 🕍  🕍	 🕍	 ✔	 ✔	 ✔

✔	  ✔	  ✔	 ✔	 🕍	 ✔   ✔	

✔	 🕍  ✔	 🕍	 ✔	 ✔ 	 ✔

✔	 🕍   ✔	 🕍	 ✔	🕍   ✔

🤷‍♂️  🕍` ✔  ✔	  ✔	 🕍	 🏯

Goal State:
Reaching the Goal in an optimal pat

✔	  ✔	  ✔	 ✔	 🕍	🕍	🕍

✔	 🕍	🕍	🕍	 ✔	 ✔   ✔

🛴	 🛴	🛴	 ✔	 🕍	 ✔  ✔	

🛴	 🕍	🛴	🕍	🛴	🛴 	🛴

🛴	 🕍	🛴	🕍	🛴	🕍   🛴

🤷‍♂️ 🕍`🛴 🛴	🛴	🕍	🏯

Valid States :

To move one step at a time to the ✔ Position from the position where your are in any direction.

Cost Function:

Let the cost be 1 for every move you go from the Point where you are

Successor Moves:

(All the valid positions from the given location in any direction) - (Already Visited positions)

### 3.Error in the Given code:

​                     The Given code is using Stack implementation for finding the Successor moves. and Taking all the possible moves from a given location which is causing it to enter an Infinite loop. Which is causing the Program to run forever. 

For example:

✔	  ✔	  ✔	   ✔	🕍	🕍   🕍

✔	 🕍	  🕍	🕍	✔	 ✔	 ✔

✔	  ✔	  🌊   🌊	🕍	 ✔   ✔	

✔	  🕍  🌊    🕍	✔	 ✔ 	 ✔

✔	  🕍   ✔ 	🕍	✔   🕍   ✔

🤷‍♂️  🕍`  ✔	 ✔	 ✔	🕍	 🏯

While Using Stack the positions at 🌊 are getting Looped endlessly. This is nothing but a Depth First Search Model.

We can overcome this effect by Tracking the visited nodes and Giving the successor function only the childs  which are not visited.

But, This has a side effect of not getting the optimal path when the Goal state has multiple paths.

*****We can overcome this by using Breadth First search model, Where we use queue (FIFO) data structure for the successor function and by keeping track of the visited nodes.

### 4.Path Implementation

​			I added an extra Function to the given code to return Directions based on the current move as 

```python
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
```

As the BFS keep tracks of the path until it reaches the Goal State. 

By taking a empty string and appending the direction to the path we can keep track of the path. we can be returned at the END.

###                                    

### 								  Part - 2 Hide and Seek

In this We will use Depth First Search Algorithm to find the solution.

- find '.' and replace with 'F'
- Find '.' where it doesn't conflict with previous 'F'.
- Iterate until Goal State is reached By Keeping track of the already visited states.

###### **State space**

All the possible moves and states of the map for the given conditions.
It will be in the form of tree with all the successor states attached to its parent state

###### **Initial state**
The starting state of the given map

✔	  ✔	  ✔	   ✔	🕍	🕍   🕍

✔	 🕍   🕍	🕍	✔	 ✔	 ✔

✔	 ✔	   ✔	✔	🕍	 ✔   ✔	

✔	  🕍	✔	🕍	 ✔	 ✔ 	 ✔

✔	  🕍	✔	🕍	 ✔	🕍   ✔

🤷‍♂️  🕍`  ✔	 ✔	 ✔	 🕍	 🏯

###### **Goal state**

For K=6 where all the friends are placed without conflicts

🤦‍♂️	✔	  ✔	   ✔  🕍  🕍   🕍

✔	  🕍	🕍	🕍	 ✔	  ✔	  ✔

✔	  ✔	    ✔	🤦‍♂️ 🕍   ✔   ✔

✔	  🕍	✔	🕍	 ✔	 🤦‍♂️	✔

✔     🕍  🤦‍♂️	🕍	  ✔	   🕍  🤦‍♂️

🤷‍♂️  🕍`  ✔	 ✔	 🤦‍♂️	🕍	🏯

###### **Successor function**

All possible places to place the Next friend on the board without conflicts.

###### **Cost function**

Cost function is same for all the moves, Which can be taken as '1' for each move.                    







