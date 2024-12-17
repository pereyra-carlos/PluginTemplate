import pulsectl

def event_callback(ev):
    # Solo nos interesa los eventos 'change' en dispositivos de tipo 'sink'
    if ev.facility == 'sink' and ev.t == 'change':
        with pulsectl.Pulse('volume-listener') as pulse:
            # Obtener la información del sink usando el índice del evento
            try:
                sink = pulse.sink_info(ev.index)
                # Calcular el volumen promedio como porcentaje
                volume_avg = round(100 * sum(sink.volume.values) / len(sink.volume.values))
                print(f'Volume change detected on sink {ev.index} ({sink.name}): {volume_avg}%')
            except Exception as e:
                print(f'Failed to fetch sink information: {e}')

with pulsectl.Pulse('event-listener') as pulse:
    pulse.event_callback_set(event_callback)
    pulse.event_mask_set('all')  # Escuchar todos los tipos de eventos para asegurarse de no perder ninguno
    print('Listening to volume changes on PulseAudio sinks (press Ctrl+C to stop)...')
    try:
        while True:
            pulse.event_listen()
    except KeyboardInterrupt:
        print('Stopped by user.')
