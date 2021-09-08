from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
from TradingView import watchList
from AlphaVantage import technicalIndicator
from excel import excelRead
from Insider import insidetrack
from InsiderSold import insidetracksold
from smtpGmail import gmail


if "__main__" == __name__:
    symbol = excelRead.readData()

    ######################################### Insider Tracking #########################################
    t = insidetrack.tracker()
    ts = insidetracksold.trackerSold()
    # print(t)
    # print(ts)

    ######################################### TradingView #########################################
    # watchList.analysis()

    ######################################### AlphaVantage #########################################
    for i in range(len(symbol)):
        MACD = technicalIndicator.MACD(symbol[i])
        # print(MACD)
        RSI = technicalIndicator.RSI(symbol[i])
        if float(RSI) > 40:
            print('It is not ready to purchase ' +
                  str(symbol[i]) + ' because ' + RSI + ' is still too high and above 70 is OVERBOUGHT')

        elif float(RSI) < 40:
            print('It is ready to purchase ' +
                  str(symbol[i]) + ' because ' + RSI + ' is cooled down and below 30 is OVERSOLD')

    # EMA = technicalIndicator.EMA()
    # print(EMA)

    ######################################### Gmail #########################################

    gmail.sendMail('chunghwan14@gmail.com',
                   'chunghwan14@gmail.com', '\n' + t + '\n\n\n\n' + ts)
