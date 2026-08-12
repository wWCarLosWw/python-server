import os
from threading import Thread
import discord
from discord.ext import commands
from flask import Flask

# 1. إعداد فلاسك لفتح المنفذ المطلوب في Render
app = Flask('')


@app.route('/')
def home():
  return 'Bot is running!'


def run_flask():
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)


def keep_alive():
  t = Thread(target=run_flask)
  t.start()


# تشغيل السيرفر أولاً
keep_alive()

# 2. إعدادات بوت الديسكورد
intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

VOICE_CHANNEL_IDS = [
    1516020814053642340,
    1516020972694802515,
    1459695916889149440,
    1459695855526477845,
    1527903471922184192,
    152785258598451854,
]


@bot.event
async def on_ready():
  print(f'تم تسجيل الدخول بنجاح باسم {bot.user.name}')

  for channel_id in VOICE_CHANNEL_IDS:
    channel = bot.get_channel(channel_id)
    if channel and isinstance(channel, discord.VoiceChannel):
      try:
        if not discord.utils.get(bot.voice_clients, channel=channel):
          await channel.connect()
          print(f'تم الدخول إلى الروم بنجاح {channel.name}')
      except Exception as e:
        print(f'حدث خطأ أثناء محاولة الدخول إلى الروم {channel_id}: {e}')


# 3. تشغيل البوت في النهاية
bot.run(os.getenv('DISCORD_TOKEN'))