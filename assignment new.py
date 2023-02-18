def rainaverage(l):
# Create a dictionary to store the total rainfall and number of counts for each city
   a={}    
   count={}
   for (city,rainfall) in l:
        if city in a:
             a[city]+=rainfall
             count[city]+=1
        else:
             a[city]=rainfall
             count[city]=1
# Calculate the average rainfall for each city and store it in a list 
   average =[]
   for city in sorted(a.keys()):
        ar=a[city]/count[city]
        average.append((city,ar)) 
   return average 