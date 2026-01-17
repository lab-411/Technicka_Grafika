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


    
# <font color='navy'> Úpravy </font>

Súčasťou `CircuitMacros` sú makrá a premenné, pomocou ktorých môžeme upravovať zobrazenie prvkov v zapojení. Môžeme hrubšími čiarami zvýrazniť kritickú časť obvodu, farebne oddeliť a zvýrazniť popis obvodov, popis prvkov alebo upozorniť na konštrukčné detaily.

## <font color='teal'> Farba  </font>

Pre zmenu farby kreslenie je definované makro *setrgb(r, g, b)*, ktorého argumentami sú RGB zložky farby. Pre jednoduchšiu zmenu farby kreslenia je možné použiť makrá pre pomenované farby *color_<meno farby>* zo súboru [lib_color.ckt](./src/lib_color.ckt). Zmena farby sa vzťahuje na všetky nasledujúce kreslené objekty vrátane farby textu, návrat k pôvodnej farbe (čiernej) je pomocou makra *color_reset*, {numref}`cm_0104a`.  

    include(lib_color.ckt)

    resistor(2,,E); 
    color_blue; llabel(,R_1,); 
    
    color_reset;
    dot; 
    {  resistor(down_ 1.5,,E); rlabel(,R_3,);  }

    color_red;
    capacitor(right_ 1.5,,E); llabel(,C_1,); rlabel(,10 \mu F,);
    
    resistor(right_ 2,,ES); 
    color_reset; 
    llabel(,R_4,); rlabel(,10 \Omega,);

    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_color.ckt)

resistor(2,,E); 
color_blue; llabel(,R_1,); color_reset;
dot; 
{ resistor(down_ 1.5,,E); rlabel(,R_3,);}

color_red;
capacitor(right_ 1.5,,E); llabel(,C_1,); rlabel(,10 \mu F,);
resistor(right_ 1.5,,ES); 
color_reset; 
llabel(,R_4,); rlabel(,10 \Omega,);
'''

_ = cm_compile('cm_0104a', data,  dpi=600)   
```

```{figure} ./src/cm_0104a.png
:width: 300px
:name: cm_0104a

Použitie pomenovaných farieb 
```


## <font color='teal'> Zvýraznenie </font>

Zvýraznene prvku v zapojení dosiahneme zmenou šírky čiary, táto je určená makrom  *linethick_(n)*, volanie makra bez argumentu nastaví pôvodnú hrúbku. Zmena hrúbky čiary neovplyvňuje zobrazenie textov, {numref}`cm_0104b`.

       right_; 
       resistor(2,,E); llabel(,R_1,); 
    R2:[ linethick_(1.2);         # lokálna zmena hrubky čiary
          resistor(2,,ES);
       ]
       llabel(,R_2,); rlabel(,470 \Omega / 5 W,);
       linethick_();
       resistor(2,,E); llabel(,R_3,);



```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
right_; 
resistor(2,,E); llabel(,R_1,); 
R2: [ linethick_(1.2); 
      resistor(2,,ES);
    ]
    llabel(,R_2,); rlabel(,470 \Omega / 5 W,);
resistor(2,,E); llabel(,R_3,);
'''

_ = cm_compile('cm_0104b', data,  dpi=600)   
```

```{figure} ./src/cm_0104b.png
:width: 400px
:name: cm_0104b

Zvýraznenie komponentu zmenou hrúbky čiary.
```
    

## <font color='teal'> Zmena veľkosti  </font>

Veľkosť prvkov zapojenia je úmerná hodnote premennej *linewid*, ktorá je definovaná v nastavení parametrov prostredia a je možné ju v programe meniť. Zmena veľkosti prvkov neovplyvňuje veľkosť textu, {numref}`cm_0104c`.

       right_; 
       resistor(2,,E); llabel(,R_1,);    # štandardná veľkosť
    R2:[ linewid = linewid*1.5;      # lokálna zmena velkosti v bloku  
          resistor(2,,ES);
       ]
       llabel(,R_2,); rlabel(,470 \Omega / 5 W,);
       resistor(2,,E); llabel(,R_3,);    # štandardná veľkosť


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
right_; 
resistor(2,,E); llabel(,R_1,); 

R2: [ linewid = linewid*1.5; 
      resistor(2,,ES);
    ]
    llabel(,R_2,); rlabel(,470 \Omega / 5 W,);

resistor(2,,E); llabel(,R_3,); 
'''

_ = cm_compile('cm_0104c', data,  dpi=600)   
```

```{figure} ./src/cm_0104c.png
:width: 400px
:name: cm_0104c

Zmena veľkosti komponentov pomocou premennej *linewid*.
```

## <font color='teal'> Tienenie </font>

Pre doplnenie tienenia k prvku zapojenie použijeme obdĺžnik, ktorý umiestnime do stredu prvku a jeho rozmery odvodíme od premennej *elen_*, ktorá definuje veľkosť prvku, {numref}`cm_0104d`.

    right_; 
    resistor(2,,E); llabel(,R_1,); 

    SH:[                                               # blok
         RR:resistor(2,,ES);
            llabel(,R_2,); rlabel(,470 \Omega / 5 W,); # vnutorny popis  
            boxrad=0.1;                                # tienenie
            box wid elen_ ht elen_*4/5 at RR.center dashed;
        ]
        llabel(,Shield,);                              # vonkajsi popis 
        { dot(at SH.s); ground;}                       # pripojenie tienenia

        resistor(2,,E); llabel(,R_3,);


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
    right_; 
    resistor(2,,E); llabel(,R_1,); 

    SH:[  
         RR:resistor(2,,ES);
            llabel(,R_2,); rlabel(,470 \Omega / 5 W,);
            boxrad=0.1;
            box wid elen_ ht elen_*4/5 at RR.center dashed;
        ]
        llabel(,Shield,);  
        { dot(at SH.s); ground;}

        resistor(2,,E); llabel(,R_3,); 
'''

_ = cm_compile('cm_0104d', data,  dpi=600)   
```

```{figure} ./src/cm_0104d.png
:width: 400px
:name: cm_0104d

Tienenie prvku zapojenia.
```


## <font color='teal'> Pozadie </font>

Ak potrebujeme zvýrazniť plochu na ktorej je nakreslená časť zariadenia (napríklad na vizuálne oddelenie samostatných funkčných celkov ako je predzosilovač, filter, ochranné obvody a pod.), musíme podklad nakresliť vopred. V prípade jedného prvku odvodíme rozmery plochy priamo z predefinovaných parametrov prostredia, {numref}`cm_0104e`.

    include(lib_color.ckt);
    right_; 
    resistor(2,,E); llabel(,R_1,); 

    [  
      color_grey;
      boxrad=0.1
      box wid elen_ ht elen_*4/5 fill 0.95 ;
      color_reset;
      resistor(from last box.w to last box.e,, ES);
      llabel(,R_2,); rlabel(,470 \Omega / 5 W,);
    ]
    resistor(2,,E); llabel(,R_3,);


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_color.ckt);
right_; 
resistor(2,,E); llabel(,R_1,); 

[  
      color_grey;
      boxrad=0.1
      box wid elen_ ht elen_*4/5 fill 0.95 ;
      color_reset;
      resistor(from last box.w to last box.e,, ES);
      llabel(,R_2,); rlabel(,470 \Omega / 5 W,);

]
resistor(2,,E); llabel(,R_3,);
'''

_ = cm_compile('cm_0104e', data,  dpi=600)   
```

```{figure} ./src/cm_0104e.png
:width: 400px
:name: cm_0104e

Zvýraznenie pozadia jedného prvku zapojenia.
```


V prípade väčších obvodov je vhodné si určiť veľkosť zvýraznenej plochy a na jej obvode si zadefinovať body pripojenia, {numref}`cm_0104f`. Zapojenie potom nakreslíme na zvýraznenú plochu ako zložený objekt s vlastnosťami plošného prvku.
 
    d  = elen_*5/6;    # veľkosť prvkov
    dx = 2*d;          # šírka plochu
    dy = 2*d*4/5;      # výška plochy

    FL:[  
        color_grey;
        boxrad=0.1
    BX: box wid dx ht dy fill 0.95 ;
    IN1:BX.w + (0,d/2); IN2: BX.w + (0,-d/2);    # súradnice bodov na obvode 
    OU1:BX.e + (0,d/2); OU2: BX.e + (0,-d/2 );
        color_reset;

        line from IN1 right_ d/2;                # zapojenie na ploche
        dot; {inductor(down_ d,W); rlabel(,L,); DD1:dot;}
        capacitor(right_ d); rlabel(,C,);
        dot; {inductor(down_ d,W); llabel(,L,); DD2:dot;}
        line  to OU1;
        line from IN2 to DD1 then to DD2 then to OU2;
    ]
                                                 # vonkajšie obvody
    resistor(from FL.IN1 left_ d,,E); rlabel(,R_g,);
    AC:source(down_ d); {rlabel(,V_g,); ACsymbol(at AC,,, L);}
    line to FL.IN2;

    line from FL.OU1 right_ 1;
    resistor(down_ d,,E); llabel(,R_z,);
    line to FL.OU2;

    "LC Filter" at FL.n above;


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_color.ckt);

d  = elen_*5/6; 
dx = 2*d; 
dy = 2*d*4/5; 

FL:[  
          color_grey;
          boxrad=0.1
      BX: box wid dx ht dy fill 0.95 ;
      IN1:BX.w + (0,d/2); IN2: BX.w + (0,-d/2);
      OU1:BX.e + (0,d/2); OU2: BX.e + (0,-d/2 );
          color_reset;

          line from IN1 right_ d/2; 
          dot; {inductor(down_ d,W); rlabel(,L,); DD1:dot;}
          capacitor(right_ d); rlabel(,C,);
          dot; {inductor(down_ d,W); llabel(,L,); DD2:dot;}
          line  to OU1;
          line from IN2 to DD1 then to DD2 then to OU2;
   ]

   resistor(from FL.IN1 left_ d,,E); rlabel(,R_g,);
   AC:source(down_ d); {rlabel(,V_g,); ACsymbol(at AC,,, L);}
   line to FL.IN2;

   line from FL.OU1 right_ 1;
   resistor(down_ d,,E); llabel(,R_z,);
   line to FL.OU2;

   "LC Filter" at FL.n above;

color_red; 
line <- from FL.IN1+(-0.1, 0.1) left_ 3/4 up_ 3/4; "IN1" at last line .end above
line <- from FL.OU1+( 0.1, 0.1) right_ 3/4 up_ 3/4; "OU1" at last line .end above
line <- from FL.IN2+(-0.1, -0.1) left_ 3/4 down_ 3/4; "IN2" at last line .end below
line <- from FL.OU2+( 0.1, -0.1) right_ 3/4 down_ 3/4; "OU2" at last line .end below
'''

_ = cm_compile('cm_0104f', data,  dpi=600)   
```

```{figure} ./src/cm_0104f.png
:width: 450px
:name: cm_0104f

Zvýraznená časť zapojenia obvodu.
```
 
