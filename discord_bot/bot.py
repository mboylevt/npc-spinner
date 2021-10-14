import discord

from core import traits, names
from core.npc import NPC

# Please add your bot client token here.  
# The token is listed on your application's "Bots" page
TOKEN = 'YOUR BOT TOKEN HERE'
client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!spin'):
        data = message.content.split(' ')
        if len(data) < 4:
            await client.send_message(message.channel, "Spin like this: !spin <race> <gender> <archtype> [traitcount]")
        else:
            race = data[1]
            gender = data[2]
            archtype = data[3]
            if len(data) > 4:
                trait_count = int(data[4])
            else:
                trait_count = 5

            npc = NPC(
                archtype=archtype,
                gender=gender,
                race=race,
                name=names.generate_name(race, gender),
                traits=traits.get_traits_by_count_and_archtype(trait_count, archtype)
            )

            headline = "*{race} {gender}*\n{first} {last}\n".format(race=npc.race, gender=npc.gender, first=npc.name['first'],
                                                                 last=npc.name['last'])
            trait_text = ""
            for trait in npc.traits:
                trait_text = trait_text + '\t' + trait + '\n'
            await client.send_message(message.channel, headline + trait_text)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
