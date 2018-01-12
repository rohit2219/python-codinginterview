def f(*args,**kwargs): 
	print(args,"---",kwargs)
	return
	
def ff(a,ls):
	print ("list",ls,a)
	ls.append(a)
	print ("list",ls)
	return 

#ff(4,[3,4,5])	
#ff(4,[])
l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}


#f()
#f(1,2,3)                    
f(1,2,3,"groovy")           
f(a=1,b=2,c=3)              
#f(a=1,b=2,c=3,zzz="hi")     
#f(1,2,3,a=1,b=2,c=3)  
