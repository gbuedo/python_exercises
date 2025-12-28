usuarios = [{"nombre": "María", "edad": 30, "ciudad": "Madrid"},
{"nombre": "Pedro", "edad": 25, "ciudad": "Barcelona"}]

for usuario in usuarios:
    print(f"{usuario['nombre']} vive en {usuario['ciudad']} y tiene {usuario['edad']} años.")