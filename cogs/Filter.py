import discord
from discord.ext import commands
from Nastavitve import botid,imgch,manjkaslika,admins,links,censored

class Filter(commands.Cog):

    def __init__(self, client):
        self.client = client

#filter
    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel) and message.author.id != botid: #Preveri če je DM
            dmreply = discord.Embed(title="Trollgang!", description="", color=0x00ff00)
            dmreply.set_author(name="PeroMartic", url="https://www.youtube.com/peromartic", icon_url="https://i.imgur.com/KwxvASH.jpg")
            dmreply.set_thumbnail(url="https://i.imgur.com/KwxvASH.jpg")
            dmreply.add_field(name="**YOUTUBE**", value="https://www.youtube.com/peromartic", inline=True)
            dmreply.add_field(name="**INSTAGRAM**", value="https://www.instagram.com/pero.martic", inline=True)
            dmreply.add_field(name="**SNAPCHAT**", value="https://www.snapchat.com/add/peromartic", inline=True)
            dmreply.add_field(name="**DISCORD**", value="https://bit.ly/peromartic", inline=True)
            dmreply.add_field(name="**MAJICE**", value="https://trollgang.si", inline=True)
            dmreply.add_field(name="**PICI & PERO**", value="https://www.youtube.com/picipero", inline=True)
            dmreply.set_footer(text="Powered by TrollGang")
            try:  # Poskuša odstraniti napake
                await message.author.send(embed=dmreply) #pošlje embed z linki
                return  # Konča komando
            except discord.errors.NotFound or discord.errors.Forbidden:  # Odstrani napake
                return  # Konča komando
        if message.author.id != botid: #Svojih sporočil ne pregleduje
            if message.author.id not in admins: #Sporočil administratorjev ne pregleduje
                if any(link in message.content.lower() for link in links): #Preveri če vsebuje kombinacije linkov
                    try: #Poskuša odstraniti napake
                        await message.channel.purge(limit=1) #Briše sporočilo če najde povezavo
                        await message.author.send(censored) #Pošlje DM obvestilo o kršenju
                        return #Konča komando
                    except discord.errors.NotFound or discord.errors.Forbidden: #Odstrani napake
                        return #Konča komando
                else: #Če ne zasledi linka
                    if message.channel.id == imgch: #Preverja kanal SLIKE
                        if not message.attachments: #Preveri za datoteke v sporočilu
                            try: #Poskuša odstraniti napake
                                await message.channel.purge(limit=1) #Odstrani sporočilo če nima slike
                                await message.author.send(manjkaslika) #Pošlje DM o manjkajoči sliki
                                return #Konča komando
                            except discord.errors.NotFound or discord.errors.Forbidden: #Odstrani napake
                                return #Konča komando
                        else: #Če zazna datoteko
                            return #Konča komando
                    else: #Če ni kanal SLIKE
                        return #Konča komando
            else: #Če zazna admina
                return #Konča komando
        else: #Če zazna sam sebe
            return #Konča komando


def setup(client):
    client.add_cog(Filter(client))

