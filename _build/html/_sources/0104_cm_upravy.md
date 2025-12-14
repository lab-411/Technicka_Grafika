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

## <font color='teal'>  Zmena farby  </font>

Pre zmenu farby kreslenie je definované makro *setrgb(r, g, b)*, ktorého argumentami sú RGB zložky farby. Pre jednoduchšiu zmenu farby kreslenia je možné použiť makrá pre pomenované farby *color_<meno farby>* zo súboru [lib_color.ckt](./src/lib_color.ckt). Zmena farby sa vzťahuje na všetky nasledujúce kreslené objekty vrátane farby textu, návrat k pôvodnej farbe (čiernej) je pomocou makra *color_reset*.  

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


## <font color='teal'>  Zvýraznenie prvku </font>

Zvýraznene prvku v zapojení dosiahneme zmenou šírky čiary, táto je určená makrom  *linethick_(n)*, volanie makra bez argumentu nastaví pôvodnú hrúbku. Zmena hrúbky čiary neovplyvňuje zobrazenie textov.

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
    

## <font color='teal'>  Zmena veľkosti prvkov   </font>

Veľkosť prvkov zapojenia je úmerná hodnote premennej *linewid*, ktorá je definovaná v nastavení parametrov prostredia a je možné ju v programe meniť. Zmena veľkosti prvkov neovplyvňuje veľkosť textu.

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

## <font color='teal'> Tienenie prvkov </font>

Pre doplnenie tienenia k prvku zapojenie použijeme obdĺžnik, ktorý umiestnime do stredu prvku a jeho rozmery odvodíme od premennej *elen_*, ktorá definuje veľkosť prvku.

    right_; 
    resistor(2,,E); llabel(,R_1,); 

    SH:[                                               # blok
         RR:resistor(2,,ES);
            llabel(,R_2,); rlabel(,470 \Omega / 5 W,); # vnutorny popis  
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






