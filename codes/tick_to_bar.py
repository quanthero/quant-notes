import os
import pandas as pd
import datetime


path = 'C:/baidunetdiskdownload/2021年更新/2021.12/000001'

for file in os.listdir(path)[20:21]:
    file_path = os.path.join(path, file)
    df = pd.read_csv(file_path)
    code = os.path.basename(path)
    df['code'] = code
    df['time']=pd.to_datetime(df['datetime'])
    print(df)
    df=df.set_index('time')
    price_df=df['price'].resample('1min').ohlc()
    price_df=price_df.dropna()
    vols=df['vol'].resample('1min').sum()
    # vols=vols.dropna()
    vol_df=pd.DataFrame(vols,columns=['vol'])
    vol_df=vol_df.dropna()
    print(price_df)
    print(vol_df)
