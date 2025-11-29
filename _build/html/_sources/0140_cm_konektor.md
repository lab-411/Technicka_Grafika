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

#Grid(6,1.5);
command "\sf"

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

    tbox(text, wid, ht, <|>|<>)
    tconn(linespec, chars|keys, wid)

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
#command "\sf"
"tb\\ox" at (1.5, 3);
"tc\\onn" at (4, 3);

move to (0.5,1.0); line 1; tbox(V_1, 1, , <); 
move to (0.5,1.5); tbox(V_2, 1, , >); line 1
move to (0.5,2.0); line 1; tbox(V_3, 1, , <>)

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

Fyzické pripojenie elektronických obvodov je zvyčajne realizované konektormi alebo svorkovnicami. 

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 
d = 2;

log_init;         # inicializacia makier pre logicke obvody

move to (3,1);
up_; 
H1: Header(2, 6,,,fill_(0.9)); 
"Konektor" at H1.w rjust;
"1" at H1.P1 rjust;
"2" at H1.P2 rjust;
"11" at H1.P11 ljust;
"12" at H1.P12 ljust;

#line from H1.P1 down_ d/4 then right_ 2*d;
#line from H1.P2 up_ d/4 then right_ 2*d;
'''

_ = cm_compile('cm_0240a', data, dpi=600)   
```

```{figure} ./src/cm_0240a.png
:width: 300px
:name: cm_020

Parametrické komponenty
```



