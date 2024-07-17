def sum_list(list):
  if(list==None):
    print('None')
  sum=0
  for item in list:
    sum=sum+item
  print("La somma è {}".format(sum))

my_list=[1, 2, 3, 4]

sum_list(my_list)

for item in my_list:
  print(item)