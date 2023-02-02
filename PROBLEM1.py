def primepartition(m):
   if m<=1:
    return False
  def is_prime(n):
    for i in range(2,int(n**0.5)+1):
      if n%i==0:
        return False
    return True
  for i in range(2,int(m/2)+1):
       if is_prime(i) and is_prime(m-i):
         return True
  return False  
            


      
            
