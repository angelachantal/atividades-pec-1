# Define a função "separar_data", que recebe por parâmetro a variável "dmc".
def separar_data (dma):
    # a variável "a" recebe o resto da divisão inteira da variável "dma" por 10000; em seguida, a variávem "dma" recebe a divisão inteira da própria variável por 10000
    a = dma % 10000
    dma //= 10000
    
    # a variável "m" recebe o resto da divisão inteira da variável "dma" por 100; em seguida, a variávem "dma" recebe a divisão inteira da própria variável por 100
    m = dma % 100
    dma //= 100
    
    # a variável "d" recebe a variável "dma".
    d = dma
    
    # ao ser chamada, a função "separar_data" retorna as variáveis "d, m, a".
    return d, m, a

# Define a função "signo", que recebe por parâmetro as variáveis "dia" e "mês".
def signo (dia, mes):

# A função "signo", ao ser chamada, retorna o signo, de acordo com as variáveis "mês" e "dia". Exemplo: Se mês for igual a três, e dia for menor que 21, deve retornar "Peixes", caso contrário, retorna "Áries".
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'

# Define a função "remover_acentos", que recebe por parâmetro a variável "texto".
def remover_acentos(texto):
    # Importa a função "normalize" do módulo "unicodedata"
    from unicodedata import normalize
    # Ao ser chamada, a função retorna "texto" sem caracteres acentuados.
    return normalize ('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

# Define a função "horoscopo", que recebe por parâmetro a variável "signo_desejado". Ao ser chamada, a função retorna o signo e o respectivo horóscopo. 
def horoscopo(signo_desejado):
    # Iporta o módulo "urllib.request"
    import urllib.request
    
    # A variável "signo_formatado" chama a função "remover_acentos", que tem como parâmetro a variável "signo_desejado". O retorno é convertido para minúscula
    signo_formatado = remover_acentos(signo_desejado).lower()
    
    # A variável "minha_url" recebe a string "https://www.horoscopovirtual.com.br/horoscopo/" e concatena com a variável "signo_formatado".
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado
    
    requisicao = urllib.request.Request(
        url=minha_url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    resposta = urllib.request.urlopen(requisicao)
    
    pagina = resposta.read().decode('utf-8')
    
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'
    
    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)
    
    return signo_desejado + ':' + pagina[inicio:final]

def main():
    # A variável "nascimento" recebe um valor inserido pelo teclado, convertido para inteiro.
    nascimento = int(input('Digite sua data de nascimento no formato DDMMAAAA: '))
    
    # As variáveis "dia", "mês", "_" recebem o retorno da função "separar_data", que tem como parâmetro a variável "nascimento"
    dia, mes, _ = separar_data(nascimento)
    # a variável "meu_signo" recebe o retorno da função "signo", para as variáveis "dia" e "mês"
    meu_signo = signo(dia,mes)
    # a variável "horóscopo_de_hoje" recebe o retorno da função "horoscopo", para a variável "meu_signo"
    horoscopo_de_hoje = horoscopo(meu_signo)
    
    # Mostra na tela a variável "horóscopo_de_hoje"
    print(horoscopo_de_hoje)
    
if __name__=='__main__':
    main()