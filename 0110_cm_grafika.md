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

# <font color='navy'> Grafika </font>

Súčasťou zapojení vytváraných v `CircuitMacros` môžu byť aj lineárne a plošné grafické objekty vykreslované pomocou príkazov jazuka *dpic*. Čiara sa využíva na prepájanie prvkov zapojenia, ďaľšie grafické tvary môžeme využiť na doplnenie zapojenia alebo zvýraznenie niektorých častí. Rovnako môžeme pomocou nich vytvárať rôzne blokové zapojenia alebo vývojové diagramy. 

```{admonition} Poznámka
Základné grafické objekty (*line*, *spline*, *arc*, *box*, *circle*, *ellipse*, *move*, *arrow*) sú príkazmi jazyka `dpic` a majú preto inú formu zápisu ako makrá definované v `CircuitMacros`, ktoré sú naprogramované s využitím týchto príkazov. Program na vykreslenie zapojenia preto pozostáva z makier pre vykreslovanie komplikovanejších prvkov ako aj príkazov *dpic* pre kreslenie jednoduchých objektov.
```

Všeobecný formát pre definíciu grafických objektov v *dpic* má tvar

    [reference:] object [atribútes] [placement] [parameters] [string]
    
    reference  - označenie objektu pre prístup k jeho parametrom
    object     - grafický objekt (line, box ...)
    atribútes  - tvar objektu (šípky ...)
    placement  - umiestnenie objektu
    parameters - parametre zobrazenia (dotted, dashed ...)
    string     - text ktorý sa zobrazí v geometrickom strede objektu
    
    

## <font color='teal'> Čiary </font>

Definovanie čiary je  možné niekoľkými spôsobmi. V súradnicovej sústave môžeme zadať polohu absolútne dvojicou `(x,y)`. alebo  smerom kreslenia a dĺžkou relatívne voči poslednej polohe, ktorá je obsahom premennej `Here`. Pri prácu so súradnicami môžeme využívať vektorovú aritmetiku. Vykreslením čiary sa aktualizuje hodnota `Here` na polohu koncového bodu čiary. 

    [reference:] line [atribútes] [linespec] [string]
    
    attributes - <-|<->|-> vykreslenie šípky na konci čiary

    linespec   -  from position | to position | direction [ expr ]
                  | linespec linespec
                  | linespec then linespec
                  
    string     - text vykreslený v strede čiary


Príklad použitia

    L1: line -> from (1,1) to (2,2) "line L1" 
    
    L1:                 - referencia
    ->                  - atribút, šipka na konci čiary
    from (1,1) to (2,2) - placement, umiestnenie objektu na ploche
    "line L1"           - text v geometrickom strede objektu
                  
                  
Nasledujúce príklady ukazuje niekoľko možností použitia čiary.

    Origin: Here 
    line from (1,1) to (3,2); # A. absolutne polohy bodov, nastavuje 
                              #    poziciu Here na konc. bod 
    line from Here to (4,2);  # B. ciara od aktualnej pozicie
    line to (5,3);            # C. to iste od posledneho bodu
    line to Here + (0,1);     # D. relativne od poslednej pozicie 
    line left_ 2;             # E. relativne zadanim smeru v jednej osi
    line left_ 1 up_ 1;       # F. relativne v dvoch osiach

                              # G. zadanim postupnosti bodov
    line from (6,1) to (7,2) to (8,1) to (9,2); {"G" above};

                              # H. postupnostou relativnych krokov
    line -> from (6,5) right_ 1 then right_ 1 down_ 2 then right_ 1 up_ 1;


    
```{code-cell} ipython3  
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)
Origin: Here 

Grid(10,5.5);
line from (1,1) to (3,2); {"A" above};  # A. absolutne polohy bodov, nastavuje 
                                        #    poziciu Here na konc. bod 
line from Here to (4,2);  {"B" below};  # B. ciara od aktualnej pozicie
line to (5,3);            {"C" below};  # C. to iste od posledneho bodu
line to Here + (0,1);     {"D" ljust};  # D. relativne od poslednej pozicie 
line left_ 2;             {"E" above};  # E. relativne zadanim smeru v jednej osi
line left_ 1 up_ 1;       {"F" rjust};  # F. relativne v dvoch osiach

                                        # G. zadanim postupnosti bodov
line from (6,1) to (7,2) to (8,1) to (9,2); {"G" above};

                                        # H. postupnostou relativnych krokov
line -> from (6,5) right_ 1 then right_ 1 down_ 2 then right_ 1 up_ 1; {"H" above};
'''

_ = cm_compile('cm_0110a', data,  dpi=600)   
```

```{figure} ./src/cm_0110a.png
:width: 500px
:name: cm_0110a

[Spôsoby](./src/cm_0110a.ckt) vykreslenia čiary na pracovnej ploche.
```

```{admonition} Poznámka
Všimnite si v predchádzajúcom príklade, že relatívnu pozíciu môžeme zadať nielen v kolmých smeroch *right_*, *left_*, *up_*, *down_*

    line right_ 2;

ale aj ich kombináciu, ktorá vykreslí šikmú čiaru 

    line right_ 2 down_ 1;
```


## <font color='teal'> Krivky  </font>

Krivky môžeme kresliť rôznymi spôsobmi, pre krivky definované ako spline môžeme nastaviť parametrom tvar krivky (tension parameter). Čiary aj krivky môžeme modifikovať parametrami *dashed* a *dotted*, za ktorými môže nasledovať numerická hodnota udávajúca hustotu čiarok alebo bodiek, ich zobrazenie závisí od nastavenie parametrov kreslenia. 

    [reference:] spline [t] [atribútes] [linespec] 
    
    t          - napätie (tension) krivky v rozsahu 0...1 
    
    attributes - <-|<->|-> vykreslenie šípky na konci krivky

    linespec   -  from position | to position | direction [ expr ]
                  | linespec linespec
                  | linespec then linespec
                  
    
Pri krivkách nie je možné vykresliť v ich definícii text v ich strede ako pri čiare. Príklad použitia kriviek

    Grid(8.5,2.5);
    color_red;        # A. spline krivka, súradnic rovnake ako pri čiare
    spline from (0,1.5) right_ 1 up_ 1 then right_ 0.5 down_ 1 then \
           right_ 1 down_ 2 then up_ 3; "A" rjust below; 

                            
    color_blue;        # B. obojstranná šipka na krivke                       
    spline <-> from (5.5,0) to (6,2) to (7,0.5) to (8.5,2); "B" rjust above; 


    color_dark_green;  # C. Parameter tension
    spline 1.4 from (3, 0.) up_ 2 then right_ 2 then down_ 2 dashed .08;
    spline 1.0 from (3, 0.) up_ 2 then right_ 2 then down_ 2;
    spline 0.6 from (3, 0.) up_ 2 then right_ 2 then down_ 2 dotted .05;"C" rjust above;



```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)
Grid(8.5,2.5);
color_red;        # A. spline krivka, súradnic rovnake ako pri čiare
spline from (0,1.5) right_ 1 up_ 1 then right_ 0.5 down_ 1 then right_ 1 down_ 2 then up_ 3; "A" rjust below; 

                         
color_blue;        # B. obojstranná šipka na krivke                       
spline <-> from (5.5,0) to (6,2) to (7,0.5) to (8.5,2); "B" rjust above; 


color_dark_green;  # C. Parameter tension
spline 1.4 from (3, 0.) up_ 2 then right_ 2 then down_ 2 dashed .08;
spline 1.0 from (3, 0.) up_ 2 then right_ 2 then down_ 2;
spline 0.6 from (3, 0.) up_ 2 then right_ 2 then down_ 2 dotted .05;"C" rjust above;
'''

_ = cm_compile('cm_0110b', data, dpi=600)   
```


```{figure} ./src/cm_0110b.png
:width: 500px
:name: cm_0110b

Použitie splajnových kriviek.
```


### <font color='brown'> Atribúty lineárnych prvkov  </font>

Pre čiaru a splajnovú krivku sú definované štandardné atribúty, ku ktorým sa pristupuje referenciou na objekt a operátorom `.`


    .start    .s          - bod v ktorom bol začiatok kreslenia
    .end      .e          - bod v ktorom skončilo kreslenie
    .center   .c          - geometrický stred prvku
    
Každý atribút reprezentuje súradnicu v tvare dvojice hodnôt (x,y). Príklad použitia atribútov

    L: line to (1,1);
    
    L.center    - je ekvivalentom  (L.center.x, L.center.y)  
                  alebo (L.c.x, L.c.y)
    
    (L.s, L.e)  - je ekvivalentom (L.s.x, L.e.y)

    
## <font color='teal'> Plošné objekty </font>

Definícia plošných objektov, obdĺžnik, kružnica a elipsa, má v `dpic` tvar

    [reference:] box [at pos] [wid x] [ht y] [parameters] [string]
    [reference:] circle [at pos] [rad r] [parameters] [string]
    [reference:] ellipse [at pos] [wid x] [ht y] [parameters] [string]
    
    at pos     - poloha stredu objektu
    wid        - šírka
    ht         - výška
    rad        - polomer
    parameters - parametre zobrazenia (fill ...)
    string     - text v strede objektu
    
Pri zadaní príkazu vykreslenia objektu tento zadáme len menom bez parametrov, objekt sa vykreslí s prednastavenými (default) hodnotami. Podobne ako pri čiarach je možné upraviť zobrazenie okraja objektov parametrami *dashed* a *dotted* a výplň parametrom *fill*. Zaoblenie rohov pri obdĺžniku je možné upraviť premennou *boxrad*. 

       color_red;      
    A: box wid 1 ht 1 at (1,0.5) "A"; line -> right_ 1;
    
       color_blue; boxrad = 0.15; 
    B: box wid 1 ht 1 dashed "B";
    
       color_dark_green;  line <-> up_ 1 from A.n;
    C: box wid 1 ht 1 fill 0.9 "C";
    
       color_dark_cyan; line -> from last box.e right_ 1
    D: circle rad 0.5 "D";
    Y: (0.5 between D and B) + (2,0)

       color_coral;
    E: ellipse at Y wid 2 ht 1 "E"
       line -> from D.e to (E.n, D.e) to E.n;
       line -> from B.e to (E.s, B.e) to E.s;

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
    include(lib_color.ckt);
color_red;      
A: box wid 1 ht 1 at (1,0.5) "A"; line -> right_ 1;
   color_blue; boxrad = 0.15; 
B: box wid 1 ht 1 dashed "B";
   color_dark_green;  line <-> up_ 1 from A.n;
C: box wid 1 ht 1 fill 0.9 "C";
   color_dark_cyan; line -> from last box.e right_ 1
D: circle rad 0.5 "D";
Y: (0.5 between D and B) + (2,0)
   color_coral;
E: ellipse at Y wid 2 ht 1 "E"
   line -> from D.e to (E.n, D.e) to E.n;
   line -> from B.e to (E.s, B.e) to E.s;
'''

_ = cm_compile('cm_0110f', data, dpi=600)   
```

```{figure} ./src/cm_0110f.png
:width: 380px
:name: cm_0110f

Plošné objekty.
```
       
### <font color='brown'> Atribúty plošných prvkov  </font>    

Pri obryse plošných objektov sú atribúty definované podľa svetových strán.

    .ne       .se     .nw       .sw
    .t        .top              .north   .n
    .b        .bot    .bottom   .south   .s
    .right    .r                .east    .e
    .left     .l                .west    .w
    .start
    .end
    .center                     .centre  .c


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
Origin: Here 

B: box wid 4 ht 2 

move to B.west;   "B.w"  rjust;    # rovnako ako B.w
move to B.c;      "B.c";    
move to B.e;      "B.e"  ljust;   
move to B.n;      "B.n"  above; 
move to B.s;      "B.s"  below;

move to B.ne;     "B.ne"  above ljust; 
move to B.nw;     "B.nw"  above rjust; 

move to B.se;     "B.se"  below ljust; 
move to B.sw;     "B.sw"  below rjust; 
'''

_ = cm_compile('cm_0110c', data, dpi=600)   
```

```{figure} ./src/cm_0110c.png
:width: 300px
:name: cm_0110c

Atribúty pre box, orientácia podľa svetových strán
```

## <font color='teal'> Kruhový oblúk </font>

Kruhový oblúk je objekt, ktorý zdiela atribútu lineárnych ako aj plošných objektov. Oblúk je definovaný smerom a pomocou dvoch alebo troch bodov

    arc  [atribútes] cw|ccw from position to position [with .c at centre]
    
    atribútes - <-|<->|-> vykreslenie šípky na konci oblúka
    cw|ccw    - smer oblúka
    position  - súradnice počiatočného a koncového bodu oblúka
    centre    - súradnice stredu kružnice oblúka
    
Bez zadaného stredu je oblúk vykreslený ako polkružnica so stredom medzi koncovými bodmi oblúka.


    P1: (1, 1);
    P2: (4, 4);
    P3: (3.5, 1.5)
                                        # označenie
        circle rad 0.1 at P1;           # zaciatok
        circle rad 0.1 at P2;           # koniec
        rad 0.1 at P3;                  # stred A2
        
        color_red;
    A1: arc cw from P1 to P2            # obluk A1 bez zadaného stredu
        "A1" at A1.nw above rjust;
    L1: line from P1 to P2 dashed; 
        circle rad 0.1 at L1.c;         # stred A1
        
        color_blue
    A2: arc -> cw from P1 to P2 with .c at P3
        line from P1 to P3 dashed;
        line from P2 to P3 dashed;
        "A2" at A2.nw above rjust;

    
```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)
Origin: Here 

Grid(5, 5);

P1: (1, 1);
P2: (4, 4);
P3: (3.5, 1.5)

circle rad 0.1 at P1;
circle rad 0.1 at P2;
circle rad 0.1 at P3;

color_red;
A1: arc cw from P1 to P2 
"A1" at A1.nw above rjust;
L1: line from P1 to P2 dashed; 
circle rad 0.1 at L1.c;
color_blue
A2: arc -> cw from P1 to P2 with .c at P3
line from P1 to P3 dashed;
line from P2 to P3 dashed;
"A2" at A2.nw above rjust;

'''

_ = cm_compile('cm_0110d', data, dpi=600)   
```

```{figure} ./src/cm_0110d.png
:width: 300px
:name: cm_0110d

[Vykreslenie](./src/cm_0110d.ckt) kruhového oblúku
```

## <font color='teal'> Šípky </font>

Ako je uvedené v defínícii čiar a kriviek, na ich  koncoch môžeme v prípade potreby vykresliť šípku doplnením atribútov  *<-*, *<->*, *->* alebo príkazom *arrow*, ktorý umožňuje nastavenie parametrov šíky 

    [reference:] arrow [atribútes] [linespec] [parameters]
    
    attributes - <-|<->|-> vykreslenie šípky na konci čiary

    linespec   -  from position | to position | direction [ expr ]
                  | linespec linespec
                  | linespec then linespec
                  
    parameters - tvar a veľkosť šípky
                 thick  - hrúbka čiary (0.8)
                 ht     - výška šípky  (0.1)
                 wid    - šírka šípky  (0.05)
 
Príklady použitia 

    include(lib_color.ckt);
    include(lib_base.ckt);

    Grid(8.5,2.5);
    color_red;
    arrow -> from (0,0) to (1.5,1.5) thick 2 ht 0.5 wid 0.5
    color_blue;
    arrow from (2,0.5) right_ 2;    {"A" ljust};  # šipka v smere kreslenia      
    arrow <- from (2,1) right_ 2;   {"B" ljust};  # sipka smerom dolava
    line <-> from (2,1.5) right_ 2; {"C" ljust};  # obojsmerna sipka 

    color_dark_cyan;                              # šipka v obluku 
    arc -> cw from (5,0.5) to (8,0.5) thick 1.5 wid 0.25 dashed "D";

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
    include(lib_color.ckt);
    include(lib_base.ckt);

    Grid(8.5,2.5);
    color_red;
    arrow -> from (0,0) to (1.5,1.5) thick 2 ht 0.5 wid 0.5
    color_blue;
    arrow from (2,0.5) right_ 2;    {"A" ljust};  # K. obojsmerna šipka      
    arrow <- from (2,1) right_ 2;   {"B" ljust};  # L. sipka smerom dolava
    line <-> from (2,1.5) right_ 2; {"C" ljust};  # M. obojsmerna sipka 

    color_dark_cyan;                              # sipka v obluku 
    arc -> cw from (5,0.5) to (8,0.5) thick 1.5 wid 0.25 dashed "D";
'''

_ = cm_compile('cm_0110e', data, dpi=600)   
```

```{figure} ./src/cm_0110e.png
:width: 500px
:name: cm_0110e

Vykreslenie šípiek.
```
