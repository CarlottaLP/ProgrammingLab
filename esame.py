#def eccezioni
class ExamException(Exception):
    pass

class CSVTimeSeriesFile(str):
    #def inizializzazione
    def __init__(self, file_name):
        self.file_name = file_name

    #def funzione che prende i dati
    def get_data(self):
        try:
            my_file = open(self.file_name, 'r')
            
        #non si apre il file
        except Exception:
            raise ExamException("C'è stato un errore nell'apertura del file")

        #liste
        time_series = []
        epoch_list = []
        for line in my_file:
            element = line.split(',')
            if element[0] == 'epoch':
                continue
                
            else:
                #elementi mancanti
                if len(element) < 2:
                    continue
                try:
                    epoch = int(element[0])
                    temperature = float(element[1])
                    
                #errore conversione valori
                except Exception:
                    continue
                    
                #controllo epoch < epoch precedenti e già esistenti
                for item in epoch_list:
                    if epoch < item:
                        raise ExamException(f"Il valore relativo all'epoch numero: {epoch} con temperatura pari a: {temperature} è fuori posto; ci sono errori nei dati")
                if epoch in epoch_list:
                    raise ExamException(f"Esiste un duplicato relativo all'epoch numero: {epoch}; ci sono errori nei dati")

                epoch_list.append(epoch)

                #lista finale
                time_series.append([epoch, temperature])

        #controllo liste non vuote
        if not time_series:
            raise ExamException("Non ci sono abbastanza dati per continuare")

        #chiusura
        my_file.close()

        #ritorno
        return time_series


#inserimento dati
time_series_file = CSVTimeSeriesFile('prova2.csv')
time_series = time_series_file.get_data()


#funzione differenze temperature
def compute_daily_max_difference(list_name):
    list_diff = []
    day_dict = {}

    #creazione dizionario giornate
    for item in list_name:
        temperature = item[1]
        epoch = item[0]
        day = int(epoch / 86400)

        #controllo day diversi
        if day not in day_dict:
            day_dict[day] = []
        day_dict[day].append(temperature)

    #calcolo differenze
    for item in day_dict.keys():
        val_temp = list(day_dict[item])
        if len(val_temp) > 1:
            max_temp = val_temp[0]
            min_temp = val_temp[0]
            for item in val_temp:
                if item < min_temp:
                    min_temp = item
                if item > max_temp:
                    max_temp = item
            diff = round(max_temp - min_temp, 1)
            list_diff.append(diff)
        else:  #None se c'è un solo valore
            list_diff.append(None)

    #ritorno
    return list_diff


#con time_series
time_series_diff = compute_daily_max_difference(time_series)
print(f"Le differenze massime giornaliere tra le temperature registrate sono: {time_series_diff}")