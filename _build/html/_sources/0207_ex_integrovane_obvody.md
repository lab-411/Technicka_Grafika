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

Integrované obvody sú prvky elektronických obvodov, ktorých zobrazenie v technickej dokumentácii závidí od kontextu ich použitia. V katalogových listoch sa vyskytuje ich zobrazenie z pohľadu zapojenia ich terminálov, čo je dôležité pri návrhu plošných spojov, pri kreslení zapojení je zase zvykom orintovať vývody obvodov podľa ich významu, zvyčajne vstupy vľavo a výstupy vpravo.

```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
    cct_init
log_init

command "\sf"

define(`IC555_1', `[
  BX: box wid 2 ht 5*lg_pinsep;
      linethick_(3);
      lg_pin(BX.nw - (0, lg_pinsep),   GND, Pin1, w, 1)
      lg_pin(BX.nw - (0, 2*lg_pinsep), TRIG, Pin2, w, 2)
      lg_pin(BX.nw - (0, 3*lg_pinsep), OUT, Pin3, w, 3)
      lg_pin(BX.nw - (0, 4*lg_pinsep), lg_bartxt(RESET), Pin4, w, 4)

      lg_pin(BX.ne - (0, lg_pinsep), Vcc, Pin8, e, 8)
      lg_pin(BX.ne - (0, 2*lg_pinsep), DIS, Pin7, e, 7)
      lg_pin(BX.ne - (0, 3*lg_pinsep), THR, Pin6, e, 6)
      lg_pin(BX.ne - (0, 4*lg_pinsep), CTRL, Pin5, e, 5)
      linethick_();
      arc ccw from BX.n-(.2,0) to BX.n+(0.2,0) with .c at BX.n
]')

define(`IC555_2', `[
  BX: box wid 2 ht 6*lg_pinsep;
      lg_pin(BX.nw - (0, 2*lg_pinsep), DIS, Pin7, w, 7)
      lg_pin(BX.nw - (0, 3*lg_pinsep), THR, Pin6, w, 6)
      lg_pin(BX.nw - (0, 4*lg_pinsep), TRIG, Pin2, w, 2)

      lg_pin(BX.sw + (1.5*lg_pinsep, 0),   GND, Pin1, s, 1)
      lg_pin(BX.sw + (3.5*lg_pinsep, 0),  CTRL, Pin5, s, 5)

      lg_pin(BX.nw + (1.5*lg_pinsep, 0), lg_bartxt(RESET), Pin4, n, 4)
      lg_pin(BX.nw + (3.5*lg_pinsep, 0), Vcc, Pin8, n, 8)

      lg_pin(BX.ne - (0, 3*lg_pinsep), OUT, Pin3, e, 3)

]')


IC1: IC555_1 at (2,2); "555" at IC1.BX.n above;
IC2: IC555_2 at (6,2);
'''

_ = cm_compile('./img/ic_001', data, dpi=600 )   
```

```{figure} ./img/ic_001.png
:width: 400px
:name: ic_001

[Symbol](./img/ic_001.ckt) integrovaného obvodu. 
```


