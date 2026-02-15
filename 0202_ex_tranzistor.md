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


# <font color='navy'> Tranzistory </font> 

## <font color='teal'>  Bipolárny tranzistor </font> 

Bipolárny tranzistor patrí medzi multipóly a okrem štandardných atribútov definaných pre plošné objekty má naviac atribúty pre určenie polohy vývodov bázy, kolektora a emitora. Bipolárny tranzistor z knižnice `CircuitMacros` zobrazuje makro *bi_tr()*, {numref}`cm_202a`:

    Q1:bi_tr(up_ );     Q2:bi_tr(up_ ,R);    Q3:bi_tr(up_,,,E);    Q4:bi_tr(up_,R,,E); 
    Q5:bi_tr(up_,,P);   Q6:bi_tr(up_,R,P);   Q7:bi_tr(up_,,P,E);   Q8:bi_tr(up_,R,P,E); 


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)

#Grid(12,2);
command"\sf"
move to (.5,1);
hlf=0.5;

Q1:bi_tr(up_ ); {"Q1" at Q1.n above; }
move right_ hlf
Q2:bi_tr(up_ ,R); {"Q2" at Q2.n above; }
move right_ hlf
Q3:bi_tr(up_,,,E); {"Q3" at Q3.n above; }
move right_ hlf
Q4:bi_tr(up_,R,,E); {"Q4" at Q4.n above; }

move right_ hlf
Q5:bi_tr(up_,,P); {"Q5" at Q5.n above; }
move right_ hlf
Q6:bi_tr(up_,R,P); {"Q6" at Q6.n above; }
move right_ hlf
Q7:bi_tr(up_,,P,E); {"Q7" at Q7.n above; }
move right_ hlf
Q8:bi_tr(up_,R,P,E); {"Q8" at Q8.n above; }
'''

_ = cm_compile('cm_202a', data, dpi=600 )   
```

```{figure} ./src/cm_202a.png
:width: 550px
:name: cm_202a

Značka bipolárneho tranzistora *bi_tr()*.
```


    bi_tr(linespec,L|R,P,E);
    
    parametre:
    
      linespec             - orientácia a dĺžka prívodov
      L | R                - poloha bázy vľavo (L) alebo vpravo (R)
      N | P                - NPN / PNP
      E                    - púzdro tranzistora
      
    atribúty:
    
    .s   .w   .n.  .e      - stredy strán obrysu
    .sw  .se  .nw  .ne     - rohy obrysu
    .B                     - poloha bázy
    .E                     - poloha emitora
    .C                     - poloha kolektora

    

Pretože vývody tranzistora nie sú v usporiadané mriežke, musíme obvody s tranzistormi kresliť tak, že centrálnym prvkom zapojenie je tranzistor a ostatné komponenty ukladáme tak, že ich polohy, a ak je to vhodné aj ich veľkosť určujeme voči polohám jeho vývodov. V nasledujúcom príklade, {numref}`cm_202b`, je poloha rezistora odvodená od polohy vývodu bázy, dĺžka rezistora $R_{b1}$ je určená polohou značky zeme pri rezistore $R_e$. Pre popis spojovacieho bodu $V_b$ bolo použité makro *dlabel()*.

```{code-block}
:emphasize-lines: 7,8,9
    ...
T1: bi_tr(2, L, N,E); 
    resistor(from T1.E down_ 1.5,,E); rlabel(,R_e,);
GN: gnd;                           # zem
    ...
    line from T1.B left_ 0.8;      # poloha Here
D1: dot; dlabel(0,0,,V_b,,AL);     # spojovaci bod a popis
    resistor(from D1 down_ (D1.y - GN.n.y),,E); rlabel(,R_{b1},);
    gnd;
    ...
```

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
    include(lib_base.ckt)
    include(lib_color.ckt)
    #Grid(7,7);
    move to (4,2)
    up_;
T1: bi_tr(2, L, N,E); 
    resistor(from T1.E down_ 1.5,,E); rlabel(,R_e,);
GN: gnd;

RC: resistor(from T1.C up_ 1.5,,E); llabel(,R_c,);
DC: dot;
    tconn(0.75,O); clabel(,,V_+); 
    
    color_red
    line from T1.B left_ 0.8; 
D1: dot; dlabel(0,0,,V_b,,AL);
    resistor(from D1 down_ (D1.y - GN.n.y),,E); rlabel(,R_{b1},);
    gnd;
    color_black;
    
    resistor(from D1 up_ (RC.end.y - D1.y),,E); llabel(,R_{b2},); 
    line to DC;

    capacitor(from D1 left_ 1.5); rlabel(,C_{b},); 
    tconn(0.5,O); rlabel(,V_{in},);

    move to T1.C; 
D2: dot; dlabel(0,0,,V_c,,R);
    capacitor(from D2 right_ 1.5); llabel(,C_{c},); 
    tconn(0.5,O); llabel(,V_{out},);

    move to T1.E; 
D3: dot; dlabel(0,0,,V_e,,R); 
    line right_ 1;
    capacitor(down_ 1.5); llabel(,C_{e},); 
    gnd;
'''

_ = cm_compile('cm_202b', data, dpi=600 )   
```

```{figure} ./src/cm_202b.png
:width: 350px
:name: cm_202b

[Obvod](./src/cm_202b.ckt) vykreslený s použitím relatívnych súradníc.
```


### <font color='brown'> Modifikácie značiek </font> 

Ak vyžadujeme, aby vývody prvkov boli v presných a známych súradniciach (v mriežke) alebo máme špecifické požiadavky na tvar značky, najjednoduchším spôsobom je vytvorenie si makra značky vlastného prvku. V knižnici [lib_user.ckt](./src/lib_user.ckt) sú definované ekvivalenty bipolárnych tranzistorov *bjt_NPN()* a *bjt_PNP()*. Ako predloha pre zobrazenia bipolárnych tranzistorov boli použité značky z ručne kreslených zapojení pomocou šablón z československých odborných časopisov zo 70/80 rokov minulého storočia, {numref}`cm_202c`:

    Q1:bjt_NPN(1,1,L);    Q2:bjt_NPN(1,1,L,N);   Q3:bjt_PNP(1,1,L);  Q4:bjt_PNP(1,1,L,N);
    Q5:bjt_NPN(1,1,R);    Q6:bjt_NPN(1,1,R,N);   Q7:bjt_PNP(1,1,R);  Q8:bjt_PNP(1,1,R,N);

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)
command"\sf"
#Grid(10, 2.5);

move to (0.5, 2);
Q1:bjt_NPN(1,1,L);   {"Q1" at Q1.n above; }
Q2:bjt_NPN(1,1,L,N); {"Q2" at Q2.n above; }

Q3:bjt_PNP(1,1,L);   {"Q3" at Q3.n above; }
Q4:bjt_PNP(1,1,L,N); {"Q4" at Q4.n above; }

move to (0.5, 0.5);
Q5:bjt_NPN(1,1,R);   {"Q5" at Q5.s below; }
Q6:bjt_NPN(1,1,R,N); {"Q6" at Q6.s below; }

Q7:bjt_PNP(1,1,R);   {"Q7" at Q7.s below; }
Q8:bjt_PNP(1,1,R,N); {"Q8" at Q8.s below; }

move to (9, 1.25);
Q10: bjt_NPN(1.5, 1, R);
"\textit{Q10}" at Q10.e;
"\textit{Q10.B}" at Q10.B rjust;
"\textit{Q10.E}" at Q10.E below; 
"\textit{Q10.C}" at Q10.C above; 
'''

_ = cm_compile('cm_202c', data, dpi=600 )   
```

```{figure} ./src/cm_202c.png
:width: 550px
:name: cm_202c

Upravené značky bipolárnych tranzistorov *bjt_NPN()* a *bjt_PNP()*
```

    bjt_NPN(length_ce, length_b, L|R|U|D, C|N)
    
    parametre:
    
      length_ce            - dĺžka prívodov medzi kolektorom a emitorom
      length_b             - dĺžka prívodu bázy
      L | R | U | P        - smer otočenia 
      C | N                - zobrazenie s púzdrom (C) a bez púzdra (N)
      
    atribúty:
    
    .s   .w   .n.  .e      - stredy strán obrysu
    .sw  .se  .nw  .ne     - rohy obrysu
    .B                     - poloha bázy
    .E                     - poloha emitora
    .C                     - poloha kolektora



Nasledujúci príklad, {numref}`cm_202h`,  ukazuje použitie modifikovaných značiek bipolárnych tranzistorov:

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)

Grid(6.5,7);
linethick = 1;
move to (3.5,1.5);
up_;
T2:  bjt_NPN(1,1.5, R);  {"$Q_2$" at T2.e; }
     move to Here+(0, 2)
T1:  bjt_PNP(1, 1.5, R); {"$Q_1$" at T1.e; }

R1:  resistor(from T2.E down_ 1.5,,E); llabel(,R_e,);

     line from T1.C down_ 0.25; line down_ 0.75; b_current(i_1,above_, );
DT1: dot;
     line down_ 0.25; line to T2.C; b_current(i_2,above_,);
     line from DT1 right_ 1; tconn(0.5,O); "$V_{out}$" ljust;
     
R2: resistor(from T1.E up_ 1.5,,E); rlabel(,R_e,);
    
     move to T2.B; 
DT2: dot;  # stred, vstup

     resistor(from DT2 up_ 1.5,,E); llabel(,3R,);
DT4: dot;
     resistor(from DT4 to T1.B,,E); llabel(,3R,);
DT5: dot;  # baza T1
R3:  resistor(from DT2 down_ 2,,E); rlabel(,R,);

     line from R3.end to R1.end;  
     dot; right_; line -> 1; "$V-$" ljust;

R4: resistor(from DT5 up_ 2,,E); llabel(,R,);
    line from R4.end to R2.end;
    dot;  right_; line -> 1; "$V+$" ljust;

    line from DT4 left_ 1; tconn(0.5,O); "$V_{in}$" rjust;
'''

_ = cm_compile('cm_202h', data, dpi=600 )   
```

```{figure} ./src/cm_202h.png
:width: 350px
:name: cm_202h

Jednoduchý [obvod](./src/cm_202d.ckt)  s bipolárnymi tranzistormi v súradnicovej mriežke.
```
Pomocou vlastných makier si môžeme vytvoriť nové alebo modifikované prvky pre tvorbu vlastného štýlu článkov, knižných publikácií alebo ak potrebujeme prekresliť nejaké staršie zapojenie a chceme dodržať pôvodný grafický štýl, {numref}`cm_090`:

```{figure} ./img/ar_1989_02.png
:width: 400px
:name: cm_090

Zapojenie z časopisu Amatérske rádio, ručne kreslené zapojenie pomocou šablón.
```

Pri prekreslovaní zapojenia,{numref}`cm_202d`, v tomto príklade chceme dodržať podobný typ písma použitého na obrázku, ktorému sa najviac blíži šíkmé bezpätkové písmo typu *sans-serif*. Pre vykreslenie takto formátovaných textov si vytvoríme pomocné makro *itsf()*.

```{code-block}
:caption: Makro pre formátovanie textu
:emphasize-lines: 1,7,8
define(`itsf', `"\textit{\textsf{$1}}"')   

...
# použitie makra
R4: resistor(from T1.E down_ 1.2,,E); 
    { 
        itsf(R4)  at R4.c + (-0.14, 0.15) rjust;  
        itsf(100) at R4.c + (-0.14,-0.15) rjust; 
    }   
...
``` 



 
```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''

include(lib_base.ckt)
include(lib_user.ckt)
include(lib_color.ckt)
define(`itsf', `"\textit{\textsf{$1}}"')


linethick = 1;
move to (3,2);
T1: bjt_NPN(1.2); 
    move to Here+(1.5,0);
T2: bjt_NPN(1.2); 

color_red;
R4: resistor(from T1.E down_ 1.2,,E); 
    { itsf(R4)  at R4.c + (-0.14, 0.15) rjust;  
      itsf(100) at R4.c + (-0.14,-0.15) rjust; 
    }
color_black;
DT1: dot;
move to T1.E;
     dot;
     line from T1.E to T2.E;

move to T1.C;
     dot;
 R2: resistor(from T1.C up_ 1.2,,E);
     { itsf(1k) at R2.c + (-0.15,0) rjust; 
       itsf(R2) at R2.c + ( 0.15,0) ljust; 
    }
    dot;
 R3: resistor(from T1.C right_ 1.9,,E);
     { itsf(R3) at R3.c  + (0, 0.15) above; 
       itsf(2k2) at R3.c + (0,-0.15) below;
     } 
     line down_ (Here.y - T2.B.y) then to T2.B;

move to T2.C;
     dot;
 R5: resistor(from T2.C up_ 1.2,,E);
     { itsf(R5) at R5.c + (-0.15, 0.15) rjust ; 
       itsf(1k) at R5.c +  (-0.15,-0.15) rjust ; 
    }
    dot;

 R1: resistor(from T1.B left_ 1,,E);
     { itsf(R1) at R1.c  + (0, 0.15) above; 
       itsf(10k) at R1.c + (0,-0.15) below;
     }

    line from R2.end to R5.end;
    line from R2.end left_ 2.5; C1: circle rad 0.08;  itsf(1) at last circle.w rjust;
    line from R4.end left_ 2.5;     circle rad 0.08;  itsf(6) at last circle.w rjust;
    line from T2.C right_ 1.5;  C33:circle rad 0.08;  itsf(3) at last circle.e ljust;
    line from R5.end right_ 1.5;C11:circle rad 0.08;  itsf(1) at last circle.e ljust;
    line from R4.end right_ 4.5;    circle rad 0.08;  itsf(6) at last circle.e ljust;
    line from R1.end left_ 0.5; C3: circle rad 0.08;  itsf(3) at last circle.w rjust;
    itsf(VST)     at (C1+C3)/2 + (0,-0.5);
    itsf(VÝST)    at (C11+C33)/2;
    itsf(2xKC238) at R2.end above ljust;
    itsf(T1) at T1.e + (-0.1,0);
    itsf(T2) at T2.e + (-0.1,0);

'''

_ = cm_compile('cm_202d', data, dpi=600 )   
```

```{figure} ./src/cm_202d.png
:width: 400px
:name: cm_202d

Prekreslený [obvod](./src/cm_202d.ckt) z predchádzajúceho obrázku.
```

 
Pre kreslenie vnútorného zapojenia integrovaných obvodov alebo zjednodušené zapojenia častí zapojení sa používajú značky tranzistorov bez púzdier a so skrátenými vývodmi. Pre presné umiestňovanie takýchto prvkov je potom potrebné použiť konštrukciu *with ... at* s deklarovaním vývodu, ku ktorému sa umiestnenie značky vzťahuje, {numref}`cm_202e`:


```{code-block}
:caption: Použitie konštrukcie *with ... at*
:emphasize-lines: 6
    ...
    line up_ 0.8; 
DV: dot;

    # umiestnenie T11 s emitorom do bodu DV
T11: bjt_NPN(1,1,R,N) with .E at Here;   
    line from T11.B left_ 0.8;
    
    # T1 s redukovanou dlzkou vyvodov medzi kolektorom a emitorom 
T1: bjt_NPN(0.6,1,R,N) with .E at Here;  

    # pripojenie odporu R1 s dĺžkou určenou polohou emitorov T1 a T11
    resistor(from T11.E left_ (T11.E.x - T1.E.x),,E); {llabel(,R_1,);}
    line to T1.E; dot;
    ...
```


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''

include(lib_base.ckt)
include(lib_user.ckt)
include(lib_color.ckt)

     move to (3,1);
T2:  bjt_PNP(0.6,1,R,N); {"$T2$" at T2.c + (-0.4, 0.5);}

     line from T2.E right 0.8; 
T22: bjt_PNP(1,1,R,N);    {"$T22$" at T22.e;}
     resistor(from T22.E left_ (T22.E.x - T2.E.x),,E); {rlabel(,R_2,);}
     line to T2.E; dot;

     line from T2.C right_ -(Here.x - T22.C.x); 
     dot; {line -> down_ 0.8;  "V-" below; }
     line to T22.C;

     move to T22.E; dot;
     line up_ 0.8; 
     dot; {line right_ 1.5; C1: circle rad 0.1}
     line up_ 0.8; 
     color_red;
DV:  dot;   { line <- from Here+(.1,0) to Here+(1,0); "DV" at Here ljust; }
     

T11: bjt_NPN(1,1,R,N) with .E at Here;     {"$T11$" at T11.e;}
     line from T11.B left_ 0.8;
T1:  bjt_NPN(0.6,1,R,N) with .E at Here;  {"$T1$" at T1.c + (-0.4, 0.5);}
     resistor(from T11.E left_ (T11.E.x - T1.E.x),,E); {llabel(,R_1,);} 
     line to T1.E; dot;
     color_black;
     
     line from T1.C right_ -(Here.x - T11.C.x); 
     dot; {line -> up_ 0.8;  "V+" above; }
     line to T11.C

     move to T1.B;
     down_;
DC:  dc_source( (T1.B.y - C1.c.y), 0.8, P); { line <- from DC.C.c+(-0.5,-0.5) to DC.C.c+(-0.5,0.5) "$V_1$" rjust}
     dot; {line left_ 1.5; C2: circle rad 0.1;}
     line to T2.B;

     line -> from C1.c + (0, -0.2) down_ 1 "$V_{out}$" ljust; circle rad 0.1 at Here + (0, -0.2); line down_ 0.25; gnd;
     line -> from C2.c + (0, -0.2) down_ 1 "$V_{in}$" ljust; circle rad 0.1 at Here + (0, -0.2); line down_ 0.25; gnd;
'''

_ = cm_compile('cm_202e', data, dpi=600 )   
```

```{figure} ./src/cm_202e.png
:width: 380px
:name: cm_202e

[Použitie](./src/cm_202e.ckt) zjednodušených značiek tranzistorov.
```


Vnútorné zapojenia integrovaných obvodov sú často súčasťou katalógových listov a zobrazujú ekvivalentné zapojenie obvodu s diskrétnymi komponentami. Zapojenia často bývajú zjednodušené bez zobrazenia pomocných a parazitných prvkov pre lepšie pochopenie činnosti obvodu alebo jeho simuláciu, {numref}`cm_202f`. Skutočná vnútorná štruktúra obvodu býva zvyčajne značne komplikovanejšia.


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''

include(lib_base.ckt)
include(lib_user.ckt)

move to (2,2);

T3: bjt_NPN(0.6, 1, L, N); {"$T_3$" at T3.w ljust};  dot;
T4: bjt_NPN(0.6, 1, R, N); {"$T_4$" at T4.e rjust};

resistor(down_ 1.5 from T3.E,,E); rlabel(,1k,); line -> down_ 0.5; "$-$" at last line.end  below rjust
resistor(down_ 1.5 from T4.E,,E); llabel(,1k,); line -> down_ 0.5; "$-$" at last line.end  below rjust

# kolektory vstupn0ho dielu
move to T3.C; 
line up_ 0.75; 
Q3: dot; {line to (T3.B, Here) then to T3.B;}
line up_ 2;
T1: bjt_PNP(0.6, 1, R, N) with .C at Here; "$T_1$" at T1.e rjust;

move to T4.C; 
line to (Here, Q3); 
Q4: dot;
line up_ to (Here, T1.C);
T2: bjt_PNP(0.6, 1, L, N) with .C at Here; "$T_2$" at T2.w ljust;

line  from T1.E right_ (T2.E.x - T1.E.x)/2; dot; 
{reversed(`source',up_ 2,I); llabel(,I_k = 20 \mu A,);line -> up_ 0.5; "$+$" at last line.end ljust; }
line to T2.E;

# vstupne terminaly
line from T1.B left_ 0.5;
C1: circle rad 0.1;
 line -> from C1.c + (0, -0.2) down_ 0.75 "$U_{N}$" ljust; circle rad 0.1 at Here + (0, -0.2); line down_ 0.25; gnd;

line from T2.B right_ 0.5;
C2: circle rad 0.1;
 line -> from C2.c + (0, -0.2) down_ 0.75 "$U_{P}$" ljust; circle rad 0.1 at Here + (0, -0.2); line down_ 0.25; gnd;

# koncovy stupen
line from Q4 right_ 2.5; b_current("$I_1$",below_,,E,1);
QQ: dot; line 0.15;

T5: bjt_NPN(.6,1,R,N);  {"$T_5$" at T5.e rjust};
line from T5.E right_ 0.05;
T6: bjt_NPN(.6,1,R,N);  {"$T_6$" at T6.e rjust};
line -> from T6.E down_ 1; "$-$" at last line.end  below rjust
line from T5.C to (T6.C, T5.C); dot; {line to T6.C;}
line up_ 1;
Q5: dot; {diode(up_ 0.5, ,R); diode(up_ 0.5, ,R); DD: dot;}
line right_ 0.5; 
T8: bjt_PNP(1,1,R,N);  {"$T_8$" at T8.e rjust};
    move to T8.E; dot; line right_ 1; C3: circle rad 0.1;
    line -> from C3.c + (0, -0.2) down_ 0.75 "$U_{a}$" ljust; circle rad 0.1 at Here + (0, -0.2); line down_ 0.25; gnd;
T9: bjt_NPN(1,1,R,N) with .E at T8.E;  {"$T_9$" at T9.e rjust};
    line from T9.B to DD;

LA: line from Q5 left_ 0.95 dashed;
LB: line from QQ up_ to (QQ,Q5) then right_ 0.95 dashed;
CC: capacitor(from LA.end to LB.end ); llabel(,C_k,); rlabel(,30pF,)

# napajanie koncoveho stupna
line -> from T8.C down_ 0.75; "$-$" at last line.end rjust;
line -> from T9.C up_   0.75; "$+$" at last line.end rjust;
move to DD;
{reversed(`source',up_ 2,I); llabel(,I_2 = 300 \mu A,);line -> up_ 0.5; "$+$" at last line.end ljust; }

'''

_ = cm_compile('cm_202f', data, dpi=600 )   
```

```{figure} ./src/cm_202f.png
:width: 600px
:name: cm_202f

[Príklad](./src/cm_202f.ckt) zobrazenia jednodušenej vnútornej štruktúru operačného zosilovača 741.
```

## <font color='teal'>  FET tranzistor </font> 

Pre zobrazenie štandardných diskrétnych MOSFET tranzistorov sú v `CircuitMacros` definované makrá pre základné typy *e_fet()* a *d_fet()*, {numref}`cm_202g`:

     Q1:e_fet(up_ ,,P,);  Q2:e_fet(up_ ,R,,);   Q3:e_fet(up_,,P);     Q4:e_fet(up_,R,P);
     Q5:d_fet(up_);       Q6:d_fet(up_,R);      Q7:d_fet(up_,,P);     Q8:d_fet(up_,R,P);
    
     Q9:e_fet(up_,,,S);  Q10:e_fet(up_,R,,S);  Q11:e_fet(up_,,P,S);  Q12:e_fet(up_,R,P,S);
    Q13:d_fet(up_,,,S);  Q14:d_fet(up_,R,,S);  Q15:d_fet(up_,,P,S);  Q16:d_fet(up_,R,P,S);


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

#Grid(11.5,4);
command"\sf"

# Usual defs...
move to (.6,3);
hlf=0.5;

Q1:e_fet(up_ ,,P,); {"Q1" at Q1.n above;}
move right_ hlf
Q2:e_fet(up_ ,R,,); {"Q2" at Q2.n above;}
move right_ hlf
Q3:e_fet(up_,,P);   {"Q3" at Q3.n above;}
move right_ hlf
Q4:e_fet(up_,R,P);  {"Q4" at Q4.n above;}
move right_ hlf
Q5:d_fet(up_);      {"Q5" at Q5.n above;}
move right_ hlf
Q6:d_fet(up_,R);    {"Q6" at Q6.n above;}
move right_ hlf
Q7:d_fet(up_,,P);   {"Q7" at Q7.n above;}
move right_ hlf
Q8:d_fet(up_,R,P);  {"Q8" at Q8.n above;}
 
 
move to (0.35,1);  
Q9: e_fet(up_,,,S);   {"Q9" at Q9.s below;}
move right_ hlf
Q10: e_fet(up_,R,,S); {"Q10" at Q10.s below;}
move right_ hlf
Q11: e_fet(up_,,P,S); {"Q11" at Q11.s below;}
move right_ hlf
Q12: e_fet(up_,R,P,S); {"Q12" at Q12.s below;}
move right_ hlf
Q13: d_fet(up_,,,S);  {"Q13" at Q13.s below;}
move right_ hlf
Q14: d_fet(up_,R,,S); {"Q14" at Q14.s below;}
move right_ hlf
Q15: d_fet(up_,,P,S);  {"Q15" at Q15.s below;}
move right_ hlf
Q16: d_fet(up_,R,P,S);  {"Q16" at Q16.s below;}
'''

_ = cm_compile('cm_202g', data, dpi=600 )   
```

```{figure} ./src/cm_202g.png
:width: 600px
:name: cm_202g

Značky MOSFET tranzistorov *e_fet()* a *d_fet()*
```


    e_fet(linespec,R,P,E|S)  - enhancement MOSFET
    d_fet(linespec,R,P,E|S)  - depletion MOSFET 
    
    parametre:
    
      linespec             - orientácia a dĺžka prívodov
      R                    - poloha gate vpravo (R), bez parametra vľavo
      P                    - vodivosť typu P-Kanál, bez parametra N-Kanál
      E|S                  - púzdro tranzistora (E), zjednodušená značka (S)
      
    atribúty:
    
    .s   .w   .n.  .e      - stredy strán obrysu
    .sw  .se  .nw  .ne     - rohy obrysu
    .G                     - poloha bázy
    .S                     - poloha source
    .D                     - poloha drain

Pri kreslení vnútornej štruktúry CMOS integrovaných obvodov sa v zapojeniach vyskytujú prepojenia, ktoré nemajú analógiu v diskrétnych komponentoch a vyplývajú z topológie obvodu. Príkladom môže byť formálne pripojenie substrátu tranzistora Q3 v nasledujúcom zapojení, {numref}`cm_202u`, pri ktorom bolo použité makro *mosfet()*. Makro umožnuje kreslenie špeciálnych modifikácií FET tranzistorov, detailný popis makra uvedený v [dokumentácii](./data/Circuit_macros_10_6.pdf).

    Q3: mosfet(down_,R,uMEDSuB) with .S at last line.end; { "Q3" at Q3.nw ljust;}

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)
include(lib_color.ckt)
command"\sf"

#----------------------------------------------------
# NAND
Q1: e_fet(down_,R,P); { "Q1" at Q1.nw ljust; }
Q2: e_fet(down_, ,P) at Q1.c + (1.5,0); { "Q2" at Q2.ne rjust; }
    line from Q2.S to Q1.S;
    dot; up_; power(1, $\sf V_{dd}$)
    line from Q2.D to Q1.D;
    dot;
    line down_ 0.5;
DT1:dot;
    line down_ 0.25;
#Q3: e_fet(up_,,S) with .D at last line.end;

    color_red;
Q3: mosfet(down_,R,uMEDSuB) with .S at last line.end;  { "Q3" at Q3.nw ljust; }
    color_black;
    
Q4: e_fet(up_,,) with .D at Q3.D; { "Q4" at Q4.nw ljust; }
DT2:dot(at Q4.S);
    gnd(0.5) 
    
    line from Q3.B right_ 0.5;
    line to (Here, DT2) then to DT2;
    
    line from Q3.G left_ 0.5; 
    dot; {line left_ 1; tbox("A",,, <) }
    line to (Here, Q1.G) then to Q1.G
    
    line from Q4.G left_ 0.5;
    dot; {line left_ 1; tbox("B",,, <) }
    line down_ 1.5; 
    line to (Q2.G+(0.25,0), Here);
    line to (Here, Q2.G) then to Q2.G;

#-----------------------------------------------------------
# invertor
    line from DT1 right 3;
DT3:dot;
    line up_ 1.2 then right_ 0.25;
Q5: e_fet(down_,R,P) with .G at last line.end;   
    line from DT3 down_ 1.2 then right_ 0.25;
Q6: e_fet(up_,,) with .G at last line.end;
    gnd(0.5) at Q6.S;
    power(1, $\sf V_{dd}$) at Q5.S;
    line from Q5.D to Q6.D;
DT4:0.5 between Q5.D and Q6.D; 
    dot(at DT4); line right_ 1; {tbox("Y");}  
'''

_ = cm_compile('cm_202u', data, dpi=600 )   
```

```{figure} ./src/cm_202u.png
:width: 400px
:name: cm_202u

[Zapojenie](./src/cm_202u.ckt) hradla AND v technológii CMOS.
```

Niektorí výrobcovia mikrokontrolérov používajú pre zjednodušený popis funkcie častí logického obvodu kombinovanú značku FET tranzistora, ktorá namiesto jeho štruktúry zobrazuje jeho vzťah k ostatným častiam zapojenia. Tranzitor s vodivosťou typu P je zobrazený s krúžkom na hradle, čo znamená, že bude otvorený pri privedení signálu s úrovňou **L** na jeho hradlo, 
{numref}`cm_202v`:

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)
include(lib_color.ckt)
command"\sf"
up_
move to (3.5,5)

    gnd();
Q1: fet_N(1.5,L);
    dot; {line right_ 1; tbox("Port Pin",1.5); }
Q2: fet_P(1.5,L);
    power(0.5, $\sf V_{cc}$)

    line from Q2.G left_ 0.5;
    line to (Here, Q1.G);
    dot; {line left_ 0.5; tbox("Digital Out",2,,<); }
    line to Q1.G
    circle at Q2.c - (2.5,0) rad 0.25 "A"


move to (11.5,5)
    up_;
    gnd();
Q3: fet_N(1.5,L);
    dot; {line right_ 1; tbox("Port Pin",1.5); }
Q4: fet_P(1.5,L);
    power(0.5, $\sf V_{cc}$)
R1: resistor(left_ 1 from Q3.G,E)
R2: resistor(left_ 1 from Q4.G,E)
    line 0.5 from R2.end;
    line to (Here, R1.end);
    dot; {line left_ 0.5; tbox("Digital Out",2,,<); }
    line to R1.end;
    circle at Q4.c - (3,0) rad 0.25 "B"


move to (3.5, 0)

    up_;
    gnd;
    resistor(1.5, E); rlabel(,\sf R_{PD},)
    dot; 
    {
        {line left_ 1.5; tbox("Digital In",2,, >);}
        line right_ 1;
        tbox("Port Pin",1.5); 
    }
Q5: fet_P(1.5,L);
    power(0.5, $\sf V_{cc}$);
    {line from Q5.G left_ 1; tbox("Digital Out",2,,<); }
    circle at Q5.c - (2.5,-1) rad 0.25 "C";


move to (11.5, 0)
    up_;
    gnd;
Q6: fet_N(1.5,L);
    dot; 
    {
        {line left_ 1.5; tbox("Digital In",2,, >);}
        line right_ 1;
        tbox("Port Pin",1.5); 
    }
    resistor(up_ 1.5, E); rlabel(,\sf R_{PU},)
    power(0.5, $\sf V_{cc}$);
    {line from Q6.G left_ 1; tbox("Digital Out",2,,<); }
    circle at Q6.c - (2.5,-2) rad 0.25 "D";
'''

_ = cm_compile('cm_202v', data, dpi=600 )   
```

```{figure} ./src/cm_202v.png
:width: 600px
:name: cm_202v

[Konfigurácie](./src/cm_202v.ckt) koncového stupňa pinu portu mikrokontroléra.
```

