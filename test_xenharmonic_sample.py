from xenharmlib import EDOTuning, export, UpDownNotation

edos = [31, 19, 11]
for edo in edos:
    edoTuning = EDOTuning(edo)
    n_edo = UpDownNotation(edoTuning)
    chord = n_edo.note_scale(
        [n_edo.note(s, 4) for s in ['C', 'E', 'G', 'Bb']]
    )
    filename = f'microtonal_chord_{edo}edo.wav'
    export.audio.export_wav(filename, chord, duration = 2.0, play_as_chord= True, sample_rate=22500)
