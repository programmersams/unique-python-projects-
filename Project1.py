 def bintodec(binary):
  index = 0
  calculations = []
  binary = binary[::-1]
  numbers = list(binary)
  bin =["0","1",0,1]
  for num in numbers:
    
    if numbers[index]== "0":
      calculations.append(0)
    elif num not in bin :
      print("please enter a binary number")
    elif index == 0:
      calculations.append(1)
    else :
      calculations.append(2**index)
    
    index = index+1

  decimal = sum(calculations)
  print(f'Decimal version of the number:{decimal}')
while True:

  binary = input("Enter a binary number:")
  start = bintodec(binary)
  
  

  

