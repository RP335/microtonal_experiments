
import os
from xenharmlib import EDOTuning, export, UpDownNotation, play
import numpy as np
output_dir = 'microtonal_audio_files'
os.makedirs(output_dir, exist_ok=True)

def generate_and_export_chords(edo,  duration=2.0, sample_rate=22050):
    edoTuning = EDOTuning(edo)
    root = edoTuning.pitch(0)
    third = edoTuning.pitch(4*edo/12)
    fifth = edoTuning.pitch(7*edo/12)
    for i in range (15):
        triad = edoTuning.pitch_scale([root, third, fifth]).transpose((np.random.randint(50,61))*edo/12)
        filename = os.path.join(output_dir, f'microtonal_chord_{edo}edo_{i+1}.wav')
        export.audio.export_wav(filename, triad, duration=duration, play_as_chord=True, sample_rate=sample_rate)


edos = [11, 15, 19, 31, 53, 24]
for edo in edos:
    generate_and_export_chords(edo, 2.0, 22050 )
# import os
# from xenharmlib import EDOTuning, export, UpDownNotation
#
# # Example chord_map
# chord_map = {
#     'B7': ('C7', 'M', 7),
#     'F#7': ('C7', 'A', 4),
#     'C#7': ('C7', 'A', 1),
#     'G7': ('C7', 'P', 5),
#     'D7': ('C7', 'M', 2),
#     'A7': ('C7', 'M', 6),
#     'Eb7': ('C7', 'm', 3),
#     'Bb7': ('C7', 'm', 7),
#     'F7': ('C7', 'P', 4)
# }
#
# output_dir = 'microtonal_audio_files'
# os.makedirs(output_dir, exist_ok=True)
#
#
# def generate_and_export_chords(edo, root_chords, duration=2.0, sample_rate=22050):
#     edoTuning = EDOTuning(edo)
#     notation = UpDownNotation(edoTuning)
#
#     C7 = notation.note_scale([notation.note(s, 0) for s in root_chords['C7']])
#
#     for chord_name, (root, interval, steps) in chord_map.items():
#         root_chord = C7
#         sh = notation.shorthand_interval
#         transposed_chord = root_chord.transpose(sh(interval, steps))
#
#         filename = os.path.join(output_dir, f'microtonal_chord_{edo}edo_{chord_name}.wav')
#         export.audio.export_wav(filename, transposed_chord, duration=duration, play_as_chord=True,
#                                 sample_rate=sample_rate)
#         print(f'Exported microtonal chord audio to {filename}')
#
#
#
# root_chords = {
#     'C7': ['C', 'E', 'G']
# }
#
# edos = [31, 11, 19, 24]
# for edo in edos:
#     generate_and_export_chords(edo, root_chords)
#
#
# print(f'Generated WAV files in {output_dir} directory.')


# edo12 = EDOTuning(12)
# edo31 = EDOTuning(31)
# n_edo12 = UpDownNotation(edo12)
# n_edo31 = UpDownNotation(edo31)
#
# edo12_chord = n_edo12.note_scale(
#     [n_edo12.note(s, 4) for s in ['C', 'E', 'G', 'Bb']]
# )
#
# edo31_chord = n_edo31.note_scale(
#     [n_edo31.note(s, 4) for s in ['C#', 'F', 'G#', 'vBb']]
# )

# edo12 = EDOTuning(31)
# c0 = edo12.pitch(0)
# e0 = edo12.pitch(4*31/12)
# g0 = edo12.pitch(7*31/12)
#
# c_triad = edo12.pitch_scale([c0, e0, g0]).transpose(50*31/12)
# #
# play(c_triad, duration=2, play_as_chord=True)
# play(edo31_chord, duration=2, play_as_chord=True)
