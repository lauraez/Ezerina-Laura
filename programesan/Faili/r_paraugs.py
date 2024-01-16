f = open('demo.txt','r',encoding='utf-8') #atver failu
print(f.read()) #izdrukā faila saturu

f = open('demo.txt','r',encoding='utf-8')
print(f.readline())  # nolasa pirmo rindinu

f = open('demo.txt','r',encoding='utf-8') #atver failu
print(f.read(10))  # atgriež 10 simbolus tai skaita atstarpes



f.close() # aiztaisa failu