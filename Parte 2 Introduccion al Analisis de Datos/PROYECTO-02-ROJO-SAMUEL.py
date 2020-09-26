import pandas as pd

desired_width = 10
pd.set_option('display.max_columns', 10)  # Redefinimos el maximo de columnas a mostrar para poder verlas en el editor

#   Mensaje de Bienvenida
print("\n-----------------------------------------------------------------------------")
print("--------------------- SYNERGY LOGISTICS ANALYSIS TOOL -----------------------")
print("-----------------------------------------------------------------------------\n")

#   Carga de datos
print("# Iniciando carga de datos ...")
df = pd.read_csv("synergy_logistics_database.csv")
print("# Datos cargados")
print("#############################################################################")
print("Preview: \n", df.head())
print("#############################################################################")
#   Bucle para hacer analisis
while(1):
    #   Definir opcion a mostrar
    print("-----------------------------------------------------------------------------")
    print("Seleccione la opcion que desee visualizar: ")
    print("[1] Rutas de importacion y exportacion")
    print("[2] Medio de transporte utilizado")
    print("[3] Valor total de importaciones y exportaciones")

    #   Solicitud del valor y verificacion de su validez
    max_tries = 4
    for i in range(max_tries):
        try:
            selector = int(input("\nIngrese el numero de opcion: "))
            if isinstance(selector, int) and 1 <= selector <= (max_tries - 1):
                break
            else:
                print("El dato debe ser un numero dentro de las opciones, intentelo de nuevo")
        except:
            print("El dato debe ser un numero dentro de las opciones, intentelo de nuevo")

    if i >= 2:
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              "\nDemasiados intentos incorrectos"
              "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit()   #   Si se ve rebasado el maximo de intentos, se termina el programa.
    print("-----------------------------------------------------------------------------")
    #   Rutas de importacion y exportacion
    if selector == 1:
        print("\n#############################################################################")
        print("##################### Rutas de Importacion/Exportacion ######################")
        print("#############################################################################\n")

        """
        El codigo sigue la logica de filtrar segun sea importacion o exportacion, para posteriormente
        agrupar por categorias de direccion, origen y destino. Posteriormente cuenta la cantidad de 
        datos agrupados y suma el total_value para darnos un total por ruta. Despues los ordena de mayor
        a menor por cantidad de viajes y finalmente se asigna un index como referencia visual, por ultimo
        se calculo un ratio del valor acumulado dividido entre viajes en la ruta para conocer su aporte por viaje.
        """
        #   Cuenta de rutas mas utilizadas
        print("++++++++++++++++++++++++++++++ Rutas mas usadas ++++++++++++++++++++++++++++++")
        Exportaciones = df.groupby(["direction", "origin", "destination"])['total_value']\
            .agg({'count', 'sum'})\
            .rename(columns={'count': 'Cuenta', 'sum': 'Valor_acumulado'})\
            .sort_values(by=['Cuenta'], ascending=False)\
            .reset_index()
        Exportaciones["Ratio"] = Exportaciones["Valor_acumulado"]/Exportaciones["Cuenta"]
        print(Exportaciones.head(10))

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #   Medio de transporte utilizado
    if selector == 2:
        print("\n#############################################################################")
        print("###################### Medio de transporte utilizado ########################")
        print("#############################################################################\n")

        """
        En esta seccion se hace un query agrupando por el medio de transporte, calculando la cantidad de viajes,
        la suma total del valor de estos generado por las importaciones y exportaciones y calculando el ratio
        de valor/cantidad de viajes.
        """
        print("++++++++++++++++++++++++++++ Medios de transporte +++++++++++++++++++++++++++")
        Transporte = df.groupby(["transport_mode"])[
            'total_value'] \
            .agg({'count', 'sum'}) \
            .rename(columns={'count': 'Cuenta', 'sum': 'Valor_acumulado'}) \
            .sort_values(by=['Cuenta'], ascending=False) \
            .reset_index()

        Transporte["Ratio"] = Transporte["Valor_acumulado"] / Transporte["Cuenta"]
        print(Transporte)

    #   Valor total de importaciones y exportaciones
    if selector == 3:
        print("\n#############################################################################")
        print("################## Valor total de Importacion/Exportacion ###################")
        print("#############################################################################\n")

        """
        El siguiente codigo agrupa por origen, para obtener el pais sin importar si es exportacion o importacion
        posteriormente calcula la cantidad de viajes y el acumulado de valor, los ordena de forma descendente por 
        valor acumulado y les asigna un indice como referencia. Posteriormente se calcula el total general, el cual
        servira para identificar a los paises que generan el 80% del ingreso general.
        """
        print("++++++++++++++++++++++ Valor de Importacion/Exportacion +++++++++++++++++++++")
        Paises = df.groupby(["origin"])[
            'total_value'] \
            .agg({'count', 'sum'}) \
            .rename(columns={'count': 'Cuenta', 'sum': 'Valor_acumulado'}) \
            .sort_values(by=['Valor_acumulado'], ascending=False) \
            .reset_index()
        acumulado_total = Paises["Valor_acumulado"].sum()   #   Calculo del acumulado total del valor generado
        Paises["Ratio"] = Paises["Valor_acumulado"] / Paises["Cuenta"]
        print(Paises)

        #   Buscar e imprimir a los 8 paises que generen el 80% del valor
        print("+++++++++++++++++++++ Paises que generan el 80% de valor ++++++++++++++++++++")
        acum = 0
        i = 0
        while 1:
            acum += int(Paises.iloc[[i]]["Valor_acumulado"])
            if acum >= acumulado_total*0.8:
                break
            i += 1

        print(Paises[0:i+1])

    #   Solicitud de salida o analisis nuevo
    outvar = input("\n¿Desea realizar otra opcion? (SI/NO)\n")
    if outvar.lower() != 'si':
        print("\nGracias por haber utilizado esta herramienta de analisis")
        print("-----------------------------------------------------------------------------")
        print("--------------------- SYNERGY LOGISTICS ANALYSIS TOOL -----------------------")
        print("-----------------------------------------------------------------------------\n")
        break




