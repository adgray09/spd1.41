# Q: Given a list of n numbers, determine if it contains any duplicate numbers.


def duplicate_numbers(arr, size): 
    print("The repeating numbers are: ") 

    for i in range(0, size): 
        if arr[abs(arr[i])] >= 0: 
            arr[abs(arr[i])] = -arr[abs(arr[i])] 
        else: 
            print (abs(arr[i]), end = " ") 
            
def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        print('fizzbuzz')
    elif input % 3 == 0:
        print('fizz')
    elif input % 5 == 0:
        print('buzz')
    else:
        print(input)
    
        
fizz_buzz(15)
numbers = [1,1,3,4,5,6,6,7,7]

duplicate_numbers(numbers,9)