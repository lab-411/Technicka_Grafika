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


# <font color='navy'> RLC obvody  </font> 

## <font color='teal'>  Odporový delič </font> 

V príklade sériového zapojenie rezistorov sú použité nasledujúce konštrukcie, {numref}`cm_200a`:

* používanie spoločnej premennej `d` pre škálovanie rozmerov prvkov zapojenia ako aj ich polohy. 
* atribúty pre určenie súradníc, napr. *(Here, R2.end)*
* príkaz *rarrow* pre zobrazenie napätí na rezistoroch
* príkaz *b_current* pre zobrazenie prúdu obvodom
* použitie vetiev


        d = 1.5;
        R1: resistor(down_ d,,E); llabel(,R_1,); rarrow(u_{1}, ->, 0.2);
        D1: dot; {right_ tconn(,O); "A" ljust;}
        R2: resistor(down_ d,,E); llabel(,R_2,); rarrow(u_{2}, ->, 0.2);
        D2: dot; {right_ tconn(,O); "B" ljust; }

        DC: source(at D1-(2,0)  up_ d); 
        {    DCsymbol(at DC.c,,,R); 
            "$V_0$" at DC.center -(0.6,0); 
            rarrow(u_{0}, <-, 0.3);
        }
        {    line up_ to (Here, R1.start);
            line right_ to R1.start; b_current(i,,,Start, 1.5);
        }
        line from DC.start to (Here, R2.end) then to R2.end;


```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
    d = 1.5;

R1: resistor(down_ d,,E); llabel(,R_1,); rarrow(u_{1}, ->, 0.2)
D1: dot; {right_ tconn(,O); "A" ljust;}
R2: resistor(down_ d,,E); llabel(,R_2,); rarrow(u_{2}, ->, 0.2);
D2: dot; {right_ tconn(,O); "B" ljust; }

DC: source(at D1-(2,0)  up_ d); 
   {    DCsymbol(at DC.c,,,R); 
        "$V_0$" at DC.center -(0.6,0); 
        rarrow(u_{0}, <-, 0.3);
    }
    {    line up_ to (Here, R1.start);
         line right_ to R1.start; b_current(i,,,Start, 1.5);
    }
    line from DC.start to (Here, R2.end) then to R2.end;
'''

_ = cm_compile('cm_200a', data,  dpi=600)   
```

```{figure} ./src/cm_200a.png
:width: 230px
:name: cm_200a

[Príklad](./src/cm_200a.ckt) zapojenia s popísaním veličín v obvode.
```

## <font color='teal'> Konfigurácia hviezda - trojuholník </font> 

V príklade zapojenie rezistorov pre konverziu hviezdy na trojuholník sú použité nasledujúce konštrukcie, {numref}`cm_200b`:

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
from src.utils import *

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

_ = cm_compile('cm_200b', data,  dpi=600)   
```

```{figure} ./src/cm_200b.png
:width: 550px
:name: cm_200b

[Zapojenie](./src/cm_200b.ckt) konfigurácie hviezda-trojuholník.
```

## <font color='teal'> Jednoduché rádio </font> 

V príklade zapojenia jednoduchého rádia je použité makro *gnd()* pre vykreslenie alternatívnej značky zeme, {numref}`cm_200d`. Centrálnym elementom schémy je transformátor. Pre umiestnenie sluchátka je použitá konštrukcia *with ... at ..*.

```{code-block}
:emphasize-lines: 2,3,4,5,6,7,8,27
# makro pre vykreslenie 'europskej' zeme
define(`gnd',`[
    ifelse(defn(`d'),  $1, d=1/4,  d=$1)
    L: line from Here to Here + (0, -d)
    linethick_(2);
    line from L.end + (-1/4, 0) to L.end + (1/4, 0);
    linethick_();
]')

TR: transformer(down_ 1.25,L,7,AW,4);
    llabel(,L_3,); rlabel(,L_1,);    

    linethick_(1.5)              # jadro transformatora
    line at TR.c up_ 1 dashed    # hrubšia čiara
    linethick_()                 # onovenie pôvodnej hrúbky

C:  capacitor(from TR.P2 down_ 0.75); rlabel(,C_3,); variable(,A);
G:  gnd();

    line from TR.S2 to (TR.S2, C.end)
    gnd;
   
    line from TR.S1 up_ 0.25 then right_ 0.25;
    diode(1); llabel(,D,);
LL: line right_ 0.25 then down_ 0.5; 

EP: earphone() with .Box.n at LL.end; llabel(,Sl,);
    line from EP.Box.s to (EP.Box.s, C.end);
    gnd;

    line from TR.P1 up_ 0.5; antenna()
```

```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
define(`gnd',`[
    ifelse(defn(`d'),  $1, d=1/4,  d=$1)
    L: line from Here to Here + (0, -d)
    linethick_(2);
    line from L.end + (-1/4, 0) to L.end + (1/4, 0);
    linethick_();
]')


TR: transformer(down_ 1.25,L,7,AW,4);
    llabel(,L_3,); rlabel(,L_1,);    


linethick_(1.5)    # core
line at TR.c up_ 1 dashed
linethick_()

C: capacitor(from TR.P2 down_ 0.75); rlabel(,C_3,); variable(,A);
G: gnd();

line from TR.S2 to (TR.S2, C.end)
gnd;
line from TR.S1 up_ 0.25 then right_ 0.25;
diode(1); llabel(,D,);
LL: line right_ 0.25 then down_ 0.5; 

EP: earphone() with .Box.n at LL.end; llabel(,Sl,);
line from EP.Box.s to (EP.Box.s, C.end);
gnd;

line from TR.P1 up_ 0.5; antenna()
'''

_ = cm_compile('cm_200d', data,  dpi=600)   
```

```{figure} ./src/cm_200d.png
:width: 200px
:name: cm_200d

[Zapojenie](./src/cm_200d.ckt) jednoduchého rádia. 
```




## <font color='teal'> Štvorpól </font> 

V nasledujúcom príklade zapojenia štvorpólu je použitá vetva pre vykreslenie zeme, vyznačená červeno, {numref}`cm_200c`. Vo vetve je je automaticky vytvorená lokálna kópia premennej `Here`, ktorá je platná na polohovanie prvkov obvodu v rámci vetvy uzatvorenej medzi `{ ... }`. Po vykonaní kódu bloku je platná pôvodná hodnota `Here`. 


```{code-block}
:emphasize-lines: 12,13,14
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
```


```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

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

_ = cm_compile('cm_200c', data,  dpi=600)   
```

```{figure} ./src/cm_200c.png
:width: 450px
:name: cm_200c

[Zapojenie](./src/cm_200c.ckt) štvorpólu.
```
        
        
        
