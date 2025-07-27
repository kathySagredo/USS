""" crear un programa con un lenguaje que utilice el paradigma imperativo que solicite 
la cantidad de estudiantes y sus respectivas calificaciones, calcule el promedio y 
además determine la calificación máxima y mínima. Implementar un menú para mostrar 
cada cálculo por separado. """

# Funciones 
def promedio(notas, cantidad_notas):
    acum = 0
    for nota in notas:
        acum = acum + nota
    return acum/cantidad_notas

def nota_maxima(notas, cantidad_notas):
    i=0
    max = notas[i]
    while i < cantidad_notas:
        if notas[i] > max:
            max = notas[i]
        i=i+1
    return max

def nota_minima(notas, cantidad_notas):
    i=0
    min = notas[i]
    while i < cantidad_notas:
        if notas[i] < min:
            min = notas[i]
        i= i+1
    return min

def main():
    # Solicitud de datos: Cantidad de notas
    print("###### Bienvenido a sistema de calificaciones ######")
    # Manejo de errores para el ingreso de una cantidad de notas valida
    while True:
        try:
            cantidad_notas = int(input("Por favor, ¿cuántas notas desea ingresar?: "))
            if cantidad_notas <= 0:
                print("Por favor, ingresa solo enteros positivos.")
            else:
                break
        except ValueError:
            print("Ingresa un número valido")
    
    # Solicitud de datos: Notas
    notas = []
    n=0
    while n < cantidad_notas:
        # Manejo de errores para el ingreso de notas validas
        try:
            nota_ingresada = float(input(f"Ingresar nota {n+1}: "))
            if nota_ingresada < 1.0 or nota_ingresada > 7.0:
                print("Ingrese un valor entre 1.0 y 7.0")
            else:
                notas.append(nota_ingresada)
                n=n+1
        except ValueError:
            print("Ingresa un número valido, tipo decimal o entero.")
   
    # Menú, llamada de funciones
    while True:
        print("""
        ¿Qué quiere hacer?
              1. Calcular promedio
              2. Calcular la nota máxima
              3. Calcular la nota minima
              4. Salir 
        """)
        opcion = input("Ingresa el número de la opción: ")
        if opcion == "1":
            print("El promedio de notas es:", promedio(notas, cantidad_notas))
        elif opcion == "2":
            print("La nota máxima es:", nota_maxima(notas, cantidad_notas))
        elif opcion == "3":
            print("La nota mínima es:", nota_minima(notas, cantidad_notas))
        elif opcion == "4":
            print("Vuelva pronto.")
            break
        else:
            print("¡Oh no!, ingresa una opción valida.")

# Llamada función principal    
main()

