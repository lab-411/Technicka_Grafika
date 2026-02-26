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


# <font color='navy'> Externý editor </font>

Jednoduché integrované jednoduché prostredie `PyCirkuit` vyhovuje pri tvorbe a editácii menších obrázkov. Ak potrebujeme súčasne pracovať s niekoľkými zdrojovými súbormi a vytvárať rozsiahlejšie zapojenia, je vhodné použiť editor s bohatšími možnosťami pre editovanie textov a previazať ho s vhodným prehliadačom obrázkov. Vhodným editorom je napríklad [Geany](https://www.geany.org/), ktorý je možné rozšíriť o farebné zvýrazňovanie syntaxe. Pre prehliadanie obrázkov existuje množstvo programov. Na platforme Linuxu je možné použiť jednoduchý prehliadač obrázkov [sxiv](https://grfreire.github.io/sxiv/sxiv.1.html), ktorý automaticky obnovuje zobrazenie obrázku po každej jeho zmene,  {numref}`cm0915a`. 

```{figure} ./img/geany.png
:width: 800px
:name: cm0915a

Editor *Geany* a prehliadač obrázkov *sxiv*.
```

## <font color='teal'> Linux </font>

Editor *Geany* ako aj prehliadač obrázkov *sxiv* sú súčasťou distribúcií Linuxu a je možné ich nainštalovať priamo z repozitárov:

    sudo apt-get install geany
    sudo apt-get install sxiv
    
### <font color='brown'> Konfigurácia editora </font>

Editor *Geany* rozšírime o zvýrazňovanie syntaxe pomocou konfiguračných súborov obsahujúcich kĺúčové slová a mená makier, ktoré uložíme do adresárov:

* [filetype_extensions.conf](./data/filetype_extensions.conf) - nahráme do adresára *HOME/.config/geany/filedefs/*
* [filetypes.CircuitMacros.conf](./data/filetypes.CircuitMacros.conf) - nahráme do adresára *HOME/.config/geany/filedefs/*
* [main.ckt](./data/main.ckt) - nahráme do adresára *HOME/.config/geany/templates/files/* 

Po spustení editor bude farebne zvýrazňovať syntax jazyka *dpic* a názvy makier z *CircuitMacros*. Pretože rozšírenie pre analýzu zdrojového kódu je založené na analyzátore určenom pre jazyk **C**, nemusia sa správne rozpoznať niektoré jazykové konštrukcie špecifické pre jazyk *dpic* a makroprocesor *m4*. 

### <font color='brown'> Pracovný adresár </font>

Po inštalácii programov je vhodné usporiadať pracovný adresár v konfigurácii podľa obrázku {numref}`cm0915b`. Do adresára uložíme shell skripty [cmc.sh](./src/cmr.sh) a [cmr.sh](./src/cmr.sh), ktoré sú popísané v kapitole [Export obrázkov](./0900_priloha_cli.md). 

```{code-cell} ipython3  
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_color.ckt)

command "\sf"
boxrad=0.05;
B1: box wid 2.5 ht 0.5 "HOME/Work"; {color_red; "Pracovný adresár" at last box.e ljust; color_reset;}
line from B1.s down 1; dot;
{
    line right_ 1; B2: box wid 2 ht 0.5 "./cm";
    line from B2.s down_ 0.5
    box wid 2 ht 0.5 "libgcct.m4" invis fill 0.9; {color_red; "CircuitMacros" at last box.e ljust; color_reset;}
    box wid 2 ht 0.5 "libgen.m4" invis fill 0.9;  {color_red; "štandardné knižnice" at last box.e ljust; color_reset;}
    box wid 2 ht 0.5 "..." invis fill 0.9;
}

line down_ 2.8;
box wid 2.75 ht 0.5 "cmc.sh" invis fill 0.9; {color_red; "Skript pre kompiláciu" at last box.e ljust; color_reset;}
box wid 2.75 ht 0.5 "cmr.sh" invis fill 0.9; {color_red; "Skript pre zobrazenie" at last box.e ljust; color_reset;}
box wid 2.75 ht 0.5 "lib\_color.ckt" invis fill 0.9; {color_red; "Uživateľské knižnice" at last box.e ljust; color_reset;}
box wid 2.75 ht 0.5 "lib\_user.ckt" invis fill 0.9;
box wid 2.75 ht 0.5 "..." invis fill 0.9;
box wid 2.75 ht 0.5 "my\_program.ckt" invis fill 0.9; {color_red; "Pracovný súbor" at last box.e ljust; color_reset;}
'''

_ = cm_compile('cm_0915b', data,  dpi=600)   
```

```{figure} ./src/cm_0915b.png
:name: cm0915b
:width: 350px

Konfigurácia pracovného adresáru.
```

Nový súbor vytvoríme v editore *Geany* z hlavného menu voľbou *New (with Template) -> main.ckt*. Pred kompiláciou je potrebné súbor uložiť do pracovného adresára. Kompilácia a prehliadanie obrázkov je nakonfigurované v *Geany* pre klávesy: 

    F5 - kompilácia a zobrazenie obrázku
    F8 - kompilácia
    F9 - zobrazenie

Ak je aktívne zobrazenie (F5), po novej kompilácii (F8) sa obrázok v prehliadači *sxiv* automaticky prekreslí.




