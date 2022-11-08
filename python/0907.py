# comment
"""
multiline comment
"""
    
def checkPi(pi):
    if pi == 3.14:
        print("pi is 3.14")
    elif pi == 3:
        print("pi is 3")
    else:
        print("bad....")

pi = 3 # pi inside main hides this variable
def main():
    pi = 22/7
    checkPi(pi)
    
    list1 = [1,2,3,4, "5",[6,7,8]]
    print(list1)
    list2 = [9,10,11]
    list3 = list1 + list2
    print(list3)
    str1 = "dsfsg"
    print(str1[0])
    
    for element in list3:
        print(element)
        element = 2
        
    for index in range(len(list2)):
        print(list2[index])
        list2[index] = 2
        
    print(list2)
    
    if 2 in list2: print("YAY")
if __name__ == "__main__":
    main()
    
str1 = '"String"'
str2 = "'String'"
str3 = """multiline 
string"""

print(str1,str2,str3)

str4 = str1 + " " + str2

print(str4)

str5 = str1 + " " + str(pi)

print(str5)
