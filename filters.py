import json
from typing import Optional

import networks


def search_symbol_matches(symbol: str, mainnet: Optional[bool] = None):

    with open('all.json', mode='r') as raw:
        chains = json.loads(raw.read())

    filtered_list = []
    for chain_id in chains:
        token_list = chains.get(chain_id)
        if mainnet:
            if chain_id in networks.MAINNET.values():
                for token in token_list:
                    ticker = token.get('symbol')
                    if symbol.lower() in ticker.lower():
                        filtered_list.append(token)
        elif mainnet is False:
            if chain_id in networks.TESTNET.values():
                for token in token_list:
                    ticker = token.get('symbol')
                    if symbol.lower() in ticker.lower():
                        filtered_list.append(token)
        elif mainnet is None:
            for token in token_list:
                ticker = token.get('symbol')
                if symbol.lower() in ticker.lower():
                    filtered_list.append(token)

    if mainnet is None:
        description = '_symbol_match_' + symbol
    else:
        description = '_symbol_match_' + symbol + f'_[{mainnet=}]'
    _write_to_json(description, filtered_list)


def filter_by_symbol(symbol: str, mainnet: Optional[bool] = None):

    with open('all.json', mode='r') as raw:
        chains = json.loads(raw.read())

    filtered_list = []
    for chain_id in chains:
        token_list = chains.get(chain_id)
        if mainnet:
            if chain_id in networks.MAINNET.values():
                for token in token_list:
                    ticker = token.get('symbol')
                    if ticker.lower() == symbol.lower():
                        filtered_list.append(token)
        elif mainnet is False:
            if chain_id in networks.TESTNET.values():
                for token in token_list:
                    ticker = token.get('symbol')
                    if ticker.lower() == symbol.lower():
                        filtered_list.append(token)
        elif mainnet is None:
            for token in token_list:
                ticker = token.get('symbol')
                if ticker.lower() == symbol.lower():
                    filtered_list.append(token)

    if mainnet is None:
        description = '_symbol' + symbol
    else:
        description = '_symbol' + symbol + f'_[{mainnet=}]'
    _write_to_json(description, filtered_list)


def filter_by_chain_id(chain_id: int):

    with open('all.json', mode='r') as raw:
        chains = json.loads(raw.read())

    chain_name = networks.ALL.get(str(chain_id))
    filtered_list = chains.get(str(chain_id))
    description = '_chain_id_' + str(chain_id) + f'_[{chain_name=}]'
    _write_to_json(description, filtered_list)


def filter_by_sources(sources_list: list, mainnet: Optional[bool] = None):

    with open('all.json', mode='r') as raw:
        chains = json.loads(raw.read())

    filtered_list = []
    for chain_id in chains:
        token_list = chains.get(chain_id)
        if mainnet:
            if chain_id in networks.MAINNET.values():
                for token in token_list:
                    listed_in = token.get('listedIn')
                    for source in sources_list:
                        if source in listed_in:
                            filtered_list.append(token)
                            break
        elif mainnet is False:
            if chain_id in networks.TESTNET.values():
                for token in token_list:
                    listed_in = token.get('listedIn')
                    for source in sources_list:
                        if source in listed_in:
                            filtered_list.append(token)
                            break
        elif mainnet is None:
            for token in token_list:
                listed_in = token.get('listedIn')
                for source in sources_list:
                    if source in listed_in:
                        filtered_list.append(token)
                        break

    description = ''
    if mainnet is None:
        for source in sources_list:
            description += '_' + source
    else:
        for source in sources_list:
            description += '_' + source
        description += f'_[{mainnet=}]'
    _write_to_json(description, filtered_list)


def _write_to_json(description: str, filtered_list: list):
    with open(f'filtered_by{description}.json', 'w') as f:
        f.write(json.dumps(filtered_list, indent=4))
