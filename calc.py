#!/bin/python3.10
def add(num1: int| float,
        num2: int| float,)-> int| float:
  """
  Parametrs : num1: int | float
              num2: int | float
  Which Performs Addition of Two Numbers
  """
  return f"Addition of {num1} + {num2} = {num1+num2}"

add(10.09, 20.78)

def sub(num:int, num2:int)->int:
	"""This funcation return substrction of two numbers"""
	return f"Multiplication of {num1} and {num2} =:{num1-num2}"
sub(20,10)

def mul(num1:int, num2:int)-> int:
	"""This funcation retuns multiplication of two numbers"""
	return f"Multiplication of {num1} and {num2} =:{num1*num2}"
mul(20,2)
def div(num1:int, num2:int)-> int:
	"""This funcation returns division  of two numbers"""
	return f"division of {num1} and {num2} =: {num1//num2}"
div(20,2)

