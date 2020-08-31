from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches  # Importar Datos de lifestore_file

#   Declarar usuarios definidos y sus passwords
Registred_users = [["Admin", "1234"],
                   ["Admin2", "456"]]
#   Declarar variable de ingreso
regFlag = 0
#   Definir cantidad maxima de productos
max_Prod = 0
for i in range(len(lifestore_products)):
    if lifestore_products[i][0] > max_Prod:
        max_Prod = lifestore_products[i][0]

#   Bucle principal
while 1:
    #   Login
    # print("Bienvenido, favor de iniciar sesion:\n")
    # user = input("Usuario: ")
    # pwd = input('Contraseña: ')
    print("Credenciales")
    input("Presiona")
    user = "Admin"
    pwd = "1234"

    #   Revisar credenciales
    for usr in Registred_users:
        if (usr[0] == user) and (usr[1] == pwd):
            regFlag = 1
    if regFlag == 0:
        print("Usuario o contraseña incorrectos")

    #   Bucle de sistema de analisis
    while regFlag == 1:
        #   Generar lista que relacione las ventas, busquedas y productos
        #   Contar ventas y rating acumulado
        sales = [0] * max_Prod
        rating = [0] * max_Prod
        for i in range(len(lifestore_sales)):
            sales[lifestore_sales[i][1]] += 1
            rating[lifestore_sales[i][1]] += lifestore_sales[i][2]
        #   Contar Busquedas
        searches = [0] * max_Prod
        for i in range(len(lifestore_searches)):
            searches[lifestore_searches[i][1]] += 1

        #   Asociar numero de ventas y busquedas a numero de producto
        sales_list = []
        avgRat = None
        for i in range(max_Prod):
            if sales[i] != 0:
                avgRat = rating[i]/sales[i]
            else:
                avgRat = 0
            sales_list.append((i, sales[i], searches[i],
                               lifestore_products[i][3],
                               avgRat))  # [id, number of sales, number of searches, category, avg rating]
        #   Func p/ Ordenar la lista (aun no se ven funciones, pero es para evitar un for solo para ordenar y poder usar sort)
        def ordVentas(val):
            return val[1]
        def ordBusquedas(val):
            return val[2]
        def ordCat(val):
            return val[3], val[1]
        def ordRat(val):
            return val[4]
        def ordDate(val):
            return val[3][6:], val[3][3:5], val[3][0:3]

        #   Seleccion de analisis a observar
        print("\nPresione el número de la opción que desee observar.")
        print(" [1] Productos más vendidos y productos rezagados\n", "[2] Productos por reseña en el servicio\n",
              "[3] Sugerir una estrategia")
        option_analisis = input("¿Que análisis desea ver?\n")
        try:
            option_analisis = int(option_analisis)
        except:
            print("Error: Opcion no valida.")

        if option_analisis == 1:
            #   [1] Productos más vendidos y productos rezagados
            #   Brindar listado de 50 productos con mayores ventas
            sales_list.sort(key=ordVentas, reverse=True)  # Ordenar por ventas (Descendente)
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("--- LISTADO DE 50 PRODUCTOS MAS VENDIDOS ---")
            print("--------------------------------------------")
            print("--------------------------------------------")
            if len(sales_list) >= 50:  # Revisar tamaño de lista para evitar error en el for
                num_sales = 50
            else:
                num_sales = len(sales_list)
            for i in range(num_sales):
                print(
                    f"{i + 1}: NOMBRE: {lifestore_products[sales_list[i][0]-1][1]} --- ID_PROD: {sales_list[i][0]} --- #VENTAS: {sales_list[i][1]} ")
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("--------------------------------------------")
            input("Presione enter para continuar")

            #   100 productos con mas búsquedas
            sales_list.sort(key=ordBusquedas, reverse=True)  # Ordenar por Busquedas (Descendente)
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("-- LISTADO DE 100 PRODUCTOS MAS BUSCADOS ---")
            print("--------------------------------------------")
            print("--------------------------------------------")
            if len(sales_list) >= 100:  # Revisar tamaño de lista para evitar error en el for
                num_sales = 100
            else:
                num_sales = len(sales_list)

            for i in range(num_sales):
                print(
                    f"{i + 1}: NOMBRE: {lifestore_products[sales_list[i][0]-1][1]} --- ID_PROD: {sales_list[i][0]} --- #BUSQUEDAS: {sales_list[i][2]} ")
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("--------------------------------------------")
            input("Presione enter para continuar")

            # Categorias
            sales_list.sort(key=ordVentas)  # Ordenar por Ventas (Ascendente)
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("-- LISTADO DE 50 PRODUCTOS MENOS VENDIDOS --")
            print("--------------------------------------------")
            print("--------------------------------------------")
            if len(sales_list) >= 50:  # Revisar tamaño de lista para evitar error en el for
                num_sales = 50
            else:
                num_sales = len(sales_list)
            #   Generar variable de 50 menos vendidos (o los que alcancen)
            sales_cat = sales_list[:num_sales]
            sales_cat.sort(key=ordCat)  #   Ordenar por Categoria y por ventas de forma ascendente
            catTitle = []   #   Variable de apoyo para impresión de separador por categoria
            for i in range(len(sales_cat)):
                if catTitle != sales_cat[i][3]:
                    print("----------------"+sales_cat[i][3]+"----------------")
                    catTitle = sales_cat[i][3]
                print(f"{i + 1}: NOMBRE: {lifestore_products[sales_cat[i][0]-1][1]} --- ID_PROD: {sales_cat[i][0]} --- #VENTAS: {sales_cat[i][1]} ")
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("--------------------------------------------")
            input("Presione enter para continuar")

            #   100 productos con menos búsquedas
            sales_list.sort(key=ordBusquedas)  # Ordenar por Busquedas (Ascendente)
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("- LISTADO DE 100 PRODUCTOS MENOS BUSCADOS --")
            print("--------------------------------------------")
            print("--------------------------------------------")
            if len(sales_list) >= 100:  # Revisar tamaño de lista para evitar error en el for
                num_sales = 100
            else:
                num_sales = len(sales_list)

            for i in range(num_sales):
                print(
                    f"{i + 1}: NOMBRE: {lifestore_products[sales_list[i][0]-1][1]} --- ID_PROD: {sales_list[i][0]} --- #BUSQUEDAS: {sales_list[i][2]} ")
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("--------------------------------------------")
            print("--------------------------------------------")
            input("Presione enter para continuar")


        elif option_analisis == 2:
            #   [2] Productos por reseña en el servicio
            #   Seleccionar solo los registros con ventas (Productos sin ventas no deben considerarse puesto que no han sido evaluados)
            RateArray = []
            for i in range(len(sales_list)):
                if sales_list[i][4] != 0:
                    RateArray.append(sales_list[i])

            #   20 Mejores reseñas
            RateArray.sort(key=ordRat, reverse=True)  #   Ordenar de forma Descendente
            print("********************************************")
            print("********************************************")
            print("*********** 20 MEJORES RESEÑAS *************")
            print("********************************************")
            print("********************************************")
            if len(RateArray) >= 20:  # Revisar tamaño de lista para evitar error en el for
                num_sales = 20
            else:
                num_sales = len(RateArray)
            for i in range(num_sales):
                print(f"{i + 1}: NOMBRE: {lifestore_products[RateArray[i][0]-1][1]} --- ID_PROD: {RateArray[i][0]} --- #RATING: {RateArray[i][4]} ")
            print("********************************************")
            print("********************************************")
            print("********************************************")
            print("********************************************")
            input("Presione enter para continuar")

            #   20 Peores reseñas
            RateArray.sort(key=ordRat)  # Ordenar de forma ascendente
            print("********************************************")
            print("********************************************")
            print("************ 20 PEORES RESEÑAS *************")
            print("********************************************")
            print("********************************************")
            for i in range(num_sales):
                print(
                    f"{i + 1}: NOMBRE: {lifestore_products[RateArray[i][0]-1][1]} --- ID_PROD: {RateArray[i][0]} --- #RATING: {RateArray[i][4]} ")
            print("********************************************")
            print("********************************************")
            print("********************************************")
            print("********************************************")
            input("Presione enter para continuar")

        elif option_analisis == 3:
            #   [3] Sugerir una estrategia
            #   Generar un reporte de Ventas
            lifestore_sales.sort(key=ordDate)
            year = lifestore_sales[0][3][6:]
            month = lifestore_sales[0][3][3:5]
            day = lifestore_sales[0][3][:2]
            VentMes = 0
            IngMes = 0
            DiasMes = 0
            Reporte_Ventas = []
            for i in range(len(lifestore_sales)):
                if day != lifestore_sales[i][3][:2]:
                    DiasMes += 1
                    day = lifestore_sales[i][3][:2]
                if year != lifestore_sales[i][3][6:] or month != lifestore_sales[i][3][3:5]:
                    Reporte_Ventas.append([VentMes, IngMes, month, year, DiasMes])  # Ventas en el mes, ingreso mensual, mes, año, numero de dias con ventas
                    VentMes = 0
                    IngMes = 0
                    DiasMes = 0
                    year = lifestore_sales[i][3][6:]
                    month = lifestore_sales[i][3][3:5]
                    day = lifestore_sales[i][3][:2]
                VentMes += 1
                IngMes += lifestore_products[lifestore_sales[i][1]-1][2]
            DiasMes += 1
            Reporte_Ventas.append([VentMes, IngMes, month, year, DiasMes])
            #   Imprimir resultados anuales
            year = Reporte_Ventas[0][3]
            TotAnual = 0
            print(f"######## {year} ########")
            for i in range(len(Reporte_Ventas)):
                if year != Reporte_Ventas[i][3]:
                    print(f"Total anual fue: ${TotAnual}")
                    TotAnual = 0
                    year = Reporte_Ventas[i][3]
                    print(f"######## {year} ########")
                TotAnual += Reporte_Ventas[i][1]
            print(f"Total anual fue: ${TotAnual}")





        #   Revisar otra opcion
        print("\n\n¿Desea revisar otra opción?")
        option_out = input("Ingrese si para revisar otra opción, cualquier otra entrada para salir. ")
        if option_out.lower() != "si" and option_out.lower() != "s":
            print("\n...Cerrando sesión...")
            regFlag == 0  # "Cierre de sesión"
            break

    #   Usar otro usuario
    print("\n\n¿Desea iniciar sesión con otro usuario?")
    option_out = input("Ingrese si para iniciar otra sesión, cualquier otra entrada para salir. ")
    if option_out.lower() != "si" and option_out.lower() != "s":
        print("\n...Saliendo...")
        break
