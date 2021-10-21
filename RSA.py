from math import e
import random

# Recebe um n inteiro qualquer, que terá sua primalidade verificada
# Retorna um booleano True se n for primo e False se n não for primo
def miller_rabin(n: int) -> bool:
    if((n <= 2 ) or (n == 5)):
        return False 
    if(n == 3):
        return True # Esses dois if's são para verificar os casos base
    fator_impar = (n-1)/2
    potencias_de_dois = 1  # n-1 = fator_impar * 2^{potencias_de_dois}
    while(fator_impar%2 == 0):
        fator_impar = fator_impar/2
        potencias_de_dois += 1
    fator_impar = int(fator_impar)
    b = random.randrange(2, n-2) # Base aleatória no intervalo 1 < b < n-1
    verificacao = pow(b,2, n)
    if( verificacao == 1 or verificacao == n-1):
        return True
    for i in range(potencias_de_dois - 2):
        verificacao = pow(verificacao,2,n)
        if(verificacao == 1):
            return False
        if(verificacao == n-1):
            return True
    return False # Por default será falso para evitarmos a passagem de números não primos

# Recebe um n inteiro qualquer, que definirá o range de geração do número primo entre 10^n e 10^{n+2}
# Retorna um inteiro provavelmente primo 
def gera_primos(n: int) -> int:
    buscando_primo = True
    while buscando_primo == True:
        rand_num = random.randrange(10**n + 1,10**(n+2))
        if(all(miller_rabin(rand_num) == True for i in range(10))):
            buscando_primo = False
    return rand_num

# Recebe dois inteiros a e b quaisquer
# Retorna o a em módulo b em sua forma reduzida
def modulo_reduzido(a:int,b:int) -> int:
    resto = a%b
    if(b - resto < resto):
        resto = resto - b
    return resto

# Recebe dois números primos quaisquer
# Retorna a função totiente entre eles
def funcao_totiente(a:int,b:int) -> int:
    return ((a - 1) * (b-1)) 

# Recebe dois inteiros quaisquer a e b
# Retorna o mdc, alpha, beta
def euclidiano_extendido(a:int,b:int):
  resto = a%b
  quociente= a//b
  if resto == 0:
    return b,0,1
  else:
    d,x,y = euclidiano_extendido(b,resto)
    return  d,y,x-quociente*y 

# Recebe os inteiros a e n
# Retorna o inverso multiplicativo de a na base n 
def inverso_multiplicativo(a:int,n:int): #qual é o inverso multiplicativo de a em módulo n?
  d,alpha,beta=euclidiano_extendido(a,n)
  if d==1: #a e n são primos entre si (mdc(a,n)=1)
    return alpha  #alpha*a é congruente à 1 módulo n

# Recebe uma função totiente
# Retorna um número inversível em módulo *totiente*
def gera_inversivel(totiente:int) -> int:
    e = random.randrange(1, totiente)
    mdc,alpha,beta = euclidiano_extendido(e,totiente)
    while(mdc != 1):
        e = random.randrange(1, totiente)
        mdc,alpha,beta = euclidiano_extendido(e,totiente)
    return e

# Recebe um inteiro qualquer >= 0, que definirá o tamanho dos primos p e q e, consequentemente, o grau de segurança da encriptação
# Retorna as chaves do RSA
def gera_chaves(protecao:int):
    p = gera_primos(protecao)
    q = gera_primos(protecao)
    n = p * q
    totiente = funcao_totiente(p,q)
    e = gera_inversivel(totiente)
    d = inverso_multiplicativo(e, totiente)
    inverso_p_em_q = inverso_multiplicativo(p,q)
    inverso_q_em_p = inverso_multiplicativo(q,p)
    return n, e, d, p, q, inverso_p_em_q, inverso_q_em_p, modulo_reduzido(d,p-1), modulo_reduzido(d,q-1)

# Recebe o texto que será criptografado e as chaves públicas
# Retorna o texto encriptado
def encriptar(texto:str, n:int, e:int) -> list:
    simbolos_para_codigos = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
    '5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
    '-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
    'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
    'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
    's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
    'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
    'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
    'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
    'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
    'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
    'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
    'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
    'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
    ':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
    '%': 235, '@': 236, ' ': 237, '\n': 238}
    texto_encriptado = []
    for letra in texto:
        codigo = simbolos_para_codigos[letra]
        codigo = pow(codigo, e, n)
        texto_encriptado.append(codigo)
    return texto_encriptado

# Recebe uma lista de letra encriptadas, a chave pública n e a chave privada d
# Retorna o texto descriptado 
def descriptar(blocos:list, n:int, d:int) -> str:
    codigos_para_simbolos = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
    116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
    124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
    132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
    139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
    147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
    155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
    163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
    171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
    178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
    186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
    194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
    212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
    219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
    227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
    235: '%', 236: '@', 237: ' ', 238: '\n'}
    texto = ""
    for codigo in blocos:
        letra = pow(codigo,d,n)
        texto += codigos_para_simbolos[letra]
    return texto
 
# Função para testar a efetividade do código
def test():
    n, e, d, p, q, inverso_p_em_q, inverso_q_em_p, modulo_reduzido_d_em_pmenos,  modulo_reduzido_d_em_qmenos = gera_chaves(0)
    texto = input("Frase qualquer: ")
    print(descriptar((encriptar(texto,n,e)),n,d))

print(gera_primos(16))
