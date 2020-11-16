Programa em python para consultas aos rastreamentos do site [Melhor Rastreio](https://www.melhorrastreio.com.br/) e [Melhor Envio](https://melhorenvio.com.br/)

# Como Usar
Clone este repositório para seu computador e import a função `track_melhor_rastreio` do arquivo `python_melhor_rastreio.py`

Use a função com a URL do rastreamento ou somente com o código de rastreamento

```python
from python_melhor_rastreio import track_melhor_rastreio

track_melhor_rastreio('https://www.melhorrastreio.com.br/rastreio/18161300019484')

#or

track_melhor_rastreio('18161300019484')
```

A função acima retornará um dicionário com a descrição e a data do último evento do rastreamento

```python
{'description': 'ENTREGUE', 'date': '06/11/2020'}
```
