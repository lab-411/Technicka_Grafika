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
# <font color='navy'> Terminály </font>

Každé elektronické zapojenie má pripojovacie body - terminály, ktoré môžu byť formálne (napájanie, zem, vstup, výstup ...) zvyčajne pripojené jedným uzlom alebo reálne (konektor, svorkovnica ...), ktoré sú pripojené do niekoľkých uzlov obvodu.

## <font color='teal'> Napájanie, zem, vstupy a výstupy </font>

Terminály pre napájania a zem majú význam spoločného spojenia všetkých rovnako označených terminálov, čím okrem jasnej deklarácie ich významu aj výrazne zjednodušujú zapojenie, pretože nie je potrebné kresliť vodiče ktoré ich spájajú.


    ground( at position, T|stem_length, N|F|S|L|P[A]|E, U|D|L|R|degrees )
    
        parametre:
    
        position        - poloha značky
    
        T|stem_length   - zrušenie prívodu (T) alebo dĺžka prívodu 
    
        N|F|S|L|P[A]|E  - typ zeme
                    N   - bez označenia, uzemnenie
                    F   - uzemnenie kostry 
                    S   - digitálna zem
                    L   
                    P   - pripojenie ochranneho vodiča
                    E   - analogová zem, europske značenie
                    
        U|D|L|R|degrees - orientácia alebo uhol otočenia


```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)

#command "\sf"
ground(at (0.5,1),,N); "N" at last box above;
ground(at (1.5,1),,F); "F" at last box above;
ground(at (2.5,1),,S); "S" at last box above;
ground(at (3.5,1),,L); "L" at last box+(0,0.3) above;
ground(at (4.5,1),,P); "P" at last box+(0,0.3) above;
ground(at (5.5,1),,E,); "E" at last box above;
'''

_ = cm_compile('cm_0140a', data, dpi=600)   
```

```{figure} ./src/cm_0140a.png
:width: 350px
:name: cm_140a

Značky zeme.
```

Terminály *tbox()* v tvare vlajky sa najčastejšie používajú v zapojeniach s digitálnymi obvodmi, kde na rozdiel od analogových obvodov nie je z kontextu zrejmý význam terminálu. Tvar vlajky určuje v tomto prípade smer toku informácií, čo je zvlášť dôležité pri použití zberníc, kde nie sú terminály priamo pripojené k výstupom logických obvodov.

    tbox(text, wid, ht, <|>|<>, fill)
    
    parametre:
    
        text        - označenie značky
        wid         - šírka
        ht          - výška
        <|>|<>      - orientácia značky
        fill        - výplň príkazom fill_(n), n = 0.0...1.0

Terminály *tconn()* reprezentujú ukončenie vodiča zvyčajne označené menom, ktoré môže zároveň označovať aj meno pinu vo fyzickom konektore. Význam tvaru terminálu závisí od používaných konvencií pri kreslení zapojení. 

    tconn(linespec, O|<|<<|>>|>|A|M", wid)
    
    parametre:
    
        linespec        - dlžka terminálu
        O|<|<<|>>|>|A|M - typ terminálu
        wid             - velkosť značky O,M

        
```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *
data = r'''
include(lib_base.ckt)
"tb\\ox()" at (1.5, 3);
"tc\\onn()" at (4, 3);

move to (0.5,1.0); line 1; tbox(V_1, 1, , <); 
move to (0.5,1.5); tbox(V_2, 1, , >); line 1
move to (0.5,2.0); line 1; tbox(V_3, 1, , <>, fill_(0.9))

move to (3.5,0.5); T1: tconn(,O); "$0$" at T1.e ljust
move to (3.5,1.0); T2: tconn(,>); "$>$" at T2.e ljust
move to (3.5,1.5); T3: tconn(,<); "$<$" at T3.e ljust
move to (3.5,2.0); T4: tconn(,A); "$A$" at T4.e ljust
move to (3.5,2.5); T5: tconn(,M); "$M$" at T5.e ljust
'''

_ = cm_compile('cm_0140b', data, dpi=600)   
```

```{figure} ./src/cm_0140b.png
:width: 300px
:name: cm_140b

Vstupno-výstupné terminály.
```

## <font color='teal'> Konektory </font>

Fyzické pripojenie elektronických obvodov je zvyčajne realizované konektormi alebo svorkovnicami. Značka konektora môže byť formálna, kde je znázornená poloha pinu konektora (jednoradový, dvojradový ...) alebo môže znázorňovať aj fyzické usporiadanie pinov konektora (DIN, D-SUB ...). 

```{figure} ./img/DIN_connector.png
:width: 600px
:name: din

Signálové konektory typu DIN, [zdroj](https://en.wikipedia.org/wiki/DIN_connector).
```

```{figure} ./img/dsub_connector.png
:width: 500px
:name: dsyb

Signálové konektory typu D-sub, [zdroj](https://en.wikipedia.org/wiki/D-subminiature).
```

V knižnici `CircuiytMacros` je pre zobrazenie jedno a dvojradových lineárnych konektorov pre ploché káble ako aj pre kolíkové lišty a spojky definované makro *Header()*. V praxi sa môžeme stretnúť s veľkým množstvo typov a prevedení kolíkových líšt a konektorov.

```{figure} ./img/headers.jpg
:width: 500px
:name: header

Kolíkové lišty a konektory.
```


Značka je parametrická, pri použití makra definujeme tvar konektora a počet pinov.

     Header(1|2, rows, wid, ht, type)
     
     parametre:
    
        1|2    - jedno alebo dvojradový konektor
        rows   - počet pinov v jednom rade
        wid    - šírka konektora
        ht     - výška konektora
        type   - výplň príkazom fill_(n), n = 0.0...1.0
        
     atribúty
     
        P1 ... Pn - piny konektora
        
Makro *tstrip()* zobrazuje jednoradový konektor s obojstranými prívodmi.
     
     tstrip(R|L|U|D|degrees, n, chars),
     
     parametre:
     
        R|L|U|D|degree - orientácia
        n              - počet pinov
        chars          - parametre oddelené bokočiarkou
                         D vyplnene piny
                         O zrušenie oddelenia pinov
                         wid=w  šírka konektora
                         hr=h   výška konektora
                         výplň príkazom fill_(n), n = 0.0...1.0

    atribúty
     
        T1 ... Tn      - piny konektora
        L1 ... Ln      - prívody ku pinom zlava
        R1 ... Rn      - prívody ku pinom zprava
     

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 
d = 2;

log_init;         # inicializacia makier pre logicke obvody

move to (1,1);
up_; 
H1: Header(2, 6,,,fill_(0.9)); 
"(2,6,,,)" at H1.w rjust;

move to (1,2.5);
H2: Header(1, 6,,,fill_(0.9));
"(1,6,,,)" at H2.w rjust;

move to (1,3.5);
H3: Header(1, 4,0.5,2,fill_(0.9));
"(1,4,0.5,2,)" at H3.w rjust;

move to (4,1.35);
T1: tstrip(R,6,); 
"(R,6)" at T1.e ljust;

move to (4,1.15+1.5);
T2: tstrip(R,6,DO); 
"(R,6,DU)" at T2.e ljust;

move to (4,1.15+2.5);
T2: tstrip(R,4,O; wid=3; ht=.5); 
"(R,4,O;wid=3;ht=.5)" at T2.n above;

"He\\ader()" at (1,0.5);
"ts\\trip()" at (4,0.5);

'''

_ = cm_compile('cm_0140c', data, dpi=600)   
```

```{figure} ./src/cm_0140c.png
:width: 450px
:name: cm_0140c

[Príklady](./src/cm_0140c.ckt) modifikácií radových konektorov.
```

V niektorých prípadoch je vhodné zobrazenie reálneho usporiadanie pinov konektora a pripojenie pinov. Vzhľadom k obrovskému množstvu typov konektorov a ich typových modifikácii je potrebné si vytvoriť pre zobrazenie daného typu vlastné makro. V knižnici [lib_user.ckt](./src/lib_user.ckt) je definované makro *DE9_M* pre 9-pinový D-sub konektor, príklad jeho použitia 

    include(lib_user.ckt)
    move to (1,2); DS1: DE9_M(L);
    move to (6,2); DS2: DE9_M(L);
    dy = (DS1.P3.y-DS1.P2.y); dx = (DS1.P2+DS2.P3).x;

    color_blue;
    line from DS1.P5 to DS2.P5;
    color_red;
    line from DS1.P3 to (dx/2-dy, DS1.P3.y) then to (dx/2+dy, DS2.P2.y) then to DS2.P2;
    color_dark_green;
    line from DS1.P2 to (dx/2-dy, DS1.P2.y) then to (dx/2+dy, DS2.P3.y) then to DS2.P3;
    color_black;
    line from DS1.P1 right_ 0.5; line up_ to (Here, DS1.P6); dot; {line to DS1.P6}; 
    line to (Here, DS1.P4) then to DS1.P4;
    line from DS2.P1 right_ 0.5; line up_ to (Here, DS2.P6); dot; {line to DS2.P6}; 
    line to (Here, DS2.P4) then to DS2.P4;
    line from DS1.P7 left_ 0.5; line  up_ to (Here, DS1.P8) then to DS1.P8;
    line from DS2.P7 left_ 0.5; line  up_ to (Here, DS2.P8) then to DS2.P8;

    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)
include(lib_user.ckt)

#Grid(10,5);

#move to 1,2; Header(2,5)
right_;
move to (1,2); DS1: DE9_M(L);
move to (6,2); DS2: DE9_M(L);
dy = (DS1.P3.y-DS1.P2.y); dx = (DS1.P2+DS2.P3).x;

color_blue;
line from DS1.P5 to DS2.P5;
color_red;
line from DS1.P3 to (dx/2-dy, DS1.P3.y) then to (dx/2+dy, DS2.P2.y) then to DS2.P2;
color_dark_green;
line from DS1.P2 to (dx/2-dy, DS1.P2.y) then to (dx/2+dy, DS2.P3.y) then to DS2.P3;
color_black;
line from DS1.P1 right_ 0.5; line up_ to (Here, DS1.P6); dot; {line to DS1.P6} ; line to (Here, DS1.P4) then to DS1.P4;
line from DS2.P1 right_ 0.5; line up_ to (Here, DS2.P6); dot; {line to DS2.P6} ; line to (Here, DS2.P4) then to DS2.P4;
line from DS1.P7 left_ 0.5; line  up_ to (Here, DS1.P8) then to DS1.P8;
line from DS2.P7 left_ 0.5; line  up_ to (Here, DS2.P8) then to DS2.P8;
'''

_ = cm_compile('cm_0140d', data, dpi=600)   
```

```{figure} ./src/cm_0140d.png
:width: 400px
:name: cm_0140d

[Zapojenie](./src/cm_0140d.ckt) nulového modemu s konektormi DE-9, [zdroj](https://en.wikipedia.org/wiki/Null_modem).
```
