import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site pudim não está acessível no momento.')
else:
    print('\033[33mConsegui acessar o site Pudim com sucesso!')
