import whisper
from moviepy import VideoFileClip
from tqdm import tqdm
import os
import pdb

path = r'C:\Users\hly\PyCharmMiscProject\知乎\Video'
script = r'C:\Users\hly\PyCharmMiscProject\知乎\营销原理'
print(os.path.isdir(path))
print(os.path.isdir(script))
items = [it.replace('.txt','.mp4') for it in os.listdir(script)]

model = whisper.load_model("turbo")


for ii, item in enumerate(os.listdir(path)):
    if item not in items:
        print(f'current file : {ii} -> {item}')
        mp4_filepath = os.path.join(path, item)
        script_path = os.path.join(script, item.replace('.mp4','.txt'))

        base_path = r'C:\Users\hly\PyCharmMiscProject\知乎\TMP'
        tmp_dir = os.path.join(base_path, 'tmp')
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)

        mp3_filepath = tmp_dir
        video_clip = VideoFileClip(mp4_filepath)
        time_duration = int(video_clip.duration)
        segment_size = 10

        full_text = ""

        for ii in tqdm(range(0, time_duration, segment_size)):
            if ii + segment_size < time_duration:
                clipped_video = video_clip.subclipped(ii, ii + segment_size)
            else:
                clipped_video = video_clip.subclipped(ii, time_duration)
            audio_clip = clipped_video.audio
            mp3_file = os.path.join(mp3_filepath, str(ii) + ".mp3")
            audio_clip.write_audiofile(mp3_file)
            result = model.transcribe(audio=mp3_file)
            full_text += result["text"]

        with open(script_path,'w', encoding='utf-8') as f:
          f.write(full_text)
          full_text = ""

        print("extracted text")
        print(full_text)
        print(f'text has been save to {script_path}')

