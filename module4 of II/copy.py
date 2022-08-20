def make_closure(par):
    loc = par
    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)
for i in range(5):
    print(i, fsqr(i), fcub(i))  #the closure function is to be 
                                #called in a way it has been created i.e. with or without parameters
