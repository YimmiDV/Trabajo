diccionario= {
    "JUISIOSO" : "Persona responsable",
    "CAUSA" : " amigo, mejor amigo o persona confiable",
    "CHIMBA" : "hay expectattivas",
    "AGUACATE":  "conocido tambien como palta ",
    "CRINGE" : "algo raro o embarazoso"
    
    
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in diccionario.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(diccionario[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("la palabra no se encontro")
