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

Pred kreslením logických obvodov musíme inicializovať knižnicu makier *log_init*. Knižnica obsahuje makrá pre kreslenie základných kombinačných a sekvenčných obvodov. Hradlá kombinačných logických obvodov môžu mať niekoľko vstupov, ich počet definujeme pomocou parametra *n*.

         AND_gate(3)    NAND_gate(3)    OR_gate(2)    NOR_gate(3)    NXOR_gate(2)
                                NOT_gate()                     BUFFER_gate()

Zobrazenie hradiel kombinačné logických obvodov s variabilným počtom vstupov (and, nand, or, nor, xor), {numref}`cm_0206k`: 
                                
```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)
cct_init
log_init

define(`IN3', `
   line left_ 0.25 from $1.In1;
   line left_ 0.25 from $1.In2;
   line left_ 0.25 from $1.In3;
   line right_ 0.25 from $1.Out;
   move to last line.end + (0.5,0)
')

define(`IN2', `
   line left_ 0.25 from $1.In1;
   line left_ 0.25 from $1.In2;
   line right_ 0.25 from $1.Out;
   move to last line.end + (0.5,0)
')

# Enter your drawing code here
right_;
G1: AND_gate(3); IN3(G1);
G2: NAND_gate(3); IN3(G2);
G3: OR_gate(2); IN2(G3);
G4: NOR_gate(3); IN3(G4);
G5: NXOR_gate(2); IN2(G5);
move to G2.c  + (-0.5,-1.25)
G6: NOT_gate(2,,0.8,0.8); 
move to G4.c  + (-0.5,-1.25)
G6: BUFFER_gate(2,,0.8,0.8);
'''

_ = cm_compile('cm_0206k', data ,  dpi=600)   
```

```{figure} ./src/cm_0206k.png
:width: 500px
:name: cm_0206k

Hradlá kombinačných logických obvodov.

```

Definície makier pre hradlá s *n* vstupmi:


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
    
    
Definície makier pre hradlá s jedným vstupom (invertor, buffer):

    NOT_gate(linespec,[B][N|n],wid,height, attributes)
    BUFFER_gate(linespec, [N|B], wid, ht, [N|P]*, [N|P]*, [N|P]*, attributes)
    
    parametre:
    
        linespec - dĺžka a umiestnenie rezistora
        N        - negovaný vstup 
        B        - zobrazenie ako bloku podľa IEEE Standard 91-1984
        n        - (písmeno) výmena negácie z výstupu na vstupe (pri NOT)
        wid      - šírka 
        ht       - výška
        
    atribúty:

        ak je definovaný parameter linespec, hradlá majú atribúty 
        ako dvojpóly (.start, .centre, .end), inak
        
        In1      - poloha vstupu
        Out      - poloha výstupu
        C        - stred hradla
        NE       - prívod napájania (VCC) 
        SE       - prívod napájania (GND)

Pri kreslení logických obvodov je vhodné najskôr porozkladať hradlá po ploche a potom ich postupne prepájať. Na zjednodušenie prepojenia vývodov hradiel môžeme použiť jednoduché makro *conn()* s dvoma parametrami, ktoré sú súradnicami koncových bodov prepojenia. Zapojenie jednoduchého multiplexera je na obrázku {numref}`cm_0206a`: 

    define(`conn', `
            line from $1 left_ (($1 - $2)/2).x;
            line up_ to (Here.x, $2.y) then to $2;
        ')
        
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

#Grid(10,3.5);

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

Základné typy sekvenčných obvodov (D, T, RS, JK) sú definované pomocou makra *FlipFlop()*, {numref}`cm_0206m`: 

        FlipFlop(D,Q1)    FlipFlop(T,Q2)    FlipFlop(RS,Q3)    FlipFlop(JK)
    
```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)
cct_init
log_init

right_;
H1: FlipFlop(D,Q1); move to H1+(1.5,0)
H2: FlipFlop(T,Q2);  move to H2+(1.5,0)
H3: FlipFlop(RS,Q3);  move to H3+(1.5,0)
H4: FlipFlop(JK)
'''

_ = cm_compile('cm_0206m', data ,  dpi=600)   
```

```{figure} ./src/cm_0206m.png
:width: 550px
:name: cm_0206m

Zobrazenie typických sekvenčných obvodov.
```
Definícia makra *FlipFlop()* má tvar: 

    FlipFlop(type, label, boxspec, pinlength)
    
    parametre:
    
        type      - typ obvodu D|T|RS|JK 
        label     - označenie obvodu
        boxspec   - parametre značky ako pre box 
        pinlength - dĺžka pinu

    atribúty:

        podľa mena pinu .D .CK .Q .NQ .R .S .J .K .PR .CLR
        
Pre vytváranie vlastných značiek obvodov môžeme použiť makrá popísané v kapitole [Integrované obvody](0207_ex_integrovane_obvody.md) alebo makro *FlipFlopX()*, podrobný popis je v dokumentácii. Na obrázku {numref}`cm_0206n` je zobrazené použitie nového makra *JK93()* v zapojení zobrazujúcom vnútornú štruktúru časovača 7493:

    # JK obvod v strukture citaca 7493
    define(`JK93', `[
    BX:box wid 1.5 ht 6*lg_pinsep;
        lg_pin(BX.nw - (0, 1*lg_pinsep), J,  PinJ,   w,  ,0);
        lg_pin(BX.nw - (0, 3*lg_pinsep), CK, PinCK, wEN,,0);
        lg_pin(BX.nw - (0, 5*lg_pinsep), K,  PinK,   w,  ,0);
        lg_pin(BX.ne - (0, 3*lg_pinsep), Q,  PinQ,   e,  ,0);
        lg_pin(BX.s ,                    R,  PinR,  sN,  ,0 )
    ]')



```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)
cct_init
log_init

command "\footnotesize \sf"
define(`JK93', `[
   BX:box wid 1.5 ht 6*lg_pinsep;
      lg_pin(BX.nw - (0, 1*lg_pinsep), J,  PinJ,   w,  ,0);
      lg_pin(BX.nw - (0, 3*lg_pinsep), CK, PinCK, wEN,,0);
      lg_pin(BX.nw - (0, 5*lg_pinsep), K,  PinK,   w,  ,0);
      lg_pin(BX.ne - (0, 3*lg_pinsep), Q,  PinQ,   e,  ,0);
      lg_pin(BX.s ,                    R,  PinR,  sN,  ,0 )
]')

H1: JK93; move to H1.c+(2,0);
H2: JK93; move to H2.c+(2,0)
H3: JK93; move to H3.c+(2,0)
H4: JK93;


line from H1.PinQ right_ 0.5 then down_ 3; T1: tconn(0.5,O); "QA" at T1.s below
line from H2.PinQ right_ 0.5; {dot; line to H3.PinCK + (-0.15,0);}
line down_ 3; T2: tconn(0.5,O); "QB" at T2.s below
line from H3.PinQ right_ 0.5; {dot; line to H4.PinCK + (-0.15,0);} 
line down_ 3; T3: tconn(0.5,O); "QC" at T3.s below
line from H4.PinQ right_ 0.5 then down_ 3; T4: tconn(0.5,O); "QD" at T4.s below

line from H1.PinR + (0,-0.15) down_ 1.5; dot; 
{   line left_  2; 
    right_; H5: AND_gate(2) with .Out at last line.end;
    line from H5.In1 left_ 0.5; T5: tconn(0.5, O);  "MR1" at T5.w rjust;
    line from H5.In2 left_ 0.5; T6: tconn(0.5, O);  "MR2" at T6.w rjust;
}
line right_ to (H2.PinR, Here); dot; {line to H2.PinR +(0,-0.15);}
line right_ to (H3.PinR, Here); dot; {line to H3.PinR +(0,-0.15);}
line right_ to (H4.PinR, Here); dot; {line to H4.PinR +(0,-0.15);}


line from H1.PinCK+(-0.15,0) to (T5.e, H1.PinCK); left_; T7: tconn(0.5, O);  "CKA" at T7.w rjust;
line from H2.PinCK+(-0.15,0) left_ 0.35 then down 1.75; 
line to (T5.e, Here);  left_; T8: tconn(0.5, O);  "CKB" at T8.w rjust;
'''

_ = cm_compile('cm_0206n', data ,  dpi=600)   
```

```{figure} ./src/cm_0206n.png
:width: 600px
:name: cm_0206n

Vnútorné zapojenie čitača 7493 podľa TI (TODO-ODKAZ).
```

## <font color='teal'> Zbernice </font> 

Digitálne systémy vo svojej architektúre často využívajú hierarchické usporiadanie obvodov do skupín zdielajúcich spoločný komunikačný systém, zbernicu. Rozkreslenie zbernice na jednotlivé vodiče môže byť niekedy neprehľadné, tak ako to ukazuje obrázok  {numref}`img_0206c`. 

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
    line from DT3 to (DT3, S2.Pin3); DT7: dot;line  to S2.Pin3

    line from DT5 down_ 2.5; ;line -> to (S1.Pin1, Here)
    right_
S3: SPI_Slave() with .Pin1 at last line .end
    "SPI" at S3.c +(0.3,0) above; "Slave" at S3.c +(0.3,0) below;
    line from DT6 to (DT6, S3.Pin2); line -> to S3.Pin2
    line from DT7 to (DT7, S3.Pin3); line  to S3.Pin3

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

Blokové [zapojenie](./src/img_0206c.ckt) SPI zbernice v režime MDP (Multidrop). 
```

Použitím zberníc môžeme celé zapojenie zjednodušiť a sprehladniť, {numref}`img_0206d`. 


```{code-cell} ipython3  
:tags: ["remove-cell"]
from src.utils import *

data = r'''
cct_init                # inicializacia lokalnych premennych
log_init

include(lib_bus.ckt)
include(lib_spi.ckt)

command"\sf"

M: SPI_Master(0); "SPI" at M.c +(-0.3,0) above; "Master" at M.c +(-0.3,0) below;
B1: bus_dr(6) with .REF at M.Pin1

B2: bus_ul(4) with .END at B1.END
S1: SPI_Slave(0) with .Pin4 at bus_ref(B2,1); "SPI" at S1.c +(0.3,0) above; "Slave" at S1.c +(0.3,0) below;
    bus_txl(B2,lg_bartxt(CS1),1)

B3: bus_ul(4) with .END at B2.END+(0,-2.25)
S2: SPI_Slave(0) with .Pin4 at bus_ref(B3,1); "SPI" at S2.c +(0.3,0) above; "Slave" at S2.c +(0.3,0) below;
    bus_txl(B3,lg_bartxt(CS2),1)

B4: bus_ul(4) with .END at B3.END+(0,-2.25)
S3: SPI_Slave(0) with .Pin4 at bus_ref(B4,1); "SPI" at S3.c +(0.3,0) above; "Slave" at S3.c +(0.3,0) below;
    bus_txl(B4,lg_bartxt(CS3),1)

bus_conn(B2,B3)
bus_conn(B3,B4)
'''

_ = cm_compile('img_0206d', data,  dpi=600)   
```

```{figure} ./src/img_0206d.png
:width: 350px
:name: img_0206d

[Zapojenie](./src/img_0206d.ckt) SPI rozhrania pomocou vykreslenia zbernice.
```

Zbernice môžeme pripájať k obvodom pomocou konektorov definovaných makrami v súbore [lib_bus.ckt](./src/lib_bus.ckt). Parametrom makier je počet vodičov zbernice, pomocou ďaľších makier môžeme popisovať jednotlivé vetvy zbernice ako aj ziskať referenciu na koniec každej vetvy, {numref}`img_0206e`. 

```{code-cell} ipython3  
:tags: ["remove-cell"]
from src.utils import *

data = r'''
cct_init                # inicializacia lokalnych premennych
log_init

include(lib_bus.ckt)
include(lib_spi.ckt)

command"\sf"

B1: bus_dr(6) with .REF at (1,3)  ; "bus\_dr(6)" at B1.nw ljust above;
B2: bus_dl(5) with .REF at (4.5,3); "bus\_dl(5)" at B2.ne rjust above;
B3: bus_ul(4) with .REF at (6.5,1); "bus\_ul(4)" at B3.se rjust below;
B4: bus_ur(3) with .REF at (7,1)  ; "bus\_ul(3)" at B4.sw ljust below;
'''

_ = cm_compile('img_0206e', data,  dpi=600)   
```

```{figure} ./src/img_0206e.png
:width: 400px
:name: img_0206e

Makrá pre kreslenie pripojenia zbernice k obvodu.
```
Každý konektor zbernice má vetvy číslované od začiatku zbernice. Číslovanie vetiev je nezávislé od číslovania pinov pripojeného obvodu. Definícia makier pre pripojenie zbernice k obvodu má tvar: 

    bus_dl(n,d)  - makra pre pripajanie zbernice k obvodom 
    bus_dr(n,d)
    bus_ul(n,d)
    bus_ur(n,d)
    
    parametre:
        n        - počet vetiev
        d        - dĺžka vetvy

    atribúty:
        REF     - poloha referenčného pinu č.1
        START   - začiatok zbernice
        END     - koniec zbernice
        DOC     - pozícia pre popisovanie zbernice
    
Pomocné makrá pre popis zbernice, polohu koncového bodu vetvy majú tvar:

    bus_txl(bus, text, pin) - makrá pre popis vetvy zbernice, zarovnanie doľava
    bus_txr(bus, text, pin) - zarovnanie doprava
    bus_ref(bus, pin)       - poloha koncovej vetvy zbernice 
    bus_conn(bus1, bus2)    - spojenie zberníc úsečkou
    
    parametre:
        bus     - referencia na zbernicu
        text    - popis, bez úvodzoviek
        pin     - čislo pinu zbernice
    
    
Pri pripájaní zberníc k obvodu využijeme konštrukciu *with ... at ...*. Koniec prvej vetvy konektoru je prístupný pod atribútom *REF*, ktorý pripojíme k zvolenému pinu obvodu, {numref}`img_0206f`:

    IC: IC74138(); "74138" at IC.s below; 
    B1: bus_dl(3) with .REF at IC.Pin3;
    B2: bus_ur(3) with.END at B1.END+(0,-1)
        bus_conn(B1,B2)
    
        line left_ 1 from bus_ref(B2,1); tbox(A,,lg_pinsep,<>)
        line left_ 1 from bus_ref(B2,2); tbox(B,,lg_pinsep,<>)
        line left_ 1 from bus_ref(B2,3); tbox(C,,lg_pinsep,<>)

```{code-cell} ipython3  
:tags: ["remove-cell"]
from src.utils import *

data = r'''
cct_init                # inicializacia lokalnych premennych
log_init

include(lib_bus.ckt)

command"\sf"

define(`IC74138',`[ 
    right_;
   Chip: box wid_ lg_chipwd ht_ 9*lg_pinsep
   lg_pin(Chip.sw_+(0,lg_pinsep),GND,Pin8,w,8)
   lg_pin(Chip.sw_+(0,2*lg_pinsep),lg_bartxt(G2a),Pin4,wN,4)
   lg_pin(Chip.sw_+(0,3*lg_pinsep),lg_bartxt(G2b),Pin5,wN,5)
   lg_pin(Chip.sw_+(0,4*lg_pinsep) ,G1,Pin6,w,6)
   lg_pin(Chip.sw_+(0,6*lg_pinsep),A,Pin1,w,1)
   lg_pin(Chip.sw_+(0,7*lg_pinsep),B,Pin2,w,2)
   lg_pin(Chip.sw_+(0,8*lg_pinsep),C,Pin3,w,3)
   
   lg_pin(Chip.se_+(0,lg_pinsep)   ,Y0,Pin15,eN,15)
   lg_pin(Chip.se_+(0,2*lg_pinsep) ,Y1,Pin15,eN,14)
   lg_pin(Chip.se_+(0,3*lg_pinsep) ,Y2,Pin15,eN,13)
   lg_pin(Chip.se_+(0,4*lg_pinsep) ,Y3,Pin15,eN,12)
   lg_pin(Chip.se_+(0,5*lg_pinsep) ,Y4,Pin15,eN,11)
   lg_pin(Chip.se_+(0,6*lg_pinsep) ,Y5,Pin15,eN,10)
   lg_pin(Chip.se_+(0,7*lg_pinsep) ,Y6,Pin15,eN,9)
   lg_pin(Chip.se_+(0,8*lg_pinsep) ,Y7,Pin15,eN,7)
]')


IC: IC74138(); "74138" at IC.s below; 
B1: bus_dl(3) with .REF at IC.Pin3;
B2: bus_ur(3) with.END at B1.END+(0,-1)
    bus_conn(B1,B2);
    line left_ 1 from bus_ref(B2,1); tbox(\sf A,,lg_pinsep,<>)
    line left_ 1 from bus_ref(B2,2); tbox(\sf B,,lg_pinsep,<>)
    line left_ 1 from bus_ref(B2,3); tbox(\sf C,,lg_pinsep,<>)
    bus_txl(B1,DB1,1)
    bus_txl(B1,DB2,2)
    bus_txl(B1,DB3,3)
    
    bus_txr(B2,DB3, 1)
    bus_txr(B2,DB2,0)
    bus_txr(B2,DB1,-1)
    
'''

_ = cm_compile('img_0206f', data,  dpi=600)   
```

```{figure} ./src/img_0206f.png
:width: 400px
:name: img_0206f

Pripojenie zbernice k obvodu.
``


