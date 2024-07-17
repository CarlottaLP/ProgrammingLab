#modifica CSV.py che stampi a schermo messaggi di errore per file non esistenti

class CSV(str):
    #def inizializzazione
    def __init__(self, file_name):
      self.file_name=file_name

    #def funzione che prende i dati
    def get_data(self):
      try:
        my_file=open(self.file_name, 'r')
      except Exception as e:
        print("C'è stato un errore nell'apertura del file")
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
      print('La lista delle liste è: {}'.format(lines))

#prova
prova=CSV('shampoo.csv')
prova.get_data()