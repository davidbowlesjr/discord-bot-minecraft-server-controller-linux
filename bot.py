# bot.py
import os

from mcstatus import JavaServer
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MINECRAFT_DIR = os.getenv('MINECRAFT_DIR')
SERVER_IP_PUBLIC = os.getenv('SERVER_IP_PUBLIC')
SERVER_IP_LOCAL = os.getenv('SERVER_IP_LOCAL')
RUN_SERVER_COMMAND = os.getenv('RUN_SERVER_COMMAND')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} connected to Discord')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_content = message.content.lower()

    if (not(message_content.startswith('x'))):
        return
    
    if message_content == 'x start':
         await message.channel.send(start())
    elif message_content == 'x ping' or message_content == 'x status':
         await message.channel.send(ping())
    elif message_content == 'x stop':
         await message.channel.send(stop())
    elif message_content == 'x players':
         await message.channel.send(getPlayers())     
    elif message_content == 'x help':
         await message.channel.send("Commands are [Start, Stop, Ping, Status, Players, Help] case insensitive")
    elif 'sex mod' in message_content:
         await message.channel.send("Fuck you")
    
        

def ping():
    try:
        server = JavaServer.lookup(SERVER_IP_PUBLIC)
        serverStatus = server.status()
        return (f"The server has {serverStatus.players.online} players online and replied in {int(serverStatus.latency)} ms")
    except:
        if status():
            return "The server is running but not online (could be starting)"
        return "The server is offline"
    
def getPlayers():
    try:
        query = JavaServer.lookup(SERVER_IP_LOCAL).query()
        return(f"The server has the following players online: {', '.join(query.players.names)}")
    except:
        if status():
            return "The server is running but not online (could be starting)"
        return "The server is offline"


def start():
    if not status():
        os.chdir(MINECRAFT_DIR)
        os.system('screen -dmS "minecraft" ' + RUN_SERVER_COMMAND)
        return("Server started.")
    else:
        return("Server already started.")

def stop():
    if status():
        os.system('screen -S minecraft -X stuff "{}\015"'.format('stop'))
        return("Server stopped.")
    else:
        return("Server not running.")

def status():
    output = os.popen('screen -ls').read()
    if '.minecraft'  in output:
        return True
    else:
        return False

    

client.run(TOKEN)