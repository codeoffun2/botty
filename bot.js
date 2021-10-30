const { Client, Intents } = require("discord.js");
const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES]
});

// When the app is ready it will write out Ready using this
client.once('ready', () => {
	console.log('Ready!');
});

client.on('message', message => {
	if (message.content === '!Hello') {
        // send back "Pong." to the channel the message was sent in
        message.channel.send('hello to you too.');
	}

});

client.on('message', (message) => {
 let regex = /who/i;
 if (regex.test(message.content)) {
  message.channel.send("ur mom");
 }

});

client.on('message', (message) => {
 let regex = /ligma/i;
 if (regex.test(message.content)) {
  message.channel.send("balls");
 }

});

// Replace the value between the quotes with your token
client.login('redacted for privacy');
