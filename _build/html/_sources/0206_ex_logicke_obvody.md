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
from src.utils import *

data = r'''
include(lib_base.ckt)
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

_ = cm_compile('cm_0206a', data,  dpi=600)   
```

```{figure} ./src/cm_0206a.png
:width: 500px
:name: cm_0206a

[Zapojenie](./src/cm_0206a.ckt) multiplexera
```
## <font color='teal'> Sekvenčné obvody </font> 


## <font color='teal'> Zbernice </font> 


```{code-cell} ipython3  
:tags: ["remove-cell"]
from src.utils import *

data = r'''
log_init

command "\sf"

define(`SPI_Master', `[
  BX: box wid 2.5 ht 7*lg_pinsep;

      lg_pin(BX.ne - (0, 1*lg_pinsep),  SCLK, Pin8, e,,0 );
      lg_pin(BX.ne - (0, 2*lg_pinsep),  MOSI, Pin7, e,,0 );
      lg_pin(BX.ne - (0, 3*lg_pinsep),  MISO, Pin6, e,,0 );
      lg_pin(BX.ne - (0, 4*lg_pinsep),  lg_bartxt(CS1), Pin5, e,,0 );
      lg_pin(BX.ne - (0, 5*lg_pinsep),  lg_bartxt(CS2), Pin4, e,,0 );
      lg_pin(BX.ne - (0, 6*lg_pinsep),  lg_bartxt(CS3), Pin3, e,,0 );

]')

define(`SPI_Slave', `[
  BX: box wid 2 ht 5*lg_pinsep;

      lg_pin(BX.nw - (0, 1*lg_pinsep),  SCLK, Pin1, w,,0);
      lg_pin(BX.nw - (0, 2*lg_pinsep),  MOSI, Pin2, w,, 0);
      lg_pin(BX.nw - (0, 3*lg_pinsep),  MISO, Pin3, w,, 0);
      lg_pin(BX.nw - (0, 4*lg_pinsep),  lg_bartxt(CS), Pin4, w,,0 );
]')

M: SPI_Master(); "SPI" at M.c +(-0.3,0) above; "Master" at M.c +(-0.3,0) below;
   line from M.Pin8 right 1.5;  DT1: dot; 
   line from M.Pin7 right 1.25; DT2: dot; 
   line <-from M.Pin6 right 1.;   DT3: dot;

   line from DT1-> right 1;
S1: SPI_Slave() with .Pin1 at last line .end; 
    "SPI" at S1.c +(0.3,0) above; "Slave" at S1.c +(0.3,0) below;
    line -> from DT2 to S1.Pin2
    line from DT3 to S1.Pin3
    line -> from M.Pin5 to S1.Pin4

    line from DT1 down_ 2.5; DT5: dot;line -> to (S1.Pin1, Here)
    right_
S2: SPI_Slave() with .Pin1 at last line .end
    "SPI" at S2.c +(0.3,0) above; "Slave" at S2.c +(0.3,0) below;
    line from DT2 to (DT2, S2.Pin2); DT6: dot;line -> to S2.Pin2
    line from DT3 to (DT3, S2.Pin3); DT7: dot;line -> to S2.Pin3

    line from DT5 down_ 2.5; ;line -> to (S1.Pin1, Here)
    right_
S3: SPI_Slave() with .Pin1 at last line .end
    "SPI" at S3.c +(0.3,0) above; "Slave" at S3.c +(0.3,0) below;
    line from DT6 to (DT6, S3.Pin2); line -> to S3.Pin2
    line from DT7 to (DT7, S3.Pin3); line -> to S3.Pin3

X:  0.3 between M.Pin4 and S2.Pin4;
    line -> from M.Pin4 to (X, M.Pin4) then to (X, S2.Pin4) then to S2.Pin4

Y:  0.2 between M.Pin3 and S3.Pin4;
    line -> from M.Pin3 to (Y, M.Pin3) then to (Y, S3.Pin4) then to S3.Pin4 
'''

_ = cm_compile('img_0206c', data,  dpi=600)   
```

```{figure} ./src/img_0206c.png
:width: 350px
:name: img_0206c

Blokové [zapojenie](./src/img_0206c.ckt) SPI rozhrania 
```

