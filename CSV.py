#funzione che prende i dati di una lista in un documento esterno e crea una lista di liste

class CSV(str):
    #def inizializzazione
    def __init__(self, file_name):
        self.file_name=file_name
        
    #def funzione che prende i dati
    def get_data(self):
      my_file=open(self.file_name, 'r')
      lines=[]
      for line in my_file:
        element=line.split(',')
        list=[]
        if element[0]!='Date':
          date=element[0]
          sale=element[1]
          s=float(sale)
          list.append([date,s])
          lines.append(list)
      print(f'La lista delle liste è: {lines}')

#test
prova=CSV('shampoo.csv')
prova.get_data()