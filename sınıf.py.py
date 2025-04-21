class ogrenciler:
  def __init__(self):
    self.ogrenciler=[]
  def ogrenciler_ekle(self,ogrenci):
    self.ogrenciler.append(ogrenci)
  def ogrenci_yazdir(self):
    for ogrenci in self.ogrenciler:
      print(i.ad)
class ogrenci:
  def __init__(self,id,ad):
    self.id=id
    self.ad=ad
  def ogr_bilg_al(self):
    self.id=input("id:")
    self.ad=input("ad:")
class ders:
  def __init__(self,ders):
    self.ders=ders
class dersler:
  def __init__(self):
    self.dersler=[]
  def ders_ekle(self,ders):
    self.dersler.append(ders)

class sınıf:
  def __init__(self,ıd):
    self.ogrenciler=[]
    self.dersler=[]