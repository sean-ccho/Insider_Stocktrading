from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import pandas as pd
import matplotlib.pyplot as plt
from excel import excelRead

ts = TimeSeries(key='5BXBGO0O397FNY19', output_format='pandas')
tech = TechIndicators(key='5BXBGO0O397FNY19')


class technicalIndicator:

    def MACD(symbol):

        # MACD Value Calculation
        data_MACD, meta_data_MACD = tech.get_macd(
            symbol=symbol, interval='daily', series_type='open')

        MACD_dict_value = data_MACD["2021-09-07"]
        MACD_signal = MACD_dict_value["MACD_Signal"]
        MACD_blue = MACD_dict_value["MACD"]
        MACD_calc = float(MACD_blue) - float(MACD_signal)
        return MACD_calc

    def RSI(symbol):
        # RSI Value Calculation
        data_RSI, meta_data_RSI = tech.get_rsi(
            symbol=symbol, interval='daily', time_period="10", series_type='close')

        RSI_dict_value = data_RSI["2021-09-07"]
        RSI_value = RSI_dict_value["RSI"]

        # RSI_value = float(RSI_dict_value[0])

        return RSI_value
        # print(data_MACD["2021-09-07"])
