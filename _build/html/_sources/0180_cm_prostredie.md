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

# <font color='navy'>  Prostredie   </font>

## <font color='teal'> Nastavenie parametrov plochy  </font>

Vlastnosti pracovnej plochy pre kreslenie zapojení ako aj zobrazenie objektov na ploche je možné nastavovať pomocou premenných pracovného prostredia. Základné nastavenie pomocou premennej `scale` definuje veľkosť dĺžkovej jednotky (škálu) a premenné `maxpswid` a  `maxpsht` určujú maximálne rozmery pracovnej plochy:

    scale = 1               # základná jednotka je 1 inch (2.54cm) - default 
    scale = 2.54            # základná jednotka je 1 cm
    scale = 25.4            # základná jednotka je 1 mm
    maxpswid = 20           # maximálna šírka obrazku v základných jednotkách - default 11.5
    maxpsht = 10            # maximálna výška obrazku v základných jednotkách - default 8.5


### <font color='brown'> Preddefinované premenné </font>

Vlastnosti základných objektov sú určené množinou preddefinovaných premenných. Aby pri zmene škálovanie obrázku nedošlo k zmene zobrazenia, sú tieto premenné modifikované (vynásobené) hodnotou premennej `scale`:
   
| Premenná   | Hodnota | Význam 
|:---        | :----   | :--    
| arcrad     | 0.25    | polomer oblúka
| arrowht    | 0.1     | dĺžka šípku
| arrowwid   | 0.05    | šírka šípky
| boxht      | 0.5     | výška obdĺžnika
| boxrad     | 0       | polomer zaoblených rohov obdĺžnika
| boxwid     | 0.75    | šírka obdĺžnika
| circlerad  | 0.25    | polomer kružnice
| dashwid    | 0.05    | dĺžka čiarky v čiarkovanej čiare alebo krivke
| ellipseht  | 0.5     | výška elipsy
| ellipsewid | 0.75    | šírka elipsy
| lineht     | 0.5     | výška zvislých čiar
| linewid    | 0.5     | dĺžka vodorovných čiar
| moveht     | 0.5     | dĺžka vertikálnych pohybov
| movewid    | 0.5     | dĺžka horizontálnych pohybov
| textht     | 0       | predpokladaná výška textu (11pt pre postscript, PDF, and SVG)
| textoffset | 2.5/72  | medzera v zarovnaní textu
| textwid    | 0       | predpokladaná šírka textu
 
Premenné prostredia, ktoré hodnota `scale` nemení:

| Premenná   | Hodnota | Význam 
|:---        | :----   | :--    
| arrowhead  | 1       | tvar hrotu šípky
| fillval    | 0.5     | hustota výplne
| linethick  | 0.8     | hrúbka čiary v bodoch
| maxpsht    | 11.5    | maximálna povolená výška diagramu
| maxpswid   | 8.5     | maximálna povolená šírka diagramu
        

## <font color='teal'> Príklad konfigurácie prostredia  </font>
        
V tejto knihe používame pre kreslenie nastavenie základnej jednotky 1cm. Použitie súradnicovej mriežky je v tejto mierke a dáva predstavu o reálnej veľkosti obrázku pri jeho použití v publikácii. Základná konfigurácia prostredia pre obrázok o maximálnom rozmere strany A4 má potom formát podľa nasledujúceho programu, {numref}`cm_0180a`:

```{code-block}
:caption: Príklad konfigurácie prostredia a vykreslenia objektov s preddefinovanými parametrami.
.PS
scale = 2.54            # základna jednotka v obrázku 1cm
maxpswid = 21           # maximálna šírka 21cm pre A4 format 21x30cm
maxpsht = 30            # maximálna výška 30cm
cct_init                # inicializácia knižnice makier CircuitMacros

include(base.ckt)       # import uživateľskej knižnice makier
Grid(5,3);              # zobrazenie mriežky - makro z uživateľskej knižnice
d = 1;                  # premenná 1cm

arrowht = 0.3;          # ukážka pouzitia parametrov šípok
arrowwid = 0.2;

arrowhead=0; line -> from (0.5,0.5) right_ d;
arrowhead=1; line -> from (0.5,1,0) right_ d;
arrowhead=3; line -> from (0.5,1.5) right_ d;

circlerad = 0.5;
circle at (3,0.5);      # kružnica s preddefinovaným polomerom

boxwid = 2;
boxht = 1;
boxrad = 0.25;
box at (3,2) dashed;    # obdľžnik s preddefinovanými parametrami

.PE
```


```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)
d = 1;
Grid(5,3);

arrowht=.3
arrowwid = .2

arrowhead=0; line -> from (0.5,0.5) right_ d
arrowhead=1; line -> from (0.5,1) right_ d
arrowhead=3;  line -> from (0.5,1.5) right_ d

circlerad=0.5;
circle at (3,0.5);

boxwid=2;
boxht=1;
boxrad=0.25;
box at (3,2) dashed;
'''

_ = cm_compile('cm_0180a', data,  dpi=600)   
```

```{figure} ./src/cm_0180a.png
:width: 350px
:name: cm_0180a

[Vykreslenie](./src/cm_0180a.ckt) súradnicovej mriežky s rozmermi 5x3 cm
```

Hodnoty súradníc, ako aj aktuálnej (poslednej) pozície, ktorá je hodnotou premennej `Here`, sú potom v základných jednotkách. Poloha počiatku mriežky je v ľavom dolnom roku stránky. Po renderovaní stránky sú voľné okraje obrázku orezané. 
