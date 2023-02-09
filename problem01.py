def remdup(l):
    notsame=[]
    l.reverse()
    for i in range(len(l)):
        if l[i] not in notsame:
            notsame.append(l[i])
    notsame.reverse()
    return notsame

# *******************************************************************************************
"""So as per the question i have made a program
  In function remdup( ) 
  I have taken a variable notsame=[] and assigned a empty list to it..
  Then the given list is reversed using l.reverse( ) builtin function...
  This is done bcz it makes the compiler easy to check...
  Now we are running a loop to check the element in the list...
  IF the element in the list is not in the empty list notsame...
  Insert the element using append keyword...
  Then reverse notsame list...
  return notsame list"""