from plot import *
from cvrp import *

def main():
    il_order,vehicles,object_f,demands,vrp_dict,cities = initData(1,10)
  
    printRoutes(il_order,vehicles,object_f,demands,vrp_dict,cities)
main()