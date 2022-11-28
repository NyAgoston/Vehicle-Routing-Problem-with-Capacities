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
## Examples
* 1 vehicle 10 city (TSP)
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/1-10.png)
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/1-10r.png)
* 2 vehicle 10 city
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/2-10.png)
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/2-10r.png)
* 4 vehicle 20 city
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/4-20.png)
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/4-20r.png)
* 5 vehicle 20 city
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/5-20.png)
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/5-20r.png)
* 10 vehicle 50 city
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/10-50.png)
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/10-50r.png)
* 20 vehicle 200 city
    - ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/20-200.png)
## Sources
* https://ai.leventefazekas.hu/lessons/2022-10-11-travelling-salesman/
* https://ai.leventefazekas.hu/lessons/2022-10-16-simulated-annealing/
## Simulated Annealing
* For the base program i'am using the linear multiplicative cooling strategy
* I compared it with the Logarithmical multiplicative strategy
## Conclusion
The more cities and vehicles we are working with the harder it is to fulfill the demand limitation. The problem comes because the demands are auto generated therefor not every solution will be good.