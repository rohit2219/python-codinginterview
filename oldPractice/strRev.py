# Function to print reverse of the passed string
import copy
def reverse(string,temp=''):
    if len(string) == 0:
        print('return temp:',temp)
        return temp

    print('recursion temp:',temp,'--string:',string)
    temp = temp + string[-1:]
    return reverse(string[:-1],temp)

# Driver program to test above function
string1 = "Hello How are you sir"
print('return reverse',reverse(string1))
