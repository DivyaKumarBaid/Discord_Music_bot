# Discord_Music_bot

pre-requirements:

PyNaCl FFmpeg discord.py
I have been using repl package installer to install these files
rest refer to google to install these packages

Pretext:

This is a discord bot made using the lastest discord.py api as of march 2021. This bot plays mp3 file from the storage i.e. all the mp3 files available to play from the file of your bot. I did this program in python language and have used discord.py , youtube_dl , PyNaCl , FFmpeg and several other packages and api's. Initially this bot was biuld on repl.it IDE and can run for infinite time i.e. it will be online continuously.

Logic:

This bot uses url of youtube to download the song in mp3  format and then play in specified voice channel of your server for 24/7 be it a single song or a playlist it will download and loop thorugh different songs available as download. There is a funtion that runs continuously and is triggered by a user command and we can specify in which channel to play or else by default it will play it on General channel. I have added a method to deal with errors and probably wont create a problem.
We have several commands that I would list down

Commands:

  add              This adds a music to the playlist. The url must be of youtube
  clear            This command clears given number of messages and by default it clears last 5 messages
  clear_playlist   This command removes every available mp3 file
  join             This adds bot to the given channel and by default in General
  play             This command plays song from the available ones.Providing channel would let the bot t=run there else by default it will run in General
  remove           This command removes the specified .mp3 file
  songs            This command lists all the songs available to play
  stop             This stops the music playing and the bot leaves the voice channel
  
  Silent features:
  I have used embeded texts and auto delete message for bots message on playing a song.We can also use permission for commands using @commands.has_permissions(#parameters)
  
  Steps to use my code :
  1.) login into discords developers portal (https://discord.com/developers/docs/game-and-server-management/vanity-perks) and add a new application 
  2.) create a bot
  3.) head to oauth2 and click on bot under scope and administrator under bot permission.This would give your bot administrator right
  4.) copy the link given in OAuth2 above the bots permission
  5.) paste the link in browser to add the bot to your server
  6.) now head to repl.ot
  7.) create an account and start a new project wiht python as language
  8.)  Click on the three dot button and upload my file there 
            OR 
       Copy the main.py code from mine to the repl's one
       Create an .env file in the same directory as the main file is in and copy the code
       Create a keep_alive.py file and copy my code
  
 9.)  Now again go to the bot section in discord developers portal and Copy the token that is in the bot section
 10.) Paste the toke in the .env file as TOKEN= ##copiedtoken
 11.) Now run the code
  
     This will show up a web page on the right hand side of the, copy the url
     
 12.) Head to Uptimerobot (https://uptimerobot.com/) wesite to use it as a monitor to ping your bot to keep it alive
 13.) create a monitor giving the https.// address copied from repl there and start monitor
       
       NOW YOUR BOT WILL BE RUNNING FINE AND CONTINUOUSLY
       
 I WOULD WELCOME ANY IMPROVEMENT TO THE BOT AND WILL DEFINATELY UPDATE IT IN THE UPCOMING TIME.
 
 TO KNOW MORE PRECISELY THE WAY TO CREATE BOT I WOULD SUGGEST YOU TO GO THROUGH https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
 
