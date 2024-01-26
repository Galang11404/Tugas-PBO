# konversi celsius
class celcius:
    def __init__(self, celcius):
         self.c = celcius

    def get_fahrenheit(self):
         return (9/5 * self.c) + 32

    def get_reamur(self):
         return 4/5 * self.c
 
    def get_kelvin(self):
         return self.c + 273
    
# input
fahrenheit = celcius(10)
reamur = celcius(20)
kelvin = celcius(30)

# output
print('Konversi Celcius:')
print('Fahrenheit:', fahrenheit.get_fahrenheit())
print('Reamur:', reamur.get_reamur())
print('Kelvin:', kelvin.get_kelvin())
print('--------------------------')

# Konversi Reamur
class reamur:
    def __init__(self, reamur):
         self.r = reamur

    def get_celcius(self):
         return 5/4 * self.r
    
    def get_fahrenheit(self):
         return (9/4 * self.r) + 32
    
    def get_kelvin(self):
         return 5/4 * self.r + 273
    
# input
Celcius = reamur(23)
fahrenheit = reamur(11)
kelvin = reamur(12)

# Output
print('Konversi Reamur:')
print('Celcius:', Celcius.get_celcius())
print('Fahrenheit:', fahrenheit.get_fahrenheit())
print('Kelvin:', kelvin.get_kelvin())
print('----------------------')
               
# Konversi Fahrenheit
class fahrenheit:
     def __init__(self, fahrenheit):
          self.f = fahrenheit

     def get_celcius(self):
          return 5/9 * (self.f - 32)

     def get_kelvin(self):
          return 5/9 * (self.f - 32) + 273
     
     def get_reamur(self):
          return 4/9 * (self.f - 32)
     
# Input
Celcius = fahrenheit(50)
reamur = fahrenheit(50)
kelvin = fahrenheit(50)

# Output
print('Konversi Fahrenheit')
print('Celcius:', Celcius.get_celcius())
print('reamur:', reamur.get_reamur())
print('Kelvin:', kelvin.get_kelvin())
print('-----------------------------')

# Konversi kelvin
class kelvin:
     def __init__(self,kelvin):
          self.k = kelvin

     def get_celcius(self):
          return self.k - 273

     def get_reamur(self):
          return 4/5 * (self.k - 273)

     def get_fahrenheit(self):
          return 9/5 * (self.k - 273) + 32     
     
# Input
Celcius = kelvin(32)
fahrenheit = kelvin(44)
reamur = kelvin(25)

# Output
print('Konversi Kelvin')
print('Celcius:', Celcius.get_celcius())
print('Fahrenheit:', fahrenheit.get_fahrenheit())
print('Reamur:', reamur.get_reamur())
print('-----------------------------')