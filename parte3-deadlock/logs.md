# Registros da atividade 3 — Deadlock

## Versão travada

Em `travada.py`, T1 adquire primeiro `lockA` e T2 adquire primeiro `lockB`. Depois, cada thread tenta adquirir o lock que já está com a outra. Forma-se uma espera circular e nenhuma delas alcança os comandos de liberação.

Saída registrada:

```text
T1 adquiriu lockA
T2 adquiriu lockB
T2 tentando adquirir lockA
T1 tentando adquirir lockB
T1 e T2 travaram
```

## Versão corrigida

Em `corrigida.py`, ambas as threads adquirem `lockA` antes de tentar `lockB`. Uma thread conclui e libera os locks antes de a outra prosseguir, evitando a espera circular.

Saída registrada:

```text
T1 concluiu acquireA
T1 concluiu acquireB
T1 concluiu releaseB
T1 concluiu releaseA
T2 concluiu acquireA
T2 concluiu acquireB
T2 concluiu releaseB
T2 concluiu releaseA
DEu boa
```

Os registros são exemplos de uma execução; a ordem das mensagens pode variar conforme o escalonamento das threads.

## Condição de Coffman quebrada

A versão corrigida quebra a condição de espera circular ao impor uma ordem global de aquisição dos recursos. As duas threads pedem primeiro A e depois B; assim, não conseguem manter locks em ordens opostas enquanto esperam uma pela outra.
