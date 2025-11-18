---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# <font color='navy'> Logické obvody </font> 

## <font color='teal'> Kombinačné obvody </font> 

Pred kreslením logických obvodov musíme inicializovať knižnicu makier *log_init*. Pretože hradlá kombinačných logických obvodov môžu mať niekoľko vstupov, makrá obsahujú parameter *n*, ktorým definujeme počet ich vstupov.

    AND_gate (n, [N][B], [wid, [ht]])
    OR_gate  (n, [N][B], [wid, [ht]])
    NOR_gate (n, [N|B],, [wid, [ht]])
    NAND_gate(n, [N][B], [wid, [ht]])
    NXOR_gate(n, N,      [wid, [ht]])
    
    parametre:
      
        n   - počet vstupov hradla
        N   - negované vstupy
        B   - zobrazenie hradla ako bloku podľa IEEE Standard 91-1984
        wid - šírka 
        ht  - výška
        
    atribúty:
    
        In1 ... InN  - poloha vstupov
        Out          - poloha výstupu
        N_Out        - poloha stredu negovaneho vystupu (kružnice)
    
    
Hradlá s jedným vstupom

    NOT_gate(linespec,[B][N|n],wid,height, attributes)
    BUFFER_gate(linespec, [N|B], wid, ht, [N|P]*, [N|P]*, [N|P]*, attributes)
    
    parametre:
    
        linespec - dĺžka a umiestnenie rezistora
        N        - negovaný vstup 
        B        - zobrazenie ako bloku podľa IEEE Standard 91-1984
        n        - (písmeno) výmena negácie z výstupu na vstupe (pri NOT)
        wid      - šírka 
        ht       - výška

Pri kreslení logických obvodov je vhodné najskôr porozkladať hradlá po ploche a potom ich postupne prepájať. Na zjednodušenie prepojenia vývodov hradiel môžeme použiť jednoduché makro *conn()* s dvoma parametrami - súradnicami koncových bodov prepojenia.

    define(`conn', `
        line from $1 left_ (($1 - $2)/2).x;
        line up_ to (Here.x, $2.y) then to $2;
    ')


Zapojenie jednoduchého multiplexera
        
    G1: AND_gate(2) at (5, 2); "\sf G1" at G1.n above;
    G2: AND_gate(2) at (5, 0.5); "\sf G2" at G2.n above;
    G3: OR_gate(2) at (7, (G1.c.y + G2.c.y)/2 ); "\sf G3" at G3.n above;
    G4: NOT_gate() at (3.5, 2.5); "\sf G4" at G4.n above;
        conn(G3.In1, G1.Out)
        conn(G3.In2, G2.Out)
        conn(G1.In1, G4.Out)

        line from G4.In1 left_ 0.35; DT: dot; line left_ 0.5; "\sf Q" at last line.end rjust;
        line from G1.In2 to (LL.end.x, G1.In2.y); "\sf D1" at last line.end rjust; 
        line from G2.In2 to (LL.end.x, G2.In2.y); "\sf D0" at last line.end rjust;  
        line from G2.In1 to (DT.x, G2.In1.y) then to DT;
        line from G3.Out right_ 1;  "\sf Y" at last line.end ljust;  

```{code-cell} ipython3 
:tags: ["remove-cell"]
from cm.utils import *

data = r'''
include(base.ckt)
cct_init
log_init

define(`conn', `
	line from $1 left_ (($1 - $2)/2).x;
	line up_ to (Here.x, $2.y) then to $2;
')

Grid(10,3.5);

G1: AND_gate(2) at (5, 2); "\sf G1" at G1.n above;
G2: AND_gate(2) at (5, 0.5); "\sf G2" at G2.n above;
G3: OR_gate(2) at (7, (G1.c.y + G2.c.y)/2 ); "\sf G3" at G3.n above;
G4: NOT_gate() at (3.5, 2.5); "\sf G4" at G4.n above;
conn(G3.In1, G1.Out)
conn(G3.In2, G2.Out)
conn(G1.In1, G4.Out)

line from G4.In1 left_ 0.35; DT: dot; LL: line left_ 0.5; "\sf Q" at last line.end rjust;
line from G1.In2 to (LL.end.x, G1.In2.y); "\sf D1" at last line.end rjust; 
line from G2.In2 to (LL.end.x, G2.In2.y); "\sf D0" at last line.end rjust;  
line from G2.In1 to (DT.x, G2.In1.y) then to DT;
line from G3.Out right_ 1;  "\sf Y" at last line.end ljust; 
'''

_ = cm_compile('./img/log_001', data,  dpi=600)   
```

```{figure} ./img/log_001.png
:width: 500px
:name: log_001

Multiplexer
```
## <font color='teal'> Sekvenčné obvody </font> 
