import discord

from core import traits, names
from core.npc import NPC

# Please add your bot client token here.  
# The token is listed on your application's "Bots" page
from core.spell import parse_spells, get_spells_by_level

TOKEN = 'NjQ1NDQ0MjU2NTAwMTU0NDAw.XdCqzg.mwWFpjWsrlct8Prpt95ElLlTlSg'
client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!spin'):
        data = message.content.split(' ')
        if len(data) < 4:

            await message.channel.send("Spin like this: !spin <race> <gender> <archtype> [traitcount]")
        else:
            race = data[1]
            gender = data[2]
            archtype = data[3]
            if len(data) > 4:
                trait_count = int(data[4])
            else:
                trait_count = 5
            if len(data) > 5:
                caster_level = int(data[5])
            else:
                caster_level = None

            spells = None
            if caster_level:
                full_spell_list = parse_spells()
                spells = get_spells_by_level(caster_level, full_spell_list)

            npc = NPC(
                archtype=archtype,
                gender=gender,
                race=race,
                name=names.generate_name(race, gender),
                traits=traits.get_traits_by_count_and_archtype(trait_count, archtype),
                spells=spells
            )

            headline = "*{race} {gender}*\n{first} {last}\n".format(race=npc.race, gender=npc.gender, first=npc.name['first'],
                                                                 last=npc.name['last'])
            trait_text = ""
            for trait in npc.traits:
                trait_text = trait_text + '\t' + trait + '\n'

            resp_text = headline + trait_text

            if spells:
                spell_text = "Spells:\n"
                for spell_level in spells.keys():
                    spell_text = spell_text + '\tLevel ' + str(spell_level) + ':\n'
                    for spell in spells[spell_level].keys():
                        spell_text = spell_text + '\t\t' + spell + ':\n'
                resp_text += spell_text

            await message.channel.send('```' + resp_text + '```')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
