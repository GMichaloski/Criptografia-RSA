# Criptografia-RSA
Implementação da criptografia RSA para o trabalho final da matéria Números Inteiros e Criptografia, lecionada em 2021.2 na UFRJ

Enunciado do trabalho: 

Questão 8. Implemente o RSA em Python (ou qualquer outra linguagem)!
Sua implementação deve ter (pelo menos) os seguintes componentes.
a. Uma função para gerar números primos. Sua função deve receber como
entrada um natural n e gerar um número (provavelmente) primo p satisfazendo
10n < p < 10n+2, sorteando p aleatoriamente no intervalo desejado e rodando
10 testes de Miller–Rabin com bases b aleatórias no intervalo 1 < b < p − 1.
(Naturalmente, p só deve ser aceito como provavelmente primo se todos os testes
forem inconclusivos.) <br />
b. Uma função chamada gera_chaves (por favor use este nome) para gerar
chaves do RSA. Sua função deve usar sua função da letra a para gerar primos
p e q, cada um com aproximadamente 50 algarismos, e retornar:
• n = pq
• algum número e inversível módulo φ(n) = (p − 1)(q − 1)
• o inverso d de e módulo φ(n)
Para uma solução realmente completa, sua função deve retornar também:
• p
• q
• o inverso de p módulo q
• o inverso de q módulo p
• a forma reduzida de d módulo p − 1
• a forma reduzida de d módulo q − 1.
c. Uma função chamada encriptar (por favor use este nome) que recebe como
entrada uma string texto e números n e e, e retorna uma lista de números que
seja uma sequência válida dos blocos numéricos resultantes da encriptação do
texto com chave pública de módulo n e expoente e.
d. Uma função chamada descriptar (por favor use este nome) que recebe
como entrada uma lista blocos e números n e d, e retorna a string resultante
da descriptação da sequência de blocos usando a chave privada de módulo n e
expoente d.
