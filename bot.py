import discord
from discord.ext import commands
import time
import os
import json

# CONFIG FILES // CONFIG.JSON
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f);
else:
    configTemplate = {"Token": "", "Prefix": ""};
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f);

token = configData["Token"];
prefix = configData["Prefix"];

intents = discord.Intents.all();                                       
bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None);

color = discord.Color.dark_gold(); # ΕΔΩ ΒΑΣΕΤΕ ΤΟ ΧΡΩΜΑ ΣΤΟ EMBED ΣΑΣ
servername = '' # ΕΔΩ ΒΑΖΕΤΕ ΤΟ ΟΝΟΜΑ ΤΟΥ ΣΕΡΒΕΡ ΣΑΣ
imagelink = '' # ΕΔΩ ΒΑΖΕΤΕ ΤΟ LINK ΤΗΣ ΕΙΚΟΝΑΣ ΤΟΥ ΣΕΡΒΕΡ

# ROLE IDS
StaffRole =  # Εδώ βάζεις το role id του Staff
EmsRole =  # Εδώ ΄βάζεις το role id του Ems
PoliceRole =  # Εδώ ΄βάζεις το role id του Police

# APPLICATION LINKS
StaffLink = '' # Εδώ ΄βάζεις το application link (Google Documents) του Police
EmsLink = '' # Εδώ ΄βάζεις το application link (Google Documents) του Ems
PoliceLink = '' # Εδώ ΄βάζεις το application link (Google Documents) του Staff

@bot.event  
async def on_ready():
    print('Thank you for using my bot, if you have any questions dm: Playboy®#2737')
    time.sleep(3)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your Applications"));
    print(f"{bot.user} has logged in");

@bot.command()
async def apps(ctx):
    StaffEmbed = discord.Embed(description=f"[<@&{StaffRole}>]({StaffLink})", color=color);
    EmsEmbed = discord.Embed(description=f"[<@&{EmsRole}>]({EmsLink})", color=color);
    PoliceEmbed = discord.Embed(description=f"[<@&{PoliceRole}>]({PoliceLink})", color=color);
    embeds = [StaffEmbed, EmsEmbed, PoliceEmbed]
    for i in embeds:
        await ctx.send(embed=i);

bot.run(token)
