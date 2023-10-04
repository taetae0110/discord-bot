import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

#command_prefix는 봇의접두사 입니다!
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("ONLINE")

@bot.command()
async def 말따라해ctx, arg):
    await ctx.send(arg)

#TOKEN에 디스코드봇 토큰넣으심되용
client.run("TOKEN")
