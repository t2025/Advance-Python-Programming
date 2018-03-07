#list operations 
arr=[]
size=int(input("Enter the nunber of elements you want to insert in list"))
#insert operation
def insert():
    for i in range(0,size):
        t=int(input("Enter the number"))
        arr.append(t)
    print(arr) 
insert()
#Add the element at beinning

def add_elelment():
    number=int(input("Enter the number to be inserted"))
    position=int(input("Enter the position"))
    arr.insert(position,number)
    print(arr)                      
add_elelment()    

#search an element into list
def search_element():
    num=int(input("Enter the number you want to search in the list"))
    for i in range(0,size+1):
        if(arr[i]==num):
            print("Found")
            print(i)
            break
        else:
            print("Not found")
search_element()            
#Checking if two lists are equal or not
arr1=[]
sz=int(input("Enter the number of elements you want to insert"))
def insert_second():
    for i in range(0,sz):
         num1=int(input("Enter number"))
         arr1.append(num1)
    if size==sz:
        for i in range(0,size):
            if (arr[i]==arr1[i]):
                print("Matched")
            else:
                print("Not matched")      
insert_second ()   
#Sorting lists
def sort():
    print(arr.sort())
    print(arr1.sort())

