import discord
import os


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
  print('Member joined, sending application')
  if member.dm_channel:
    return

  await member.create_dm() 
  await member.dm_channel.send('IGN:')
  member.fetch_message()

@client.event
async def on_message(message):
  



  




client.run(os.getenv('TOKEN'))