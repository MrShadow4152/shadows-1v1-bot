import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

s = []
p = []
c = 0
status = cycle(['.Help','.Search'])
accept1 = 0
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.',intents = intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is Ready.')
    change_status.start()
    print(c)

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(next(status)))

@client.command(aliases=["Help"])
async def help(ctx):
    await ctx.send(f'.Search - Search for a 1v1 \n.Stop - Stop searching for a 1v1')

@client.command(aliases=['Search','1v1'])
async def search(ctx):
    await ctx.send("{} searching for opponents...".format(ctx.message.author.mention))
    s.append(ctx.message.author.id)
    c = stringcount = len(s)
    print(s[c-1])

    while c >= 2:
        r1 = random.randint(0,(c-1))
        temp_list = [el for el in s if el != s[r1]]
        r2 = random.randint(0,(c-2))
        Uid1 = s[r1]
        Uid2 = temp_list[r2]
        del s[r1]
        del s[r2]
        await ctx.send("<@"+str(Uid1)+"> vs <@"+str(Uid2)+"> \n.Accept to accept\n.Deny to deny")
        c = stringcount = len(s)
        @client.command(aliases=['Accept'])
        async def accept(ctx):
            print('bruh')

@client.command(aliases=['Stop'])
async def stop(ctx):
    await ctx.send("{} Stoped searching for opponents".format(ctx.message.author.mention))
    s.remove(ctx.message.author.id)

    
@client.command(aliases=['Deny'])
async def deny(ctx):
    print('you are bad')
client.run('ODE2NDUwMjY0NjI1OTcxMjEx.YD7Ijw.gBWZKd923mbLleTEWIOhXSBczYI')

