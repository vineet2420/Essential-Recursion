def reverse(n):
	if n==0:
		print(0);
	else:
		print(n);
		reverse(n-1);
#reverse(5);

#print number 1 given any n recursively
def print1(n):
	if n==1:
		return 1;
	else:
		return print1(n-1)
#print1(100);

def sum(n):
	if n<10:
		return n;
	else:
		return sum(n//10)+sum(n%10);


#print(sum(50))

def printTri(spc, stars):
	if stars ==0:
		return;
	else:
		print(" "*spc + "*"*stars);
		printTri(spc+1, stars-1)
#printTri(0,4)

def printStr(n):
	if n == 0:
		return;
	else:
		print(n*"*")
		printStr(n-1)
#printStr(5);

def s(x):
	print(x);
	if x==1:
		return;
	else:
		if x%2==0:
			s(x/2);
		else:
			s(3*x+1);
#s(5);

def fib(n):
	if n == 1 or n == 2:
		return 1;
	else:
		p2=fib(n-2)
		p1=fib(n-1)
		return p1+p2;
#for n in range (1,100):
#	print(fib(n));

def sumRec(lst):
	if len(lst)==1:
		return lst[0];
	else:
		return lst[0] + sumRec(lst[1:]) 
			
list= [1,2,3,4]
#print(sumRec(list))

def fact(n):
	if n<=1:
		return 1;
	else:
		return fact(n-1)*n

#print(fact(7))

def digiSum(n):
	if n<10:
		return n;
	else:
		return digiSum(n//10) + digiSum(n%10)
print(digiSum(5014));
