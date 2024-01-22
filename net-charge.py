# Ejercicio 1: Asignación de variables, listas y diccionarios

# Almacene la secuencia de preproinsulina humana en una variable llamada preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Almacene los elementos restantes de la secuencia de insulina humana en variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

# Cree un nuevo diccionario y llénelo con pares clave-valor
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Ejercicio 2: Uso de count() para contar los números de cada aminoácido

# Cuente la cantidad de aminoácidos en la insulina utilizando count() y comprensión de listas
seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

# Salida de los recuentos
print("Recuento de aminoácidos:", seqCount)

# Ejercicio 3: Escribir la fórmula de carga neta

# Inicialice la variable de pH
pH = 0

# Bucle while para calcular la carga neta mientras pH sea igual o inferior a 14
while pH <= 14:
    netCharge = (
        +(sum({x: ((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x]))) for x in ['k', 'h', 'r']}.values()))
        - (sum({x: ((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x]))) for x in ['y', 'c', 'd', 'e']}.values()))
    )
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1
