import json
from typing import Union


def search_symbol_matches(symbol: str):

    with open('all.json', mode='r') as raw:
        chains = json.loads(raw.read())

    filtered_list = []
    for chain_id in chains:
        token_list = chains.get(chain_id)
        for token in token_list:
            ticker = token.get('symbol')
            if symbol.lower() in ticker.lower():
                filtered_list.append(token)

    _write_to_json(
        criteria=symbol,
        def_name=search_symbol_matches.__name__,
        filtered_list=filtered_list
    )


def filter_by_symbol(symbol: str):

    with open('all.json', mode='r') as raw:
        chains = json.loads(raw.read())

    filtered_list = []
    for chain_id in chains:
        token_list = chains.get(chain_id)
        for token in token_list:
            ticker = token.get('symbol')
            if ticker.lower() == symbol.lower():
                filtered_list.append(token)

    _write_to_json(
        criteria=symbol,
        def_name=filter_by_symbol.__name__,
        filtered_list=filtered_list
    )


def filter_by_chain_id(chain_id: int):

    with open('all.json', mode='r') as raw:
        chains = json.loads(raw.read())

    filtered_list = chains.get(str(chain_id))

    _write_to_json(
        criteria=chain_id,
        def_name=filter_by_chain_id.__name__,
        filtered_list=filtered_list
    )


def filter_by_sources(sources_list: list):

    with open('all.json', mode='r') as raw:
        chains = json.loads(raw.read())

    filtered_list = []
    for chain_id in chains:
        token_list = chains.get(chain_id)
        for token in token_list:
            listed_in = token.get('listedIn')
            for source in sources_list:
                if source in listed_in:
                    filtered_list.append(token)
                    break

    _write_to_json(
        criteria=sources_list,
        def_name=filter_by_sources.__name__,
        filtered_list=filtered_list
    )


def _write_to_json(
        criteria: Union[str, int, list],
        def_name: str,
        filtered_list: list
):
    description = ''
    if def_name == 'filter_by_sources':
        for source in criteria:
            description += '_' + source
    elif def_name == 'filter_by_chain_id':
        description = '_chain_id_' + str(criteria)
    elif def_name == 'filter_by_symbol':
        description = '_symbol_' + criteria
    else:
        description = '_' + str(criteria)

    with open(f'filtered_by{description}.json', 'w') as f:
        f.write(json.dumps(filtered_list, indent=4))
