def read_file_to_dict(filename):
    ventas_dict = {}
    with open(filename, "r") as archivo:
            linea = archivo.read()  # leemos todo el contenido


    ventas = linea.split(";")  # separa por punto y coma

    for venta in ventas:
        if venta != "":  # evita procesar una cadena vacía (por ; final)
            producto, valor = venta.split(":")
            valor = float(valor)  # podés usar int(valor) si no hay decimales

            if producto not in ventas_dict:
                ventas_dict[producto] = []

            ventas_dict[producto].append(valor)

    return ventas_dict
#el output {'producto1': [100.0, 150.0], 'producto2': [200.0, 100.0], 'producto3': [50.0]}


def process_dict(dict1):
    for producto, ventas in dict1.items():
        total = sum(ventas)
        promedio = total / len(ventas)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
