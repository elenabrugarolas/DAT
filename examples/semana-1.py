

compi = "Pepito"

print("Hola mundo!!!" + compi)

lista = [1,2,3,4]
lista.append(5)  #añade elementos a una lista, las tuplas no son modificables 

# funcion 
def saluda(compi):
    print (f"Hola {compi}")

saluda ('pepe')

dict = { #diccionario 
    'a' : 'es a ',
    'b' : 'es b'
}
try:
    print (dict.get('c'))

except: 
    print('Aqui ha pasado algo')