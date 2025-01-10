import csv
import random
from datetime import datetime, timedelta

# Listas de nombres, estados y ciudades de México
nombres = ["Maria", "Jose", "Juan", "Ana", "Pedro", "Sofia", "Luis", "Carmen", "Miguel", "Angela"]
estados_ciudades = {
    "Jalisco": ["Guadalajara", "Puerto Vallarta", "Zapopan"],
    "Nuevo Leon": ["Monterrey", "San Pedro Garza Garcia", "Apodaca"],
    "Ciudad de Mexico": ["Benito Juarez", "Cuauhtemoc", "Miguel Hidalgo"],
    "Veracruz": ["Veracruz", "Xalapa", "Coatzacoalcos"],
    "Yucatan": ["Merida", "Valladolid", "Progreso"]
}
generos = ["Masculino", "Femenino"]

# Función para generar una fecha de nacimiento aleatoria
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

# Crear el archivo CSV
with open('../estadisticas.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nombre", "Edad", "Salario", "Localidad", "Genero", "Fecha de nacimiento"])

    for i in range(100):
        nombre = random.choice(nombres)
        edad = random.randint(18, 65)
        salario = round(random.uniform(10000, 100000), 2)
        estado = random.choice(list(estados_ciudades.keys()))
        ciudad = random.choice(estados_ciudades[estado])
        localidad = f"{estado}#{ciudad}"
        genero = random.choice(generos)
        fecha_nacimiento = random_date(datetime(1950, 1, 1), datetime(2005, 12, 31)).strftime("%Y-%m-%d")

        writer.writerow([nombre, edad, salario, localidad, genero, fecha_nacimiento])