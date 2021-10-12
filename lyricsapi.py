import lyricsgenius
import os


class GeniusAPI:
    def __init__(self, api_key = 'eVcYRzRSIyZGt6L7xqmg_mb2SS8Wr-5bR0VKaRmTDc3tMu3IxHgjcSH-FiiesynKDJdAD0km-XRP2ikcopEpMg'):
        self.api_key = api_key
        self.genius = lyricsgenius.Genius(self.api_key)

    def get_lyrics(self, song, artist = None):
        try:

            if artist is None:
                song = self.genius.search_song(song)
                
            else:
                song = self.genius.search_song(song, artist)
                
            return song.lyrics

        except Exception as e:
            return e
    

def get_current_song():
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            return file.split('.mp3')[0]











    

