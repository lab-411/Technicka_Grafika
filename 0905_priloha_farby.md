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


# <font color='navy'> Farby </font> 

Pre farebné zobrazenie objektov je možné využiť makro *setrgb()* a *rgbfill()* v ktorých sa farba definuje pomocou zložiek *r, g, b*. Pretože používanie takto definovaných farieb je nepohodlné, v súbore [lib_color.ckt](./src/lib_color.ckt) sú definované makrá vybraných pomenovaných farieb podľa [zoznamu](https://en.wikipedia.org/wiki/Web_colors).

## <font color='teal'> Farby čiar </font> 

Makro pre definíciu farby pre čiary, krivky, texty a obrys plošných objektov má tvar 

    define(`meno_farby', `setrgb(r, g, b) ')
    define(`meno_farby', `setrgb(R/255, G/255, B/255) ')
    
    r, g, b    - zložky farby v rozsahu <0.0, 1.0>
    R, G, B    - zložky farby v rozasahu <0, 255>
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_color.ckt)
move to (3.5,0);

color_black; box wid 1 ht 0.5; "co\\lor\_black" at last box .w rjust;
color_grey; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_grey" at last box .w rjust;
color_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_blue" at last box .w rjust;
color_green; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_green" at last box .w rjust;
color_red; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_red" at last box .w rjust;

color_olive; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_olive" at last box .w rjust;
color_khaki; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_khaki" at last box .w rjust;
color_dark_khaki; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_dark\_khaki" at last box .w rjust;
color_steel_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_steel\_blue" at last box .w rjust;
color_navy; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_navy" at last box .w rjust;

color_dark_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_dark\_blue" at last box .w rjust;
color_medium_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_medium\_blue" at last box .w rjust;
color_royal_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_royal\_blue" at last box .w rjust;
color_dodger_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_dodger\_blue" at last box .w rjust;
color_sky_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_sky\_blue" at last box .w rjust;

color_midnight_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_midnight\_blue" at last box .w rjust;
color_cornflower_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_cornflower\_blue" at last box .w rjust;
color_deep_sky_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_deep\_sky\_blue" at last box .w rjust;
color_powder_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_powder\_blue" at last box .w rjust;
color_orange_red; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_orange\_red" at last box .w rjust;

move to (5,0);

color_cyan; box wid 1 ht 0.5; "co\\lor\_cyan" at last box .e ljust;
color_brown; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_brown" at last box .e ljust;
color_orange; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_orange" at last box .e ljust;
color_violet; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_violet" at last box .e ljust;
color_light_grey; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_light\_grey" at last box .e ljust;

color_light_blue; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_light\_blue" at last box .e ljust;
color_dark_grey; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_dark\_grey" at last box .e ljust;
color_dark_cyan; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_dark\_cyan" at last box .e ljust;
color_dark_green; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_dark\_green" at last box .e ljust;
color_dark_orange; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_dark\_orange" at last box .e ljust;

color_dark_red; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_dark\_red" at last box .e ljust;
color_dark_violet; box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_dark\_violet" at last box .e ljust;
color_aquamarine;  box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_aquamarine" at last box .e ljust;
color_silver;  box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_silver" at last box .e ljust;
color_cadet_blue;  box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_cadetblue" at last box .e ljust;

color_coral;  box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_coral" at last box .e ljust;
color_gold;  box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_gold" at last box .e ljust;
color_mediumForestGreen;  box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_mediumForestGreen" at last box .e ljust;
color_slategrey;  box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_slategrey" at last box .e ljust;
color_firebrick;  box wid 1 ht 0.5 with .ne at last box.se + (0, -0.1); "co\\lor\_firebrick" at last box .e ljust;
'''

_ = cm_compile('cm_0905a', data, dpi=600)   
```

```{figure} ./src/cm_0905a.png
:width: 450px
:name: cm_0905a

Mená vybraných farieb 
```

Použitie pomenovaných farieb pre čiary, krivky, obrysy plošných objektov a texty.

    color_orange;       # farba čiary
    box wid 1 ht 0.5;   # pre obrys objektu bude použitá nastavená farba
    color_reset;        # nastavenie čiernej farby


## <font color='teal'> Farby výplní </font> 

Pre farebnú výplň plošných objektov a uzatvorených oblastí sú definované makrá

    define(`fill_<name>', `r, g, b')
    define(`fill_<name>', `R/255, G/255, B/255')

    rgbfill( fill_<name>, {uzavreta oblast, box, circle ...})
    rgbfill( r, g, b, {uzavreta oblast, box, circle ...})
    rgbfill( R/255, G/255, B/255, {uzavreta oblast, box, circle ...})
    
    <name>     - meno farby
    r, g, b    - zložky farby v rozsahu <0.0, 1.0>
    R, G, B    - zložky farby v rozasahu <0, 255>



```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_color.ckt)

color_reset;
move to (3.5,0);
Bx: Here
rgbfill(fill_black , BA:box wid 1 ht 0.5 at Bx.s + (0, -.35)); "fi\\ll\_black" at last box .w rjust;
rgbfill(fill_grey , BB:box wid 1 ht 0.5 at BA.s + (0, -.35)); "fi\\ll\_grey" at last box .w rjust;
rgbfill(fill_yellow , BC:box wid 1 ht 0.5 at BB.s + (0, -.35)); "fi\\ll\_yellow" at last box .w rjust;
rgbfill(fill_cyan , BD:box wid 1 ht 0.5 at BC.s + (0, -.35)); "fi\\ll\_cyan" at last box .w rjust;
rgbfill(fill_orange , BE:box wid 1 ht 0.5 at BD.s + (0, -.35)); "fi\\ll\_orange" at last box .w rjust;
rgbfill(fill_violet , BF:box wid 1 ht 0.5 at BE.s + (0, -.35)); "fi\\ll\_violet" at last box .w rjust;

move to (5,0);
Bx: Here
rgbfill(fill_dark_green , BA:box wid 1 ht 0.5 at Bx.s + (0, -.35)); "fi\\ll\_dark\_green"   at last box .e ljust;
rgbfill(fill_dark_orange, BB:box wid 1 ht 0.5 at BA.s + (0, -.35)); "fi\\ll\_dark\_orange"  at last box .e ljust;
rgbfill(fill_red,         BC:box wid 1 ht 0.5 at BB.s + (0, -.35)); "fi\\ll\_red"     at last box .e ljust;
rgbfill(fill_blue,        BD:box wid 1 ht 0.5 at BC.s + (0, -.35)); "fi\\ll\_blue"     at last box .e ljust;
rgbfill(fill_green,       BE:box wid 1 ht 0.5 at BD.s + (0, -.35)); "fi\\ll\_gren"     at last box .e ljust;
rgbfill(fill_dark_violet, BF:box wid 1 ht 0.5 at BE.s + (0, -.35)); "fi\\ll\_dark\_violet"     at last box .e ljust;
'''

_ = cm_compile('cm_0905b', data, dpi=600)   
```

```{figure} ./src/cm_0905b.png
:width: 320px
:name: cm_0905b

Mená farieb pre výplň plošných objektov.
```

    include(base.ckt)
    Grid(4,4)

    define(`triangle', `
    [  
        line from (1,1) to (0,0) then to (1,-1);
        arc cw from (1,1) to (1,-1)
    ]')

    move to (1,2);
    color_red;
    rgbfill(fill_yellow, {triangle} );


Príklad použitia farebnej výplne plošného objektu pomocou makra *rgbfill()*. Uzatvorený objekt je v makre použitý v bloku, preto vykreslenie objektu **nemení** hodnotu `Here`.

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)
Grid(4,4)

define(`triangle', `
[  
    line from (1,1) to (0,0) then to (1,-1);
    arc cw from (1,1) to (1,-1)
]')

move to (1,2);
color_red;
rgbfill(fill_yellow, {triangle} );
'''

_ = cm_compile('cm_0905c', data,  dpi=600)   
```

```{figure} ./src/cm_0905c.png
:width: 300px
:name: cm_0905c

[Príklad](./src/cm_0905c.ckt) objektu s farebnou výplňou.
```


