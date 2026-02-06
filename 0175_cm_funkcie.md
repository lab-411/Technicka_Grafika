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
# <font color='navy'> Funkcie  </font>

Programovací jazyk `dpic` neumožňuje vytváranie nových uživateľských funkcií, sú v ňom ale definované základné matematické funkcie. 


## <font color='teal'> Trigonometrické funkcie </font>

Argumenty trigonometrických funkcií sú v radiánoch:

    sin(<expr>)
    cos(<expr>)
    acos(<expr>)
    asin(<expr>)
    atan2(<expr>, <expr>)
    tan(<expr>)

## <font color='teal'> Logaritmické a exponenciálne funcie </font>
 
    exp(<expr>)
    log(<expr>)
    expe(<expr>)
    loge(<expr>)

## <font color='teal'> Numerické funkcie </font>
    
    sqrt(<expr>)
    max(<expr>, <expr>...)
    min(<expr>, <expr>...)
    int(<expr>)
    rand(<expr>)
    abs(<expr>)
    floor(<expr>)
    sign(<expr>)
    pmod(<expr>)

    
## <font color='teal'> Príklady </font>

Nasledujúce príklady ukazujú použitie funkcií pri vykreslovaní jednoduchej grafiky,  {numref}`cm_0175a`
 a  {numref}`cm_0175b`.

    Grid(3,3);
        right_;
        r = 1.5;
        move to (0,r);
    C1: circle diam 2*r;
        color_red;
        alpha = pi_ / 4;     # uhol v radianoch
        line from C1.c to C1.c + (cos(alpha), sin(alpha))*r;
    D1: dot;


```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *
data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

Origin: Here 
Grid(3,3);
    right_;
    r = 1.5;
    move to (0,r);
C1: circle diam 2*r;
    color_red;
    alpha = pi_ / 4;     # uhol v radianoch
    line from C1.c to C1.c + (cos(alpha), sin(alpha))*r;
D1: dot;
'''

_ = cm_compile('cm_0175a', data, dpi=600)   
```

```{figure} ./src/cm_0175a.png
:width: 200px
:name: cm_0175a

[Zobrazenie](./src/cm_0175a.ckt) sprievodiča a bodu na kružnici.
```

    PP:(0,0)
    for x=0 to 3.14*2 by (3.14/100) do {
        r1 = 2;
        px = cos(x);
        py = sin(2*x);

        r2 = 4;
        dx = r2*cos(1*x)/2 + 2;
        dy = r2*sin(3*x)/3 + 1;

        line from PP + (dx,dy)*r1 to PP + (px,py)*r2; 
    }


```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *
data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

Origin: Here 
PP:(0,0)
for x=0 to 3.14*2 by (3.14/100) do{
   r1 = 2;
   px = cos(x)
   py = sin(2*x)

   r2 = 4;
   dx = cos(1*x)
   dy = sin(3*x)

   line from PP + ((dx,dy)*r2 + (1,2))  to PP + (px,py)*r1 
}
'''

_ = cm_compile('cm_0175b', data, dpi=600)   
```

```{figure} ./src/cm_0175b.png
:width: 300px
:name: cm_0175b

[Vykreslenie](./src/cm_0175b.ckt) jednoduchej grafiky
```

