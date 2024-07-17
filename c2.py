#Modificare l’oggetto c1 in modo che alzi un’eccezione se il nome del file non è una stringa (nell’__init__())
#modificare la funzione get_data() in modo da leggere solo un intervallo di righe del file (inclusa l’intestazione, estremi inclusi, e partendo da 1), aggiungendo gli argomenti start ed end opzionali (quindi get_data(self, start=None, end=None), controllandone la correttezza e sanitizzandoli se serve
class CSV():
  #def inizializzazione
  def __init__(self, file_name):
    if not isinstance(file_name, str):
      raise TypeError('Il nome non è una stringa')
    self.file_name=file_name
    

  #def funzione che prende i dati
  def get_data(self, start=None, end=None):
    try:
      my_file=open(self.file_name, 'r')
    except Exception as e:
      print("C'è stato un errore nell'apertura del file")
    if start is not None and not isinstance(start, int):
      print("C'è stato un errore nell'inserimento dell'inizio, quindi iniziamo dalla prima riga")
      start=None
    if start is not None and start<=0:
      print("C'è stato un errore nell'inserimento dell'inizio, quindi iniziamo dalla prima riga")
      start=None
    if end is not None and not isinstance(end, int):
      end=None
    lines=[]
    line_number=1
    if end is not None:
      endd=end+1
    for line in my_file:
      if start is not None and line_number<start:
        line_number+=1
        continue
      if end is not None and line_number>end:
        break
      element=line.split(',')
      list=[]
      date=element[0]
      sale=element[1]
      list.append([date,sale])
      lines.append(list)
      line_number+=1
    print('La lista delle liste è: {}'.format(lines))
    my_file.close()
    return lines

#creazione nuova classe
class NumericalCSV(CSV):
#chiamata get_data originale
  def og_get_data(self, start=None, end=None):
    return super().get_data(start, end)

#conversione in float
  def get_data(self, start=None, end=None):
    lines_ex=super().get_data(start, end)
    val=[]
    for item in lines_ex:
      if item[0]=='Date':
        continue
      pr=item
      for item in pr:
        if len(item)<=1 or item[1] is None:
          val.append('In data {} non abbiamo abbastanza informazioni'.format(item[0]))
        else:
          try:
            v=float(item[1])
            val.append(v)
          except ValueError:
            print(f"Impossibile convertire {item[1]} in float")
    print('La lista di valori è: {}'.format(val))

#prova
prova=NumericalCSV('shampoo.csv')
prova.get_data(start=1, end=2)

#creare unit test o testing globali per CSV e NumericalCSV
import unittest
class testCSV(unittest.TestCase):
  def test_init(self):
    csv_file=CSV('shampoo_sales.csv')
    self.assertEqual(csv_file.name, 'shampoo_sales.csv')
if __name__=='__main__':
  unittest.main

if not prova.get_data(1, 2)==('[266.0, 145.9]'):
  raise Exception('Test 1-2 non passato')