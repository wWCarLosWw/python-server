import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

VOICE_CHANNEL_IDS = [1516020814053642340,1516020972694802515,1459695916889149440,1459695855526477845,1527903471922184192,1527852585598451854]

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم {bot.user.name}")
    
    for channel_id in VOICE_CHANNEL_IDS:
        channel = bot.get_channel(channel_id)
        if channel and isinstance(channel, discord.VoiceChannel):
            try:
                if not discord.utils.get(bot.voice_clients, channel=channel):
                    await channel.connect()
                print(f"تم الدخول إلى الروم بنجاح {channel.name}")
            except Exception as e:
                print(f"حدث خطأ أثناء محاولة الدخول إلى الروم {channel_id}: {e}")

bot.run(os.getenv("DISCORD_TOKEN"))

from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
  سترى_الرسالة = 'Bot is running!'
  return 'Bot is running!'


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


# استدعاء الدالة قبل تشغيل البوت
keep_alive()