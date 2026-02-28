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


# <font color='navy'>Hybridné zapojenia</font> 

Elektronické zariadenia v súčasnej dobe sú komplexné systémy, ktorých dokumentácia si vyžaduje hierarchický prístup, v ktorom na najvyššej úrovni dokumentujeme jednotlivé funkčné celky a vzťahy medzi nimi. Diagramy majú často tvar hybridných zapojení, kde pre väčšiu názornosť kombinujeme funkčné bloky s diskrétnymi komponentami reprezentujúcimi vybrané častí zariadenia.

## <font color='teal'> Blokové zapojenia </font> 

Na obrázku {numref}`img_0208a` je blokové zapojenie zariadenia pre testy mechanických vlastností 3D tlačených materiálov. Zariadenie obsahuje centrálny mikrokontrolér, analógové a digitálne periférie, ktoré sú riadené prostredníctvom rozhraní mikrokontroléra. Prepojenia medzi jednotlivými funkčnými časťami sú realizované pomocou označených zberníc (*SPI*, *I2C*) ako aj vodičmi, ktoré môžu byť jednotlivé alebo v skupine (*pulse*, *switch* ...). Pre lepšiu prehľadnosť je v zapojení označené z koľkých vodičov zbernica alebo skupina vodičov pozostáva.

```{figure} ./src/exam_02_trhacka.png
:width: 700px
:name: img_0208a

[Blokové](./src/exam_02_trhacka.ckt) zapojenie zariadenia pre mechanické testy 3D tlačených materiálov [^odkaz1].
```


## <font color='teal'> Kombinované zapojenia </font> 

V niektorých prípadoch je vhodné pre väčšíu prehľadnosť zahrnúť do zapojenia aj znázornenie fyzickej realizácie zariadenia, ktorá by v čisto elektronickej podobe nemusela byť na prvý pohľad zrejmá. Na obrázku {numref}`img_0208b` je zapojenie analogovej časti kapacitného extenzometra, v ktorom sú $EL$, $EC$ a $ER$ elektródy extenzomera, pričom elektróde $EC$ je pohyblivá. Kondenzátory $C_{P1} ... C_{P3}$ reprezentujú parazitné montážne kapacity zariadenia.

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

#Grid(10,7)
d = 2;
boxrad=.1
x=1.2;
#right_;

#command"\sf"

CC: (5,3);
#LG: line from Here-(5,0) to Here+(5,0)

# centralna elektroda
EC: box wid d/10 ht 4 fill 0.8 with .c at CC; #(5,3);  
"EC\,\," at EC.n above;

# lava elektroda
EL: box wid d/10 ht 4 fill 0.8 with .c at CC-(x,0); 
"EL\,\," at EL.n above;

# prava elektroda
ER: box wid d/10 ht 4 fill 0.8 with .c at CC+(x,0); 
"ER\,\," at ER.n above;

right_;
dot(at EL.e);
C1: capacitor(from EL.e to EC.w);variable(,A,,1.1);rlabel(,C_1,)
dot;

dot(at EC.e);
C2: capacitor(from EC.e to ER.w);variable(,A,,1.1);rlabel(,C_2,)
dot;

# parazitne kapacity
dot(at EC.s);
CP3: capacitor(from EC.s down_ 1); rlabel(,C_{P3},); gnd(0.25);


dot(at ER.e);
line from ER.e right_ 0.5;
spline right_ d/8 then down_ d/8;
CP2: capacitor(down_ 1);llabel(,C_{P2},); gnd(0.25)

dot(at EL.w);
line from EL.w left_ 0.5;
spline left_ d/8 then down_ d/8;
CP1: capacitor(down_ 1);rlabel(,C_{P1},); gnd(0.25)

# budic EL
B1: EL.w +(0,1.5); 
dot(at B1);

right_; OP1: opamp(,,,) with .W at B1+(-2.5,0) ; #{"1" at OP1.W ljust;}
V1: dot; 
line from OP1.In1 left_ 0.5;
{line from OP1.In2 left_ 0.5; down_; gnd(0.5);}
V2: dot;
resistor(left_ 1.5,E); rlabel(,R_1,); 
TC1: tconn(0.5, O, 0.2); "PH1" at TC1.w rjust;
line from V2 up_ 0.75;
resistor(right_ to (V1, Here), E); llabel(,R_2,);line to V1;
line from V1 to B1; #dot(at B1);

# budic ER
B2: ER.e +(0,1.5);
dot(at B2);

right_; OP2: opamp(,,,) with .W at B1+(-2.5,2.5) ; #{"1" at OP1.W ljust;}
V3: dot; 
line from OP2.In1 left_ 0.5;
{line from OP2.In2 left_ 0.5; down_; gnd(0.5);}
V4: dot;
resistor(left_ 1.5,E); rlabel(,R_3,);
TC2: tconn(0.5, O, 0.2); "PH2" at TC2.w rjust;
line from V4 up_ 0.75;
resistor(right_ to (V3, Here), E); llabel(,R_4,);line to V3;
line right_ to (B2+(0.5,0), Here);
line to (Here, B2)then to B2

# oddelovaci zosilovac
D5: dot(at EC.e + (0, 1));
line from D5 right_ 3.5; {dot; down_; resistor(1.5,E); rlabel(,R_P,);gnd();}
line right_ 0.5;
OP3: opamp()  with .In2 at Here;
D6: dot; TC3: tconn(0.75, O, 0.2); "SG" at TC3.e ljust;
line from D6 up_ 1;
line left_ to (OP3.In1+(-0.5,0), Here);
line to (Here, OP3.In1) then to OP3.In1

# posun
color_red; 
D7: dot(at EC.n+(0,1)); "dx" above;
line -> from D7 left_ 1;
line -> from D7 right_ 1;
'''

_ = cm_compile('cm_208b', data, dpi=600 )   
```

```{figure} ./src/cm_208b.png
:width: 650px
:name: img_0208b

Zapojenie analogovej časti kapacitného extenzometra [^odkaz2]..
```


[^odkaz1]: Blokové zapojenie prevzaté z práce:

    PhD práca ....
    
[^odkaz2]: Projekt VEGA 2/0013/25

    Interpretácia periodických a neperiodických deformácií zemskej kôry v oblasti Západných Karpát na základe paralelných meraní horizontálnych posunutí.
