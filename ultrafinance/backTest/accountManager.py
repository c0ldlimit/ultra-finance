'''
Created on Jan 29, 2011

@author: ppa
'''
from ultrafinance.lib.errors import Errors, UfException
from ultrafinance.backTest.account import Account

import logging
LOG = logging.getLogger()

class AccountManager(object):
    '''
    account manager
    Note: set metricNames before creating accounts
    '''
    def __init__(self):
        ''' constructor '''
        self.__accounts = {}
        self.__accountPositions = {}
        self.saver = None

    def createAccount(self, cash, commission = 0):
        ''' create account '''
        account = Account(cash, commission)
        self.__accounts[account.accountId] = account
        self.__accountPositions[account.accountId] = [] # list contains tuple (time, position)

        return account.accountId

    def getAccount(self, accountId):
        ''' get account '''
        return self.__accounts.get(accountId)

    def getAccounts(self):
        ''' get accounts '''
        return self.__accounts.values()

    def updateAccountsPosition(self, tickDict):
        ''' update account position based on new tick '''
        curTime = tickDict.values()[0].time

        for accountId, account in self.__accounts.items():
            account.setLastTickDict(tickDict)
            position = account.getTotalValue()

            self.__accountPositions[accountId].append((curTime, position))
            #record
            if self.saver:
                self.saver.write(curTime, "account-%s" % accountId, position)

    def getAccountPostions(self, accountId):
        ''' get account positions '''
        return self.__accountPositions.get(accountId)
