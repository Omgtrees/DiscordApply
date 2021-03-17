import discord
import os


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

APPLICANT_TABLE = {
  "3452345": {
    "ign"
  }
}

APPLICANT_DATA = {
  "ign": "",
  "age": "",
  "reason": ""
}

#id = client.get_guild(818285299578175548)
#channels = ["whitelist"]

@client.event
async def on_member_join(member):
 # APPLICANT_TABLE[member.id].append(APPLICANT_DATA)
  print('Member joined, sending application')
  if member.dm_channel:
    return

  await member.create_dm() 
  await member.dm_channel.send('IGN:')


@client.event
async def on_message(message):
  if message.author.id is client.user.id:
    return
  if message.channel is discord.DMChannel:
    if APPLICANT_TABLE[message.author.id].reason == "":  # if there is no reason
      APPLICANT_TABLE[message.author.id].reason = message.content

  print (message.content)


client.run(os.getenv('TOKEN'))