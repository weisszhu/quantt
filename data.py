#coding=utf-8
from WindPy import *
import numpy as np
import pandas as pd
import datetime,time
reload(sys)
sys.setdefaulttencoding('utf-8')


def get_one_stock_data(stock,start_day,end_day):
    w.start()
    data = w.wsd()
    one_data = pd.DataFrame()
    one_data['name'] = stock
    one_data['date'] = data.Data[0]
    one_data['open'] = data.Data[1]
    return one_data


def begin_store_day_data(stocklist,start_day,end_day):
    whole_data = pd.DataFrame()
    for stock in stocklist:
        temp = get_one_stock_data(stock,start_day,end_day)
        #合并temp和whole_data-
        pd.merge(whole_data,temp)
    return whole_data

if __name__ == '__main__':
    stocklist = ['asdfadsf']
    start_day = '2011-01-01 00:00:00'
    end_day = '2017-10-24 00:00:00'
    print begin_store_day_data(stocklist,start_day,end_day)
