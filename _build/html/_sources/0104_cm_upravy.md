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


    
# <font color='navy'> Úpravy zobrazenia </font>

Súčasťou `CircuitMacros` sú makrá a premenné, pomocou ktorých môžeme upravovať zobrazenie prvkov v zapojení. Môžeme hrubšími čiarami zvýrazniť kritickú časť obvodu, farebne oddeliť a zvýrazniť popis obvodov, popis prvkov alebo upozorniť na konštrukčné detaily.

## <font color='teal'>  Zmena farby  </font>

Pre zmenu farby kreslenie je definované makro *setrgb(r, g, b)*, ktorého argumentami sú RGB zložky farby. Pre jednoduchšiu zmenu farby kreslenia je možné použiť makrá pre pomenované farby *color_<meno farby>* zo súboru [lib_color.ckt](./src/lib_color.ckt), popis fabieb je uvedený v prílohe **Farby**. Zmena farby sa vzťahuje na všetky nasledujúce kreslené objekty vrátane farby textu, návrat k pôvodnej farbe (čiernej) je pomocou makra *color_reset*.  

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

[Použitie](./src/cm_0104a.ckt) pomenovaných farieb 
```


## <font color='teal'>  Zvýraznenie prvku </font>

Zvýraznene prvku v zapojení dosiahneme zmenou šírky čiary, táto je určená makrom   *linethick_(n)* . Hodnota argumentu $n=1$ zodpovedá štandardnej šírke čiary. Zmena hrúbky čiary neovplyvňuje zobrazenie textov.


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
Origin: Here 

move to (0,1)
linethick_(1);
resistor(,,E); llabel(,R_1,);   "\textit{lin\\ethick\_(1); res\\istor(,,E)};" ljust;

move to (0,2)
linethick_(1.5);
R2:resistor(,,E); llabel(, R_2,); "\textit{lin\\ethick\_(1.5); res\\istor(,,E)};" ljust; 
'''

_ = cm_compile('cm_0104b', data,  dpi=600)   
```

```{figure} ./src/cm_0104b.png
:width: 400px
:name: cm_0104b

[Zvýraznenie](./src/cm_0104b.ckt) komponentu.
```
    

## <font color='teal'>  Zmena veľkosti prvkov   </font>

Štandardná velkosť komponentov je určená hodnotou parametra *linewid*. Default hodnota parametra je 2.54 / 2 a je možné ju v programe meniť. Zmena veľkosti prvkov neovplyvňuje veľkosť textu.

    resistor(2,,E); llabel(,R_1,); dot;

    linewid = 2.0                      # zmena velkosti komponentu
    R1: resistor(3,,ES); llabel(,R_2,); rlabel(,470 \Omega / 5 W,)

    dot;                               # zvecseny bod
    linewid = 2.54/2                   # uprava rozmerov na standardnu velkost
    resistor(d,,E);llabel(,R_3,);      # štandardny rozmer


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
Origin: Here 

d = 2; 
resistor(2,,E); llabel(,R_1,); dot;

linewid = 2.0                      # zmena velkosti komponentu
R1: resistor(3,,ES); llabel(,R_2,); rlabel(,470 \Omega / 5 W,)

dot;                               # zvecseny bod
linewid = 2.54/2                   # uprava rozmerov na standardnu velkost
resistor(d,,E);llabel(,R_3,);      # štandardny rozmer
'''

_ = cm_compile('cm_0104c', data,  dpi=600)   
```

```{figure} ./src/cm_0104c.png
:width: 400px
:name: cm_0104c

[Zmena](./src/cm_0104c.ckt) veľkosti komponentov
```





