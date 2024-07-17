#iteratore che da due numeri mi da tutti i numeri tra loro compresi, e gli estremi
class Esercizio:
  def __init__(self, inizio, fine):
    self.inizio=inizio
    self.fine=fine
  def __iter__ (self):
    self.x=self.a
    return self
  def __next__ (self):
    if self.x<=self.b:
      self.x+=1
      return self.x-1
    raise StopIteration