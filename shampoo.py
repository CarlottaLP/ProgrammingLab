def sum_csv(file_name):
    values=[]
    my_file=open(file_name,'r')
    sum=0.0
    for line in my_file:
        element=line.split(',')
        if element[0]!='Date':
            value=element[1]
            v=float(value)
            values.append(v)
    for item in values:
        sum=sum+item
    print("La somma è: {}".format(sum))

sum_csv('shampoo.csv')