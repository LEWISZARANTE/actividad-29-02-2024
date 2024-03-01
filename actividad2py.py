# Precios de los productos
PRECIO_COMPUTADOR_ESCRITORIO = 800
PRECIO_COMPUTADOR_MESA = 600
PRECIO_TABLETA = 400
PRECIO_VIDEOBEAM = 1000
PRECIO_TELEVISOR = 1200

# Cantidad inicial de productos
cantidad_computador_escritorio = 0
cantidad_computador_mesa = 0
cantidad_tableta = 0
cantidad_videobeam = 0
cantidad_televisor = 0

while True:
    print("\nPRODUCTOS DISPONIBLES:")
    print("1. computador de escritorio")
    print("2. computador de mesa")
    print("3. tableta")
    print("4. videobeam")
    print("5. televisor")
    print("6. facturar")
    opcion = int(input("seleccione una opcion: "))

    if opcion == 1:
        cantidad_computador_escritorio += 1
    elif opcion == 2:
        cantidad_computador_mesa += 1
    elif opcion == 3:
        cantidad_tableta += 1
    elif opcion == 4:
        cantidad_videobeam += 1
    elif opcion == 5:
        cantidad_televisor += 1
    elif opcion == 6: 
        total_pagar = (cantidad_computador_escritorio * PRECIO_COMPUTADOR_ESCRITORIO +
                       cantidad_computador_mesa * PRECIO_COMPUTADOR_MESA +
                       cantidad_tableta * PRECIO_TABLETA +
                       cantidad_videobeam * PRECIO_VIDEOBEAM +
                       cantidad_televisor * PRECIO_TELEVISOR)
        print("\nRESUMEN DE COMPRA:")
        print("computadores de escritorio:", cantidad_computador_escritorio)
        print("computador de mesa:", cantidad_computador_mesa)
        print("tabletas:", cantidad_tableta)
        print("videobeam:", cantidad_videobeam)
        print("televisores:", cantidad_televisor)
        print("total a pagar:", total_pagar)
        break
