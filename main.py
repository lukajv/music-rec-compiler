import discord

# Read token from token.txt
token_file = open("token.txt")
token = token_file.read().strip()
token_file.close()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logged in!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")

client.run(token)
