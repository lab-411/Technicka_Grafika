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
# <font color='navy'> Parametrické komponenty </font>

V Circuit-Macros je možné vlastnosti niektorých komponentov definovať pomocou parametrov, zvyčajne u komponentov, ktoré obsahujú opakujúce sa časti, napríklad konektory, vstupy logických hradiel a pod.

```{code-cell} ipython3 
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 
d = 2;

log_init;         # inicializacia makier pre logicke obvody

move to (3,1);
up_; 
H1: Header(2, 6,,,fill_(0.9)); 
"Konektor" at H1.w rjust;
"1" at H1.P1 rjust;
"2" at H1.P2 rjust;
"11" at H1.P11 ljust;
"12" at H1.P12 ljust;

line from H1.P1 down_ d/4 then right_ 2*d;
line from H1.P2 up_ d/4 then right_ 2*d;

move to (3, 4);
right_; G1: NAND_gate(4); 

line from G1.In1 left_ d/2;
line from G1.In2 left_ d/2;
line from G1.In3 left_ d/2;
line from G1.In4 left_ d/2;
line from G1.Out right_ d/2;
'''

_ = cm_compile('./src/cm_0240a', data, dpi=600)   
```

```{figure} ./src/cm_0240a.png
:width: 300px
:name: cm_020

Parametrické komponenty
```

Pri parametrických komponentoch môžeme použiť dynamické vytváranie mien atribútov v textovom reťazci obsahujúcom príkaz. Reťazec môžeme vytvoriť parametricky pomocou funkcie *sprintf()*. Textový reťazec vykonáme pomocou príkazu *exec*. 

```{code-cell} ipython3 
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

Origin: Here 
d = 2;
log_init;         
move to (5,1);
right_; 
G2: NAND_gate(8);

for i=1 to 8 do { 
    exec sprintf("line from G2.In%g left_ d",i); 
}

line from G2.Out right_ d/2;
'''

_ = cm_compile('./src/cm_0240b', data, dpi=600)   
```

```{figure} ./src/cm_0240b.png
:width: 180px
:name: cm_021

Logický parametrický komponent
```


