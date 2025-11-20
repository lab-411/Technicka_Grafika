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

## <font color='teal'> Nastavenie parametrov pracovnej plochy  </font>

Vlastnosti pracovnej plochy pre kreslenie zapojení ako aj zobrazenie objektov na ploche je možné nastavovať pomocou premenných praovného prostredia. Základné nastavenie pomocou premennej `scale` definuje veľkosť dĺžkovej jednotky (škálu) a premenné `maxpswid` a  `maxpsht` maximálne rozmery pracovnej plochy

    scale = 1               # základná jednotka je 1 inch (2.54cm) - default 
    scale = 2.54            # základná jednotka je 1 cm
    scale = 25.4            # základná jednotka je 1 mm
    maxpswid = 20           # maximálna šírka obrazku v základných jednotkách - default 11.5
    maxpsht = 10            # maximálna výška obrazku v základných jednotkách - default 8.5

V tejto knihe používame nastavenie základnej jednotky 1cm, zobrazenie súradnicovej mriežky je v tejto mierke a dáva predstavu o reálnej veľkosti obrázku pri jeho použití v publikácii. Základná konfigurácia prostredia použitá v tejto publikácii má potom formát

```
.PS
scale = 2.54            # zakladna jednotka v obrazku 1cm
maxpswid = 30           # maximálna šírka 30cm
maxpsht = 30            # maximálna výška 30cm
cct_init                # inicializácia knižnice makier CircuitMacros

include(base.ckt)       # import uživatelskej knižnice makier
Grid(5,3);              # zobrazenie mriežky - makro z uživatelskej knižnice
d = 1;                  # premenna 1cm
.PE
```


```{code-cell} ipython3 
:tags: ["remove-cell"]
from cm.utils import *

data = r'''
include(lib_base.ckt)
d = 1;
Grid(5,3);
'''

_ = cm_compile('./src/cm_0180a', data,  dpi=600)   
```

```{figure} ./src/cm_0180a.png
:width: 350px
:name: cm_0180a

[Vykreslenie](./src/cm_0180a.ckt) súradnicovej mriežky s rozmermi 5x3 cm
```

Hodnota aktuálnej (poslednej) pozície je hodnotou premennej `Here` v základných jednotkách.  

### <font color='brown'> Preddefinované premenné </font>

Vlastnosti základných objektov sú určené množinou preddefinovaných premenných. Aby pri zmene škálovanie obrázku nedošlo k zmene zobrazenia, sú tieto premenná modifikované (vynásobené) hodnotou premennej `scale`. 
   
| Premenná   | Hodnota | Význam 
|:---        | :----   | :--    
| arcrad     | 0.25    | arc radius
| arrowht    | 0.1     | length of arrowhead
| arrowwid   | 0.05    | width of arrowhead
| boxht      | 0.5     | box height
| boxrad     | 0       | radius of rounded box corners
| boxwid     | 0.75    | box width
| circlerad  | 0.25    | circle radius
| dashwid    | 0.05    | dash length for dashed lines
| ellipseht  | 0.5     | ellipse height
| ellipsewid | 0.75    | ellipse width
| lineht     | 0.5     | height of vertical lines
| linewid    | 0.5     | length of horizontal lines
| moveht     | 0.5     | length of vertical moves
| movewid    | 0.5     | length of horizontal moves
| textht     | 0       | assumed height of text (11pt for postscript, PDF, and SVG)
| textoffset | 2.5/72  | text justification gap
| textwid    | 0       | assumed width of text
 
Premenné prostredia, ktoré hodnota `scale` nemení.

| Premenná   | Hodnota | Význam 
|:---        | :----   | :--    
| arrowhead  | 1       | arrowhead shape
| fillval    | 0.5     | fill density
| linethick  | 0.8     | line thickness in points
| maxpsht    | 11.5    | maximum allowed diagram height
| maxpswid   | 8.5     | maximum allowed diagram width
        

TODO - Príkady použitia parametrov prostredia
