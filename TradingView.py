from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
from excel import excelRead


class watchList:

    def analysis():
        watchList = ["TSLA", "america", "NASDAQ"]

        exe = excelRead.readData()
        print(exe)

        tesla = TA_Handler(
            symbol=watchList[0],
            screener=watchList[1],
            exchange=watchList[2],
            # interval=Interval.INTERVAL_1_DAY
            interval=Interval.INTERVAL_1_WEEK
        )
        # print(tesla.get_analysis().summary)
        # # Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}

        print(tesla.get_analysis().indicators["MACD.macd"])
        # print(tesla.get_analysis().indicators["MACD.signal"])
        # print(tesla.get_analysis().indicators["Mom"])
        # print(tesla.get_analysis().indicators["RSI"])
