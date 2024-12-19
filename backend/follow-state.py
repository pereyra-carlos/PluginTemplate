def proceso_largo(n):
    parcial = 0
    for i in range(n):
        parcial += i
        yield parcial  # Retorna el estado parcial sin terminar la función

for estado_intermedio in proceso_largo(5):
    print("Estado intermedio:", estado_intermedio)
