# reverse a string without using string slices or inbuilt methods

def reverse(string):
    word = ""
    for char in string:
        word = char + word
        # print(char)
        print(word)
    return word
        
        
print(reverse('hello'))
        