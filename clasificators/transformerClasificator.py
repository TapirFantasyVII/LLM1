import json
from transformers import pipeline

def clasificarTransform(frase, classifier):

    resultado = classifier(
        frase,
        candidate_labels=["SOLTAR", "MOVER", "REVISAR", "AGARRAR"]
    )

    maxVal = 0
    etiqueta = "NONE"

    print(resultado)

    for etiquetaActual, valor in zip(
        resultado["labels"],
        resultado["scores"]
    ):
        if valor > maxVal:
            maxVal = valor
            etiqueta = etiquetaActual

    return etiqueta
    


# Leer JSON
with open("../frases.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)


# Obtener datos de entrenamiento
datosTrain = datos["test"]
classifier = pipeline("zero-shot-classification")

aciertos = 0
total = 0


# Clasificar frases
for frase in datosTrain:

    print("Texto:", frase["texto"])
    print("Etiqueta esperada:", frase["etiqueta"])

    etiqueta = clasificarTransform(frase["texto"], classifier)

    print("Etiqueta obtenida:", etiqueta)

    total += 1

    if etiqueta == frase["etiqueta"]:
        aciertos += 1

    print()


print("Aciertos:", aciertos)
print("Total:", total)
print("Precisión:", aciertos / total * 100, "%")