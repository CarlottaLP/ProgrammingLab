#creazione classe figlia di CSV che converte le vendite in float

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
      return lines

#creazione nuova classe
class NumericalCSV(CSV):
  #chiamata get_data originale
  def og_get_data(self):
    lines=super().get_data()

  #conversione in float
  def get_data(self):
    lines_ex = super().get_data()
    val = []
    for item in lines_ex:
        if len(item) == 2:
            try:
                date = item[0]
                va = float(item[1])
                val.append(va)  # Manteniamo la struttura data, valore
            except ValueError:
                print(f"Impossibile convertire {item[1]} in float")
        else:
            val.append(f'In data {item[0]} non abbiamo abbastanza informazioni')
    print('La lista di valori è: {}'.format(val))
    return val




#prova
prova=NumericalCSV('shampoo.csv')
prova.get_data()