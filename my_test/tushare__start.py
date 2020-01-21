# -*-coding=utf-8-*-

import tushare as ts 

pingan_code='601318'
shangqi_code='600104'
icbc_code='601398'
real_time=ts.get_realtime_quotes([pingan_code,shangqi_code,icbc_code])

print(real_time)


