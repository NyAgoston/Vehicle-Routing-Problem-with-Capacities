# Vehicle-Routing-Problem-with-Capacities
## Description

CVRP is based on Vehicle Routing Problem with a limitaton, every vehicle has a capacity and every city has a demand.
## Solution
* First we select a vehicle city combination but there's a limitation. It will only work if the number of cities is dividable with the vehicles.
* The cities coordinates are randomly selected between 0 and 1000
* Demands are random values between 1 and 9. It is generated in a while loop until the sum of this array modus the num of vehicles is equals 0.
* the capaciti is determined by dividing the sum of capacities by the num of vehicles
* The starting order can be choosen in two ways
    * By the closest order when every cities neighbour is the closest to itself, its not the best but very close to it
    * Simply just generating a random order
* ![image](https://github.com/NyAgoston/Vehicle-Routing-Problem-with-Capacities/blob/main/img/1-10.png)

