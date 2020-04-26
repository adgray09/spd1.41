# Q1: Decode the 8 bit binary (base 2) number 1110 1100 into 
# its equivalent decimal (base 10) value. 
# Upload a picture or text file showing your work.

# number = 4+8+32+64+128
# print(number)
#Answer = 236

# Q2: Encode the decimal (base 10) value 34 into its 
# equivalent binary digits (base 2). Upload a picture or text file 
# showing your work.

#64 exceeds 34 so 32 is our first 1 
#34 -> 32
#34 - 32 = 2
# 128 64 [32] 16 8 4 [2] 1 
#       0  1  0  0  0  1

#Answer = 100010

# Q3: Decode the hexadecimal (base 16) value 0xC4A into its 
#equivalent decimal (base 10) value. Upload a picture
#or text file showing your work.

# A times 1 is 10
# 4 times 16 is 64
# C times 16 times 16 is 3072 
# 10 + 64 + 3072 is 3146 
# answer = 3146

# Q4: Encode the decimal (base 10) value 79 into its equivalent 
# hexadecimal (base 16) digits. Upload a picture or text 
# file showing your work.

# F = 15
# 4 times 16 is 64
# 64 + 15 = 79
# answer = 4F

#Q5: 
def compute_sum(n):
    for i in range(0, n):
        n = n + i
    return n

print(compute_sum(4))



# Q5.1: base case is checking if n equals 1
# need to know how large n equals then need to run recursive part until 
# n equals 1, once it equals one return 1 to break recursive part

def recursive_compute_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_compute_sum(n-1)

# base case is checking if n equals 1

print(recursive_compute_sum(6))

# Q6: Describe how binary search works using pseudocode

# we begin at middle of the data structure setting a middle variable 
# have a variable for the first and last index
# we then check if desired item is less than or greater than middle
# this halves the search time

# Q6.1: Why is binary search so much more efficient than linear or sequential search?

# it is much more effiecient because it doesn't need to search the entire structure
# but rather it searches half of the structure
# where as linear you have to start from the first index on

    


