def calcsqrt(x):
	#using Newton Raphson Method	
	niter=5
	i=0
	root=x/2
	while(i<niter):
		root=0.5*(root+(2/root))
		i=i+1
	return root

print "root is "+str(calcsqrt(5))
