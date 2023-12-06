def allcaps (f):
    def inner():
        val = f()
        if(isinstance(val,list)):
            for i in range(len(val)):
                if(isinstance(val[i],str)):
                    val[i] = val[i].upper()
            return val
        if(isinstance(val,str)):
           return val.upper()
   
    return inner
