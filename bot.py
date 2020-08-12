import connect
import discord

client = discord.Client()
msg_author = []

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == connect.GUILD:
            break

    print(f'{client.user.name} has connected to the following server: ')
    print(f'- {guild.name} | id: {guild.id}')

@client.event
async def new_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Holy moly doki doki.. everyone let welcome our new member @{member.user.name}'
    )

@client.event
async def on_message(message):
    birthday_greetings = ('hbd', 'happy birthday', 'habede')

    if message.author == client.user:
        return 

    if message.author.name not in msg_author:   
        if message.content.lower() in birthday_greetings:
            await message.channel.send('Happy Birthday! 🎈🎉\n'*10)
            msg_author.append(message.author.name)    
    else:
        await message.channel.send('Jangan spam atuh gan!!')
        

client.run(connect.TOKEN)

