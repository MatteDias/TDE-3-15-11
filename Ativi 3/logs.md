Travada :

O processador tenta revezar (estilo Round Robin) só que isso 
não funciona com a ordem do acquire, pois o acquire sempre vai tentar pegar lockA
só que lockA só será liberado quando o T1 liberar. Nesse caso isso não acontece,
por conta que ocorre um deadlock ao o T2 tentar fazer um acquire antes do T1
fazer um release().

e "c:/Users/arthu/Projetos/TDE-3-15-11/Ativi 3/travada.py"          
T1 adquiriu lockA                                                   
T2 adquiriu lockB                                                   
T1 tentando adquirir lockB
T2 tentando adquirir lockA
T1 e T2 travaram


Corrigida:

Nesse caso funciona pois o T1 conclui seu trabalho antes de tentar
adquirir o lockB, logo o T2 pode adquirir o lockA.

e "c:/Users/arthu/Projetos/TDE-3-15-11/Ativi 3/corrigida.py"        
T1 adquiriu lockA                                                   
T1 tentando adquirir lockB                                          
T1 concluiu
T2 adquiriu lockA
T2 tentando adquirir lockB
T2 concluiu
DEu boa


-----------------------------------


Explicação da condição de Coffman quebrada:

- Espera Circular

No código que travava, o T1 segurava o lockA esperando o lockB, e o T2 segurava o lockB esperando o lockA, criando um ciclo onde um esperava o outro liberar. 

Na versão corrigida, foi definida uma regra de ordem global: os dois precisam dar acquire no lockA antes de tentar pegar o lockB. Como ninguém consegue pegar o lockB sem ter pego o lockA primeiro, não tem como o T2 pegar o lockB e travar o T1. Quem pegar o lockA primeiro faz o serviço, dá release() nos dois e depois o outro faz o mesmo, quebrando o ciclo e evitando o deadlock.
