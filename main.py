import math
res = 0

errorsimp = 0
while res != 3:
    re1 = 0
    print("-------Menu-------")
    print("1.- Metodo trapecio")
    print("2.- Metodo Simpson")
    print("3.- Salir del programa")
    res = input("Ingrese una opcion: ")
    if res == "1":
        print("-----Metodo Trapecio Caso General-----")
        print("Ejercicio propuesto: 3*xj**2")
        n = float(input("Ingrese el valor de n: "))
        b = float(input("Ingrese el valor de b: "))
        a = float(input("Ingrese el valor de a: "))
        h = (b - a) / n
        ncont = 0
        Efamasjh = 0
        fbigualf2 = 0
        n1 = 0
        ia = 3*b**2
        ib = 3*a**2

        while ncont <= n:
            xj = (a + (ncont * h))
            fx = 3*xj**2
            if 0 < ncont < n:
                Efamasjh = Efamasjh + fx
            elif ncont == n:
                fbigualf2 = fx
            elif ncont == 0:
                n1 = fx
            print("n = ", ncont, "  Xj = ", xj, "  fx = ", fx)
            ncont += 1

        Efamasjh2 = Efamasjh * 2
        sumatoria1 = n1 + fbigualf2 + Efamasjh2
        hd2 = h / 2
        final = hd2 * sumatoria1

        print("")
        print(n1, " ", Efamasjh, " ", fbigualf2, " ", Efamasjh2, " ", sumatoria1, " ", hd2, " ")
        print("Respuesta final: ", final)
        Error = abs(8 - final)
        print("Error:", Error)


    elif res == "2":
        print("-----Metodo Simpson-----")
        print("Ejercicio propuesto: 3*xj**2")
        n = float(input("Ingrese el valor de n: "))
        b = float(input("Ingrese el valor de b: "))
        a = float(input("Ingrese el valor de a: "))
        h = (b - a) / n
        ncont = 0
        pares = 0
        inpares = 0
        fbigualf2 = 0
        Efamasjh = 0
        n1 = 0
        while ncont <= n:
            xj = (a + (ncont * h))
            fx = 3*xj**2
            if ncont % 2 == 0:
                if ncont != n and ncont != a:
                    pares = pares + fx
            else:
                inpares = inpares + fx
            if ncont == 0:
                Efamasjh = fx
            elif ncont == n:
                fbigualf2 = fx

            print("n = ", ncont, "  Xj = ", xj, "  fx = ", fx)
            ncont += 1

        sumainparesx2 = inpares * 4
        sumaparesx2 = pares * 2
        sumatoria = Efamasjh + sumainparesx2 + sumaparesx2 + fbigualf2
        hd3 = h/3
        final = sumatoria * hd3
        print("")
        print(Efamasjh, " ", inpares, " ", fbigualf2, " ", sumainparesx2, " ", pares, " ", sumaparesx2, " ", sumatoria, " ", hd3, " ")
        print("Respuesta final: ", final)
        Error = abs(8 - final)
        print("Error:", Error)
    elif res == "3":
        print("Saliendo del programa...")
    else:
        print("Ingrese una opción valida")

