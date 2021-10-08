import lyricsgenius


class GeniusAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.genius = lyricsgenius.Genius(self.api_key)

    def get_lyrics(self, artist, song):
        try:
            song = self.genius.search_song(song, artist)
            return song.lyrics
        except Exception as e:
            print(e)
            return None


    
GeniusAPI = GeniusAPI()
print(GeniusAPI.get_lyrics('The Beatles', 'Hey Jude'))
