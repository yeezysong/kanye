import os
import json
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

# Set the folder to the current directory
songs_folder = './'
playlist_metadata = []

# Iterate over each mp3 file in the songs folder
for filename in os.listdir(songs_folder):
    if filename.endswith('.mp3'):
        file_path = os.path.join(songs_folder, filename)
        audio = MP3(file_path, ID3=EasyID3)
        song_data = {
            'filename': filename,
            'title': audio.get('title', [''])[0],
            'artist': audio.get('artist', [''])[0],
            'album': audio.get('album', [''])[0],
            'genre': audio.get('genre', [''])[0],
            'duration': round(audio.info.length, 2) if audio.info else 0
        }
        playlist_metadata.append(song_data)

# Save metadata to playlist_metadata.json
with open(os.path.join(songs_folder, 'playlist_metadata.json'), 'w') as f:
    json.dump(playlist_metadata, f, indent=4)

print("Metadata saved to playlist_metadata.json")
