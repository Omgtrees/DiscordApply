import discord
import os


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

# APPLICANT_TABLE = {
#   "3452345": {
#     "ign"
#   }
# }

APPLICANT_DATA = {
  "ign": [],
  "age": [],
  "reason": []
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
  if isinstance(message.channel, discord.channel.DMChannel):
    APPLICANT_DATA["ign"].append(message.content)
    print (APPLICANT_DATA.items())

 # if message.channel is discord.DMchannel

client.run(os.getenv('TOKEN'))