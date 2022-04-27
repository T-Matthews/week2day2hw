#FUNCTION EXERCISE: Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names
first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

def combine_names(first_names,last_names):
    combined_names=[]
    for i in range(len(first_names)):
        combined_names.append(first_names[i]+" "+last_names[i])
    print(combined_names)
    

combine_names(first_name,last_name)



#EXERCISE 1: Given a list as a parameter,write a function that returns a list of numbers that are less than ten
#For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]
mylist=[1,11,14,5,8,9]
def sort_by_size(user_list):
    ordered_list=[]
    for i in user_list:
        if i<10:
            ordered_list.append(i)
            
    ordered_list = sorted(ordered_list)
    
    print(ordered_list)
    return ordered_list
    


sort_by_size(mylist)


#Exercise 2:Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def list_merge(list1, list2):
    print(sorted(list1+list2))
    return sorted(list1+list2)


list_merge(l_1,l_2)
    
