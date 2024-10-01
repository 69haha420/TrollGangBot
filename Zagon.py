import discord
import os
from discord.ext import commands
from Nastavitve import prfx,token,actname,actype,actstatus

client = commands.Bot(command_prefix = prfx)
client.remove_command('help')

#login
@client.event
async def on_ready():
    activity = discord.Activity(name=actname, type=actype)
    await client.change_presence(activity=activity, status=actstatus)
    print(f'Prijava uspela: {client.user}')

#Load extensions
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'✔ {filename[:-3]} ✔')
        except Exception as e:
            print(f'❌ {filename[:-3]} ❌')

#token
client.run(token)