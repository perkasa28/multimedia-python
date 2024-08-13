from pydub import AudioSegment
import simpleaudio as sa


# # Memuat file audio
audio = AudioSegment.from_file('music.mp3')

wave_obj = sa.WaveObject.from_wave_file('format.wav')
play_obj = wave_obj.play()

play_obj.wait_done()

# # Menyimpan file audio
# audio.export('music.mp3', format='mp3')

# # ##PEMOTONGAN AUDIO
#clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
# clipped_audio.export('music.mp3', format='mp3')
# audio.export('clipped.mp3', format='mp3')

# ##PENGGABUNGAN AUDIO
#combined_audio = audio + clipped_audio
#combined_audio.export('combine.mp3', format='mp3')
# audio.export('clipped.mp3', format='mp3')

# ##MENGUBAH FORMAT AUDIO
# audio.export('format.wav', format='wav')


# ##PENGATURAN VOLUME
louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('volume.mp3', format='mp3')