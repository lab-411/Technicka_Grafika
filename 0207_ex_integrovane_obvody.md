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


# <font color='navy'> Integrované obvody </font> 

Integrované obvody sú prvky elektronických obvodov, ktorých zobrazenie v technickej dokumentácii závidí od kontextu ich použitia. V katalogových listoch sa vyskytuje ich zobrazenie z pohľadu zapojenia ich terminálov, čo je dôležité pri návrhu plošných spojov. Pri kreslení zapojení je obvyklé používať blokovú značku obvodu a orientovať vývody obvodov podľa ich významu, zvyčajne vstupy vľavo a výstupy vpravo. V niektorých prípadoch môže byť bloková značka v dokumentácii doplnená o vnútorné zapojenie integrovaného obvodu. Nasledujúci príklad ukazuje zobrazenia integrovaného obvodu 555, makkrá pre značky sú implementované v knižnici [lib_ic555,ckt](./src/lib_ic555.ckt).  


```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
cct_init
log_init

include(lib_base.ckt)
include(lib_user.ckt)
include(lib_ic555.ckt)

command "\sf"

IC1: IC555_1 at (2,6.5); "555" at IC1.BX.n above;
IC2: IC555_2 at (7,6.5);
IC3: IC555_3 at (5,1);
'''

_ = cm_compile('./src/cm_0207a', data, dpi=600 )   
```

```{figure} ./src/cm_0207a.png
:width: 400px
:name: cm_0207a

Rôzne spôsoby [zobrazenia](./src/cm_0207a.ckt) integrovaného obvodu. 
```

Pri vytváraní značiek integrovaných obvodov môžeme využívať makrá

    lg_pin(location, label, Picname, n|e|s|w[L|M|I|O][N][E], pinno, optlen)
    lg_bartxt()
    
    lg_plen
    lg_pinsep


    
```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
cct_init
log_init
include(lib_base.ckt)
include(lib_color.ckt)
include(lib_ic555.ckt)
command "\sf"

IC: IC555_2;
    line from IC.Pin7 left 1;
    dot;
    {R1: resistor(up_ 1.5,,E); llabel(,\sf R_1,); DT1: dot; }
     R2: resistor(down_ 1.5,,E); rlabel(,\sf R_2,); DT2: dot;
     C1: capacitor(1,); rlabel(,\sf C,); gnd();

     
     move to IC.Pin5; C2: capacitor(0.75,); llabel(,\sf 10nF,); gnd();
     move to IC.Pin1; gnd(0.5);
'''

_ = cm_compile('./src/cm_0207b', data, dpi=600 )   
```

```{figure} ./src/cm_0207b.png
:width: 400px
:name: cm_0207b

Rôzne spôsoby [zobrazenia](./src/cm_0207a.ckt) integrovaného obvodu. 
```
