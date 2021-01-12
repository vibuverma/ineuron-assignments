#----------------------------------------------------------------------------------------------------------------------------------------
# Answer 1.1
class one:
    def __init__(self, a, b, c):
        self.a= float(a)
        self.b= float(b)
        self.c= float(c)
a= int(input("a= "))
b= int(input("b= "))
c= int(input("c= ")) 


class two(one):
    def __init__(self, a, b, c):
        super().__init__(a,b,c)

    def area(self):
        s= (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

t= two(a,b,c)
print("Area: {} ".format(t.area()))

#----------------------------------------------------------------------------------------------------------------------------------------
# Answer 1.2
def longwords(wordlist, length):
    return (word for word in wordlist if len(word) >= length)

def main():
    words = input("Enter words, separated by spaces: ").split()
    length = int(input("Minimum length of words to keep: "))
    print("Words longer than {} are {}.".format(length,
          ', '.join(longwords(words, length))))

main()

#----------------------------------------------------------------------------------------------------------------------------------------
# Answer 2.1
def map_length(List):
    
    return list(map(len, List))

word_list=list(input(" Enter Words : ").split(","))

list_1=[x.strip() for x in word_list]

word_length=map_length(list_1)

print("Length of Words are :",word_length )

#----------------------------------------------------------------------------------------------------------------------------------------
# Answer 2.2
def check_vowel(inputChar):
    return_value=''
    if(len(inputChar)==1):
        vowel_list=['a','e','i','o','u']
        if (inputChar.lower() in vowel_list):
            return_value= True
        else:
            return_value= False
    else:
        return_value="Please enter single character only!"        
    return return_value
input_word = input("Input Value: ")

output=check_vowel(input_word) 

print("Output Value:",output)