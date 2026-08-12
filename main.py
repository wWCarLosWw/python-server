import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

VOICE_CHANNEL_IDS = [1516020972694802515]

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