#from datetime import time
import time

from discordwebhook import Discord

from stock_price import StockPrice

b = input('銘柄コードを入れてください:')
get = StockPrice.get_stockprice(b)
print('現在の株価は'+str(get.price)+'円です。')
a = float(input('通知する株価を入力してください:'))
print(str(a)+'円でアラートを設定しました。')
#株価アラーム
while True:
    get = StockPrice.get_stockprice(b)
    #print(get.price)
    if float(get.price) == a:
        #urlはdiscordのwebhookURLを使う,discoじゃなくてもいいけど。。。
        discord = Discord(url="----")
        #通知メッセージの内容
        discord.post(content="通知")
        #print('discordに通知しました')
        break
    else:
        time.sleep(1)
    

