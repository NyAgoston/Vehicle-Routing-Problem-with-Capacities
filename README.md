# Vehicle-Routing-Problem-with-Capacities
## Description

CVRP is based on Vehicle Routing Problem with a limitaton, every vehicle has a capacity and every city has a demand.
## Solution
* First we select a vehicle city combination but there's a limitation. It will only work if the number of cities is dividable by the number of vehicles.
* The cities coordinates are randomly selected between 0 and 1000
* Demands are random values between 1 and 9. It is generated in a while loop until the sum of this array modus the num of vehicles is equals 0.
* the capaciti is determined by dividing the sum of demands by the number of vehicles
* The starting order can be selected in two ways
    * By the closest order when every cities neighbour is the closest to itself, its not the best but very close to it
    * Simply just generating a random order
* The solution requires an array that countains the distances between every city combinations
* If we have everything we than the neighborhood_search function is called with the lesser optimal order
* Inside neighborhood_search random indexes are switched and if the orders lenght after the switching is less than the current orders, then we keep the changes.
    * Inside the if statement the demands are checked, we pass the order and the two generated indexes to a function, it creates an n dimensional array, and if the sub arrays demands that contains the 2 indexes are over the capaciti ten it returns false
    * Simulated annealing is used here, if the random number is less than the Pt than we accept the less optimal solution
* The final optimal order is plotted using matplotlib
## Example
* 1 vehicle 10 city (TSP)
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/1-10.png)
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/1-10r.png)

