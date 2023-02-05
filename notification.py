#from datetime import time
import time

from discordwebhook import Discord

from stock_price import StockPrice

alarm_code = input('銘柄コードを入れてください:')
get = StockPrice.get_stockprice(alarm_code)
print('現在の株価は'+str(get.price)+'円です。')
alarm_price = float(input('通知する株価を入力してください:'))
print(str(alarm_price)+'円でアラートを設定しました。')
#株価アラーム
while True:
    get = StockPrice.get_stockprice(alarm_code)
    #print(get.price)
    if float(get.price) == alarm_price:
        #urlはdiscordのwebhookURLを使う,discoじゃなくてもいいけど。。。
        discord = Discord(url="----")
        #通知メッセージの内容
        discord.post(content="通知")
        #print('discordに通知しました')
        break
    else:
        time.sleep(1)
    

