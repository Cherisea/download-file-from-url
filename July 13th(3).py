from urllib import request

Baidu_url = 'https://query1.finance.yahoo.com/v7/finance/download/BABA?period1=1497339548&period2=1499931548&interval=1d&events=history&crumb=IFOvkvmnlRX'
def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'Baidu.csv'
    fx = open('Baidu.csv', 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

download_stock_data(Baidu_url)
