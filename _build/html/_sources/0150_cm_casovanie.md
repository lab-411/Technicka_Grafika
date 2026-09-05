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
# <font color='navy'> Časové priebehy </font>

Súčasťou mnohých elektronických zapojení sú priebehy signálov v elektronickom obvode závislé od času. Pre tvorbu časových priebehov môžeme využiť niektoré z dostupných programov ako napríklad [plantuml](https://plantuml.com/timing-diagram), v *CircuitMacros* môžeme využiť jednoduchú knižnicu [lib_time](./src/lib_time.ckt).
Pri kreslení diagramov je vhodné použiť mriežku *Grid(x,y)*, ktorá zjednodušuje orientáciu pri zadávaní časových priebehov a relácií medzi nimi.

## <font color='teal'> Statické úrovne a prechody medzi úrovňami</font>

Hodnota amplitúdy logických úrovní pre príkazy kreslenia elementov časového priebehu je prednastavená na hodnotu 0.7, pre kreslenie priebehu je začiatkom zadaný stred logickej stopy. Amplitúdu logických úrovní je možné zmeniť hodnotou premennej *pulse_level*.

Každý element časového priebehu je "orámovaný" neviditeľným boxom označeným ako *B*, tento je možné využiť v prípade potreby ako referenciu pre polohovanie popisu priebehu.


    level(d, L|H|X, D)     - vykreslenie logických úrovní
    pulse(d, delay, LH|NL) - vykreslenie prechodov medzi logickými úrovňami
    
      parametre:
        d                  - dĺžka stavu
        L|H|X              - úroveň L, H, X-neurčitý stav 
        D                  - čiarkovaný priebeh
        delay              - 0..1, oneskorenie zobrazenia prechodu, d*delay
        
        

```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_time.ckt)
include(lib_base.ckt)

command "\sf"
Grid(10,1)
pulse_level = 0.75
move to (0,0.5); QL: level(1.5,L); "L" at QL.B.c; 
move to (2,0.5); QH: level(1.5,H); "H" at QH.B.c; 
move to (4,0.5); QX: level(1.5,X, D); "X" at QX.B.n; 
move to (6,0.5); PH: pulse(1.5, 0.25, LH); "L-H" at PH.B.c; 
move to (8,0.5); PL: pulse(1.5, 0.25, HL); "H-L" at PL.B.c; 

'''

_ = cm_compile('cm_0150a', data, dpi=600)   
```

```{figure} ./src/cm_0150a.png
:width: 600px
:name: cm_140a

Statické úrovne a prechody medzi úrovňami.
```

## <font color='teal'> Dáta </font>

    data(d, text, L|R|X)    - vykreslenie dát
    
      parametre:
        d                  - dĺžka stavu
        text               - popis dát, text v úvodzovkách 
        L|R|X              - typ dát, otvorené zľava, zprava, neučité / opakované dáta
        
```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_time.ckt)
include(lib_base.ckt)
include(lib_color.ckt)

command "\sf"
Grid(10,1)
pulse_level = 0.75
move to (0,0.5); DL: data(1.5,"",L); "L" at DL.B.n above; 
move to (2,0.5); DR: data(1.5,"",R); "R" at DR.B.n above; 
move to (4,0.5); DX: data(1.5,"",X); "X" at DX.B.n above; 
color_red();
move to (6,0.5); data(1.5,"$d_0$"); data(1.5,"$d_1$");  
'''

_ = cm_compile('cm_0150b', data, dpi=600)   
```

```{figure} ./src/cm_0150b.png
:width: 600px
:name: cm_140b

Vykreslenie dát s popisom.
```

## <font color='teal'> Hodinové impulzy </font>

    clock(d, HL|LH)        - vykreslenie hodinového impulzu
    
      parametre:
        d                  - dĺžka stavu
        HL|LH              - fáza hodinového impulzu


```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *


data = r'''
include(lib_time.ckt)
include(lib_base.ckt)
include(lib_color.ckt)

command "\sf"
Grid(10,1)
pulse_level = 0.75
move to (0,0.5); CL: clock(0.75, HL); "HL" at CL.B.n above; 
move to (1,0.5); CR: clock(0.75, LH); "LH" at CR.B.n above;  
move to (3,0.5);
for i=0 to 5 do{
  clock(1, HL)
}
'''

_ = cm_compile('cm_0150c', data, dpi=600)   
```

```{figure} ./src/cm_0150c.png
:width: 600px
:name: cm_140c
Hodinove impulzy.
```


