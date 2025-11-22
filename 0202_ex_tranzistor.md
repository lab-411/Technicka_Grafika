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

Bipolárny tranzistor patrí medzi mnohopóly a okrem štandardných atribútov definaných pre plošné objekty má naviac atribúty pre určenie polohy vývodov báza, kolektora a emitora. Bipolárny tranzistor z knižnice `CircuitMacros` zobrazuje makro *bi_tr()*

```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)

Grid(12,2);
move to (.5,1);
hlf=0.5;

Q1:bi_tr(up_ );   
move right_ hlf
Q2:bi_tr(up_ ,R); 
move right_ hlf
Q3:bi_tr(up_,,,E)
move right_ hlf
Q4:bi_tr(up_,R,,E); 

move right_ hlf
Q5:bi_tr(up_,,P)
move right_ hlf
Q6:bi_tr(up_,R,P)
move right_ hlf
Q7:bi_tr(up_,,P,E)
move right_ hlf
Q8:bi_tr(up_,R,P,E)
'''

_ = cm_compile('./src/cm_202a', data, dpi=600 )   
```

```{figure} ./src/cm_202a.png
:width: 620px
:name: cm_202a

[Značka](./src/cm_202a.ckt) bipolárneho tranzistora *bi_tr()*.
```





    bi_tr(linespec,L|R,P,E);
    
    parametre:
    
      linespec             - orientácia a dĺžka prívodov
      L | R                - poloha bázy vlavo (L) alebo vpravo (R)
      N | P                - NPN / PNP
      E                    - púzdro tranzistora
      
    atribúty:
    
    .s   .w   .n.  .e      - stredy strán obrysu
    .sw  .se  .nw  .ne     - rohy obrysu
    .B                     - poloha bázy
    .E                     - poloha emitora
    .C                     - poloha kolektora

Pretože vývody tranzistora nie sú v mriežke, musíme  obvody s tranzistormi kresliť tak, že centrálnym prvkom zapojenie je tranzistor a ostatné komponenty ukladáme tak, že ich polohy a ak je to vhodné aj ich veľkosť určujeme voči polohám jeho vývodov. V nasledujúcom príklade je poloha rezistora odvodená od polohy vývodu bázy, dĺžka rezistora $R_{b1}$ je určená polohou značky zeme pri rezistore $R_e$. Pre popis spojovacieho bodu $V_b$ bolo použité makro *dlabel()*.

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


```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
    include(lib_base.ckt)
    include(lib_color.ckt)
    Grid(7,7);
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

_ = cm_compile('./src/cm_202b', data, dpi=600 )   
```

```{figure} ./src/cm_202b.png
:width: 350px
:name: cm_202b

[Obvod](./src/cm_202b.ckt) vykreslený s použitím relatívnych súradníc.
```


### <font color='brown'> Modifikácie značiek </font> 

Ak vyžadujeme aby vývody prvkov boli v presných a známich súradniciach (v mriežke) alebo máme špecifické požiadavky na tvar značky, najjednoduchším spôsobom je vytvorenie si makra značky vlastného prvku. V knižnici [lib_user.ckt](./src/lib_user.ckt) sú definované ekvivalenty bipolárnych tranzistorov *bjt_NPN()* a *bjt_PNP()*. Ako predloha pre zobrazenia bipolárnych tranzistorov boli použité značky z ručne kreslených zapojení pomocou šablón z československých odborných časopisov zo 70/80 rokov minulého storočia.


```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)
Grid(10, 2.5);

move to (0.5, 2);
bjt_NPN(1,1,L);
bjt_NPN(1,1,L,N);

bjt_PNP(1,1,L);
bjt_PNP(1,1,L,N);

move to (0.5, 0.5);
bjt_NPN(1,1,R);
bjt_NPN(1,1,R,N);

bjt_PNP(1,1,R);
bjt_PNP(1,1,R,N);

move to (7.5, 1.25);
Q1: bjt_NPN(1.5, 1, R);
"\textit{Q1}" at Q1.e;
"\textit{Q1.B}" at Q1.B rjust;
"\textit{Q1.E}" at Q1.E below; 
"\textit{Q1.C}" at Q1.C above; 
'''

_ = cm_compile('./src/cm_202c', data, dpi=600 )   
```

```{figure} ./src/cm_202c.png
:width: 550px
:name: cm_202c

Značky bipolárnych tranzistorov *bjt_NPN()* a *bjt_PNP()*
```

    bjt_NPN(length_ce, length_b, L|R|U|D, C|N)
    
    parametre:
    
      length_ce            - dĺžka prívodov medzi kolektoroma emitorom
      length_b             - dĺžka prívodu bázy
      L | R | U | P        - smer otočenia 
      C | N                - zobrazenie s púzdrom (C) a bez púzdra (N)
      
    atribúty:
    
    .s   .w   .n.  .e      - stredy strán obrysu
    .sw  .se  .nw  .ne     - rohy obrysu
    .B                     - poloha bázy
    .E                     - poloha emitora
    .C                     - poloha kolektora



Nasledujúci príklad ukazuje použitie modifikovaných značiek bipolárnych tranzistorov.  

```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

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

_ = cm_compile('./src/cm_202h', data, dpi=600 )   
```

```{figure} ./src/cm_202h.png
:width: 350px
:name: cm_202h

Jednoduchý [obvod](./src/cm_202d.ckt)  s bipolárnymi tranzistormi v súradnicovej mriežke.
```
Pomocou vlastných makier si môžeme vytvoriť nové alebo modifikované prvky pre tvorbu vlastného štýlu článkov, knižných publikácií alebo ak potrebujeme prekresliť nejaké staršie zapojenie a chceme dodržať pôvodný grafický štýl.   

```{figure} ./img/ar_1989_02.png
:width: 400px
:name: cm_090

Zapojenie z časopisu Amatérske rádio, ručne kreslené zapojenie pomocou šablón.
```

Pri prekreslovaní zapojenia v tomto príklade chceme dodržať podobný typ písma použitého na obrázku, ktorému sa najviac blíži šíkmé bezpätkové písmo typu *sans-serif*. Pre vykreslenie takto formátovaných textov si vytvoríme pomocné makro *itsf()*:

    # makro pre formatovanie textu
    define(`itsf', `"\textit{\textsf{$1}}"')   
    
    ...
    # použitie makra
    R4: resistor(from T1.E down_ 1.2,,E); 
        { 
            itsf(R4)  at R4.c + (-0.14, 0.15) rjust;  
            itsf(100) at R4.c + (-0.14,-0.15) rjust; 
        }   
    ...
    

```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

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

_ = cm_compile('./src/cm_202d', data, dpi=600 )   
```

```{figure} ./src/cm_202d.png
:width: 400px
:name: cm_202d

Prekreslený [obvod](./src/cm_202d.ckt) z predchádzajúceho obrázku.
```

 
Pre kreslenie vnútorného zapojenia integrovaných obvodov alebo zjednodušené zapojenia častí zapojení sa používajú značky tranzistorov bez púzdier a so skrátenými vývodmi. Pre presné umiestňovanie takýchto prvkov je potom potrebné použiť konštrukciu *with ... at* s deklarovaním vývodu, ku ktorému sa umiestnenie značky vzťahuje.

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

```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

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

_ = cm_compile('./src/cm_202e', data, dpi=600 )   
```

```{figure} ./src/cm_202e.png
:width: 380px
:name: cm_202e

[Použitie](./src/cm_202e.ckt) zjednodušených značiek tranzistorov.
```


Vnútorné zapojenia integrovaných obvodov sú často súčasťou katalógových listov a zobrazujú ekvivalentné zapojenie obvodu s diskrétnymi komponentami. Zapojenia často bývajú zjednodušené bez zobrazenia pomocných a parazitných prvkov pre lepšie pochopenie činnosti obvodu alebo jeho simuláciu, skutočná vnútorná štruktúra obvodu býva zvyčajne značne komplikovanejšia.


```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

data = r'''

include(lib_base.ckt)
include(lib_user.ckt)

#Grid(10,10);
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

_ = cm_compile('./src/cm_202f', data, dpi=600 )   
```

```{figure} ./src/cm_202f.png
:width: 600px
:name: cm_202f

[Príklad](./src/cm_202f.ckt) zobrazenia jednodušenej vnútornej štruktúru operačného zosilovača 741.
```

## <font color='teal'>  FET tranzistor </font> 

Pre zobrazenie štandardných MOSFET tranzistorov sú definované makrá *e_fet()* a *d_fet()*. Popis makier špeciálnych typov FET tranzistorov je uvedý v dokumentácii k programu.

```{code-cell} ipython3  
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
include(lib_base.ckt)
Grid(11.5,4);

# Usual defs...
move to (.6,3);
hlf=0.5;

Q1:e_fet(up_ ,,P,S);   
move right_ hlf
Q2:e_fet(up_ ,R); 
move right_ hlf
Q3:e_fet(up_,,P)
move right_ hlf
Q4:e_fet(up_,R,P); 

move right_ hlf
Q5:d_fet(up_)
move right_ hlf
Q6:d_fet(up_,R)
move right_ hlf
Q7:d_fet(up_,,P)
move right_ hlf
Q8:d_fet(up_,R,P)
 
move to (0.35,1);
e_fet(up_,,,S)
move right_ hlf
e_fet(up_,R,,S)
move right_ hlf
e_fet(up_,,P,S)
move right_ hlf
e_fet(up_,R,P,S)
move right_ hlf
d_fet(up_,,,S)
move right_ hlf
d_fet(up_,R,,S)
move right_ hlf
d_fet(up_,,P,S)
move right_ hlf
d_fet(up_,R,P,S)
'''

_ = cm_compile('./src/cm_202g', data, dpi=600 )   
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
      R                    - poloha gate vpravo (R), bez parametra vlavo
      P                    - vodivosť typu P-Kanál, bez parametra N-Kanál
      E|S                  - púzdro tranzistora (E), zjednodušená značka (S)
      
    atribúty:
    
    .s   .w   .n.  .e      - stredy strán obrysu
    .sw  .se  .nw  .ne     - rohy obrysu
    .G                     - poloha bázy
    .S                     - poloha source
    .D                     - poloha drain

