def sum(num1, num2):
	return num1 + num2
def sub(num1, num2):
	return num1 - num2
def multi(num1, num2):
	return num1 * num2
def divide(num1, num2):
	return num1 / num2

n1 = int(input("enter number 1: "))
n2 = int(input("enter number 2: "))
act = input("enter action: ")

if act == "add":
	print(sum(n1, n2))
if act == "subtract":
	print(sub(n1, n2))
if act == "multiply":
	print(multi(n1, n2))
if act == "divide":
	print(divide(n1, n2))
input()
