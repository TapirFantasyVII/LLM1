from transformers import pipeline

classifier = pipeline("sentiment-analysis")
 
a = input("Introduce una expresión y la clasificare en positivo o negativa: ")

print(classifier(a))