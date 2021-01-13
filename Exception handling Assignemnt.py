#----------------------------------------------------------------------------------------------------------------------------------------
# Answer 1
def dividing(x,y):
    try:
        result= x // y
        print("Answer is : ", result)
    except ZeroDivisionError:
        print("Dividing by zero not allowed")
dividing(5,0) 
#----------------------------------------------------------------------------------------------------------------------------------------
# Answer 2
Subject=['Americans', 'Indians']
Verb=['play', 'watch']
Object=['Baseball', 'Cricket']
All_sentences=[(sub +" "+ ver +" " + obj) for sub in Subject for ver in Verb for obj in Object]
for sentence in All_sentences:
    print(sentence)
#----------------------------------------------------------------------------------------------------------------------------------------
