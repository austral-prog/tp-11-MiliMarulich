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


def process_dict(data):
    for producto in sorted(data.keys()):
        ventas = data[producto]
        total = sum(ventas)
        if len(ventas) > 0:
            promedio = total / len(ventas)
            total_str = "{:.2f}".format(total)
            promedio_str = "{:.2f}".format(promedio)
            print(producto + ": ventas totales $" + total_str + ", promedio $" + promedio_str)
        else:
            print(producto + ": no hay ventas registradas")
