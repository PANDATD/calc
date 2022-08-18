#!/bin/ussr/python3.10

def add(number1: int| float, number2: int| float) -> int | float :
  """This Funcation will returns Addition of Two no
  
  Param1: number1: int | float 
  Param2: number2: int | float 
  
  """
  return print(f"Additon of Two No's -> {number1+number2}",sep='<------->',end=' <------ END OF PROGRAM',flush=True,)
               
print(help(add))
add(12,23)