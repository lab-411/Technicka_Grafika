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

# <font color='navy'> Dvojpóly</font>

Základné elektronické komponenty (R,L,C, dióda, zdroje ...) sú v `CircuitMacros` reprezentované ako dvojpóly. Na ich pripojenie do elektrického obvodu sú použité dva uzly. Typ dvojpólu je určený menom a jeho vzhľad je možno meniť parametrami. Pre každý dvojpól je možné v zapojení zadať jeho meno, hodnotu alebo typ a v prípade potreby aj označenie vývodov. Všeobecný formát makra pre zobrazenie dvojpólov má tvar

    [reference:] object([linespec], [parameters ...]);
    
    reference  - označenie objektu pre prístup k jeho parametrom
    object     - typ dvojpólu (resistor, capacitor ...)
    linespec   - dĺžka prívodov a umiestnenie objektu
    parameters - parametre určujúce tvar objektu
    
Pri použití makra bez parametrov sa vykreslí dvojpól v prednastavenom tvare.
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here;             R1: resistor(2,,E);  llabel(,R_1,); "re\\sistor(2,,E)" at R1.start rjust;
move to Origin + (0,1);   C1: capacitor(2);    llabel(,C_1,); "ca\\pacitor(2)" at C1.start rjust;
move to Origin + (0,2);   L1: inductor(2);     llabel(,L_1,); "in\\ductor(2)" at L1.start rjust;
move to Origin + (0,3);   D1: diode(2);        llabel(,D_1,); "di\\ode(2)" at D1.start rjust;

move to Origin + (3,3);   F1: fuse(2);         llabel(,F_1,); "fu\\se(2)" at F1.end ljust;
move to Origin + (3,2);   J1: jumper(2);       llabel(,X_1,); "ju\\mper(2)" at J1.end ljust;
move to Origin + (3,1);   S1: source(2);       "sour\\ce(2)" at S1.end ljust;
move to Origin + (3,0);   B1: battery(2);      "ba\\ttery(2)" at B1.end ljust;
'''

_ = cm_compile('cm_0100a', data,  dpi=600)   
```

```{figure} ./src/cm_0100a.png
:width: 480px
:name: cm_0100a

Príklady dvojpólov. 
```

Základné rozmery a tvar dvojpólov v knižniciach `CircuitMacros` sú zobrazené na nasledujúcom obrázku. Rozmery objektu závisia od aktuálneho nastavenia parametrov prostredia, ktoré sú popísané v kapitole **Prostredie**.

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_color.ckt)
linewid = 2.0*2.54;
command "\tt"

linethick_(1.5);
L1: inductor(elen_,L);

# ohranicenie prvku
color_dark_green;
thinlines_;
box dotted wid last [].wid ht last [].ht at last [];
move to .85 between last [].sw and last [].se;

# popis atributov
#spline <- down arrowht*2.9 right arrowht/2 then right 0.15; " last []" ljust;

color_blue;
arrow <- down 0.8 from L1.start chop 0.05; "L1.start" below;
arrow <- down 0.8 from L1.end chop 0.05;   "L1.end"   below;
arrow <- down last [].c.y-last arrow.end.y from L1.c; "L1.centre" below;

# popis rozmerov
color_red;
dimension_(from L1.start to L1.end,1.5,elen\_,1);
dimension_(right_ dimen_ from L1.c-(dimen_/2,0),1,dimen\_,1.2);
'''

_ = cm_compile('cm_0100j', data, dpi=600)   
```

```{figure} ./src/cm_0100j.png
:width: 450px
:name: cm_0100j

Rozmery dvojpólu a jeho atribúty.
```


Vlastnosti dvojpólov potom popisujú nasledujúce parametre 
    
    premenné
    
      dimen_    - veľkosť prvku určená na základe parametrov kresliacej plochy 
      elen_     - dĺžka vývodov prvku, štandardne 1.5*dimen_
    
    atribúty
    
      .start   - súradnice začiatku vykresľovania prvku
      .centre  - súradnice stredu prvku
      .end     - súradnice ukončenia vykresľovania prvku
        
        
Definície najčastejšie používaných dvojpólov - rezistor, kondenzátor, cievka, dióda a zdroj sú uvedené v nasledujúcich kapitolách. Kompletný zoznam makier pre kreslenie dvojpólov a ich parametrov je v [dokumentácii](./data/Circuit_macros_10_6.pdf). 


## <font color='teal'> Rezistor </font>

Makro pre zobrazenie rezistora v `CircuitMacros` je možné parametrami upraviť pre zobrazenie rôznych typov príbuzných prvkov. Definícia makra pre vykreslenie rezistora

    rezistor(linespec, n, param, cwidth);
    
    parametre:
    
        linespec - dĺžka a umiestnenie rezistora
    
        n        - pocet cyklov rezistora v anglos. zobrazeni (default 3) 
    
        param    - typ rezistora
                    E   - box, európske označenie
                    ES  - box prečiarknutý
                    Q   - posunute anglos. zobrazenie 
                    H   - štvorcove zobrazenie - výkonovy rezistor
                    V   - varistor
    
        cwidth   - rozmer cyklov rezistora v anglos. zobrazení 
        

Makro bez parametrov vykreslí rezistor s prednastavenými hodnotami ako značku rezistora v anglosaskej notácii.

    R1: resistor;       R2: resistor(3,6,);   R3: resistor(,,Q);   R4: resistor(,,H);      
    R5: resistor(,,E);  R6: resistor(,,ES);   R7: resistor(,,V);   R8: resistor(3,,E,1.5);    


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 
move to (0.5, 1.5);   

resistor;           llabel(,R_1,); 
resistor(3,6,);     llabel(,R_2,); rlabel(,n=6,);  
resistor(,,Q);      llabel(,R_3,);   
resistor(,,H);      llabel(,R_4,); 

move to (0.5, 0.25); 

resistor(,,E);      llabel(,R_5,); 
resistor(,,ES);     llabel(,R_6,); 
resistor(,,V);      llabel(,R_7,); 
resistor(3,,E,1.5); llabel(,R_8,); rlabel(,linespec=3,);
'''

_ = cm_compile('cm_0100b', data, dpi=600)   
```

```{figure} ./src/cm_0100b.png
:width: 450px
:name: cm_0100b

Typy rezistorov.
```

```{warning} 
 Medzery pred parametrom makra sú ignorované, v niektorých prípadoch ale môžu byť medzery za parametrom pokladané za súčasť parametra makra. Je preto vhodné zadávať parametre makier bez medzier.
    
    resistor(,, E );       # chyba, ignorovanie parametra E
    resistor(,,E);         # správne vykreslenie rezistora 
    
```


## <font color='teal'> Kondenzátor </font>

Kondenzátor je orientovaný dvojpól, preto okrem jeho typu môžeme parametrom **Rev** zvoliť jeho polaritu. Pomocou parametrov **height** a **width** môžeme upraviť veľkosť a vzdialenosť elektród.  

    capacitor(linespec, chars, [Rev], height, width)
    
    parametre:
    
        linespec - dĺžka a umiestnenie kondenzátora
        
        chars    - typ kondenzátoea
                    F or blank: flat plate
                    dF flat plate with hatched fill
                    C curved-plate
                    dC curved-plate with variability arrowhead
                    CP constant phase element
                    E polarized boxed plates
                    K filled boxed plates
                    M unfilled boxes
                    N one rectangular plate
                    P alternate polarized
                    + adds a polarity sign
                    +L polarity sign to the left of drawing direction
                    
        Rev     - reversed polarity
        
        height  - defaults F: dimen_/3, C,P: dimen_/4, E,K: dimen_/5
        
        wid     - defaults F: height*0.3, C,P: height*0.4, CP:height*0.8, E,K: height 

Makro bez paramerov vykreslí kondenzátor s prednastavenými rozmermi.

    C1: capacitor;      C2: capacitor(,C,);  C3: capacitor(,E);    C4: capacitor(,K);     
    C5: capacitor(,M,,0.75, 0.25);  
                        C6: capacitor(,P);   C7: capacitor(, CP);  C8: capacitor(,+LC);    
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 
move to (0.5, 1.5);   

capacitor;          llabel(,C_1,); 
capacitor(,C,);     llabel(,C_2,);    
capacitor(,E);      llabel(,C_3,); 
capacitor(,K);      llabel(,C_4,); 

move to (0.5, 0.0); 

capacitor(,M, ,0.75, 0.25);      llabel(,C_5,); 
capacitor(,P);      llabel(,C_6,);  
capacitor(, CP);    llabel(,C_7,);   
capacitor(,+LC);     llabel(,C_8,); 
'''

_ = cm_compile('cm_0100c', data, dpi=600)   
```

```{figure} ./src/cm_0100c.png
:width: 450px
:name: cm_0100c

Typy kondenzátorov.
```
    
## <font color='teal'> Cievka </font>

Pri cievke môžeme meniť tvar vinutia, počet závitov, ich veľkosť a môžeme k cievke pridať jadro.

    inductor(linespec, W|L, cycles, M|P|K, loop wid)
    
        parametre:
    
        linespec  - dĺžka a umiestnenie cievky
        
        W|L       - (default narrow), W: wide, L: looped;
    
        cycles    - number of arcs or cycles (default 4);
        
        M|P|Kn    - M magnetic core
                    P powder (dashed) core, 
                    K long-dashed core, 
                    n=integer (default 2) number of corelines named M4Core1, M4Core2
                    
       loop width - default L, W: dimen_/5; other:dimen_/8 
       
       
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 
move to (0.5, 1.5);   

inductor;          llabel(,L_1,); dot;
inductor(,W);      llabel(,L_2,); rlabel(,W,);  dot;  
inductor(,L);      llabel(,L_3,); rlabel(,L,);  dot;
L4: inductor(,L,6);     llabel(,L_4,); "L,6" at L4.center + (0,-.05) below;  
'''

_ = cm_compile('cm_0100d', data, dpi=600)   
```

```{figure} ./src/cm_0100d.png
:width: 450px
:name: cm_0100d

Typy cievok.
```
    
## <font color='teal'> Dióda </font>

Dióda je orientovaný dvojpól. Parametrom **Rev** môžeme otočiť smer diódy. Doplnenie typu diódy písmenom **K** vykreslí nevyplnenú značku diódy.

    diode(linespec, chars, [Rev][E])
    
        parametre:
    
        linespec - dĺžka a umiestnenie diódy
        
        chars   - typ diódy
                    B    bi-directional
                    b    bi-directional with outlined zener crossbar
                    CR   current regulator
                    D    diac
                    G    Gunn
                    L    open form with centre line
                    LE[R]: LED [right]
                    P[R] photodiode [right]
                    S    Schottky
                    Sh   Shockley
                    T    tunnel
                    U    limiting
                    V    varicap
                    v    varicap (curved plate)
                    w    varicap (reversed polarity)
                    Z    zener
                    appending K to arg 2 draws open arrowheads; 
                    
        Rev|E   -   Rev - reversed polarity, E - zobrazenie púzdra 

Makro bez paramerov vykreslí diódu s prednastavenými rozmermi.

    D1: diode;      D2: diode(,S,);    D3: diode(,V);   D4: diode(,v);    
    D5: diode(,U);  D6: diode(,ZK);    D7: diode(,T);   D8: diode(,,R);  

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 
move to (0.5, 1.5);   

diode;          llabel(,D_1,); 
diode(,S,);     llabel(,D_2,); rlabel(,S,);  
diode(,V);      llabel(,D_3,); rlabel(,V,);  
diode(,v);      llabel(,D_4,); rlabel(,v,);

move to (0.5, 0.25); 

diode(,U);     llabel(,D_5,); rlabel(,U,);  
diode(,ZK);    llabel(,D_6,); rlabel(,ZK,); 
diode(,T);     llabel(,D_7,); rlabel(,T,);  
diode(,,R);    llabel(,D_8,); rlabel(,Rev,);
'''

_ = cm_compile('cm_0100e', data, dpi=600)   
```

```{figure} ./src/cm_0100e.png
:width: 450px
:name: cm_0100e

Typy diód.
```
    

## <font color='teal'> Zdroje </font>

    source(linespec, chars, diameter, R, body attributes, body name)
    
    parametre:
    
        linespec - dĺžka a umiestnenie diódy
        
        chars    - typ zobrazenia
                    AC  AC source;
                    B   bulb;
                    F   fluorescent;
                    G   generator;
                    H   step function;
                    I   current source;
                    i   alternate current source;
                    ii  double arrow current source;
                    ti  truncated-bar alternate current source;
                    L   lamp;
                    N   neon;
                    NA  neon 2;
                    NB  neon 3;
                    P   pulse;
                    Q   charge;
                    R:  ramp; S: sinusoid;
                    SC  quarter arc, SCr right orientation;
                    SE  arc, SEr right orientation;
                    T   triangle;
                    U   square-wave;
                    V   voltage source;
                    X   interior X;
                    v   alternate voltage source;
                    tv  truncated-bar alternate voltage source;
                    other: custom interior label or waveform;
    
        diameter     - priemer kruhu zdroja
    
        R       - reversed polarity;
    
        body attributes  modifies the circle (body) with e.g., color or fill;
    
        body names
    
    
    
## <font color='teal'> Popis dvojpólov </font>

Pre popis dvojpólov sú definované podporné makrá *llabel()*, *clabel()*, *rlabel()* a *dlabel()* pre popis posledného uloženého prvku. Pre označenie je možné použiť syntax pre zápis matematických vzťahov LaTeX-u. Text popisu nemusí byť uzatvorený medzi znakmi `$...$`.  

    llabel( slabel, xlabel, elabel )  - označenie po lavej strane v smere ukladania
    clabel( slabel, xlabel, elabel )  - označenie po pravej strane v smere ukladanie 
    rlabel( slabel, xlabel, elabel )  - označenie cez stred v smere ukladania
    dlabel( long, lat, slabel, xlabel, elabel, [X][A|B][L|R])
                                      - označenie s offsetom voči stredu 
  
    slabel       - označenie v bode začiatku prvku
    xlabel       - označenie v strede prvku
    elabel       - označenie v bode konca prvku
    long         - pozdĺžna vzdialenosť od od určenej pozície
    lat          - kolmá vdialenosť od určenej pozície
    
    X            - stred prvku
    A            - above, text nad zadanou pozíciou
    B            - below, text pod zadanou pozíciou
    L            - ljust, zarovnanie textu doľava
    R            - rjust, zarovnanie textu doprava
    
Umiestnenie popisu zavisí od aktuálneho smeru ukladania komponentu. *rlabel()* ukladá text po pravej strane v smere ukladania. V prípade potreby môžeme modifikovať aj font a veľkosť textu

    R1: resistor(,,);   llabel(a,R_1,b); 
    C2: capacitor,,C);  llabel( ,C_2, );   rlabel(, 10 \mu F, ); 
    R3: resistor(,,E);  llabel( ,R_3, ); clabel(, $\scriptsize{123}$, ); 

    R4: resistor(,,E);  dlabel(0.75, 0.35, aa ,R_4, bb ,X); 
    R5: resistor(,,E);  dlabel(0.5, 0.3, aa ,R_5, bb ,L);
    D6: diode(2);       llabel( ,\sf D_6,); rlabel(,$\sf \footnotesize{ 1N4007 }$,); 


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 

R1: resistor(right_ 2 at (0,2),,);   llabel(a,R_1,b); 
C2: capacitor(right_ 2,,C);   llabel( ,C_2, );   rlabel(, 10 \mu F, ); 
R3: resistor(right_ 2,,E);   llabel( ,R_3, ); clabel(, $\scriptsize{123}$, ); 

R4: resistor(right_ 2 at (0,0.5),,E);   dlabel(0.75, 0.35, aa ,R_4, bb ,X); 
R5: resistor(right_ 2 ,,E);   dlabel(0.5, 0.3, aa ,R_5, bb ,L);
D6: diode(2);   llabel( ,\sf D_6, );   rlabel(,  $ \sf \footnotesize{ 1N4007 }$, ); 
'''

_ = cm_compile('cm_0100f', data, dpi=600)   
```

```{figure} ./src/cm_0100f.png
:width: 350px
:name: cm_0100f

[Makrá](./src/cm_0100f.ckt) pre popis dvojpólov.
```

## <font color='teal'> Umiestňovanie dvojpólov </font>

Na pracovnej ploche môžeme umiestňovať dvojpóly niekoľkými spôsobmi:

1. Zadaním východzieho bodu kreslenia presunom kurzora 

        move to pos; 
        object([length], ... );

2. Zadaním polohy stredu dvojpólu, smeru a velkosti 

        object( at pos [dir [length]], ... );

3. Zadaním smeru, veľkosti objektu a polohy východzieho bodu 

        object( [dir] [lenght] from pos, ... );

4. Pokračovaním od koncového bodu predchádzajúceho objektu 

        object(dir [length], ... );

5. Zadaním koncových bodov dvojpólu 

        object(from pos_A to pos_B);

Príklady použitia
        
```{code-block}
move to (1,2.5); resistor(2);       # (1)
resistor(at (2,1.5) right_ 2,,E);   # (2)
resistor(right_ 2 from (1,0.5))     # (3)

move to (4,2.5); 
RA: resistor(right_ 2); 
RB: resistor(down_ 2);              # (4)
resistor(from RA.start to RB.end);  # (5)
```

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)
define(`xc', `
  {
   Q: Here; line from Q+(-.1,-.1) to Q+(0.1, 0.1); 
   line from Q+(-.1, .1) to Q+(0.1, -0.1);
   circle at Q rad 0.1*1.4; 
   color_black;
   }
')

Grid(7,3);

circle at (0.5,2.5)rad 0.25 "1"
right_; move to (1,2.5); color_red; xc;
resistor(2);    # (1)

circle at (0.5,1.5)rad 0.25 "2"
move to (2,1.5); color_red; xc;
resistor(at (2,1.5) right_ 2,,E)


circle at (0.5, 0.5)rad 0.25 "3";
move to (1,0.5); color_red; xc;
resistor(right_ 2 from (1,0.5))

circle at (6.5, 2.5)rad 0.25 "4"; move to (6,2.5); color_red; xc;
move to (4,2.5); color_blue; xc;
RA: resistor(right_ 2); llabel(,R_a,); 
RB: resistor(down_ 2); llabel(,R_b,); color_blue; xc;
resistor(from RA.start to RB.end)
circle at (4.65, 1.15)rad 0.25 "5"; 
'''

_ = cm_compile('cm_0100k', data, dpi=600)   
```

```{figure} ./src/cm_0100k.png
:width: 450px
:name: cm_0100k

Príklady umiestňovania dvojpólov.
```

## <font color='teal'> Modifikácie dvojpólov </font>

### <font color='brown'> Premenné prvky  </font>

Pre zobrazenie premenných prvkov môžeme využiť makro *variable()*

    variable(‘element’,[A|P|L|[u]N]|[u]NN]][C|S],[+|-]angle,length)
    variable(,[A|P|L|[u]N]|[u]NN]][C|S],[+|-]angle,length)
    
        parametre:
    
        element   - meno makra prvku, na ktorom bude vykreslený typ zmeny
        
        [A|P|L|[u]N]|[u]NN]][C|S]
                  - označenie typu zmeny
                      A - šipka
                      P - potenciometer
                      L - čiara
                      N - parametrická zmena
                     uN
                    uNN
                    C|S - značka parametra
                    
        [+|-] angle - uhol a smer označenia zmeny, 
        
        length      - dĺžka označenia 

Makro môžeme použiť dvoma spôsobmi:

* s prvým argumentom, v ktorom zadáme makro s parametrami prvku, ktorý chceme označiť ako premenný, 
* makro použijeme podobne ako makrá na popis prvkov *llabel ..*, v tomto prípade ponecháme prvý argument prázdny.

            move to (0,0)
            variable(`R1: resistor(right_ 2,,)',A); llabel(,R_1,); rlabel(a,10,b)

        R2: resistor(right_ 2,,E); variable(,P);   llabel(,R_2,); rlabel(,100,); 

            move to (1,1)
        V1: source(up_ 2, AC); variable(,A,,1.5);  llabel(,V_1,);

            move to (3,1)
        C1: capacitor(up_ 2); rlabel(,C_1,); variable(,N,,);

    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 

move to (0,0)
variable(`R1: resistor(right_ 2,,)',A); llabel(,R_1,); rlabel(a,10,b)

resistor(right_ 2,,E); variable(,P);   llabel(,R_2,); rlabel(,100,); 

move to (1,1)
source(up_ 2, AC); variable(,A,,1.5);  llabel(,V_1,);

move to (3,1)
capacitor(up_ 2); rlabel(,C_1,); variable(,N,,);  
'''

_ = cm_compile('cm_0100g', data, dpi=600)   
```

```{figure} ./src/cm_0100g.png
:width: 220px
:name: cm_0100g

[Zobrazenie](./src/cm_0100g.ckt) premenných prvkov.
```
V analogových zapojeniach bývajú premenné prvku (potenciometre, trimre, kondenzátory) zobrazené s fyzickým zapojenie vývodov súčiastok tak, ako je to zobrazené na nasledjúcom obrázku. Pri ladiacich kondenzátoroch je zobrazený aj ich vzájomný mechanický súbeh.
    
```{figure} ./img/radio_325.jpg
:width: 600px

Použitie premenných prvkov v zapojení rádia s integrovaným obvodom.
```

Pre zobrazenie upravených premenných prvkov tak ako sú použité v predchádzajúcom zapojení sú v knižnici [lib_user](./src/lib_user.ckt) definované makrá *vres_v()* a *vcap_v()* 


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)

move to (1,0)
VR1: vres_v(1.5,V,L);
     { 
       "\sf 50k" at VR1.w;
       line from VR1.S down_ 0.5  
     }

move to 2.5,0
VR2: vres_v(1.5,P,L); line from VR2.s down 0.25

move to 4,0; right_
VR3: vres_v(1.5,T,R);
{ 
       "\sf 25k" at VR3.w;
       line from VR3.S down_ 0.5  
     }

move to 5.5,0; 
VR4: vres_v(1.5,S,L); line from VR4.s down 0.25

right_
move to 7,0
VC1: vcap_v(1.5, R); line from VC1.S right_ 1 dashed; 
'''

_ = cm_compile('cm_0100n', data, dpi=600)   
```

```{figure} ./src/cm_0100n.png
:width: 450px
:name: cm_0100n

Zobrazenie upravených premenných prvkov z knižnice *lib_user*.
```

Nasledujúci skript zobrazuje časť zapojenia z predchádzajúceho obrázku. Pretože rezistory v zapojení sú mierne dlhšie ako štandardné rezistory v `CircuitMacros`, bolo pre ich zobrazenie definované nové makro *res()*

    define(`res', `ebox($1, 0.8);')


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_user.ckt)

VR1: vres_v(1.5,V,R); "\sf 50k" at VR1.w below; {line from VR1.n left_ 1;}
     gnd(0.1) at VR1.R.end 
     line from VR1.S right_ 0.5; DT1: dot; 
     line 0.25; Q0:circle rad 0.08

T1:  bjt_NPN(1.5,0.8,,N) with .B at last circle.e;
     Q1: circle with .n at T1.E rad 0.08;
     DT2: dot(at T1.C)

T2:  bjt_NPN(0.6,,,N); line from T2.E to (T2.E, Q1.n)
     Q2: circle with .n at last line.end rad 0.08;
     line from T2.C right_ 0.5;
     Q3: circle rad 0.08;
     down_; move to Q2.s; gnd(0.5);

     res(from DT1 up_ 3, E); llabel(,\sf M1,)
VR2: vres_v(1.75,P,L); "\sf 1M" at VR2.w;
     res(from DT2 up_ 1.75, E); rlabel(,\sf 3k5,)
     DT3: dot; {line left_ 3; }; line 0.5;
     Q4: circle rad 0.08;
     line up_ 0.5; DT4: dot;
     {res(right_ 1.5); llabel(,\sf 350,); gnd(0.25, R); }
     res(up_ 1.5); llabel(,\sf 1k,); DT5: dot;
     
     line from VR2.n to (VR2, DT5); DT6: dot;
     right_;res(from DT5 to DT6,E); llabel(,\sf 330,)
     capacitor(from DT6 left_ 1.2,+K,, 0.4, 0.25); llabel(,\sf 50M,); gnd(.15,L);
     line from DT5 right_ 2;

# MAA325 box 
    line from Q1.w to (Q0,Q1) then to Q0.s dashed;
    line from Q0.n to (Q0,Q4) then to Q4.w dashed;
    line from Q4.e to (Q3,Q4) then to Q3.n dashed;
    line from Q3.s to (Q3,Q2) then to Q2.e dashed;
    line from Q2.w to Q1.e dashed; 
'''

_ = cm_compile('cm_0100m', data, dpi=600)   
```

```{figure} ./src/cm_0100m.png
:width: 220px
:name: cm_0100m

[Použitie](./src/cm_0100m.ckt) premenných prvkov v časti zapojenia rádia.
```

### <font color='brown'> Prúd dvojpólom  </font>

Pre zobrazenie šípky ktorá reprezentuje prúd v prívode prvku môžeme použiť makro

    b_current(label, above_|below_, In|O[ut], Start|E[nd], frac);
    
        parametre:
        
            label  - označenie veličiny (prúd ...)
            
            above_ - poloha označenia 
            below_

            In     - smer šípky
            Out

            Start  - súradnica dvojpólu, voči ktorej bude vykreslená šípka a jej smer 
            End
            
            frac  - posun šípky voči zadanej súradnici
            
Makro môžeme použiť nielen na označovanie prúdu prvkami zapojenia, ale aj na vyznačenie prúdu vetvou obvodu príkazom *line*. Hodnota parametra *frac* závisí od aktuálneho nastavenia vykreslenia šípky a parametrov prostredia, približne zodpovedá aktuálnej dĺžkovej jednotke. 
            
    R1: resistor(right_ 3,,E); 
        llabel(,R_2,); rlabel(,100,); 
        b_current(i_{12} ); 

    R1: resistor(right_ 3 at (2.5, 2.5),,E) ; 
        llabel(,R_2,); rlabel(,100,); 
        b_current(i_{34}, below_, Out, End, 0.45 ); 

    L1: line from (5,1) to (8,1) "L1" above;
        b_current(i_{56}, above_, In, Start, 0.6 ); 

    L2: line from (5,2.5) to (8,2.5) "L2" below;
        b_current(i_{78}, above_, In, End, 0.6 );
            
            
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 

Grid(9, 2.5)
move to (1,0.5)

R1: resistor(right_ 3,,E); 
    llabel(,R_2,); rlabel(,100,); 
    b_current(i_{12} ); 

R1: resistor(right_ 3 at (2.5, 2),,E) ; 
    llabel(,R_2,); rlabel(,100,); 
    b_current(i_{34}, below_, Out, End, 0.45 ); 

L1: line from (5,0.5) to (8,0.5) "L1" above;
    b_current(i_{56}, above_, In, Start, 0.6 ); 

L2: line from (5,2) to (8,2) "L2" below;
    b_current(i_{78}, above_, In, End, 0.6 );  
'''

_ = cm_compile('cm_0100h', data, dpi=600)   
```

```{figure} ./src/cm_0100h.png
:width: 550px
:name: cm_0100h

[Zobrazenie](./src/cm_0100h.ckt) prúdu rezistorom a vetvou obvodu.
```
            
### <font color='brown'> Napätie na dvojpóle </font>

Úbytok napätia na prvku znázorňujeme šipkou umiestnenou paralelne s prvkom. Pre zobrazenie môžeme využiť štandarný príkaz *line -> ...* alebo makrá

    larrow(label, direction);
    rarrow(label, direction);
    
        parametre:
        
            label  - označenie veličiny (napätie ...)
            
            direction - smer šipky zadaný ako <- alebo ->
            
Použitie makier ukazuje nasledujúci príklad

    S1: source(up_ 2.5, AC); larrow(V_{0}, <-); b_current(i_0, ,Out, End, 0.45 );
    
    R1: resistor(right_ 2.5,, E); larrow(V_{1}, ->); rlabel(,R_1,);
        dot; {tconn(1.5,O); "1" ljust;}
    
    R2: resistor(down_ 2.5,, E); larrow(V_{2}, ->); rlabel(,R_2,)
        dot; tconn(right_ 1.5,O); "2" ljust;
        line to S1.start;

    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 
move to (1,0.5)
up_
S1: source(2.5, AC); larrow(V_{0}, <-); b_current(i_0, ,Out, End, 0.45 );
resistor(right_ 2.5,, E); larrow(V_{1}, ->); rlabel(,R_1,);
dot; {tconn(1.5,O); "1" ljust;}
resistor(down_ 2.5,, E); larrow(V_{2}, ->); rlabel(,R_2,)
dot; {tconn(right_ 1.5,O); "2" ljust;}
line to S1.start; 
'''

_ = cm_compile('cm_0100i', data, dpi=600)   
```

```{figure} ./src/cm_0100i.png
:width: 300px
:name: cm_0100i

[Zobrazenie](./src/cm_0100i.ckt) úbytku napätia na rezistoroch.
```

    

