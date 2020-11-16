import requests
import datetime
import time

def track_melhor_rastreio(url_or_code):
    
    if 'http' in str(url_or_code):
        rastreio = url_or_code.split('/rastreio/')[1]
    else:
        rastreio = url_or_code
    
    url = f"https://api.melhorrastreio.com.br/api/v1/trackings/{rastreio}" 

    tentativa = 0

    while True:
        if tentativa == 5:
            return {'description':'Não encontrado no Melhor Rastreio', 'date':''}
        try:
            r = requests.get(url)
            desc = r.json()['data']['event'][-1]['events']
            data = r.json()['data']['event'][-1]['date']
            data = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%fz').strftime('%d/%m/%Y')
        except:
            tentativa +=1
            time.sleep(1)
        else:
            return {'description':desc, 'date':data}

