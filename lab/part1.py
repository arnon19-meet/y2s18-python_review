# Part 1 of the Python Review lab.

def hello_world():
	print("hello world")

def greet_by_name(name):
	print("hello ", name)

def encode(x):
	number=x*3953531
	return number

def decode(coded_message):
	x = coded_message/3953531
	return x
print(decode(encode(2)))