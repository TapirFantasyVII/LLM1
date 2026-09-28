from transformers import pipeline

generator = pipeline("text-generation")


a = input("Introduce una expresión y la completare: ")

print("Generando respuesta...")

resultado = generator(
    a,
    max_new_tokens=5
)

print("Respuesta:")
print(resultado[0]["generated_text"])