import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

s = []
c = 0
a = []
q = 0
g = 999999
h = 999999
z = []
count = 0
status = cycle(['.Help','.Search'])
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.',intents = intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is Ready.')
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    global z
    global count
    global Uid1
    global Uid2
    global r1
    global r2
    global c
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(next(status)))
    count = count + 10
    #1 day = 86400
    if count == 86400:
        z.clear()
        print(count)
        count = 0
    if c == 2:
            r1 = random.randint(0,(c-1))
            temp_list = [el for el in s if el != s[r1]]
            r2 = random.randint(0,(c-2))
            Uid1 = s[r1]
            Uid2 = temp_list[r2]
            if (str(Uid1)+str(Uid2)) in z:
                pass
            elif (str(Uid2)+str(Uid1)) in z:
                pass
            else:
                while c >= 2:
                    r1 = random.randint(0,(c-1))
                    temp_list = [el for el in s if el != s[r1]]
                    r2 = random.randint(0,(c-2))
                    Uid1 = s[r1]
                    Uid2 = temp_list[r2]
                    z.append(str(Uid2)+str(Uid1))
                    del s[r1]
                    del s[r2]
                    a.append(str(Uid1)+'A')
                    a.append(str(Uid2)+'B')
                    channel = client.get_channel(816486378011099139)
                    await channel.send("<@"+str(Uid1)+"> vs <@"+str(Uid2)+"> \n.Accept to accept\n.Deny to deny")
                    c = stringcount = len(s)

@client.command(aliases=["Help"])
async def help(ctx):
    if ctx.message.channel.id == 816486378011099139:
        await ctx.send(f'.Search - Search for a 1v1 \n.Stop - Stop searching for a 1v1 \n.Accept accept a pending 1v1 and get taken out of que \n.Deny denys a pending 1v1 (will eventually put back in que just need to finish `If accept or deny set 8 hour cool down on matching with that person` before that)')

@client.command(aliases=['Search','1v1'])
async def search(ctx):
    global c
    global z
    global Uid1
    global Uid2
    global r1
    global r2
    if ctx.message.channel.id == 816486378011099139:
        await ctx.send("{} searching for opponents...".format(ctx.message.author.mention))
        s.append(ctx.message.author.id)
        c = stringcount = len(s)
        print(s[c-1])
        if c == 2:
            r1 = random.randint(0,(c-1))
            temp_list = [el for el in s if el != s[r1]]
            r2 = random.randint(0,(c-2))
            Uid1 = s[r1]
            Uid2 = temp_list[r2]
            if (str(Uid1)+str(Uid2)) in z:
                pass
            elif (str(Uid2)+str(Uid1)) in z:
                pass
            else:
                while c >= 2:
                    r1 = random.randint(0,(c-1))
                    temp_list = [el for el in s if el != s[r1]]
                    r2 = random.randint(0,(c-2))
                    Uid1 = s[r1]
                    Uid2 = temp_list[r2]
                    z.append(str(Uid2)+str(Uid1))
                    del s[r1]
                    del s[r2]
                    a.append(str(Uid1)+'A')
                    a.append(str(Uid2)+'B')
                    await ctx.send("<@"+str(Uid1)+"> vs <@"+str(Uid2)+"> \n.Accept to accept\n.Deny to deny")
                    c = stringcount = len(s)

@client.command(aliases=['Stop'])
async def stop(ctx):
    if ctx.message.channel.id == 816486378011099139:
        if ctx.message.author.id in s:
            s.remove(ctx.message.author.id)
            await ctx.send("{} Stoped searching for opponents".format(ctx.message.author.mention))
        else:
            await ctx.send("{} there is nothing to stop".format(ctx.message.author.mention))
@client.command(aliases=['Accept'])
async def accept(ctx):
    if ctx.message.channel.id == 816486378011099139:
        global q
        global g
        global h
        if str(ctx.message.author.id)+'A' in a:
           g = a.index(str(ctx.message.author.id)+'A')
           a[g] = a[g].replace('A','')
           q = q + 1
           await ctx.send("<@"+str(ctx.message.author.id)+"> accepted "+str(q)+"/2")
           print(a)
        elif str(ctx.message.author.id)+'B' in a:
           h = a.index(str(ctx.message.author.id)+'B')
           a[h] = a[h].replace('B','')
           q = q + 1
           await ctx.send("<@"+str(ctx.message.author.id)+"> accepted "+str(q)+"/2")
           print(a)
        else:
           await ctx.send("{} Could Not Find Anything To Accept Please Contact Mr.Shadow#4152 if you have an issue".format(ctx.message.author.mention))
        if q == 2:
            if g != 999999:
                await ctx.send("<@"+str(a[g])+"> vs <@"+str(a[g-1])+"> CONFIRMED GLHF")
            elif h != 999999:
                await ctx.send("<@"+str(a[h+1])+"> vs <@"+str(a[h])+"> CONFIRMED GLHF")
            #USE THIS PART TO ADD TO LIST THAT PREVENTS MATCH UP FOR 8 HOURS
            if g != 999999:
                del a[g]
                del a[g-1]
                q = 0
                g = 999999
                h = 999999
            elif h != 999999:
                del a[h+1]
                del a[h]
                q = 0
                g = 999999
                h = 999999
        else:
            print('')

@client.command(aliases=['Deny'])
async def deny(ctx):
    if ctx.message.channel.id == 816486378011099139:
        global g
        global h
        global q
        q = 0
        if str(ctx.message.author.id)+'A' in a:
           g = a.index(str(ctx.message.author.id)+'A')
           a[g] = a[g].replace('A','')
           await ctx.send("<@"+str(ctx.message.author.id)+"> denied use .search if you would like to find another match.")
           if g != 999999:
                print(a)
                del a[g]
                del a[g-1]
                g = 999999
                h = 999999
           elif h != 999999:
                del a[h-1]
                del a[h-1]
                g = 999999
                h = 999999

        elif str(ctx.message.author.id)+'B' in a:
           h = a.index(str(ctx.message.author.id)+'B')
           a[h] = a[h].replace('B','')
           await ctx.send("<@"+str(ctx.message.author.id)+"> denied use .search if you would like to find another match.")
           if g != 999999:
                print(a)
                del a[g]
                del a[g-1]
                g = 999999
                q = 0
                h = 999999
           elif h != 999999:
                del a[h-1]
                del a[h-1]
                g = 999999
                h = 999999
                q = 0
           
        else:
           await ctx.send("{} Could Not Find Anything To Deny Please Contact Mr.Shadow#4152 if you have an issue".format(ctx.message.author.mention))

@client.command()
async def purge(ctx, ammount=5):
    if ctx.message.author.id == 397095437074563104:
        await ctx.channel.purge(limit=ammount)
    else:
        await ctx.send('you do not have the perms to purge')

client.run('ODE2NDUwMjY0NjI1OTcxMjEx.YD7Ijw.gBWZKd923mbLleTEWIOhXSBczYI')


