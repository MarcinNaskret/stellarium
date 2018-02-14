from django.shortcuts import render
import coinmarketcap
from currency_converter import CurrencyConverter

def index(request):
    c = CurrencyConverter()

    market = coinmarketcap.Market()
    coin = market.ticker('stellar')
    cena = coin[0]['price_usd']




    market_cap = float(coin[0]['market_cap_usd'])
    x24h_volume = float(coin[0]['24h_volume_usd'])
    x1h_change = coin[0]['percent_change_1h']
    x24h_change = coin[0]['percent_change_24h']
    x7d_change = coin[0]['percent_change_7d']
    price_btc = coin[0]['price_btc']
    rank = coin[0]['rank']

    market_cap = format(round(int(market_cap)), ',d')
    x24h_volume = format(round(int(x24h_volume)), ',d')



    cena_eur = c.convert(cena, 'USD', 'EUR')
    cena_eur = float("{0:.5f}".format(cena_eur))


    cena_yen = c.convert(cena, 'USD', 'CNY')
    cena_yen = float("{0:.5f}".format(cena_yen))




    up_green = "#2ECC40"
    down_red = "#FF4136"
    if float(x1h_change) < 0:
        change_1h = down_red
    elif float(x1h_change) > 0:
        change_1h = up_green

    if float(x24h_change) < 0:
        change_24h = down_red
    elif float(x24h_change) > 0:
        change_24h = up_green

    if float(x7d_change) < 0:
        change_7d = down_red
    elif float(x7d_change) > 0:
        change_7d = up_green


    return render(request, 'watcher/home.html',{"change_1h": change_1h,"change_24h": change_24h,"change_7d": change_7d,'cena': cena,'cena_eur': cena_eur,'cena_yen': cena_yen,'market_cap': market_cap,'24h_volume': x24h_volume,'1h_change': x1h_change,'24h_change': x24h_change,'7d_change': x7d_change,'price_btc': price_btc,'rank': rank,"x1h_change" : x1h_change, "x24h_change" : x24h_change, "x7d_change" : x7d_change
 })
# Create your views here.
def lumen(request):

    return render(request, 'watcher/home.html')
# Create your views here.
