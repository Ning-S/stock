# -*-coding=utf-8-*-

import tushare as ts 

pingan_code='601318'
shangqi_code='600104'
icbc_code='601398'
huada_genic='300676'
real_time=ts.get_realtime_quotes([pingan_code,shangqi_code,icbc_code,huada_genic])
need_data=real_time[['name','open','price','high','low','bid','volume','date','time']]
print(need_data)


