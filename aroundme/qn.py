def validate_pin(pin):
    if not pin:
        print("empty string")
        return False
    
    for i in pin:
        if i not in "0123456789" :
            print("string consists non numerical characters!!")
            return "Invalid"
        
    
    #if pin [4, 6]:
    #        print("string is not in specified length")
    #       return False
    
    for i in pin:
       if int(i) // 2 == 0:
            print("string consists of even number")
            return False
    else:
        return True

print (validate_pin("022"))