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

# <span style="color:navy"> Multipóly </span>

Zložitejšie elektronické prvky majú zvyčajne viacej ako dva uzly, takýmto  prvkom v teórii systémov je štvorpól, ktorý má dva vstupné a dva výstupné uzly. Okrem štandardných atribútov má multipól ešte doplňujúce atribúty súvisiace s polohou uzlov a označením uzlov. 

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

log_init;
Origin: Here
up_;
move to Here;
TR: transformer(down_ 2,L,7,W,4); {"tra\\nsformer" at (Here.x-2.5,  TR.c.y); }

move to Here+(0,0.5);
GG: gyrator;                          {"gy\\rator" at (Here.x-2.5, GG.c.y);  }

move to Here+(0,0.5);
TT: bi_tr(up_,,,E) ;                   {"bi\_t\\r" at (Here.x-2.5, TT.c.y);  }

move to Here+(0,0.5);
HH: Header(2, 6,,,fill_(0.9));         {"Heade\\r" at (Here.x-2.5,  HH.c.y); }

move to Origin + (4,0);
NN: nport;                             {"npo\\rt"  at (Here.x +2.5, NN.c.y); }

move to Here+(0,1.2);
OP: opamp(right_);                     {"opa\\mp"  at (Here.x +2.5, OP.c.y); }

move to Here+(0,0.8);
CC: contact;                           {"cont\\act"  at (Here.x +2.5, CC.c.y); }

move to Here+(0,0.8);
G1: NAND_gate(4);                      {"NAND\\\_gate"  at (Here.x +2.5, G1.c.y); }
'''

_ = cm_compile('cm_0102a', data,  dpi=600)   
```

```{figure} ./src/cm_0102a.png
:width: 500px
:name: cm_0102a

[Príklady](./src/cm_0102a.ckt) multipólov definovaných v CircuitMacros.
```


Typickým multipólom je transformátor, makro pre jeho zobrazenie má tvar

    transformer(linespec,L|R,np,[A|P][W|L][D1|D2|D12|D21],ns)
    
    parametre:
    
      linespec             - orientácia a dĺžka prícodov
      np                   - počet závitov primárneho vinutia
      ns                   - počet závitov sekundárneho vinutia
      L | R                - poloha primárho vinutia vlavo (L) alebo vpravo (R)
      W | L                - tvar zobrazenia vinutia široké (W) alebo jednoduché (L)
      A | P                - zobrazenie bez jadra (A) alebo s jadrom (P)
      D1 | D2 | D12 | D21  - označenie začiatku vinutia 
      
    atribúty:
    
    .s   .w   .n.  .e      - stredy strán obrysu
    .sw  .se  .nw  .ne     - rohy obrysu
    .P1  .P2               - poloha koncov primárneho vinutia
    .S1  .S2               - poloha koncov sekundárneho vinutia
    .TP  .TS               - poloha stredov vinutia
 
 
## <font color='teal'> Umiestňovanie multipólov </font>

Na pracovnej ploche môžeme umiestňovať multipóly niekoľkými spôsobmi

1. Zadaním východzieho bodu kreslenia presunom kurzora, objekt sa umiestni na ploche v smere ukladania v polohe príslušného atribútu .n, .s, .w .e

        move to pos; 
        object( dir length, ... );

2. Umiestnením zvoleného terminálu multipólu do určenej polohy 

        object( ...) with .attribute at pos;

3. Rovnako ako v prípade dvojpólov môžeme pomocou makier definovať smer ukladania objektov. V prípade multipólov zmena smeru ukladania nie je univerzálna a závisí od implementácie makra objektu.

        Point_(degrees); object;
        point_(radians); object;
        rpoint_(rel linespec); object
        
Príklad použitia:
    
```{code-block}
    right_; move to (1,1.); 
    transformer(down_ 1.5,L,4,W,4);                      # (1)

R1: resistor(right_ 2 from (3,2)); 
    transformer(down_ 1.5,L,4,W,4) with .P1 at R1.end;   # (2)

    move to (2.5,1);
    Point_(90); opamp;                                   # (3)
```

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)
define(`xc', `
  {
   Q: Here; line from Q+(-.1,-.1) to Q+(0.1, 0.1); 
   line from Q+(-.1, .1) to Q+(0.1, -0.1);
   circle at Q rad 0.1*1.4; 
   color_black;
   }
')

Grid(7,3);

circle at (0.5,1.)rad 0.25 "1"
right_; move to (1,1.);{ color_red; xc;}
move to (1,1.);
transformer(down_ 2,L,4,,4);

circle at (5.85, 2.35)rad 0.25 "2"
R1: resistor(right_ 2 from (3.5,2)); llabel(,R_1,); color_red; xc;
transformer(down_ 1.5,L,4,W,4) with .P1 at R1.end;

move to (2.5,1); {circle at (2.5,1.25)rad 0.25 "3"}
Point_(90); opamp
'''

_ = cm_compile('cm_0102c', data, dpi=600)   
```

```{figure} ./src/cm_0102c.png
:width: 450px
:name: cm_0102c

Príklady umiestňovania multipólov.
```
 
    
## <font color='teal'> Použitie </font> 

Použitie atribútov mnohopólu demonštruje nasledujúci príklad. Transformátor je centrálnym elementom a všetky prvky zapojenia sú umiestňované relatívne voči jeho terminálom.

    TR:  transformer(down_ 2,L,7,W,4);
         "1" at TR.P1 rjust below;     # popis transformatora 
         "2" at TR.P2 rjust above;
         "3" at TR.S1 ljust above;
         "4" at TR.S2 ljust below;
         "$TR_1$" at TR.n above;

         line from TR.P1 left_ 1;      # privody vlavo
    TC1: tconn(0.5,O);
         line from TR.P2 left_ 1; 
    TC2: tconn(0.5,O);

        line from TR.S1 up_ to (TR.S1.x, TC1.y) then right_ 0.5;
    D1: diode(1); llabel(,D_1,);       # usmerňovač
        dot;
        { tconn(1, O); }
        {C1: capacitor(down_ 2); llabel(,C_1,); }
        line from TR.S2 down_ to (TR.S2.x, TC2.y) then to C1.end;
        dot;
        tconn(right_ 1, O);


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

TR: transformer(down_ 2,L,7,W,4);
"1" at TR.P1 rjust below;
"2" at TR.P2 rjust above;
"3" at TR.S1 ljust above;
"4" at TR.S2 ljust below;
"$TR_1$" at TR.n above;

line from TR.P1 left_ 1; 
TC1: tconn(0.5,O);
line from TR.P2 left_ 1; 
TC2: tconn(0.5,O);

line from TR.S1 up_ to (TR.S1.x, TC1.y) then right_ 0.5;
D1: diode(1); llabel(,D_1,) 
DT1: dot;
{tconn(1, O); }
{C1: capacitor(down_ 2); llabel(,C_1,) }
line from TR.S2 down_ to (TR.S2.x, TC2.y) then to C1.end;
DT2: dot;
{tconn(right_ 1, O); }
'''

_ = cm_compile('cm_0102b', data,  dpi=600)   
```

```{figure} ./src/cm_0102b.png
:width: 250px
:name: cm_0102b

[Použitie](./src/cm_0102b.ckt) atribútov mnohopólu.
```
