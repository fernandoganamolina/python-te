from te import Te
te1=Te()

print("-----------RESUTADOS POR TIPO------------")
data=te1.buscar_tipo(3) #busca por tipo
for item in data:
    dict=item #pasamos el item de la lista a un diccionario
    print(f'su pedido de {dict["sabor"]} de {dict["formato"]} gramos está registrado. se recomienda consumir en {dict["descrip"]}'.upper())
    
print("-----------RESUTADOS POR FORMATO------------")    
data=te1.buscar_formato(300) #busca por formato
for item in data:
    dict=item #pasamos el item de la lista a un diccionario
    print(f'su pedido de {dict["sabor"]} de {dict["formato"]} gramos está registrado. se recomienda consumir en {dict["descrip"]}'.upper())