import discord
from flask import Flask
from threading import Thread
import os

# إعدادات الفلاسك للإبقاء على السيرفر نشطاً
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# إعدادات بوت الديسكورد
intents = discord.Intents.default()
intents.voice_states = True  # مهم جداً للرومات الصوتية
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    # ضع هنا أللدي (ID) الخاص بالروم الصوتي الذي تريد أن يدخله البوت
    CHANNEL_ID = 123456789012345678  # استبدل الرقم برقم الروم الخاص بك
    
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        try:
            await channel.connect()
            print(f"Successfully joined voice channel: {channel.name}")
        except Exception as e:
            print(f"Failed to join voice channel: {e}")

keep_alive()
token = os.environ.get('DISCORD_TOKEN')
client.run(token)