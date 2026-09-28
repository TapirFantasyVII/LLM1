import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def clasificarSklearn(frase, vectorizer, modelo):

    frase_vectorizada = vectorizer.transform([frase])

    resultado = modelo.predict(frase_vectorizada)

    return resultado[0]


# Leer JSON
with open("../frases.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)


# -------------------------
# DATOS DE ENTRENAMIENTO
# -------------------------

datosTrain = datos["train"]

frasesTrain = []
etiquetasTrain = []

for frase in datosTrain:

    frasesTrain.append(frase["texto"])
    etiquetasTrain.append(frase["etiqueta"])


# -------------------------
# VECTORALIZAR TEXTO
# -------------------------

vectorizer = TfidfVectorizer()

frasesVectorizadas = vectorizer.fit_transform(frasesTrain)


# -------------------------
# ENTRENAR MODELO
# -------------------------

modelo = LogisticRegression()

modelo.fit(
    frasesVectorizadas,
    etiquetasTrain
)


# -------------------------
# COMPROBAR CON TEST
# -------------------------

datosTest = datos["test"]

aciertos = 0
total = 0

for frase in datosTest:

    texto = frase["texto"]
    etiquetaEsperada = frase["etiqueta"]

    etiquetaObtenida = clasificarSklearn(
        texto,
        vectorizer,
        modelo
    )

    print("Texto:", texto)
    print("Etiqueta esperada:", etiquetaEsperada)
    print("Etiqueta obtenida:", etiquetaObtenida)

    if etiquetaObtenida == etiquetaEsperada:
        aciertos += 1
        print("Correcto")
    else:
        print("Incorrecto")

    total += 1

    print()


# -------------------------
# RESULTADO
# -------------------------

precision = aciertos / total * 100

print("Aciertos:", aciertos)
print("Total:", total)
print("Precisión:", precision, "%")