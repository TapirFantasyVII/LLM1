import json 

def clasificarHardCoded(frase):

    frase = frase.lower()

    palabras_ambiguas = [
        "eso",
        "aquello",
        "como antes",
        "lo mismo",
        "ahí"
    ]

    palabras_agarrar = [
        "agarra",
        "agarrar",
        "coge",
        "coger",
        "sujeta",
        "sujetar",
        "toma",
        "tomar"
    ]

    palabras_mover = [
        "mueve",
        "mover",
        "desplaza",
        "desplazar",
        "lleva",
        "llevar",
        "acerca",
        "acercar"
    ]

    palabras_soltar = [
        "suelta",
        "soltar",
        "libera",
        "liberar",
        "deja",
        "dejar"
    ]

    # Primero comprobamos negaciones
    if "no " in frase:
        return "REVISAR"

    # Después comprobamos referencias ambiguas
    for palabra in palabras_ambiguas:
        if palabra in frase:
            return "REVISAR"

    # Comprobamos AGARRAR
    for palabra in palabras_agarrar:
        if palabra in frase:
            return "AGARRAR"

    # Comprobamos MOVER
    for palabra in palabras_mover:
        if palabra in frase:
            return "MOVER"

    # Comprobamos SOLTAR
    for palabra in palabras_soltar:
        if palabra in frase:
            return "SOLTAR"

    # Si no coincide ninguna regla
    return "REVISAR"
 


# Leer JSON
with open("../frases.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)


# Obtener datos de entrenamiento
datosTrain = datos["test"] 
aciertos = 0
total = 0


# Clasificar frases
for frase in datosTrain:

    print("Texto:", frase["texto"])
    print("Etiqueta esperada:", frase["etiqueta"])

    etiqueta = clasificarHardCoded(frase["texto"])

    print("Etiqueta obtenida:", etiqueta)

    total += 1

    if etiqueta == frase["etiqueta"]:
        aciertos += 1

    print()


print("Aciertos:", aciertos)
print("Total:", total)
print("Precisión:", aciertos / total * 100, "%")