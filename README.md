Hosted on my raspberry Pi zero!
<h2> Commands </h2>

General

!help [command] - Prints a list of commands, or info on a command if one is specified.

!play <URL/query> - Plays audio from a specific URL or searches for a query on YouTube and queues the first result.

!queue - Displays all of the media that is queued.

!np - Displays the media that is currently being played.

!skip - Vote to skip the current media. Required skips/skip ratio is set in the config file. The bot’s owner will instantly skip when using !skip f.

!search [service] [#] <query> - Searches a specific service (default: YT) for a query and returns the first few results (default: 3, limit: 10). The user can then select from the results if they want to add any to the queue.

!shuffle - Shuffles the queue.

!clear - Clears the queue.

!pause - Pauses the current media.

!resume - Resumes the current media

!volume [number] - Sets the volume of the bot for everyone. Should be a number between 1 and 100. Can be relative (e.g +10 to add 10 to current volume). If no parameter is given, it will display the current volume.

!clean <number> - Searches through the number of messages given and deletes those that were sent by the bot, effectively cleaning the channel. If the bot has Manage Messages on the server, it will delete user command messages too, like !play.

!summon - Connects the bot to your current voice channel, if it has permission.

!perms - Sends a message to the user with their bot permissions.

!stream <url> - Streams a URL. This can be a Twitch, YouTube, etc livestream, or a radio 
stream. This feature of the bot is experimental and may have some issues.

!save - Saves the current song to the autoplaylist.

!karaoke - Enables karaoke mode in a server. During karaoke mode, only users with the BypassKaraokeMode permission can queue music.

!joke - Tells a joke

!temp - shows my raspberry pis temperature

Admin


!blacklist <status> <@user1>... - Add or remove users from the blacklist. Blacklisted users cannot use any bot commands. This overrides any permissions settings set in the permissions file. The owner cannot be blacklisted. Multiple users can be specified in the command. Users must be @mentioned. Status should be either +, -, add, or remove.

!joinserver - Provides the URL that can be used to add the bot to another server. This command 
is always restricted to the owner of the bot.

!leaveserver <name/id> - Forces the bot to leave a server. You must specify either the server name or id.

!pldump <playlist> - Collects URLs from a YouTube playlist or Soundcloud set and dumps them into a text file that can be copied into the autoplaylist.

!setavatar [url] - Changes the bot’s avatar to the specified URL or uploaded image. A URL does not need to be specified if an image is uploaded with the command as the message (comment).

!setname <name> - Changes the bot’s Discord username (not nickname). Discord limits these changes to 2/hr.


!setnick <nick> - Changes the bot’s nickname on a server, if it has permission to do so.

!disconnect - Disconnects the bot from the voice channel.

!restart - Restarts the bot.

!shutdown - Shuts down the bot and terminates the process.

!option <option> <y/n> - Changes a config option without restarting the bot for the current 
session. Run !help option for info.

!remove <number> - Removes a song from the queue by its numbered position. Use !queue to find 
out song positions.

!resetplaylist - Resets all songs in the server’s autoplaylist.


<h2> How to install </h2>
feel free to put issues if something goes wrong

<p>

First create a discord server.
<p>
Then go to:
https://discordapp.com/developers/applications
<p>
 Click new application and choose a name
<p>
Then click add bot in the bot section 
<p>
After that, go to the oauth2 section and select the bot scope.
<p>
Copy the url and select the server you selected 
<p>
Now you can start installing the bot!
<b> Note
<p>
These steps are for linux </b>

```BASH
sudo apt update
sudo apt install python3-pip python3-cffi
sudo pip3 install discord.py[voice] 
sudo python3 -m pip install -U discord.py[voice]
wget https://unofficial-builds.nodejs.org/download/release/v17.0.1/node-v17.0.1-linux-armv6l.tar.gz
#do this if you aren't on arm6l (aka raspberry Pi zero)
wget https://nodejs.org/dist/v17.0.1/node-v17.0.1-linux-arm64.tar.xz
tar -xf  node-v17.0.1-linux-armv6l.tar.gz 
#tar -xf node-v17.0.1-linux-arm64.tar.xz if you aren't on a raspberry Pi zero
sudo mv node-v17.0.1-linux-armv6l /usr/local/node
#sudo mv node-v17.0.1-linux-arm64.tar.xz /usr/local/node if you aren't on a raspberry Pi zero
cd /usr/bin
sudo ln -s /usr/local/node/bin/node node
sudo ln -s /usr/local/node/bin/npm npm
node -v  # Verifying that the Node.js install worked
npm -v   # Verifying that the npm install worked
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
nvm --version
npm init
npm install discord.js
sudo git install https://github.com/codeoffun2/botty/
cd botty
nano bot.js
#find line 12 and insert your bot token there
nano bot.py
#find line 8 and use your token there
screen 
ctrl-a :
sessionname bottypy
enter
python3 bot.py
ctrl-a ctrl-d
screen
ctrl-a :
sessionname bottyjs
enter
node bot.js
ctrl-a ctrl-d
```` 

<p>
visit https://github.com/Just-Some-Bots/MusicBot to learn how to install the music bot code (not mine)

<h2> LICENCE</h2>
<p>
Botty is distributed under the MIT License.
