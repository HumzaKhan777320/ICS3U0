def triangle (ch, num):
  print(ch*num)
  if (num >= 1): 
    triangle(ch, num - 1)
    return

c = input("Input s character of your choice: ")
n = int(input("Enter a number: "))
triangle(c, n)
