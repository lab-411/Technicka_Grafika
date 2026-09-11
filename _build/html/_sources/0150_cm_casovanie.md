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
move to (0,0.5); QL: level(1.5,L); "L" at QL.B.n above; 
move to (2,0.5); QH: level(1.5,H); "H" at QH.B.n above; 
move to (4,0.5); QX: level(1.5,X, D); "X" at QX.B.n above; 
move to (6,0.5); PH: pulse(1.5, 0.25, LH); "L-H" at PH.B.n above; 
move to (8,0.5); PL: pulse(1.5, 0.25, HL); "H-L" at PL.B.n above; 

'''

_ = cm_compile('cm_0150a', data, dpi=600)   
```

```{figure} ./src/cm_0150a.png
:width: 600px
:name: cm_140a

Statické úrovne signálov a prechody medzi úrovňami.
```

Každý element časového priebehu je "orámovaný" neviditeľným boxom označeným ako *B*, tento je možné využiť v prípade potreby ako referenciu pre umiestnenie popisu časového okamžiku priebehu.

```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
cct_init
log_init

include(lib_base.ckt)
include(lib_color.ckt)
include(lib_time.ckt)
include(lib_ic485.ckt)

command "\sf"
color_light_grey; line from (0, 1.5) right_ 4.65 dashed; color_red; "H" ljust ;
color_light_grey; line from (0, 0.5) right_ 4.65 dashed; color_red; "L" ljust ;
color_light_grey; line from (0, 1) right_ 4.65   dashed; color_red; "X" ljust ;

color_black;
move to (1,1); 
PH: pulse(1.5, 0.25, LH); 

color_red;
box wid (PH.B.e - PH.B.w).x ht (PH.B.n - PH.B.s).y at PH.B.c dotted; #PH.B.e - PH.B.w ht PH.B.n - PH.B.s;
color_dark_green;
line <- from PH.B.nw left_ 0.5 up_ 0.5; ".B.nw" above;
line <- from PH.B.n up_ 0.75 ; ".B.n" above;
line <- from PH.B.ne up_ 0.5 right_ 0.5; ".B.ne" above;
line <- from PH.B.e right_ 0.75; ".B.e" ljust;
line <- from PH.B.se right_ 0.5 down_ 0.5; ".B.se" below;
line <- from PH.B.s down_ 0.75 ; ".B.s" below;
line <- from PH.B.sw left_ 0.5 down_ 0.5; ".B.sw" below;
line <- from PH.B.w left_ 0.75; ".B.w" rjust;
line <- from PH.B.c right_ 1.85 down_ 0.55; ".B.c" ljust;
'''

_ = cm_compile('cm_0150f', data, dpi=600)   
```

```{figure} ./src/cm_0150f.png
:width: 400px
:name: cm_140e

Umiestnenie popisného textu k časovému priebehu.
```


## <font color='teal'> Dáta </font>

V časových diagramoch dáta reprezentujú binárny vektor, hodnota alebo symbolické označenie vektora je zvyčajne súčasťou zobrazenia dát.    

    data(d, text, L|R|X)    - vykreslenie dát
    
      parametre:
        d                  - dĺžka stavu
        text               - hodnota alebo označenie dát, text v úvodzovkách 
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
move to (6,0.5); data(1.5,"$d_0$"); data(1.5,"0xFF");  
'''

_ = cm_compile('cm_0150b', data, dpi=600)   
```

```{figure} ./src/cm_0150b.png
:width: 600px
:name: cm_140b

Vykreslenie dát s popisom.
```

## <font color='teal'> Hodinové impulzy </font>

Hodinové impulzy sú zvyčajne sekvenciou opakujúcich sa impulzov so striedou 1:1. Pre zobrazenie sekvencie hodinovým impulzov môžeme použiť príkaz cyklu. 

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
move to (0.5, 0.5); CL: clock(0.75, HL); "HL" at CL.B.n above; 
move to (1.5, 0.5); CR: clock(0.75, LH); "LH" at CR.B.n above;  
move to (3.5, 0.5);
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


### <font color='brown'> Jednoduchý diagram </font>

Na diagrame je znázornený priebeh generovania PWM signálu časovačom procesora STM32L476 v móde 1.

```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *


data = r'''
include(lib_base.ckt)                  
include(lib_time.ckt)
include(lib_color.ckt)

command "\sf"
Origin: Here 
Grid(13,5);              # vykreslenie pomocnej mriezky, origin je (0,0)

d=1.5
move to (2.5,4);
"\small{CK\_CNT}" at Here rjust;
level(1,L)

for i=0 to 5 do{
  clock(0.5, HL)
  level(1,L)
}


move to (2.5,3);
"\small{Counter}" at Here rjust;
data(d-0.5, "6" ,L)
data(d,"7")
data(d,"8")
data(d,"9")
data(d,"0")
data(d,"1")
data(d-0.5,"2", R)

move to (2.5,2);
"\small{PWM 1}" at Here rjust;
level(2.5,H);
pulse(3,0, HL)
pulse(4.5,0, LH)
#pulse(
#level(5,L);

move to (2.5,1);
"\small{UPDATE Flag}" at Here rjust;
level(5.5,L);
pulse(0.5, 0.0, LH)
level(3.5,H);

color_red;
line from (5, 0) to (5, 5) dashed .08;
line from (8, 0) to (8, 5) dashed .08;   
'''

_ = cm_compile('cm_0150d', data, dpi=600)   
```

```{figure} ./src/cm_0150d.png
:width: 600px
:name: cm_0150d
Generovanie PWM signálu.
```

::::{admonition} Zdrojový kód
:class: dropdown, tip 

```{code-block} 
:caption: Zdrojový kód k obrázku {numref}`cm_0150d`

.PS
pi=3.14159265359
                        # parametre z PIC (resp. GNU PIC)
scale = 2.54            # cm - jednotka pre obrazok
maxpswid = 30           # rozmery obrazku
maxpsht = 30            # 30 x 30cm, default je 8.5x11 inch
cct_init                # inicializacia lokalnych premennych

arrowwid  = 0.127       # parametre sipok - sirka
arrowht = 0.254         # dlzka

include(lib_base.ckt)                  
include(lib_time.ckt)
include(lib_color.ckt)

command "\sf"
Origin: Here 
Grid(13,5);              # vykreslenie pomocnej mriezky, origin je (0,0)

d=1.5
move to (2.5,4);
"\small{CK\_CNT}" at Here rjust;
level(1,L)

for i=0 to 5 do{
  clock(0.5, HL)
  level(1,L)
}

move to (2.5,3);
"\small{Counter}" at Here rjust;
data(d-0.5, "6" ,L); data(d,"7"); data(d,"8"); data(d,"9"); data(d,"0"); data(d,"1"); data(d-0.5,"2", R)

move to (2.5,2);
"\small{PWM 1}" at Here rjust;
level(2.5,H); pulse(3,0, HL); pulse(4.5,0, LH)

move to (2.5,1);
"\small{UPDATE Flag}" at Here rjust;
level(5.5,L); pulse(0.5, 0.0, LH); level(3.5,H);

color_red;
line from (5, 0) to (5, 5) dashed .08;
line from (8, 0) to (8, 5) dashed .08;   

.PE
```
::::

