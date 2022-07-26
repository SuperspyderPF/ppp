#question 1
def hello_username(username):
    
    print(" Hello, " + username + '!')
    
username=input('username input')
hello_username(username)





## question 2
num_list = list(range(1, 10)) 
 
even_nums = [100] 

def first_odds(): 
    for x in num_list:  
        if x % 2 == 0:         
              even_nums.append(x) 
        else:        
              odd_nums.append(x) 
    
    
print(even_nums) 
[2, 4, 6, 8] 
print(odd_nums) 
[1, 3, 5, 7, 9] 

##

#question 3 


def max_num_in_list(list1):

    maximum=list1[0]
    for index in range(len(list1)):
        if list1[index] > maximum:
            maximum = list1[index]
    return maximum

list1 = [3,6,9,12,44]
print(max_num_in_list(list1))

#question 4
a_year = int(input("Enter the Year to be checked: "))
def is_leap_year(a_year)
if (( input_year%400 == 0)or (( input_year%4 == 0 ) and ( input_year%100 != 0))):
    print("%d is Leap Year" %input_year)
else:
    print("%d is Not the Leap Year" %input_year)

#question 5
def is_consecutive(a_list):
   if len(a_list) < 1:
      return False
   min_val = min(a_list)
   max_val = max(a_list)
   if max_val - min_val + 1 == len(a_list):
      for i in range(len(a_list)):
         if a_list[i] < 0:
            j = -a_list[i] - min_val
         else:
            j = a_list[i] - min_val
            if a_list[j] > 0:
               a_list[j] = -a_list[j]
            else:
               return False
      return True
   return False
a_list = [6, 8, 3, 5, 4, 7]
print(is_consecutive(a_list))