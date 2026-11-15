# Trabalho de Performance em Sistemas Ciberfisicos

Repositório do Grupo 6 com três atividades sobre concorrência, semáforos e deadlock.

## Integrantes

- Gastão Eduardo Santos Borges
- Matteo Dias Silvestre
- Otávio Augusto Brouwers Londero
- Arthur de Oliveira Carvalho

## Linguagem e execução

Os programas foram feitos em Python 3. Como Python é interpretado, não é preciso compilar para executar. Com o Python instalado, abra o terminal na pasta do repositório e rode o arquivo da atividade:

```bash
python parte1-filosofos/jantar_falho.py
python parte1-filosofos/jantar_final.py
python parte2-semaforo/threadsSEMsemaforo.py
python parte2-semaforo/threadsCOMsemaforo.py
python parte3-deadlock/travada.py
python parte3-deadlock/corrigida.py
```

No Windows, use `py -3` no lugar de `python` se necessário. Para conferir a sintaxe sem iniciar os programas, use `python -m py_compile` seguido dos caminhos dos arquivos `.py`.

## Parte 1 — Jantar dos filósofos

### Como funciona

São cinco filósofos sentados em uma mesa e cinco garfos compartilhados. Para comer, cada um precisa pegar os garfos dos dois lados. No código, os filósofos são threads e cada garfo é um `Lock`.

### Versão que pode travar

Em `jantar_falho.py`, todos tentam pegar primeiro o garfo da esquerda. Se cada filósofo conseguir pegar esse garfo, todos ficam esperando pelo da direita, que está com o vizinho. Como ninguém chega à parte que libera os garfos, a execução pode entrar em deadlock.

Uma pausa de um segundo entre as aquisições facilita observar a situação. Mesmo assim, o resultado depende da ordem em que as threads são executadas; por isso, uma rodada também pode terminar sem deadlock.

### Versão corrigida

Em `jantar_final.py`, os filósofos pegam primeiro o garfo de menor número e depois o de maior número. Essa ordem quebra a espera circular. Cada filósofo come três vezes e o programa mostra a contagem no final.

## Parte 2 — Contador e semáforo

Os arquivos `threadsSEMsemaforo.py` e `threadsCOMsemaforo.py` comparam oito threads incrementando o mesmo contador. Cada thread faz 200.000 incrementos; o total esperado é 1.600.000.

### Sem semáforo

Em `threadsSEMsemaforo.py`, cada thread lê o valor do contador, cede a execução e grava o valor incrementado. Outra thread pode alterar o contador nesse intervalo, fazendo alguns incrementos se perderem.

### Com semáforo

Em `threadsCOMsemaforo.py`, o semáforo deixa apenas uma thread por vez acessar o contador. Assim, as atualizações não se sobrepõem. Os dois programas mostram o valor final e o tempo gasto; esse tempo pode mudar de uma máquina para outra.

## Parte 3 — Deadlock

### Versão travada

Em `travada.py`, a primeira thread pega o lock A e tenta pegar B. A segunda pega B e tenta pegar A. Cada uma fica esperando pelo lock que está com a outra, formando uma espera circular.

### Versão corrigida

Em `corrigida.py`, as duas threads seguem a mesma ordem e tentam pegar A antes de B. Uma pode esperar pela outra, mas não se forma o ciclo de espera. Os registros dessa atividade estão em [`parte3-deadlock/logs.md`](parte3-deadlock/logs.md).

## Saídas dos programas

As mensagens aparecem no terminal durante a execução. Na parte 1, elas mostram o estado dos filósofos e o resultado da simulação. Na parte 2, mostram o contador final, o valor esperado e o tempo. Na parte 3, o arquivo de logs reúne os registros das versões travada e corrigida. A ordem das mensagens concorrentes pode variar entre execuções.

## Vídeo

Link da apresentação no YouTube: https://youtu.be/AVx92nXX0EE
