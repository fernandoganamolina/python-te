import json
class Te:
    
    def __init__(self): #constructor que carga el json
        data=open("data.json")
        self._data=json.load(data)
        
    def getter(self): #muestra todos los datos del json
        return self._data
    
    def canti(self): #cantidad de elementos del json
        return len(self._data)
    
    def buscar(self,id): #busca item del json segun su indice
        return self._data[id]
    
    
    def buscar_formato(self,formato=0): #busca item del json segun formato ingresado (300 ó 500)
        lista2=[]
        cant=self.canti()
        for index in range(cant):
            for key,value in self._data[index].items():
                if  key=='formato' and value==formato:
                    lista2.append(self._data[index])
        return lista2 
    
    
    def buscar_tipo(self,tipo=0): #busca item del json segun tipo ingresado (1=te negro;2=te verde;3=hierbas)
        lista2=[]
        cant=self.canti()
        tipo2=['te negro','te verde','hierbas']
        for index in range(cant):
            for key,value in self._data[index].items():
                if  key=='sabor' and value==tipo2[tipo-1]:
                    lista2.append(self._data[index])
        return lista2    