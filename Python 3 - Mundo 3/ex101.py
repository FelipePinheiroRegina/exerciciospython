def voto(Ano_Nasc):
    from datetime import date  # Importando Biblioteca dentro de função, para ter um escopo local
    Ano_Atual = int(date.today().year)
    idade = int(Ano_Atual - Ano_Nasc)
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return "NÃO VOTA"
    elif 16 <= idade < 18 or idade >= 65:
        return "VOTO É OPCIONAL"
    else:
        return "VOTO É OBRIGATÓRIO"




# Programa Principal
print('\033[1;32m*' * 30)
print(f'{"ELEIÇÕES 2023":^30}')
print('*' * 30, '\033[m')
Ano_Nascimento = int(input('Entre com seu ano de nascimento: '))
Situação = str(voto(Ano_Nascimento))
print(Situação)
