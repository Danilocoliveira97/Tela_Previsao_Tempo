from translate import Translator
import requests


def traducao(txt):
    s = Translator(from_lang="english", to_lang="pt-br")
    res = s.translate(txt)
    return res


def previsao(city):
    try:
        api_key = "4be93bb1c7c34f66e1023738598e6add"
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        requiparalink = requests.get(link)
        requisicao = requiparalink.json()
        tempo = requisicao['weather'][0]['description']
        descicaotempo = requisicao['main']['temp'] - 273.15
        return f' {descicaotempo:.0f}° graus , o tempo está : {traducao(tempo)}'
    except:
        cid = " Cidade invalida"
        return cid
