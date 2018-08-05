# Write your solution for 1.4 here!
i=0
x=2
def is_prime(x):
	is_prm = True
	for i in range (2, x):
		if x%i==0:
			is_prm = False
			break
	if is_prm:
		print("its a prime")
	else:
		print("oh oh")
is_prime(x)