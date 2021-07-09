def read():
  numbers = []
  with open('./docs/numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
      numbers.append(int(line))
  print(numbers)

def write():
  names = ['Jesús', 'Facundo', 'Miguel', 'Christian', 'Adal', 'Karol', 'Nicolás']
  with open('./docs/names.txt', 'a', encoding='utf-8') as f:
    for name in names:
      f.write(name)
      f.write('\n')

def run():
  write()


if __name__ == '__main__':
  run()