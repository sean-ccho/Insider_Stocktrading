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

    # gmail.sendMail('chunghwan14@gmail.com', 'InsiderTracking',
    #                '\n' + t + '\n\n\n\n' + ts)

    gmail.sendMail('chunghwan14@gmail.com', 'Daily Insider transaction status',
                   '\n' + tss)
