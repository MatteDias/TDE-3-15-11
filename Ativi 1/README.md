# TDE-3-15-11

# Como funciona o problema

Cinco filósofos sentam em uma mesa redonda. Entre cada par de filósofos existe um garfo (5 garfos no total). O garfo `i` fica entre o filósofo `i` e o filósofo `(i+1) % 5`.

Cada filósofo repete: pensando → com fome → comendo.
Para comer, ele precisa dos dois garfos (esquerda e direita), que são compartilhados com os vizinhos. Dois vizinhos nunca podem comer ao mesmo tempo, porque usam o mesmo garfo.

No código, cada garfo é um `Lock` (só uma thread pode segurar por vez) e cada filósofo é uma thread.

# 1 Por que o impasse (deadlock) acontece

Na versão ingênua:

Todos ficam com fome quase ao mesmo tempo.
Cada um pega o garfo da **esquerda** (todos conseguem, pois cada garfo é de um só).
Cada um tenta pegar o garfo da **direita**, mas esse garfo já está na mão do vizinho.
Ninguém larga o que tem e ninguém consegue o que falta. Todos esperam para sempre.

Esse é o resultado da execução da versão ingênua:

Filosofo 0 -> pegou o garfo da esquerda (0)
Filosofo 1 -> pegou o garfo da esquerda (1)
Filosofo 2 -> pegou o garfo da esquerda (2)
Filosofo 3 -> pegou o garfo da esquerda (3)
Filosofo 4 -> pegou o garfo da esquerda (4)
Filosofo 0 -> esperando o garfo da direita (1)
Filosofo 1 -> esperando o garfo da direita (2)
DEADLOCK


No código foi colocado um time.sleep(1) entre pegar o primeiro e o segundo garfo. Sem essa pausa o deadlock é possível, mas acontece só às vezes (depende da sorte do escalonador). Com a pausa, ele aparece sempre, o que facilita a demonstração.

# Condições de Coffman

Para existir deadlock, as 4 condições abaixo precisam ser verdadeiras ao mesmo tempo:

| Condição | Na versão ingênua |
| Exclusão mútua | Um garfo só pode ser usado por um filósofo. |
| Manter-e-esperar | O filósofo segura um garfo enquanto espera o outro. |
| Não preempção | Ninguém pode tomar o garfo à força de outro filósofo. |
| Espera circular | 0 espera 1, 1 espera 2, 2 espera 3, 3 espera 4, 4 espera 0 (ciclo). |

# 2 A solução: hierarquia de recursos

Numeramos os garfos de 0 a 4 e todo filósofo pega primeiro o garfo de menor número e depois o de maior número.

Só o filósofo 4 muda de comportamento: seus garfos são o 4 (esquerda) e o 0 (direita), então ele pega primeiro o 0 e depois o 4. Todos os outros continuam pegando primeiro a esquerda.

# 3 Pseudocódigo


Dados:
  N = 5
  garfos 0..N-1  (garfo i fica entre filosofos i e (i+1) mod N)

Para cada filosofo p:
  a = p
  b = (p + 1) mod N

  SE a < b ENTAO
      menor = a
      maior = b
  SENAO
      menor = b
      maior = a

  REPETIR:
      pensar()
      estado[p] <- "com fome"
      adquirir(menor)     // espera ate o garfo estar livre
      adquirir(maior)     // espera ate o garfo estar livre
      estado[p] <- "comendo"
      comer()
      liberar(maior)
      liberar(menor)
      estado[p] <- "pensando"




# 4 Progresso e justiça (sem inanição)

Progresso: como o ciclo de espera não existe, sempre há pelo menos um filósofo que consegue os dois garfos. O sistema nunca trava.

Justiça: os Lock do Python liberam o garfo para quem está esperando, e ninguém fica com o garfo para sempre, porque cada filósofo come por um tempo curto e devolve os dois garfos antes de voltar a pensar. Enquanto pensa, ele não segura nenhum recurso, então os vizinhos podem pegar os garfos. Assim, nenhum filósofo consegue comer sempre antes dos outros.

Observação honesta: o protocolo evita deadlock com certeza, mas o Lock do Python não garante uma ordem de fila (FIFO), então a justiça perfeita não é provada formalmente. Na prática, a simulação mostra que todos os filósofos terminam suas refeições. No final da execução o código confere se cada um comeu o mesmo número de vezes:

Filosofo 0 : 3 vezes
Filosofo 1 : 3 vezes
Filosofo 2 : 3 vezes
Filosofo 3 : 3 vezes
Filosofo 4 : 3 vezes
Justica OK: todos comeram o mesmo numero de vezes (sem inanicao).

# 5 Outras soluções possíveis

Garçom (árbitro): um controlador só deixa um filósofo pegar garfos se houver garfos livres para ele.
Limite de N−1 filósofos: só 4 filósofos podem tentar comer ao mesmo tempo (um semáforo com valor 4), então sempre sobra um garfo livre.