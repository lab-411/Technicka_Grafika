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

## <font color='teal'> Úpravy  </font> 

Niektoré typy operačných zosilovačov ako aj odvodených typov, ako sú napríklad komparátory, majú ďaľšie vývody pre nastavenie ich parametrov. Pre doplnenie týchto vývodov môžeme modifikovať značku z knižnice, pričom polohu vývodov určíme z atribútov značky pomocou konštrukcie *between*, {numref}`cm_0204f`:

    define(`LF355',`[
        OP: opamp(,,,,);

            line from OP.In1 left_ 0.5;   "2" above ljust;
        INN:last line .end
            line from OP.In2 left_ 0.5;   "3" above ljust;
        INP:last line .end

        P7: 0.25 between OP.N and OP.E;
        P1: 0.50 between OP.N and OP.E;
        P5: 0.75 between OP.N and OP.E;
        P4: 0.50 between OP.S and OP.E;

            line from P7 up_ 0.45; "7" rjust;
        VSP:last line .end;

            line from P4 down_ 0.45; "4" rjust;
        VSN:last line .end;

            line from P1 up_ 0.45; "1" rjust;
        BAL1:last line .end;
            line from P5 up_ 0.45; "5" rjust;
        BAL2:last line .end;
        OUT: OP.Out; "6" at OUT above rjust;
    ]') 



```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
command"\small \sf"
define(`LF355',`[
    OP: opamp(,,,,);

        line from OP.In1 left_ 0.5;   "2" above ljust;
    INN:last line .end
        line from OP.In2 left_ 0.5;   "3" above ljust;
    INP:last line .end

    P7: 0.25 between OP.N and OP.E;
    P1: 0.5 between OP.N and OP.E;
    P5: 0.75 between OP.N and OP.E;

    P4: 0.5 between OP.S and OP.E;

        line from P7 up_ 0.45; "7" rjust;
    VSP:last line .end;

        line from P4 down_ 0.45; "4" rjust;
    VSN:last line .end;

        line from P1 up_ 0.45; "1" rjust;
    BAL1:last line .end;
        line from P5 up_ 0.45; "5" rjust;
    BAL2:last line .end;
    OUT: OP.Out; "6" at OUT above rjust;
]') 

OP: LF355(); "\sf LF\\355" at OP.OP.se above;
'''

_ = cm_compile('cm_0204f', data, dpi=600 )   
```

```{figure} ./src/cm_0204f.png
:width: 160px
:name: cm_0204f

Doplnená [značka](./src/cm_0204f.ckt) operačného zosilovača s doplnenýmí vývodmi pre kompenzáciu offsetu, [zdroj](https://www.ti.com/lit/ds/symlink/lf356.pdf). 
```

Reálne zapojenia elektronických obvodov na rozdiel od ideálnych obsahujú aj technologické detaily komponentov, ako sú čísla vývodov alebo zlúčenie niekoľkých komponentov v jednom púzdre. Na zapojení $\Delta-\Sigma$ modulátora sú operačné zosilovače *IC1a* a *IC1b* integrované v jednom púzdre so spoločným napájaním, {numref}`cm_0204e`.

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
cct_init
log_init
command"\small \sf"
include(lib_color.ckt)
include(lib_base.ckt)

#=======================================================================
# AD790
# komparator, latch
#-----------------------------------------------------------------------
define(`AD790',`[
    OP: opamp(,,,,R);

        line from OP.In1 left_ 0.5;   "2" above ljust;
    INP:last line .end
        line from OP.In2 left_ 0.5;   "3" above ljust;
    INN:last line .end

    P1: 1/3 between OP.N and OP.E;
    P8: 2/3 between OP.N and OP.E;
    P5: 0.75 between OP.S and OP.E;
    P4: 0.5 between OP.S and OP.E;
    P6: 0.25 between OP.S and OP.E;

        line from P1 up_ 0.45; "1" rjust;
    VSP:last line .end
        line from P8 up_ 0.45; "8" rjust;
    VLG:last line .end

    C1: circle rad 0.095 with .n at P5+(0,-0.035) 
        line from C1.s down_ 0.3; "5" ljust;
    LATCH: last line .end

        line from P4 down_ 0.5; "4" rjust;
    VSN:last line .end

        line from P6 down_ 0.5; "6" rjust;
    GND:last line .end;
    OUT:OP.Out; 
        "7" at OP.Out above rjust;

    line from OP.In2+(0.2,0.1) right_ 0.2 then up_ to OP.In1+(0.2+0.2,-0.1) then right_ 0.2;
]') 

#=======================================================================
# MCP6272A
# 1/2 MCP6272
#-----------------------------------------------------------------------
define(`MCP6272A',`[
    right_;
    OP: opamp(,,,,);
        line from OP.In1 left_ 0.5;   "2" above ljust;
    INN:last line .end
        line from OP.In2 left_ 0.5;   "3" above ljust;
    INP:last line .end
    OUT:OP.Out; 
        "1" at OP.Out above rjust;

        
]') 

#=======================================================================
# MCP6272B
# 2/2 MCP6272
#-----------------------------------------------------------------------
define(`MCP6272B',`[
    right_
    OP: opamp(,,,,P);
        line from OP.In2 left_ 0.5;   "6" above ljust;
    INP:last line .end
        line from OP.In1 left_ 0.5;   "5" above ljust;
    INN:last line .end
    OUT:OP.Out; 
        "7" at OP.Out above rjust;

        line from OP.V1 up_ 0.35; "8" rjust below;
    VDD:last line .end
        line from OP.V2 down_ 0.35; "4" rjust above;
    VSS:last line .end;
]') 


#=======================================================================

move to (0,0); 
right_;
AD: AD790(); "`AD790'" at AD.OP.ne; "IC2" at AD.OP.se above ljust;
L1:line from AD.LATCH down_ 0.5 then right_ 2; tconn(,O); "CLK" ljust;
   line from AD.GND down_ .25; dot;{line right_ to (AD.VSN, Here) to AD.VSN;} 
   gnd(.5);

   line from AD.VSP up_ 0.25; dot; {line right_ to (AD.VLG, Here) to AD.VLG;}
   power(0.75, +5V);

   line left_ 0.5 from AD.INP; D1: dot; line left_ 1;  
Q1:MCP6272B(); "`MCP6272'" at Q1.OP.ne; "IC1b" at Q1.OP.se above;
   line from Q1.VSS down_ 0.15; gnd();
   line from Q1.VDD up_ 0.15; power(0.35, +5V);
   line from Q1.INN left_ .25; D2: dot;
   resistor(1.75,E); rlabel(,"$\sf R_1$",);
D3:dot; 
   line left_ 0.25;
Q2:MCP6272A(); "`MCP6272'" at Q2.OP.ne rjust above; "IC1a" at Q2.OP.se above rjust;
   {line from D3 up_ 1.25; line to (Q2.INN, Here)+(-0.25,0); 
    line to (Here, Q2.INN) to Q2.INN;} 
   line from Q2.INP left_ 0.25; tconn(,O);

#-----------------------------------------------------------------------
# vetva C1
   line from D1 up_ 2.15; left_;
   capacitor( (D1-D2).x ); rlabel(,"$\sf C_1$",);
D4: dot;
   line to D2;

#-----------------------------------------------------------------------
# vetva R2   
   line from AD.OUT right_ 0.75; D4: dot; line up_ 3.25;
   left_; resistor( (D4-D2).x,E); rlabel(,"$\sf R_2$",);
   line to D2;
   line from D4 to (L1.end, D4); right_; tconn(,O); "DATA" ljust;

#-----------------------------------------------------------------------
# vetve spoj 3-3
   line from Q1.INP to (D2, Q1.INP) then down_ 1.35;
   D5: dot;
   line to (D1, Here);
   line to (Here, AD.INN) to AD.INN;
   resistor(from D5 left_ 1.75,E); rlabel(,"$\sf R_3$",);
   tconn(0.25,O); "+5V" rjust;
   resistor(from D5 down_ 1.5,E); rlabel(,"$\sf R_4$",); 
   gnd();
#-----------------------------------------------------------------------
'''

_ = cm_compile('cm_0204e', data, dpi=600 )   
```

```{figure} ./src/cm_0204e.png
:width: 650px
:name: cm_0204e

[Zapojenie](./src/cm_0204e.ckt) $\Delta-\Sigma$ modulátora použitého v detektore kondenzovanej vlhkosti v projekte kapacitného extenzometra [^projekt]. 
```


[^projekt]: Projekt VEGA 2/0013/25

    Interpretácia periodických a neperiodických deformácií zemskej kôry v oblasti Západných Karpát na základe paralelných meraní horizontálnych posunutí.
