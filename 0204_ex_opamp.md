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

Operačné zosilovače patria v `CicuitMacros` medzi mnohopóly a podobne pri ako iných mnohopóloch ich vývody nie sú uložené v celočíselnej mriežke. Okrem štandardných atribútov pre plošné objekty (*.s, ...*) sú súčasťou prvku doplnkové atribúty (*.NE ..,*) pre pozície bodov na značke a atribúty pre prístup k vývodom zosilovača. Atribúty pre pripojenie napájacích vývodov (*.V1, .V2*) sú dostupné len pri použití parametra makra *P*.

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
    
    

Pri kreslení zapojení s operačnýmí zosilovačmi musíme používať ako referenciu stred zosilovača a pripojené komponenty ukladať relatívne voči jeho vývodom.

Nasledujúci príklad ukazuje ukladanie prvkov obvodu voči zosilovaču, ktorý je na plochu uložený absolútne ako prvý komponent zapojenia. V zapojení sú použité popisy a matematické vzťahy zadané syntaxou LaTeX-u. Ako vstupné a výstupné uzly obvodu sú použité kružnice. 

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
    
        # ---- popis a matematicky vztah
        "\textit{Invertujúci zosilovač}" at OP.c + (0, -1.5);
        "$K = -\dfrac{R_2}{R_1}$" at OP.c + (0, -2.25);



```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
    include(base.ckt)
    Grid(15,5);
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

_ = cm_compile('./img/cm_095', data, dpi=600 )   
```

```{figure} ./img/cm_095.png
:width: 650px
:name: cm_095

[Zapojenie](./src/0250_opamp_inv.ckt) invertujúceho a neinvertujúceho zosilovača. 
```

Použitie parametra *P* pre zobrazenie napájacích vývodov zosilovača a použitie makra *reversed* pre zobrazenie kondenzátora $C_2$ s obrátenou polaritou ukazuje nasledujúci príklad.

    OA: opamp(,,,,P);                # zobrazenie napajacich privodov
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

from cm.utils import *

data = r'''
    include(base.ckt)

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

_ = cm_compile('./img/cm_096', data, dpi=600 )   
```

```{figure} ./img/cm_096.png
:width: 170px
:name: cm_096

[Obvod](./src/0252_opamp_power.ckt) napájania operačného zosilovača. 
```

V komplikovanejšom zapojení Wien-Robisonovho aktívneho filtra (vo výpise sú vynechané nepodstatné časti) sú použité vnorené bloky pri kreslení vetiev obvodu a použitá konštrukcia *with* pri ukladaní zosilovača *OA2* na aktuálnu polohu vývodom *In2*.

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

from cm.utils import *

data = r'''
include(base.ckt)

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

_ = cm_compile('./img/cm_097', data, dpi=600 )   
```

```{figure} ./img/cm_097.png
:width: 600px
:name: cm_097

[Zapojenie](./src/0254_opamp_filter.ckt) aktívneho filtra. 
```




