"""
Given a string, that contains a special character together with alphabets 
('a' to 'z' and 'A' to 'Z'), reverse the string in a way that special 
characters are not affected.

Ex:
Input:   str = “a,b$c”
Output:  str = “c,b$a”
Explanation: Note that $ and , are not moved anywhere.  Only subsequence “abc” is reversed

Input:   str = “Ab,c,de!$”
Output:  str = “ed,c,bA!$”

list of characters
traverse each char in list
if char is a-z or A-Z, add it to a temporary list
traverse each char again and replace char from temp list in reverse order


"""

def reverse_string(input):
    temp = []
    output = []
    for char in input:
        if char.isalpha():
            temp.append(char)
    
    i = len(temp)
    for char in input:
        if char.isalpha():
            output.append(temp[i-1])
            i -= 1
        else:
            output.append(char)
    print("".join(output))
    return "".join(output)

def reverse_string_efficient(text):
    """
    have a pointer at last and start
    traverse outer loop from last char till mid
    if alpha found, traverse input from start till 
    alpha found and replace this aplha with alpha 
    in the end.
    """
    input = list(text)
    first=-1
    for last in range(len(input)-1,int(len(input)/2),-1):
        if input[last].isalpha():
            while True:
                first += 1
                if input[first].isalpha():
                    temp = input[last]
                    input[last] = input[first]
                    input[first] = temp
                    break
                
    print("".join(input))
    return "".join(input)


if __name__ == '__main__':
    input1 = "a,b$c"
    output1 = reverse_string(input1)
    print(output1 == "c,b$a")

    input2 = "Ab,c,de!$"
    output2 = reverse_string(input2)
    print(output2 == "ed,c,bA!$")

    print(reverse_string("") == "")

    print("======")
    # print(reverse_string_efficient(input1) == "c,b$a")
    print(reverse_string_efficient(input2) == "ed,c,bA!$")