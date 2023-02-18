def flatten(l):
#    FIRST CREATE A EMPTY LIST
    a = []
    for i in l:
        #IF DATATYPE OF THE ELEMENT IN THE LIST WHILE ITTERATING IS LIST:::        
        if type(i) == list:
        #USE EXTEND KEYWORD ::WHICH DOES ->>>>>COMBINE THE TWO LIST....IN SINGLE LIST:: 
            a.extend(flatten(i))
        else:
        #ELSE INSERT IT INSIDE LIST.... 
            a.append(i)
        #RETURN a 
    return a
print(flatten([1,2,[3],[4,[5,6]]]))
