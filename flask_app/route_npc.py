from flask import Blueprint, jsonify, request

from core import names, traits
from core.npc import NPC

npc = Blueprint('npc', __name__)


@npc.route('/status')
def status():
    return jsonify({'status': 'ok'})


@npc.route('/npc_slack', methods=['GET', 'POST'])
def npc_gen_slack():
    return request.form
    data = request.form['text'].split(' ')
    race = data[0]
    sex = data[1]
    archtype = data[2]
    if len(data) > 3:
        trait_count = int(data[3])
    else:
        trait_count = 5

    npc = NPC(
        archtype=archtype,
        sex=sex,
        race=race,
        name=names.generate_name(race, sex),
        traits=traits.get_traits_by_count_and_archtype(trait_count, archtype)
    )
    return jsonify(npc.__dict__)


@npc.route('/npc', methods=['GET', 'POST'])
def npc_gen():
    race = request.args.get('race')
    sex = request.args.get('sex')
    archtype = request.args.get('archtype')
    trait_count = int(request.args.get('traitCount')) if request.args.get('traitCount') else 5

    npc = NPC(
        archtype=archtype,
        sex=sex,
        race=race,
        name=names.generate_name(race, sex),
        traits=traits.get_traits_by_count_and_archtype(trait_count, archtype)
    )
    return jsonify(npc.__dict__)