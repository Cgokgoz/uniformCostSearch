# uniformCostSearch
Uniform-Cost Search Algorithm
Uniform-cost search is a searching algorithm used for traversing a weighted tree or graph.[1]
When each edge has different cost we can use UCS. The goal of UCS finding the path with the
lowest cost. In the algorithm used to achieve the goal of UCS, the costs of the paths of neighboring
nodes are checked starting from the root node, and the least costly path is selected. The cost of the
paths of all neighboring nodes encountered until the target node is reached is calculated and the path
with the lowest cost is selected. A uniform-cost search algorithm is implemented by the priority
queue, it gives maximum priority to the lowest cumulative cost. [2]

Advantages :
• UCS algorithm guaranteed to find the least-cost solution. (Ensures optimal)

Disadvantages :
• When searching in Ucs, the number of steps is ignored, only low cost is taken into
account.This can lead the algorithm into an infinite loop
• Exponential storage required.[3]

Before creating a graph in this assigment, I take the csv file containing the data as input and
check whether there is a valid file. Then I read the file and divided the data into necessary pieces
(and skip the header) to create the graph. Using dictionary in python, I added cities to the dictionary
by associating the distances between cities and created the graph structure. I asked the user for the
root node and the targeted node as input. I checked whether the incoming inputs are valid, If not, I
asked them to enter a valid input (city). I have given the incoming inputs and the graph structure I
created to the uniform_cost_search function as a parameter. I used the Priority Queue structure for
UCS in the uniform_cost_search function. In order to calculate the path, the starting city coming
from the user was added to the Priority Queue with "0" priority. Ensure that all nodes that need to
be visited are visited until they reach the end city node and were get from queue according to the
distance between cities. In this order, it created the path with the nodes get from the queue. I printed
path and cost in the terminal.

References :
[1] , [2] : https://www.javatpoint.com/ai-uninformed-search-algorithms
[3] : https://www.cs.utexas.edu/users/novak/cs381k57.html
