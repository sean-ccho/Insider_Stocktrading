from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import pandas as pd
import matplotlib.pyplot as plt
from excel import excelRead
from datetime import datetime

ts = TimeSeries(key='5BXBGO0O397FNY19', output_format='pandas')
tech = TechIndicators(key='5BXBGO0O397FNY19')

Today = datetime.today().strftime("%Y-%m-%d")


class technicalIndicator:

    def MACD(symbol):

        # MACD Value Calculation
        data_MACD, meta_data_MACD = tech.get_macd(
            symbol=symbol, interval='daily', series_type='close')

        MACD_dict_value = data_MACD[Today]
        MACD_signal = MACD_dict_value["MACD_Signal"]
        MACD_blue = MACD_dict_value["MACD"]
        MACD_calc = float(MACD_blue) - float(MACD_signal)
        MACD_res = 'MACD Blue is ' + MACD_blue + ' and MACD Signal is ' + MACD_signal
        return MACD_res

    def RSI(symbol):
        # RSI Value Calculation
        data_RSI, meta_data_RSI = tech.get_rsi(
            symbol=symbol, interval='daily', time_period="14", series_type='close')

        RSI_dict_value = data_RSI[Today]
        RSI_value = RSI_dict_value["RSI"]

        # RSI_value = float(RSI_dict_value[0])

        return RSI_value
        # print(data_MACD["2021-09-07"])

    # def EMA():
    #     # RSI Value Calculation
    #     data_EMA, meta_data_EMA = tech.get_ema(
    #         symbol="NBM.V", interval='daily', time_period="100", series_type='close')

    #     EMA_dict_value = data_EMA["2021-09-07"]
    #     EMA_value = EMA_dict_value["EMA"]

    #     # RSI_value = float(RSI_dict_value[0])

    #     return EMA_dict_value
