from get_tokenlist import get_tokenlist
import filters


if __name__ == '__main__':
    get_tokenlist()

    # examples below
    filters.filter_by_symbol(symbol='usdt')
    filters.filter_by_symbol(symbol='usdt', mainnet=True)
    filters.filter_by_symbol(symbol='usdt', mainnet=False)

    filters.filter_by_chain_id(chain_id=56)

    filters.filter_by_sources(sources_list=['uniswap', '1inch'])
    filters.filter_by_sources(sources_list=['uniswap', '1inch'], mainnet=True)
    filters.filter_by_sources(sources_list=['uniswap', '1inch'], mainnet=False)

    # extra: for stablecoins containing 'usd' in this case
    filters.search_symbol_matches(symbol='usd')
    filters.search_symbol_matches(symbol='usd', mainnet=True)
    filters.search_symbol_matches(symbol='usd', mainnet=False)
