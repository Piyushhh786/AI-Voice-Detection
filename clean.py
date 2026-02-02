import os
import random

clips_path = r"E:\Desktop\GUVI\Malayalam_real\cv-corpus-24.0-2025-12-05-ml\cv-corpus-24.0-2025-12-05\ml\clips"

files = [
    f for f in os.listdir(clips_path)
    if os.path.isfile(os.path.join(clips_path, f))
]

num = len(files) - 50
files_to_delete = random.sample(files,num)
for file in files_to_delete:
    os.remove(os.path.join(clips_path,file))

print("Successfully deleted the files")