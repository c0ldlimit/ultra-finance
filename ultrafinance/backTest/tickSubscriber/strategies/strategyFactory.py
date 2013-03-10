'''
Created on Dec 26, 2011

@author: ppa
'''

from ultrafinance.backTest.tickSubscriber.strategies.periodStrategy import PeriodStrategy

from ultrafinance.lib.errors import Errors, UfException

class StrategyFactory(object):
    ''' Strategy factory '''
    STRATEGY_DICT = {'period': PeriodStrategy}

    @staticmethod
    def createStrategy(name, configDict):
        ''' create a metric '''
        if name not in StrategyFactory.STRATEGY_DICT:
            raise UfException(Errors.INVALID_STRATEGY_NAME,
                              "Strategy name is invalid %s" % name)
        return StrategyFactory.STRATEGY_DICT[name](configDict)

    @staticmethod
    def getAvailableTypes():
        ''' return all available types '''
        return StrategyFactory.STRATEGY_DICT.keys()
