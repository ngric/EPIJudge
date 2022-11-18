from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    low, high = float('inf'), 0
    trade = 0
    for price in prices:
        if price < low:
            trade = max(trade, high-low)
            low = price
            high = 0
        elif price > high:
            high = price
    trade = max(trade, high-low)            
    return trade
            

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
