'''
Created on Dec 25, 2011

@author: ppa
'''
from ultrafinance.model import Side, Order
from ultrafinance.backTest.tickSubscriber.strategies.baseStrategy import BaseStrategy
from ultrafinance.backTest.constant import CONF_PERIOD

import logging
LOG = logging.getLogger()

class PeriodStrategy(BaseStrategy):
    ''' period strategy '''
    def __init__(self, configDict):
        ''' constructor '''
        super(PeriodStrategy, self).__init__("periodStrategy")
        self.configDict = configDict

        assert int(configDict[CONF_PERIOD]) >= 1

        self.perAmount = 1000 # buy $100p per period
        self.period = int(configDict[CONF_PERIOD])
        self.symbols = None
        self.counter = 0

    def increaseAndCheckCounter(self):
        ''' increase counter by one and check whether a period is end '''
        self.counter += 1
        self.counter %= self.period
        if not self.counter:
            return True
        else:
            return False

    def tickUpdate(self, tickDict):
        ''' consume ticks '''
        assert self.symbols
        assert self.symbols[0] in tickDict.keys()
        symbol = self.symbols[0]
        tick = tickDict[symbol]

        if self.increaseAndCheckCounter():
            self.placeOrder(Order(accountId = self.accountId,
                                  side = Side.BUY,
                                  symbol = symbol,
                                  price = tick.close,
                                  share = self.perAmount / float(tick.close)))


