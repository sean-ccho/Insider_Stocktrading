from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
from TradingView import watchList
from AlphaVantage import technicalIndicator
from excel import excelRead
from Insider import insidetrack
from InsiderSold import insidetracksold
from InsiderTrack import personalInsiderTracker
from smtpGmail import gmail


if "__main__" == __name__:

    symbol = excelRead.readData()

    # Insider Tracking
    t = insidetrack.tracker()  # Tracks INSIDER BOUGHT alerts from CEO.CA
    ts = insidetracksold.trackerSold()  # Tracks INSIDER SOLD alerts from CEO.CA
    tss = personalInsiderTracker.tracker()  # Tracks MY Insider transaction
    # print(ts)

    # TradingView
    # watchList.analysis()

    # AlphaVantage
    try:
        for i in range(len(symbol)):
            MACD = technicalIndicator.MACD(symbol[i])
            # print(MACD)
            RSI = technicalIndicator.RSI(symbol[i])
            if float(RSI) > 70:
                gmail.sendMail('chunghwan14@gmail.com', 'NBM Sell Alert',
                               str(symbol[i]) + ' RSI = ' + RSI + ' \n MACD = ' + MACD)

                # print('It is not ready to purchase ' +
                #       str(symbol[i]) + ' because ' + RSI + ' is still too high and above 70 is OVERBOUGHT')

            elif float(RSI) < 35:
                gmail.sendMail('chunghwan14@gmail.com', 'NBM Buy Alert',
                               str(symbol[i]) + ' = ' + RSI + ' is cooled down and below 30 is OVERSOLD')
    except:
        print("No transaction for today")

        # print('It is ready to purchase ' +
        #       str(symbol[i]) + ' because ' + RSI + ' is cooled down and below 30 is OVERSOLD')

        # EMA = technicalIndicator.EMA()
        # print(EMA)

        # ######################################### Gmail #########################################

    gmail.sendMail('chunghwan14@gmail.com', 'InsiderTracking',
                   '\n' + t + '\n\n\n\n' + ts)

    gmail.sendMail('chunghwan14@gmail.com', 'Daily Insider transaction status',
                   '\n' + tss)
