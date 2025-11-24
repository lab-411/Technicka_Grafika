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


# <font color='navy'> Integrované obvody </font> 

Integrované obvody sú prvky elektronických obvodov, ktorých zobrazenie v technickej dokumentácii závidí od kontextu ich použitia. V katalogových listoch sa vyskytuje ich zobrazenie z pohľadu zapojenia ich pinov, čo je dôležité pri návrhu plošných spojov. Pri kreslení zapojení je obvyklé používať blokovú značku obvodu a orientovať terminály obvodu podľa ich významu, zvyčajne vstupy vľavo a výstupy vpravo. V niektorých prípadoch môže byť bloková značka v dokumentácii doplnená o vnútorné zapojenie integrovaného obvodu. Nasledujúci príklad ukazuje zobrazenia integrovaného obvodu 555, makkrá pre značky sú implementované v knižnici [lib_ic555,ckt](./src/lib_ic555.ckt).  


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
cct_init
log_init

include(lib_base.ckt)
include(lib_user.ckt)
include(lib_ic555.ckt)

command "\sf"

IC1: IC555_1 at (2,6.5); "555" at IC1.BX.n above;
IC2: IC555_2 at (7,6.5);
IC3: IC555_3 at (5,1);
'''

_ = cm_compile('cm_0207a', data, dpi=600 )   
```


```{figure} ./src/cm_0207a.png
:width: 400px
:name: cm_0207a

Rôzne spôsoby zobrazenia integrovaného obvodu. 
```

Pri vytváraní značiek integrovaných obvodov môžeme použiť makro *lg_pin()*

    lg_pin(location, label, pinref, n|e|s|w[L|M|I|O][N][E], pinno, optlen)
    
    parametre:
    
        location - súradnice pinu / terminálu obvodu
        label    - zobrazované meno pinu
        pinref   - referencia na pin
        n|e|s|w  - orientácia pinu
        [L|M|I|O][N][E] - typ pinu
        pinno    - číslo pinu
        optlen   - dĺžka pinu

Pomocou makra *lg_bartxt()* môžeme zobraziť čiaru nad pomenovaním negovaného pinu a pre nastavenie rozostupov medzi pinmi môžeme použiť makro *lg_pinsep* 

    lg_bartxt(meno)
    lg_pinsep

Príklad vytvorenie makra pre kreslenie značky integrovaného obvodu

    define(`IC485', `[
      BX: box wid 2 ht 5*lg_pinsep;

          lg_pin(BX.nw - (0, 1*lg_pinsep), RO, Pin1, w, 1);
          lg_pin(BX.nw - (0, 2*lg_pinsep), lg_bartxt(RE), Pin2, wN, 2);
          lg_pin(BX.nw - (0, 3*lg_pinsep), DE, Pin3, w, 3);
          lg_pin(BX.nw - (0, 4*lg_pinsep), DI, Pin4, w, 4);

          lg_pin(BX.ne - (0, 1*lg_pinsep),  Vcc, Pin8, e, 8);
          lg_pin(BX.ne - (0, 2*lg_pinsep),  lg_bartxt(B), Pin7, eN, 7);
          lg_pin(BX.ne - (0, 3*lg_pinsep),  A, Pin6, e, 6);
          lg_pin(BX.ne - (0, 4*lg_pinsep),  GND, Pin6, e, 5);
          
          arc ccw from BX.n-(.2,0) to BX.n+(0.2,0) with .c at BX.n;
          rgbfill(fill_black, {circle at BX.nw + (0.15, -0.15) rad 0.055} )
    ]')
    
    IC485; "MAX485" at last[] .s below;


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
cct_init
log_init

include(lib_base.ckt)
include(lib_color.ckt)
include(lib_user.ckt)
include(lib_ic485.ckt)

command "\sf"

IC485; "MAX485" at last[] .s below;
'''

_ = cm_compile('cm_0207c', data, dpi=600 )   
```

```{figure} ./src/cm_0207c.png
:width: 160px
:name: cm_0207c

Značka obvodu z príkladu.
```

V niektorých prípadoch nemôžeme využiť preddefinované rozostupy pinov, napríklad ak potrebujeme nakresliť značku obvodu so znázornením jeho vnútorneho zapojenia na ktorú zároveň potrebujeme naviazať piny obvodu. Môžeme si pomôcť pomocnými súradnicami, ktoré budú tvoriť virtuálne body medzi zapojením obvodu a jeho pinmi, táto konštrukcia je použitá v knižnici [lib_ic485](./src/lib_ic485.ckt).

    define(`IC485_RIGHT', `[
      P1: ( 1.5,  -1.00);        # pomocná súradnica 
      ...
      lg_pin( P1,,Pin1,e,RO);    # pin na súradnici
      ...                        # prvky vnutornej struktury    
      BUFFER_gen(TOC, 0.9, 0.9,NP,N,,, ) with .Out at P1+(-0.25,0);
      ...
    ]')
  
```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
cct_init
log_init

include(lib_base.ckt)
include(lib_color.ckt)
include(lib_user.ckt)
include(lib_ic485.ckt)

command "\sf"

IC1: IC485_LEFT;{"MAX485" at last[] .s below;}
TERM_485;
LINE_485
TERM_485;
IC2: IC485_RIGHT; {"MAX485" at last[] .s below;}
'''

_ = cm_compile('cm_0207d', data, dpi=600 )   
```

```{figure} ./src/cm_0207d.png
:width: 580px
:name: cm_0207d

Použitie značiek integrovaných obvodov s vnútorným zapojením.
```

    
Pri kreslení zapojení s integrovanými obvodmi kombinovanými s diskrétnymi analogovými prvkami je  treba inicializovať knižnice *cct_init*, *log_init* a v prípade potreby uživateľské knižnice. Je vhodné v celom zapojení používať jeden spoločný font. 
    
```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
cct_init
log_init
include(lib_base.ckt)
include(lib_color.ckt)
include(lib_ic555.ckt)
command "\sf"
#Grid(6,6)

IC: IC555_2 at (3,3);
    C2: capacitor(from IC.Pin5 down_ 0.75,); llabel(,\sf 10nF,);
        line from IC.Pin7 left 1;
        dot;
        {R1: resistor(up_ 1.5,,E); llabel(,\sf R_1,); } #DT1: dot; }
        R2: resistor(down_ 1.5,,E); rlabel(,\sf R_2,); DT2: dot;
     C1: capacitor(1.25,); rlabel(,\sf C,); 
        line right_ to (IC.Pin1, Here); 
        dot;
        {line to IC.Pin1;}
        {line to (IC.Pin5, Here) then to C2.end; }
        down_; gnd(0.5);

    # vetva napajania
        line from R1.end to (IC.Pin4, R1.end);
        dot;
        {line to IC.Pin4;} 
        {line to (IC.Pin8, Here) then to IC.Pin8;}
        up_; power(0.75, $\sf V_{cc}$ );
    # vystup        
        move to IC.Pin3; right_; tconn(,O); "$\sf V_{out}$" at Here ljust;
        "555" at IC.BX.ne ljust below;

        d = (IC.Pin2.x - DT2.x)/2
        line from DT2 right_ d; line up_ to (Here, IC.Pin2); dot; 
        {line to IC.Pin2;} 
        line up_ to (Here, IC.Pin6) then to IC.Pin6;
'''

_ = cm_compile('cm_0207b', data, dpi=600 )   
```


```{figure} ./src/cm_0207b.png
:width: 300px
:name: cm_0207b

[Zapojenie](./src/cm_0207b.ckt) multivibrátora s obvodom 555. 
```
