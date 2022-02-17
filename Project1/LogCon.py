# f22 =(a!→b!)→((a∧!b)→c)


#IMP for table1
def IMP0(a, b):
    if a == True and b == False:
        return False
    else:
        return True
# a~b
def EQV(a, b):
    if a == True and b == True:
        return True
    elif a == False and b == False:
        return True
    else:
        return False
def XOR(a, b):
    if a == True and b == True:
         return False
    elif a == False and b == True:
          return True
    elif a == True and b == False:
          return True
    elif a == False and b == False:
          return False
        
# a ∨ b
def OR(a, b):
  if a == True or b == True:
    return True
  elif a == False or b == False:  
    return False
  elif a == False or b == True:
      return  True
  elif a == True and b == False:
        return True
      
    # !b 
def NOT(b):
 
    if b == True:
        return False
    elif b == False:
        return True
      
 # a! -> b!
def NOT_IMP(a,b):
    if a != True and b != True:
        return True
    elif a != False and b != False:
        return True
    elif a != True and b != False:
        return False
    elif a != False and b != True:
        return True
    
    #(a∧!b)    
def AND(a, b):
    if a == True and b != True:
        return False
    elif a == True and b != False:
        return True
    elif a == False and b != True:
        return False
    elif a == False and b != False:
        return False
    
   #((a∧!b)→c)  
def IMP(a, b, c):
      
      if a == True and b != True:
        if c == True:
           return True
      elif a == True and b != True:
        if c == False:
              return True
      elif a == True and b != False:
        if c == False:
             return True
      elif a == True and b != False:
        if c == True:
             return True
      elif a == False and b != True:
        if c == True:
            return True
      elif a == False and b != True:
        if c == False:
            return True
      elif a == False and b != False:
        if c == True:
             return True
      elif a == False and b != False:
        if c == False:
             return True
      else:
            return False
          
def Result(a, b, c):
     
    return NOT_IMP(IMP(a,b,c),b)          
      
 

   
       
       
       
 
          