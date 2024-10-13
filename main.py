def run():
    print("ingresa los coeficinets de las cuaciones")
    vector=[]
    for i in range(0,3):
        fila =[]
        for j in range(0,3):
            valor = input(f"Ingrese el valor para la posición ({i+1}, {j+1}): ")
            fila.append(procesarNumeros(str(valor)))
        vector.append(fila)
    
    array =[]
    for i in range(0,3):
        valor = input(f"Ingrese el valor para la posición ({i+1}: ")
        array.append(procesarNumeros(str(valor)))

    print(vector)
    resolucion(vector=vector, array=array)
    
def mcd(a, b):
        while b:
            a, b = b, a % b
        return a

def procesadoDeNumero(valor):
    if valor == int(valor): 
        print(valor)
    else:
        aux = str(valor)  
        parteEntera, parteDecimal = aux.split(".")  
        
        digitosDecimales = len(parteDecimal) 
        numerador = int(parteEntera + parteDecimal) 
        denominador = 10 ** digitosDecimales 

        divisorComun = mcd(numerador, denominador) 
        numeradorSimple = numerador // divisorComun 
        denominadorSimple = denominador // divisorComun  

        print(f"{numeradorSimple}/{denominadorSimple}")  

def procesarNumeros(valor):
    try:
        return float(valor)
    except ValueError:
        if '/' in valor:
            try:
                numerador,denominador = valor.split('/')
                return float(numerador)/float(denominador)
            except ValueError:
                return None
        else:
            return None
        
def deternimantes(vector):
    #[0][0],[0][1],[0][2]
    #[1][0],[1][1],[1][2]
    #[2][0],[2][1],[2][2]
    diagonal1=(vector[0][0]*vector[1][1]*vector[2][2])+(vector[1][0]*vector[2][1]*vector[0][2])+(vector[2][0]*vector[0][1]*vector[1][2])
    diagonal2=(vector[0][2]*vector[1][1]*vector[2][0])+(vector[1][2]*vector[2][1]*vector[0][0])+(vector[2][2]*vector[0][1]*vector[1][0])
    return diagonal1-diagonal2

def nuevoVector(vector,x,araay):
    nuevo_vector = [fila[:] for fila in vector]
    for i in range(len(vector)):
        nuevo_vector[i][x] = araay[i]
    return nuevo_vector

def resolucion(vector,array):
    deltaA = deternimantes(vector=vector)
    if deltaA == 0:
        print("El sistema no tiene solución única.")
        return
    deltaX = deternimantes(nuevoVector(vector=vector,x=0,araay=array))
    deltaY = deternimantes(nuevoVector(vector=vector,x=1,araay=array))
    deltaz = deternimantes(nuevoVector(vector=vector,x=2,araay=array))

    x = procesadoDeNumero(deltaX/deltaA)
    y = procesadoDeNumero(deltaY/deltaA)
    z = procesadoDeNumero(deltaz/deltaA)
    
    print(f"Las soluciones son: x = {x}, y = {y}, z = {z}")
    


if __name__ == "__main__":
    run()