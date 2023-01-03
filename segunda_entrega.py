class Cliente:
    #Atributos de clase
    pais = "Colombia"
    zona_horaria = "GMT-5"

    #El constructor
    def __init__(self, name, last_name, unique_identification, customer_type, compra_dolares):
    #Atributos de instancia
        self.name = name
        self.lastname = last_name
        self.identification = unique_identification
        self.customertype = customer_type

    #Método sin argumentos
    def convertir(self):
        print("El cliente acaba de generar una conversión en el e-commerce")

    #Método con argumentos
    def comprar(self, compra_dolares):
        print(f"El cliente acaba de comprar productos por valor de {compra_dolares} dólares")

    #Método __str__
    def __str__(self) -> str:
        return f"El cliente acaba de comprar productos por valor de {self._compra_dolares}"


cliente_prueba_1 = Cliente(name='Alejandro', last_name='Duque', unique_identification = 1, customer_type = 'VIP', compra_dolares=100)

cliente_prueba_1.comprar(100)