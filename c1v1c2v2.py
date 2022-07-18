CalcDeseado = (input("¿Que deseas calcular?: "))
if CalcDeseado == "c1":
    v1 = float(input("Introduce el volumen 1: "))
    c2 = float(input("Introduce la concentración 2: "))
    v2 = float(input("Introduce el volumen 2: "))
    c1 = (c2*v2)/v1
    print(f'{"tu concentracion 1 es "}{c1}')
if CalcDeseado == "v1":
    c1 = float(input("Introduce la concentración 1: "))
    c2 = float(input("Introduce la concentración 2: "))
    v2 = float(input("Introduce el volumen 2: "))
    v1 = (c2*v2)/c1
    print(f'{"tu volumen 1 es "}{v1}')
if CalcDeseado == "c2":
    c1 = float(input("Introduce la concentración 1: "))
    v1 = float(input("Introduce el volumen 1: "))
    v2 = float(input("Introduce el volumen 2: "))
    c2 = (c1*v1)/v2
    print(f'{"tu concentracion 2 es "}{c2}')
if CalcDeseado == "v2":
    c1 = float(input("Introduce la concentración 1: "))
    v1 = float(input("Introduce el volumen 1: "))
    c2 = float(input("Introduce la concentración 2: "))
    v2 = (c1*v1)/c2
    print(f'{"tu volumen 2 es "}{v2}')