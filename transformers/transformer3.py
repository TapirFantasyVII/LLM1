from transformers import pipeline

classifier = pipeline("zero-shot-classification")

frase = input("Introduce la expresión: ")

etiquetas = input("Introduce la lista de etiquetas separadas por espacio: ")

listaEtiquetas = etiquetas.split()

resultado = classifier(
    frase,
    candidate_labels=listaEtiquetas,
)

print(resultado)