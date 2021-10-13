# Discord_Music_bot
<p align="left">
<a href="https://github.com/DivyaKumarBaid/Discord_Music_bot/blob/main/LICENSE" alt="Lisence"><img src="https://img.shields.io/github/license/DivyaKumarBaid/Discord_Music_bot"></a> <a href="https://github.com/DivyaKumarBaid/Discord_Music_bot/issues" alt="Issues"><img src="https://img.shields.io/github/issues/DivyaKumarBaid/Discord_Music_bot"></a> <a href="https://twitter.com/DivyakumarBaid1?s=09" alt="Twiter-Follow"><img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2FDivyaKumarBaid%2FDiscord_Music_bot"></a>
</p>

This is a simple Discord Music bot that plays music 24/7 looping thorugh the available ones in directory.
To run this bot we need to several packages such as PyNaCl, discord.py

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) \
To install discord.py

```bash
python3 -m pip install -U discord.py
```
To install PyNaCl
```bash
pip install pynacl
```
To install youtube_dl
```bash
pip install youtube_dl
```
You also need to install [FFmpeg](https://www.ffmpeg.org/) 
API key for song lyrics should be acquired from [Genius](https://docs.genius.com/)

## Pre-Text:

This is a discord bot made using the lastest discord.py api as of march 2021. This bot plays mp3 file from the storage i.e. all the mp3 files available to play from the file of your bot. I did this program in python language and have used discord.py , youtube_dl , PyNaCl , FFmpeg and several other packages and api's. Initially this bot was build on repl.it IDE and can run for infinite time i.e. it will be online continuously using [Uptimerobot](https://uptimerobot.com/)

## How to Install

1. Create a ```python``` virtual environment.I did in repl.it
2. Clone the repo ```git clone https://github.com/DivyaKumarBaid/Discord_Music_bot.git``` or download the repository.
3. Go to the cloned/downloaded directory ``` cd Discord_Music_bot ``` 
4. Upload it in ```repl.it```
5. Create a bot in [discord developers portal]((https://discord.com/developers/docs/game-and-server-management/vanity-perks))
6. Copy the ``Token`` of the bot and paste it in the ``.env`` file as ``TOKEN``
7. Run the bot on ```repl.it```
8. Copy the ``url`` that appears on the right side of window
9. Go to [Uptimerobot](https://uptimerobot.com/) and create a monitor and paste the copied ``url`` and start the monitor.This will keep the bot alive even after you close it.

     For more precise steps have a look at [FreeCodeCamp](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)

## Commands

```
  add              This adds a music to the playlist. The url must be of youtube
  clear            This command clears given number of messages and by default it clears last 5 messages
  clear_playlist   This command removes every available mp3 file
  join             This adds bot to the given channel and by default in General
  play             This command plays song from the available ones.Providing channel would let the bot run there else by default it will run in General
  remove           This command removes the specified .mp3 file
  songs            This command lists all the songs available to play
  stop             This stops the music playing and the bot leaves the voice channel
  lyrics           This displays the lyrics for the current playing song
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
