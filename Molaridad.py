#para reactivos que tengan peso y sean en polvo
NACL= 58.44
HEPES=238.30
MGCL2ANHIDRO=95.21
TRIS= 121.14
MGCL2HEXAHIDRATO=203.31 
Metodo= (input("¿Que metodo deseas usar?: "))
if Metodo== "AUTOMATICO":
    Buffer = (input("¿Que buffer deseas preparar?: "))
    if Buffer == "HEPES":
        Volumen = float(input("Introduce el volumen en L que deseas de Hepes: "))
        Hepes = float(input("Introduce la concentración en M de Hepes: "))
        Hepesgr= HEPES*Volumen*Hepes
        NaCl = float(input("Introduce la concentración en M de NaCl: "))
        NaClgr= NACL*Volumen*NaCl
        MgCl = float(input("Introduce la concentración en M de MgCl: "))
        MgClgr= MGCL2HEXAHIDRATO*Volumen*MgCl
        Glicerol = float(input("la cantidad en mL que deseas de glicerol: "))
        Glicerolgr = Glicerol*1.26
        print(f'{"Para: "}{Volumen}{" "}{"Litros de HEPES"}')
        print(f'{"Tienes que pesar: "}{Hepesgr}{" "}{"gramos de Hepes"}')
        print(f'{"Tienes que pesar: "}{NaClgr}{" "}{"gramos de NaCl"}')
        print(f'{"Tienes que pesar: "}{MgClgr}{" "}{"gramos de MgCl Hexahidro"}')
        print(f'{"Tienes que pesar: "}{Glicerolgr}{" "}{"gramos de glicerol"}')
    if Buffer == "TRIS":
        Volumen = float(input("Introduce el volumen en L que deseas de TRIS: "))
        Tris = float(input("Introduce la concentración en M de TRIS: "))
        Trisgr= TRIS*Volumen*Tris
        NaCl = float(input("Introduce la concentración en M de NaCl: "))
        NaClgr= NACL*Volumen*NaCl
        MgCl = float(input("Introduce la concentración en M de MgCl: "))
        MgClgr= MGCL2HEXAHIDRATO*Volumen*MgCl
        Glicerol = float(input("la cantidad en mL que deseas de glicerol: "))
        Glicerolgr = Glicerol*1.26
        print(f'{"Para: "}{Volumen}{" "}{"Litros de TRIS"}')
        print(f'{"Tienes que pesar: "}{Trisgr}{" "}{"gramos de TRIS"}')
        print(f'{"Tienes que pesar: "}{NaClgr}{" "}{"gramos de NaCl"}')
        print(f'{"Tienes que pesar: "}{MgClgr}{" "}{"gramos de MgCl Hexahidro"}')
        print(f'{"Tienes que pesar: "}{Glicerolgr}{" "}{"gramos de glicerol"}')
if Metodo== "MANUAL":
    MolecularWeight= float(input("Introduce el peso molecular: "))	
    VolumenLitros= float(input("Introduce el volumen en L que deseas: "))
    MolaridadMoles= float(input("Introduce la molaridad a la que deseas (en Moles): "))
    Pesoengramos= MolecularWeight*VolumenLitros*MolaridadMoles
    print(f'{"Tienes que pesar "}{Pesoengramos}{" "}{"gramos"}{" "}{"en"}{" "}{VolumenLitros}{"Litros"}{" "}{"para tenerlo a"}{" "}{MolaridadMoles}{"Moles"}')

    