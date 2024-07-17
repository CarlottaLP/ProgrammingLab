class Testo(str):
    def __len__(self):
        return len(self.split(' '))
mio_testo=Testo('Ciao, oggi va tutto bene, con te?')
print(mio_testo)
print(len(mio_testo))

