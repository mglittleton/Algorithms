#!/usr/bin/python

import argparse


def find_max_profit(prices):
    maxSale = prices[1] - prices[0]
    currLowest = prices[0]

    for buy in range(len(prices) - 1 ):
        if prices[buy] > currLowest:
            currLowest = prices[buy]
        for sell in range(buy + 1, len(prices)):
            thisSale = prices[sell] - prices[buy]
            if thisSale > maxSale:
                maxSale = thisSale

    return maxSale

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

