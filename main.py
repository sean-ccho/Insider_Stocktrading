from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
from TradingView import watchList
from AlphaVantage import technicalIndicator
from excel import excelRead


if "__main__" == __name__:

    symbol = excelRead.readData()[0]

    MACD = technicalIndicator.MACD(symbol)
    print(MACD)

    RSI = technicalIndicator.RSI(symbol)
    print(RSI)
