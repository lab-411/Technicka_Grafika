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


# <font color='navy'> Pasívne obvody  </font> 

## <font color='teal'>  Odporový delič </font> 

V príklade sériového zapojenie rezistorov sú použité nasledujúce konštrukcie:

* zaradenie pomocnej knižnice [lib_base.ckt](./src/lib_base.ckt) a [lib_user.ckt](./src/lib_user.ckt) do zdrojového kódu, tieto obsahujú makrá pre vykreslovanie mriežky a prvky, ktoré nie sú súčasťou distribúcie `CircuitMacros`
* používanie spoločnej premennej `d` pre škálovanie rozmerov prvkov zapojenia ako aj ich polohy. Prvky zapojenia **nie sú** v tomto príklade ukladané na absolútne súradnice pracovnej plochy
* použitie atribútov komponentov na výpočty *(x,y)* súradníc, napr. *(DC.s.x, R2.end.y)*
* použitie príkazov *larrow* pre zobrazenie napätí na rezistoroch
* použitie šípky *line -> * v rozdelenej čiare na zobrazenie prúdu vetvou obvodu **TODO**

      include(lib_base.ckt)
      include(lib_user.ckt)
      d = 1.5;

      R1: resistor(down_ d,,E); rlabel(,R_1,); larrow(u_{1}, ->, 0.2)
      R2: resistor(d,,E); rlabel(,R_2,);       larrow(u_{2}, ->, 0.2)
      
      move to (R1.end -(d, -d/2 ) )  # poloha stredu zdroja vzhladom k spoju rezistorov

      DC: dc_source(d, 1); rarrow(u, ->, 0.2);
      line from DC.n to (DC.n.x, R1.start.y); 
      line -> right d/2; {"\textit{i}" at last line.e above}
      line to R1.start;

      line from DC.s to (DC.s.x, R2.end.y) to R2.end;


```{code-cell} ipython3 
:tags: ["remove-cell"]
from cm.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)
d = 1.5;

R1: resistor(down_ d,,E); rlabel(,R_1,); larrow(u_{1}, ->, 0.2)
R2: resistor(d,,E); rlabel(,R_2,);       larrow(u_{2}, ->, 0.2)
 
move to (R1.end -(d, -d/2 ) )

DC: dc_source(d, 1); rarrow(u, ->, 0.2);
line from DC.n to (DC.n.x, R1.start.y); 
line -> right d/2; {"\textit{i}" at last line.e above}
line to R1.start;

line from DC.s to (DC.s.x, R2.end.y) to R2.end;
'''

_ = cm_compile('./src/cm_200a', data,  dpi=600)   
```

```{figure} ./src/cm_200a.png
:width: 200px
:name: cm_200a

[Príklad](./src/cm_200a.ckt) sériového zapojenia rezistorov.
```

## <font color='teal'> Konfigurácia hviezda - trojuholník </font> 

V príklade zapojenie rezistorov pre konverziu hviezdy na trojuholník sú použité nasledujúce konštrukcie:

* šíkmé ukladanie dvojpólov (rezistorov) zadaním koncových bodov *resistor(from D1 to D2,,E)*
* použitie premennej `Here` pre lokalizáciu textu nad spojovacím bodom *dot; {"\textit{$A$}" at Here above}*

      include(lib_base.ckt)
      Grid(9,4.5)
      d = 2;
      move to (1.0, 1.5);                             #---------- Trojuholnik
      D1: dot; {"\textit{$B$}" at Here below}

      move to D1 + (d*cos(pi/3), d*sin(pi/3));
      D2: dot;  {"\textit{$A$}" at Here above}

      move to D1 + (d, 0)
      D3: dot;   {"\textit{$C$}" at Here below}

      R1: resistor(from D1 to D2,,E); {"\textit{$R_1$}" at R1.c + (-.4, 0.1) } 
      R2: resistor(from D1 to D3,,E); {"\textit{$R_2$}" at R2.c + (0, -0.4) }  
      R3: resistor(from D2 to D3,,E); {"\textit{$R_3$}" at R3.c + (.4, 0.1) } 

      
      move to (7,2);                                  #---------- Hviezda
      Y1: dot;
      q = 3*d/4

      move to Y1 + (q *cos(pi/2), q *sin(pi/2));
      Y2: dot;  {"\textit{$A$}" at Here above}

      move to Y1 + (q *cos(pi/6), -q *sin(pi/6));
      Y3: dot;  {"\textit{$C$}" at Here below}

      move to Y1 + (-q *cos(pi/6), -q *sin(pi/6));
      Y4: dot;  {"\textit{$B$}" at Here below}

      R11: resistor(from Y1 to Y2,,E); {"\textit{$R_{11}$}" at R11.c + (-.5, 0.1) } 
      R23: resistor(from Y1 to Y3,,E); {"\textit{$R_{23}$}" at R23.c + ( .55, 0.2) } 
      R13: resistor(from Y1 to Y4,,E); {"\textit{$R_{13}$}" at R13.c + ( -.55, 0.2) }

      line <-> from (3.5, 2) to (5,2)
      

```{code-cell} ipython3 
:tags: ["remove-cell"]
from cm.utils import *

data = r'''
include(lib_base.ckt)

d = 2;

#-----------------------------------------------------------------------
# mriezka
Grid(9,4.5)
#-----------------------------------------------------------------------
# Trojuholnik
move to (1.0, 1.5);
D1: dot; {"\textit{$B$}" at Here below}

move to D1 + (d*cos(pi/3), d*sin(pi/3));
D2: dot;  {"\textit{$A$}" at Here above}

move to D1 + (d, 0)
D3: dot;   {"\textit{$C$}" at Here below}

R1: resistor(from D1 to D2,,E); {"\textit{$R_1$}" at R1.c + (-.4, 0.1) } 
R2: resistor(from D1 to D3,,E); {"\textit{$R_2$}" at R2.c + (0, -0.4) }  
R3: resistor(from D2 to D3,,E); {"\textit{$R_3$}" at R3.c + (.4, 0.1) } 

#--------------------------------------
# Hviezda
move to (7,2);
Y1: dot;
q = 3*d/4

move to Y1 + (q *cos(pi/2), q *sin(pi/2));
Y2: dot;  {"\textit{$A$}" at Here above}

move to Y1 + (q *cos(pi/6), -q *sin(pi/6));
Y3: dot;  {"\textit{$C$}" at Here below}

move to Y1 + (-q *cos(pi/6), -q *sin(pi/6));
Y4: dot;  {"\textit{$B$}" at Here below}

R11: resistor(from Y1 to Y2,,E); {"\textit{$R_{11}$}" at R11.c + ( -.5,  0.1) } 
R23: resistor(from Y1 to Y3,,E); {"\textit{$R_{23}$}" at R23.c + (  .55, 0.2) } 
R13: resistor(from Y1 to Y4,,E); {"\textit{$R_{13}$}" at R13.c + ( -.55, 0.2) }

line <-> from (3.5, 2) to (5,2)
'''

_ = cm_compile('./src/cm_200b', data,  dpi=600)   
```

```{figure} ./src/cm_200b.png
:width: 550px
:name: cm_200b

[Zapojenie](./src/cm_200b.ckt) konfigurácie hviezda-trojuholník.
```


## <font color='teal'> Štvorpól </font> 

V nasledujúcom príklade zapojenia štvorpólu je použitý blok pre vykreslenie zeme, vyznačený červeno. V bloku sú je automaticky vytvorená lokálna kópia premennej `Here`, ktorá je platná na polohovanie prvkov obvodu v rámci bloku uzatvorenom medzi `{ ... }`. Po vykonaní kódu bloku je platná pôvodná hodnota `Here`. 


    include(lib_base.ckt)
    include(lib_color.ckt)                               
    up_;
    I1: source(2,I); llabel(,i_1,);  
        line right_ 1; 
    DA: dot; llabel(,a,); line 1;

        move to I1.start; line  right_ 1 ; 
    D0: dot; ; 
        line right_ 1; 

        color_red;
        {move to D0; line down_ 0.5; gnd;}
        color_black;

        move to (DA + D0)/2 + (1,0); 
    BX: box ht 3 wid 2.5;
        move to (BX.e.x, DA.y); line right_ 1; 
    DB: dot; llabel(,b,);

        line -> from DB right_ 1; {"$i_2$" above at last line.c}
        resistor(down_ 2,,E); llabel(,Z,); 
        line left_ 1; 
    DG: dot; line to D0;

    # popis - sipky
        line -> from DA + (0, -0.25) to D0+(0,0.25); "$u_1$" ljust at last line.c;
        line -> from DB + (0, -0.25) to DG+(0,0.25); "$u_2$" ljust at last line.c;


```{code-cell} ipython3 
:tags: ["remove-cell"]
from cm.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

up_;
I1: source(2,I); llabel(,i_1,);  
    line right_ 1; 
DA: dot; llabel(,a,); line 1;

    move to I1.start; line  right_ 1 ; 
D0: dot; ; 
    line right_ 1; 

    color_red;
    {move to D0; line down_ 0.5; gnd;}
    color_black;

    move to (DA + D0)/2 + (1,0); 
BX: box ht 3 wid 2.5;
    move to (BX.e.x, DA.y); line right_ 1; 
DB: dot; llabel(,b,);

    line -> from DB right_ 1; {"$i_2$" above at last line.c}
    resistor(down_ 2,,E); llabel(,Z,); 
    line left_ 1; 
DG: dot; line to D0;

# popis - sipky
line -> from DA + (0, -0.25) to D0+(0,0.25); "$u_1$" ljust at last line.c;
line -> from DB + (0, -0.25) to DG+(0,0.25); "$u_2$" ljust at last line.c;
'''

_ = cm_compile('./src/cm_200c', data,  dpi=600)   
```

```{figure} ./src/cm_200c.png
:width: 500px
:name: cm_200c

[Zapojenie](./src/cm_200c.ckt) štvorpólu.
```
        
        
        
