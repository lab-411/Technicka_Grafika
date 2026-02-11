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


# <font color='navy'> Operačné zosilovače  </font> 

Operačné zosilovače patria v `CicuitMacros` medzi multipóly a podobne pri ako iných multipóloch ich vývody nie sú uložené v celočíselnej mriežke. Okrem štandardných atribútov pre plošné objekty (*.s, ...*) sú súčasťou prvku doplnkové atribúty (*.NE ..,*) pre pozície bodov na značke a atribúty pre prístup k vývodom zosilovača. Atribúty pre pripojenie napájacích vývodov (*.V1, .V2*) sú dostupné len pri použití parametra  **P**, {numref}`cm_0204d`:

    opamp(linespec, label+, label-, size, TPR);
    
    parametre:
    
      linespec             - orientácia a dĺžka výstupu
      label+               - alternatívne označenie (+) vstupu
      label-               - alternatívne označenie (-) vstupu
      size                 - veľkosť
      T                    - skrátený výstup
      P                    - zobrazenie napájania
      R                    - zámena (+) (-) vstupov
      
    atribúty:
    
    .s   .w   .n.  .e      - stredy strán obrysu
    .sw  .se  .nw  .ne     - rohy obrysu
    .NE .SE                - poloha stredov hornej a dolnej strany značky
    .W                     - poloha stred medzi vstupmi
    .S .E .N               - poloha rohov značky
    .In1 .In2              - poloha vstupov (+) a (-)
    .Out                   - poloha výstupu
    .V1 .V2                - poloha napájacích prívodov, parameter P
    


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
command"\sf"
include(lib_color.ckt)

move to (0,0); 
OP: opamp(,,,,P);
color_red();
line <- from OP.W left_ 1; ".W" rjust;
line <- from OP.In1 left_ 1 up_ .5; ".In1" rjust;
line <- from OP.In2 left_ 1 down_ .5; ".In2" rjust;
line <- from OP.N up_ 1 ; ".N" above;
line <- from OP.S down_ 1 ; ".S" below;
line <- from OP.E1 up_ 1 right_ 1; ".E1" above;
line <- from OP.V1 up_ 1 ; ".V1" above;
line <- from OP.V2 down_ 1 ; ".V2" below;
line <- from OP.E2 down_ 1 right_ 1; ".E2" below;
line <- from OP.Out right_ 1; ".Out" ljust;
line <- from OP.E right_ 1 down_ 1; ".E" ljust;

move to (6,0); 
right_;
color_black();
OP: opamp(,,,,);
# color_grey();
box wid (OP.ne-OP.nw).x ht (OP.nw-OP.sw).y at OP.c dashed;
color_blue();
line <- from OP.w left_ 1; ".w" rjust;
line <- from OP.nw left_ 1 up_ 0.5; ".nw" rjust;
line <- from OP.ne right_ 1 up_ 0.5; ".ne" ljust above;
line <- from OP.ne right_ 1 up_ 0.5; ".ne" ljust above;
line <- from OP.se right_ 1 down_ 0.5; ".se" ljust above;
line <- from OP.e right_ 1; ".e" ljust;
line <- from OP.sw left_ 1 down_ 0.5; ".sw" rjust;
line <- from OP.n up_ 1; ".n" above;
line <- from OP.s down_ 1; ".s" below;
line <- from OP.NE left_ 0.5 up_ 1; ".NE" above;
line <- from OP.SE left_ 0.5 down_ 1; ".SE" below;
line <- from OP.c right_ 0.75 down_ 1.5; ".c" below;
'''

_ = cm_compile('cm_0204x', data, dpi=600 )   
```

```{figure} ./src/cm_0204x.png
:width: 550px
:name: cm_0204x

Atribúty značky operačného zosilovača.
```
    
    
Príklady použitia značky operačného zosilovača:

    A1: opamp(); 
    A2: opamp(,,,,R); 
    A3: opamp(,"\sf x" ljust, "\sf y" ljust) "\sf A3" rjust;
    A4: opamp(1,,,,TP); 
    A5: opamp(up_ 1,,,0.85,);


    
```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
A1: opamp(); {"\sf A1" at A1.n }
move to Here+(0.5,0)
A2: opamp(,,,,R); {"\sf A2" at A2.n }
move to Here+(0.5,0)
A3: opamp(,"\sf x" ljust, "\sf y" ljust) "\sf A3" rjust ;
move to Here+(0.5,0)
A4: opamp(1,,,,TP); {"\sf A4" at A4.ne rjust}
move to Here+(0.5,0)
A5: opamp(up_ 1,,,0.85,);{"\sf A5" at A5.ne }
'''

_ = cm_compile('cm_0204d', data, dpi=700 )   
```

```{figure} ./src/cm_0204d.png
:width: 550px
:name: cm_0204d

Vybrané značky operačných zosilovačov.
 
```    
    

    
    
Nasledujúci príklad, {numref}`cm_0204a`,  ukazuje ukladanie prvkov obvodu voči polohe operačnému zosilovaču, ktorý je na plochu uložený absolútne ako prvý komponent zapojenia. Pripojené komponenty ukladáme relatívne voči jeho vývodom. V zapojení sú použité popisy a matematické vzťahy zadané syntaxou systému LaTeX. Pre zobrazenie vstupných a výstupných uzlov obvodov sú použité kružnice. 

```{code-block}
# Invertujuci zosilovač

OP: opamp()
    line from OP.In1 left 0.5;
    
DN: dot;
        # ---- poloha viazaná k In1
    resistor(2,,E); llabel(,R_1,); 
    circle rad 0.1; "\textit{In}" at last circle.n above;
    
    line from DN up_ 1;
    resistor(right_ 2.5,,E); llabel(,R_2,);
    line down_ (Here.y - OP.Out.y);
    
DO: dot;
    { line to OP.Out; }
    line right_ 1;
    circle rad 0.1; "\textit{Out}" at last circle.n above;
    line from OP.In2 left_ 0.5 then down_ 0.5; gnd; 

    # ---- popis a matematický vzťah
    "\textit{Invertujúci zosilovač}" at OP.c + (0, -1.5);
    "$K = -\dfrac{R_2}{R_1}$" at OP.c + (0, -2.25);
```


        
```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
    include(lib_base.ckt)
    include(lib_user.ckt)
    
    Grid(14,5);
    move to (3,3);
OP: opamp()
    line from OP.In1 left 0.5;
DN: dot;
    resistor(2,,E); llabel(,R_1,);
    circle rad 0.1; "\textit{In}" at last circle.n above;
    
    line from DN up_ 1;
    resistor(right_ 2.5,,E); llabel(,R_2,);
    line down_ (Here.y - OP.Out.y);
DO: dot;
    { line to OP.Out; }
    line right_ 1;
    circle rad 0.1; "\textit{Out}" at last circle.n above;

    line from OP.In2 left_ 0.5 then down_ 0.5; gnd; 
    "\textit{Invertujúci zosilovač}" at OP.c + (0, -1.5);
    
    "$K = -\dfrac{R_2}{R_1}$" at OP.c + (0, -2.25);

move to OP.c + (6,0.5);
    right_;
PP: opamp(,,,,R)
    line from PP.In1 left_ 1.5;
    circle rad 0.1; "\textit{In}" at last circle.n above;
    line from PP.In2 left_ 0.5 then down_ 0.75;
    dot;
    {resistor(down_ 1.5,,E); rlabel(,R_1,); gnd;}
    resistor(right_ 2.5,,E); llabel(,R_2,);
    line up_ -(Here.y - PP.Out.y);
    dot;
    { line to PP.Out; }
    line right_ 1;
    circle rad 0.1; "\textit{Out}" at last circle.n above;
    "\textit{Neinvertujúci zosilovač}" at PP.c + (0, 1);
    
    "$K =1 + \dfrac{R_2}{R_1}$" at PP.c + (0.5, -2.25);
'''

_ = cm_compile('cm_0204a', data, dpi=700 )   
```

```{figure} ./src/cm_0204a.png
:width: 670px
:name: cm_0204a

[Zapojenie](./src/cm_0204a.ckt) invertujúceho a neinvertujúceho zosilovača. 
```

Použitie parametra **P** pre zobrazenie napájacích vývodov operačného zosilovača a použitie makra *reversed()* pre zobrazenie kondenzátora $C_2$ s obrátenou polaritou ukazuje nasledujúci príklad, {numref}`cm_0204b`:

    OA: opamp(,,,,P);                # zobrazenie napájacich prívodov
        line from OA.V1 up_ .75;
        dot;
        { 
        line right_ 0.25; 
        capacitor(right_ 1,C+); llabel(,C_1,); rlabel(,10 \mu F,); 
        line .5 then down_ 0.25; gnd;
        }
        line 0.75; circle rad 0.1; "$V+$" at last circle.n above;

        line from OA.V2 down_ .75;
        dot;
        {
            line right_ 0.25; reversed(`capacitor', right_, C+); llabel(,C_2,); 
            rlabel(,10 \mu F,); 
            line .5 then down_ 0.25; gnd;
        }
        line 0.75; circle rad 0.1; "$V-$" at last circle.s below;

        line from OA.In1 left 0.5;
        line from OA.In2 left 0.5;


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
    include(lib_base.ckt)
    include(lib_user.ckt)

OA: opamp(,,,,P);
    line from OA.V1 up_ .75;
    dot;
    {line right_ 0.25; capacitor(right_ 1,C+); llabel(,C_1,); rlabel(,10 \mu F,); line .5 then down_ 0.25; gnd;}
    line 0.75;
    circle rad 0.1; "$V+$" at last circle.n above;

    line from OA.V2 down_ .75;
    dot;
    {line right_ 0.25; reversed(`capacitor', right_, C+); llabel(,C_2,); rlabel(,10 \mu F,); line .5 then down_ 0.25; gnd;}
    line 0.75;
    circle rad 0.1; "$V-$" at last circle.s below;

    line from OA.In1 left 0.5;
    line from OA.In2 left 0.5;
'''

_ = cm_compile('cm_0204b', data, dpi=600 )   
```

```{figure} ./src/cm_0204b.png
:width: 170px
:name: cm_0204b

[Obvod](./src/cm_0204b.ckt) napájania operačného zosilovača. 
```

V komplikovanejšom zapojení Wien-Robisonovho aktívneho filtra, {numref}`cm_0204c`, sú použité vnorené bloky pri kreslení vetiev obvodu a použitá konštrukcia *with* pri ukladaní zosilovača *OA2* na aktuálnu polohu vývodu *In2*:

    OA1: opamp(,,,,); "$A_1$" at OA1.SE below ljust;
        line from OA1.In1 left_ 0.5;
        
    ...
    ...
        
    R1: resistor(right_ 2.15,,E); rlabel(,R_1,); dot;
        {line down_ (Here.y-OA1.Out.y) then to OA1.Out;}

        line right_ 1; dot;
        { C1: capacitor(down_ 2.25); rlabel(,C,);}
        line right_ 0.75; dot;
        {                                          <------ blok
        R2: resistor(down_ 2.25,,E); llabel(,R_2,); 
            dot; 
            {                                      <------ vnorený blok
                line right_ 2;
                OA2: opamp() with .In2 at Here;    <------ poloha In2
                "$A_2$" at OA2.SE below ljust;
            }
            {
                C2:  capacitor(down_ 1); rlabel(,C,);
                R22: resistor(down_ 1,,E); llabel(,R_2,);
                    gnd;
            }
            line to C1.end; 
        }
    ...
    ...

    
```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
    include(lib_base.ckt)
    include(lib_user.ckt)

OA1: opamp(,,,,); "$A_1$" at OA1.SE below ljust;
    line from OA1.In1 left_ 0.5;
    {line from OA1.In2 left 0.5 then down 0.5; gnd; }
    dot;
    { 
	resistor(2,,E); rlabel(,\dfrac{1}{\beta} R_1,);
    T1: circle rad .1;
    }
    line up_ 1.5; dot;
R1: resistor(right_ (OA1.Out.x - OA1.In1.x +0.5),,E); rlabel(,R_1,); dot;

    {line down_ (Here.y-OA1.Out.y) then to OA1.Out;}

    line right_ 1; dot;
    { C1: capacitor(down_ 2.25); rlabel(,C,);}
    line right_ 0.75; dot;
    { 
      R2: resistor(down_ 2.25,,E); llabel(,R_2,); 
          dot; 
          {
              line right_ 2;
              OA2: opamp() with .In2 at Here;
              "$A_2$" at OA2.SE below ljust;
          }
          {
             C2:  capacitor(down_ 1); rlabel(,C,);
             R22: resistor(down_ 1,,E); llabel(,R_2,);
                  gnd;
          }
          line to C1.end; 
     }
     line right_ 1;
     resistor(down_ (Here.y - OA2.In1.y),,E); llabel(,R_3,); dot;
     { line to OA2.In1; } 
     line down_ 1;
     resistor(down_ 1.5,,E); llabel(,2R_3,);
     line right_ (OA2.Out.x - Here.x) then to OA2.Out; dot;
     {    line 0.75;
          T2: circle rad .1;
     }
     line up_ 2.75 then left_ (Here.x - R1.end.x)
     resistor((OA1.Out.x - OA1.In1.x +0.5),,E); rlabel(,\dfrac{1}{\alpha} R_1,);
     line to R1.start;
 
    line -> from T1.s + (0, -0.1) down_ 1 "$V_{in}$" rjust;
    move to Here + (0, - 0.1);
    circle rad 0.1; line 0.25;
    gnd;

    line -> from T2.s + (0, -0.1) down_ 1 "$V_{out}$" ljust;
    move to Here + (0, - 0.1);
    circle rad 0.1; line 0.25;
    gnd;

    line -> from OA1.Out + (0, -0.1) down_ 1 "$V_1$" ljust;
    move to Here + (0, - 0.1);
    circle rad 0.1; line 0.25;
    gnd;

'''

_ = cm_compile('cm_0204c', data, dpi=600 )   
```

```{figure} ./src/cm_0204c.png
:width: 600px
:name: cm_0204c

[Zapojenie](./src/cm_0204c.ckt) aktívneho filtra. 
```




