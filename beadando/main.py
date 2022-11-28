from plot import *
from cvrp import *

def main():
    il_order,vehicles,object_f,demands,vrp_dict,cities = initData(20,200)
  
    printRoutes(il_order,vehicles,object_f,demands,vrp_dict,cities)
main()