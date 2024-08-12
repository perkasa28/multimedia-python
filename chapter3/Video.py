from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx



### 🎥 Memuat dan Menyimpan File Video
# Memuat file video
video = VideoFileClip('google.mp4')

# Menyimpan file video
video.write_videofile('gugel.mp4')

### ✂️ Operasi Dasar

#### Pemotongan
short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('gugel.mp4')

#### Penggabungan
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('gugel.mp4')

#### Penambahan Efek
reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('gugel.mp4')

#### Pengaturan Kecepatan
sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('gugel.mp4')