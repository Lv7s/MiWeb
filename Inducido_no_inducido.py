from xml.sax.handler import feature_validation


VolNoinducido = float(
    input("Introduce el volumen que tomaste del no inducido en uL: "))
DONoInducido = float(input("Introduce la DO inicial del no inducido: "))
DOInducido = float(input("Introduce la DO final del inducido: "))
factor = DOInducido/DONoInducido
Volinducido = VolNoinducido/factor
print(f'{"Tienes que tomar: "}{round(Volinducido,2)}{" "}{"uL del inducido para dejarlos iguales"}')
