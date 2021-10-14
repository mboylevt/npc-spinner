from flask import Blueprint, jsonify, request

from core import names, traits
from core.npc import NPC
from core.spell import parse_spells, get_spells_by_level
import json

npc = Blueprint('npc', __name__)
spells = None

@npc.route('/status')
def status():
    return jsonify({'status': 'ok'})


@npc.route('/npc_slack', methods=['GET', 'POST'])
def npc_gen_slack():
    data = request.form['text'].split(' ')
    caster_level = None
    race = data[0]
    gender = data[1]
    archtype = data[2]
    if len(data) > 3:
        trait_count = int(data[3])
    else:
        trait_count = 5
    if len(data) > 4:
        caster_level = int(data[4])

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
    headline = "*{race} {gender}*\nName: {first} {last}\n".format(race=npc.race, gender=npc.gender, first=npc.name['first'], last=npc.name['last'])
    trait_text = "Traits:\n"
    for trait in npc.traits:
        trait_text = trait_text + '\t' + trait + '\n'
    spell_text = "Spells:\n"
    for spell_level in spells.keys():
        spell_text = spell_text + '\tLevel ' + str(spell_level) + ':\n'
        for spell in spells[spell_level].keys():
            spell_text = spell_text + '\t\t' + spell + ':\n'
    resp = {
        "response_type": "in_channel",
        "text": headline + trait_text + spell_text,
        "username": "SpinNPC",
        "mrkdwn": "true"
    }
    return jsonify(resp)


@npc.route('/npc', methods=['GET', 'POST'])
def npc_gen():

    full_spell_list = parse_spells()
    spells = None

    race = request.args.get('race')
    gender = request.args.get('gender')
    archtype = request.args.get('archtype')
    trait_count = int(request.args.get('traitCount')) if request.args.get('traitCount') else 5
    caster_level = int(request.args.get('caster')) if request.args.get('caster') else None
    if caster_level:
        spells = get_spells_by_level(caster_level, full_spell_list)

    npc = NPC(
        archtype=archtype,
        gender=gender,
        race=race,
        name=names.generate_name(race, gender),
        traits=traits.get_traits_by_count_and_archtype(trait_count, archtype),
        spells=spells
    )
    return jsonify(npc.__dict__)