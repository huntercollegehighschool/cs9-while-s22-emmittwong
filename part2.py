'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
Times_to_print=int(input("Time to print: "))
times=0
while times!=Times_to_print:
  print("Hunter")
  times=times+1
