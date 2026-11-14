# Como funciona o problema

O problema consiste em cinco filósofos sentados em uma mesa redonda, onde existe um garfo entre cada um deles, totalizando cinco garfos.
Cada filósofo precisa de dois garfos para conseguir comer: o da esquerda e o da direita. Como os garfos são compartilhados, dois filósofos vizinhos não conseguem comer ao mesmo tempo. No código, cada garfo é representado por um Lock, enquanto cada filósofo funciona como uma thread. Eles ficam alternando entre pensar, sentir fome e comer.

# 1. Versão falha

Na primeira versão, todos os filósofos tentam pegar primeiro o garfo da esquerda. O problema acontece quando todos conseguem pegar esse primeiro garfo e tentam pegar o da direita.Como o garfo da direita já está sendo segurado pelo vizinho, todos ficam esperando alguém liberar o recurso. Só que ninguém consegue continuar para chegar na parte que libera os garfos.

O resultado da execução foi:

```text
Filosofo 0 -> pegou o garfo da esquerda (0)
Filosofo 1 -> pegou o garfo da esquerda (1)
Filosofo 2 -> pegou o garfo da esquerda (2)
Filosofo 3 -> pegou o garfo da esquerda (3)
Filosofo 4 -> pegou o garfo da esquerda (4)

Filosofo 0 -> esperando o garfo da direita (1)
Filosofo 1 -> esperando o garfo da direita (2)

DEADLOCK
```

Foi colocado um time.sleep(1) entre a aquisição dos dois garfos para facilitar a demonstração. Sem essa pausa, o deadlock ainda poderia acontecer, mas dependeria da ordem em que as threads fossem executadas.

# 2. Condições de Coffman

Para acontecer um deadlock, as quatro condições precisam existir ao mesmo tempo:

- **Exclusão mútua:** cada garfo só pode ser utilizado por um filósofo.
- **Manter e esperar:** o filósofo segura um garfo enquanto espera pelo outro.
- **Não preempção:** não é possível retirar um garfo de alguém à força.
- **Espera circular:** cada filósofo espera pelo garfo que está com o próximo, formando um ciclo.

Quando as quatro condições estão presentes, por isso acontece o travamento.

# 3. Versão corrigida – Hierarquia de recursos

Na versão corrigida, foi definida uma ordem para pegar os garfos. Todos os filósofos precisam pegar primeiro o garfo de menor número e depois o de maior número.

A única diferença acontece com o filósofo 4, que precisa pegar primeiro o garfo 0 e depois o garfo 4, respeitando a mesma regra dos outros.

Dessa forma, não acontece aquela situação em que todos seguram um garfo e ficam esperando pelo próximo.

O resultado da execução foi:

```text
Filosofo 0 conseguiu pegar os dois garfos
Filosofo 0 começou a comer
Filosofo 0 liberou os garfos

Filosofo 1 conseguiu pegar os dois garfos
Filosofo 1 começou a comer
Filosofo 1 liberou os garfos

...

Todos os filosofos terminaram suas refeicoes.
```

# 4. Por que a solução funciona?

A solução funciona porque foi criada uma ordem para adquirir os recursos. Assim, nenhum filósofo consegue formar um ciclo de espera com os outros.
Na versão corrigida, todos precisam respeitar a ordem dos garfos, sempre pegando primeiro o de menor número e depois o de maior número.
Com isso, a condição de **espera circular** é quebrada, evitando o deadlock.

# 5. Progresso e justiça

Na versão corrigida, os filósofos conseguem continuar comendo e liberando os garfos, sem deixar o sistema travado.
Também foi feita uma verificação no final para conferir quantas vezes cada filósofo conseguiu comer.

Resultado:

```text
Filosofo 0: 3 vezes
Filosofo 1: 3 vezes
Filosofo 2: 3 vezes
Filosofo 3: 3 vezes
Filosofo 4: 3 vezes

Justica OK: todos comeram o mesmo numero de vezes.
```

Isso mostra que, durante a simulação, todos conseguiram participar igualmente.