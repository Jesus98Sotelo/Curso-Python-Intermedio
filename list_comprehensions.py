def run():
  # squares = []
  # for i in range(1, 101):
  #   squares.append(i**2)

  # print(squares)

  # squares2 = []

  # for i in range(1, 101):
  #   if i % 3 == 0:
  #     pass
  #   else:
  #     squares2.append(i**2)
  
  squares2 = [i**2 for i in range(1, 101) if i % 3 != 0]

  print(squares2)

  list_comprehensions = [ i for i in range(1, 99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]

  print(list_comprehensions)
  
if __name__ == '__main__':
  run()