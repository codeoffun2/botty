Hosted on my raspberry Pi zero!

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
