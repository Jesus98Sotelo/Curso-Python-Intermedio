def run():
  my_list = [1, 'hello', True, 4.5]
  my_dict = {'firstname': 'Jesús', 'lastname': 'Sotelo'}

  super_list = [
    {'firstname': 'Jesús', 'lastname': 'Sotelo'},
    {'firstname': 'Enrique', 'lastname': 'Sotelo'},
    {'firstname': 'Karol', 'lastname': 'Sotelo'},
    {'firstname': 'Pepe', 'lastname': 'Rodelo'},
    {'firstname': 'JMiguel', 'lastname': 'Torres'},
  ]

  super_dic = {
    'natural_nums': [1, 2, 3, 4, 5, 6],
    'integer_nums': [-1, -2, 0, 1, 2],
    'floating_nums': [1.1, 4.5, 6.43]
  }

  for key, value in super_dic.items():
    print(key, '-', value)

  for i in super_list:
    print(i)
    for key, value in i.items():
      print(key, '-', value)
      
if __name__ == '__main__':
  run()