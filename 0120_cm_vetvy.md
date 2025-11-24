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
# <font color='navy'> Vetvy </font>

Pri kreslení elektrických zapojení sa často vyskytuje situácia, v ktorej potrebujeme nakresliť samostatnú časť obvodu (vetvu) a potom pokračovať v pôvodnom zapojení. V štandardnej situácii by sme si museli označiť vhodný prvok schémy referenciou a po nakreslení vetvu sa na pôvodnú pozíciu vrátiť pomocou povelu *move to ...*.

V `CircuitMacros` máme možnosť uzatvoriť kód vetvy obvodu do bloku kódu uzatvoreného do zložených zátvoriek. Uzatvorenie časti kódu do bloku umožňuje vytváranie časti obvodu alebo umiestnenie iných komponentov relatívne k poslednej súradnici bez toho, aby táto bola zmenená. Rovnako blok nemení ani smer ukladania definovaný mimo neho. Bloky je možné vnárať. 

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

from cm.utils import *

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

_ = cm_compile('./src/cm_0120a', data, dpi=600)   
```

```{figure} ./src/cm_0120a.png
:width: 300px
:name: cm_0120a

[Použitie](./src/cm_0120a.ckt) vetviev v zapojení
```

Bloky s výhodou využijeme pri popise prvkov zapojenie. Zadanie textu mení rovnako ako každý nový element zapojenia hodnotu `Here`, ak chceme v kreslení pokračovať v pôvodnom smere, uzatvoríme text do bloku. Príkazy pre popis dvojpólov (*llabel ...*) hodnotu `Here` nemenia.

    line -> 1;
    box wid 2 ht 1; 
    {
        "top of box" at last box.n above; 
        "bottom of box" at last box.s below;
        line from last box.nw to last box.se; 
        line from last box.sw to last box.ne; 
    }
    line -> 1;
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from cm.utils import *

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
'''

_ = cm_compile('./src/cm_0120b', data, dpi=600)   
```

```{figure} ./src/cm_0120b.png
:width: 300px
:name: cm_0120b

[Lokálne](./src/cm_0120b.ckt) súradnice v bloku
```


## <font color='teal'> Premenné a referencie </font>

Referencie a premenné vytvorené vo vnútri bloku sú globálne a je možno sa na ne odkazovať v nasledujúcom kóde ako aj v iných blokoch.


    d = 2;
    move to (2, 3);
    DT1: dot;                   # referencny bod
    {
            diode(right_ up_); dlabel(0,0,,D_1,,XAR);
        DT2: dot;              
            diode(right_ down_); dlabel(0,0,,D_2,,XAL);
    }

    {
            diode(right_ down_); dlabel(0,0,,D_3,,XBR);
        DT3: dot;
            diode(right_ up_); dlabel(0,0,,D_4,,XBL);
        DT4: dot;
    }

    # pouzitie referencii vytvorenych v blokoch
    L1: line from DT2  up_ d/2 then left_ d;   tconn(,O);
    L2: line from DT3  down_ d/2 then left_ d; tconn(,O);
    L3: line from DT4 right_ d; tconn(d/4, O);
    L4: line from DT1 left_ d/2 then down_ 7*d/8; 
        line to (L3.e.x, Here.y); tconn(right_ d/4,O);
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
Origin: Here 
d = 2;
move to (2, 3);
DT1: dot;                   # referencny bod
{
         diode(right_ up_); dlabel(0,0,,D_1,,XAR);
    DT2: dot;              
         diode(right_ down_); dlabel(0,0,,D_2,,XAL);
}

{
         diode(right_ down_);   dlabel(0,0,,D_3,,XBR);
    DT3: dot;
         diode(right_ up_);    dlabel(0,0,,D_4,,XBL);
    DT4: dot;
}

# pouzitie referencii vytvorenych v blokoch
L1: line from DT2  up_ d/2 then left_ d;   tconn(,O);
L2: line from DT3  down_ d/2 then left_ d; tconn(,O);
L3: line from DT4 right_ d; tconn(d/4, O);
L4: line from DT1 left_ d/2 then down_ 7*d/8; 
    line to (L3.e.x, Here.y); tconn(right_ d/4,O);
'''

_ = cm_compile('./src/cm_0120d', data,  dpi=600)   
```

```{figure} ./src/cm_0120d.png
:width: 300px
:name: cm_0120d

[Použitie](./src/cm_0120d.ckt) refencií v bloku
```
