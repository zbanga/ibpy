#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# Translation source for TickType.
##

# Source file: TickType.java
# Target file: TickType.py
#
# Original file copyright original author(s).
# This file copyright Troy Melhase, troy@gci.net.


class TickType(object):
    """ generated source for TickType

    """
    BID_SIZE = 0
    BID = 1
    ASK = 2
    ASK_SIZE = 3
    LAST = 4
    LAST_SIZE = 5
    HIGH = 6
    LOW = 7
    VOLUME = 8
    CLOSE = 9
    BID_OPTION = 10
    ASK_OPTION = 11
    LAST_OPTION = 12
    MODEL_OPTION = 13
    OPEN = 14
    LOW_13_WEEK = 15
    HIGH_13_WEEK = 16
    LOW_26_WEEK = 17
    HIGH_26_WEEK = 18
    LOW_52_WEEK = 19
    HIGH_52_WEEK = 20
    AVG_VOLUME = 21
    OPEN_INTEREST = 22
    OPTION_HISTORICAL_VOL = 23
    OPTION_IMPLIED_VOL = 24
    OPTION_BID_EXCH = 25
    OPTION_ASK_EXCH = 26
    OPTION_CALL_OPEN_INTEREST = 27
    OPTION_PUT_OPEN_INTEREST = 28
    OPTION_CALL_VOLUME = 29
    OPTION_PUT_VOLUME = 30
    INDEX_FUTURE_PREMIUM = 31
    BID_EXCH = 32
    ASK_EXCH = 33
    AUCTION_VOLUME = 34
    AUCTION_PRICE = 35
    AUCTION_IMBALANCE = 36
    MARK_PRICE = 37

    @classmethod
    def getField(cls, tickType):
        if tickType == cls.BID_SIZE:
            return "bidSize"
        elif tickType == cls.BID:
            return "bidPrice"
        elif tickType == cls.ASK:
            return "askPrice"
        elif tickType == cls.ASK_SIZE:
            return "askSize"
        elif tickType == cls.LAST:
            return "lastPrice"
        elif tickType == cls.LAST_SIZE:
            return "lastSize"
        elif tickType == cls.HIGH:
            return "high"
        elif tickType == cls.LOW:
            return "low"
        elif tickType == cls.VOLUME:
            return "volume"
        elif tickType == cls.CLOSE:
            return "close"
        elif tickType == cls.BID_OPTION:
            return "bidOptComp"
        elif tickType == cls.ASK_OPTION:
            return "askOptComp"
        elif tickType == cls.LAST_OPTION:
            return "lastOptComp"
        elif tickType == cls.MODEL_OPTION:
            return "modelOptComp"
        elif tickType == cls.OPEN:
            return "open"
        elif tickType == cls.LOW_13_WEEK:
            return "13WeekLow"
        elif tickType == cls.HIGH_13_WEEK:
            return "13WeekHigh"
        elif tickType == cls.LOW_26_WEEK:
            return "26WeekLow"
        elif tickType == cls.HIGH_26_WEEK:
            return "26WeekHigh"
        elif tickType == cls.LOW_52_WEEK:
            return "52WeekLow"
        elif tickType == cls.HIGH_52_WEEK:
            return "52WeekHigh"
        elif tickType == cls.AVG_VOLUME:
            return "AvgVolume"
        elif tickType == cls.OPEN_INTEREST:
            return "OpenInterest"
        elif tickType == cls.OPTION_HISTORICAL_VOL:
            return "OptionHistoricalVolatility"
        elif tickType == cls.OPTION_IMPLIED_VOL:
            return "OptionImpliedVolatility"
        elif tickType == cls.OPTION_BID_EXCH:
            return "OptionBidExchStr"
        elif tickType == cls.OPTION_ASK_EXCH:
            return "OptionAskExchStr"
        elif tickType == cls.OPTION_CALL_OPEN_INTEREST:
            return "OptionCallOpenInterest"
        elif tickType == cls.OPTION_PUT_OPEN_INTEREST:
            return "OptionPutOpenInterest"
        elif tickType == cls.OPTION_CALL_VOLUME:
            return "OptionCallVolume"
        elif tickType == cls.OPTION_PUT_VOLUME:
            return "OptionPutVolume"
        elif tickType == cls.INDEX_FUTURE_PREMIUM:
            return "IndexFuturePremium"
        elif tickType == cls.BID_EXCH:
            return "bidExch"
        elif tickType == cls.ASK_EXCH:
            return "askExch"
        elif tickType == cls.AUCTION_VOLUME:
            return "auctionVolume"
        elif tickType == cls.AUCTION_PRICE:
            return "auctionPrice"
        elif tickType == cls.AUCTION_IMBALANCE:
            return "auctionImbalance"
        elif tickType == cls.MARK_PRICE:
            return "markPrice"
        else:
            return "unknown"


