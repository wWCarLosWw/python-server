import discord
from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.voice_states = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}', flush=True)
    
    VOICE_CHANNEL_IDS = [
        1516020814053642340,
        1516020972694802515,
        1459695916889149440,
        1459695855526477845,
        1527903471922184192,
        1527852445831622696
    ]
    
    for channel_id in VOICE_CHANNEL_IDS:
        try:
            channel = await client.fetch_channel(channel_id)
            print(f"Found channel: {channel.name} (Type: {type(channel)})", flush=True)
            if channel and isinstance(channel, discord.VoiceChannel):
                await channel.connect()
                print(f"Successfully joined voice channel: {channel.name}", flush=True)
            else:
                print(f"Skipped: Channel {channel_id} is not a voice channel", flush=True)
        except Exception as e:
            print(f"ERROR connecting to channel {channel_id}: {e}", flush=True)

keep_alive()
token = os.environ.get('DISCORD_TOKEN')
client.run(token)