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
# <font color='navy'> Vetvy a bloky</font>

Pri kreslení elektrických zapojení sa často vyskytuje situácia, v ktorej potrebujeme nakresliť samostatnú časť obvodu (vetvu) a potom pokračovať v kreslení zapojenia od pôvodnej pozície. V štandardnej situácii by sme si museli označiť vhodný prvok schémy, zvyčajne spojovací bod, referenciou a po nakreslení vetvu sa na pôvodnú pozíciu vrátiť pomocou povelu *move to ...*.

## <font color='teal'> Vetvy</font>

V `CircuitMacros` je vetva tvorená kódom uzatvoreným do zložených zátvoriek `{...}`. Vetva umožňuje vytváranie časti obvodu alebo umiestnenie iných komponentov relatívne k poslednej hodnote `Here`, vo vetve sa vytvorí lokálna kópia `Here`. Rovnako vetva nemení ani pôvodný smer ukladania prvkov. Vetvy je možné do seba vnárať. 

    Origin: Here 
    d = 2;
    move to (0.5, 3);
    resistor(right_ d,E); llabel(,R1,);
    dot;                                  # aktualna poloha Here     
    
    {   # vetva smerom down_ od Here
        resistor(down_ d, E);    llabel(,R2,);
        gnd;
    }
                                          
    {   # vetva smerom up_ od Here
        resistor(up_ d,E);  rlabel(,R3,);
        P: power(); "Power" at P.n above;
        
    }
    
    # pokračovanie kreslenia v pôvodnom smere od Here
    resistor(right_ d,E);        llabel(,R4,);
    dot;
    capacitor(); llabel(,C_1,)


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

Origin: Here 
d = 2;
move to (0.5, 3);
resistor(right_ d,E);        llabel(,R1,);
dot;

color_blue;
{ 
    resistor(down_ d, E);    llabel(,R2,);
    gnd;
}

color_red;
{
    resistor(up_ d,E);       rlabel(,R3,);
    P: power();    {"Power" at P.n above};  # vnoreny blok
    
}
color_black
resistor(right_ d,E);        llabel(,R4,);
dot;
capacitor(); llabel(,C_1,)
'''

_ = cm_compile('cm_0120a', data, dpi=600)   
```

```{figure} ./src/cm_0120a.png
:width: 300px
:name: cm_0120a

[Použitie](./src/cm_0120a.ckt) vetviev v zapojení
```

Vetvy s výhodou využijeme pri popise prvkov zapojenie. Zobrazenie textu mení rovnako ako každý nový element zapojenia hodnotu `Here`, ak chceme v kreslení pokračovať s pôvodnou súradnicou, uzatvoríme text do vetvy. Príkazy pre popis dvojpólov (*llabel ...*) hodnotu `Here` nemenia.

    line -> 1;
    box wid 2 ht 1;     
    {
        "top of box" at last box.n above; 
        "bottom of box" at last box.s below;
        line from last box.nw to last box.se; 
        line from last box.sw to last box.ne; 
    }
    line -> 1;     
    box wid 2 ht 1; 
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
Origin: Here 
line -> 1;
box wid 2 ht 1; 
{
    "top of box" at last box.n above; 
    "bottom of box" at last box.s below;
    line from last box.nw to last box.se; 
    line from last box.sw to last box.ne; 
}
line -> 1;
box wid 2 ht 1; 
'''

_ = cm_compile('cm_0120b', data, dpi=600)   
```

```{figure} ./src/cm_0120b.png
:width: 400px
:name: cm_0120b

[Lokálne](./src/cm_0120b.ckt) súradnice vo vetve.
```

## <font color='teal'> Bloky </font>

Časť kódu uzatvorená v hranatých zátvorkách `[...]` predstavuje blok alebo zložený objekt. Program v bloku má vlastnú absolútnu súradnicovú sústavu a po vytvorení má vlastnosti plošného objektu. Pre kód v bloku sú automaticky vypočítané vonkajšie rozmery a sú mu priradené štandardné atribúty *.s, .n ... *. Pre ukladanie zloženého objektu platia rovnaké pravidlá ako pre každý iný plošný objekt.

    move to (1, 1.5);

    A:[  # absolute coordinate  
       B: box at (0,0) wid 2 ht 1; 
      C1: circle at (0, 0.5) rad 0.25; 
      C2: circle at (0,-0.5) rad 0.25;
      C3: circle at B.w rad 0.25;
      C4: circle at B.e rad 0.25;
    ]
    color_red;
    box at A.c wid A.wid_ ht A.ht_ dashed; 

    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)
Grid(5,3);

move to (1, 1.5);

A:[  # absolutne suradnice v bloku 
    B: box at (0,0) wid 2 ht 1; 
   C1: circle at (0, 0.5) rad 0.25; 
   C2: circle at (0,-0.5) rad 0.25;
   C3: circle at B.w rad 0.25;
   C4: circle at B.e rad 0.25;
  ]

color_red;
box at A.c wid A.wid_ ht A.ht_ dashed;  # outer contour
'''

_ = cm_compile('cm_0120e', data, dpi=600)   
```

```{figure} ./src/cm_0120e.png
:width: 350px
:name: cm_0120e

Blok reprezentujúci zložený objekt a jeho vonkajší obrys.
```

## <font color='teal'> Referencie vo vetvách a blokoch </font>

Referencie a premenné vytvorené vo vnútri bloku sú globálne a je možno sa na ne odkazovať v nasledujúcom kóde ako aj v iných blokoch.


    d = 2;
    DOT1: dot;                   # referencny bod
    { # vetva D1-D2
        D1: diode(right_ up_);  dlabel(0,0,,D_1,,XAR);
    DOT2: dot;              
        D2: diode(right_ down_);dlabel(0,0,,D_2,,XAL);
    }

    { # vetva D3-D4
        D3: diode(right_ down_);dlabel(0,0,,D_3,,XBR);
    DOT3: dot;
        D4: diode(right_ up_);  dlabel(0,0,,D_4,,XBL);
    DOT4: dot;
    }

    # pouzitie referencii vytvorenych vo vetvach
    L1: line from DOT2  up_ d/2 then left_ d;   tconn(,O);
    L2: line from DOT3  down_ d/2 then left_ d; tconn(,O);
    L3: line from DOT4 right_ d; tconn(d/4, O);
    L4: line from DOT1 left_ d/2 then down_ 7*d/8; 
        line to (L3.e.x, Here.y); tconn(right_ d/4,O);
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
Origin: Here 
d = 2;
DOT1: dot;                   # referencny bod
{ # vetva D1-D2
     D1: diode(right_ up_);  dlabel(0,0,,D_1,,XAR);
   DOT2: dot;              
     D2: diode(right_ down_);dlabel(0,0,,D_2,,XAL);
}

{ # vetva D3-D4
     D3: diode(right_ down_);dlabel(0,0,,D_3,,XBR);
   DOT3: dot;
     D4: diode(right_ up_);  dlabel(0,0,,D_4,,XBL);
   DOT4: dot;
}

# pouzitie referencii vytvorenych vo vetvach
L1: line from DOT2  up_ d/2 then left_ d;   tconn(,O);
L2: line from DOT3  down_ d/2 then left_ d; tconn(,O);
L3: line from DOT4 right_ d; tconn(d/4, O);
L4: line from DOT1 left_ d/2 then down_ 7*d/8; 
    line to (L3.e.x, Here.y); tconn(right_ d/4,O);
'''

_ = cm_compile('cm_0120d', data,  dpi=600)   
```

```{figure} ./src/cm_0120d.png
:width: 300px
:name: cm_0120d

[Použitie](./src/cm_0120d.ckt) refencií v bloku
```
