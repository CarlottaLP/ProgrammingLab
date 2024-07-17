    #def eccezioni
    class ExamException(Exception):
      pass

    class CSVTimeSeriesFile(str):
      #def inizializzazione
      def __init__(self, file_name):
        self.file_name=file_name

      #def funzione che prende i dati
      def get_data(self):
        try:
          my_file=open(self.file_name, 'r')
        #non si apre il file 
        except Exception:
          raise ExamException("C'è stato un errore nell'apertura del file")

        #liste
        time_series=[]
        epoch_list=[]
        #TOGLIERE QUESTO TRY O AGGIUNGERE UN EXCEPT!!!
        try:
          for line in my_file:
            element=line.split(',')
            if element[0]=='epoch':
              continue
            else:
              #elementi vuoti
              if not element[0].strip() or not element[1].strip():
                continue
              try:
                epoch=int(element[0])
                temperature=float(element[1])
              #errore conversione valori
              except Exception:
                continue
              #controllo epoch già esistenti e < epoch precedenti
              control_epoch=0
              for item in epoch_list:
                if epoch<item:
                  control_epoch=1
                  raise ExamException(f"Il valore relativo a {epoch} con temperatura pari a {temperature} è fuori posto e quindi non viene considerato")
              if epoch in epoch_list:
                control_epoch=1
                raise ExamException(f"Esiste un duplicato relativo a {epoch}, quindi solo il primo valore viene registrato")
              if control_epoch==1:
                continue

              epoch_list.append(epoch)

              #lista finale 
              time_series.append([epoch,temperature])

          #controllo liste non vuote
          if not time_series:
            raise ExamException("Non ci sono abbastanza dati per continuare")

        #chiusura
        finally:
          my_file.close()

        #valori voluti
        print(f'La lista delle liste è: {time_series}')
        return time_series



    #inserimento dati
    time_series_file=CSVTimeSeriesFile('prova.csv')
    time_series=time_series_file.get_data()

    #divisione lista in liste interne
    def separate_epoch(list_name, index):
      element=str(list_name[index]).split(',')
      list_int=int(element[0].strip('['))
      return list_int  

    #funzione differenze temperature
    def compute_daily_max_difference(list_name):
      list_diff=[]
      day_dict={}

      #creazione dizionario giornate
      for item in list_name:
        temperature=item[1]
        epoch=item[0]
        day=int(epoch/86399)

        control=0

        for item in day_dict:
          if day<item:
            control=1
            break
        if control==1:
          continue
        if day not in day_dict:
          day_dict[day]=[]
        day_dict[day].append(temperature)

      #calcolo differenze
      for item in day_dict:
        #BREAK
        val_temp=[]
        val_temp=day_dict.values()
        if len(val_temp)>1:

          max_temp=val_temp[0]
          min_temp=val_temp[0]
          for item in val_temp:
            if item<min_temp:
              min_temp=item
            if item>max_temp:
              max_temp=item
          diff=max_temp-min_temp
          list_diff.append(diff)
        else:#None se c'è un solo valore
          list_diff.append(None)

      #ritorno
      return list_diff

    #con time_series
    time_series_diff=compute_daily_max_difference(time_series)
    print(f"Le differenze massime giornaliere tra le temperature registrate sono: {time_series_diff}")


informazioni = {'nome': 'Dionysia', 'età': 28, 'luogo': 'Atene'}

#accede al valore associato alla chiave 'età'
print(informazioni['età'])

#output

#28