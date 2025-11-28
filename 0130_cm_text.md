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

# <font color='navy'> Texty </font>

Základné formátovanie textov a popisov prvkov zapojenie je možné priamo v `CircuitMacros` pomocou makier *rlabel ...*, rozšírené formátovanie textov je možné s využitím príkazov jazyka `dpic` a renderovania textu pomocou LaTeX-u. 
Text môže obsahovať diakritiku, formátovacie príkazy ako aj matematické výrazy v syntaxi LaTeX-u. 

## <font color='teal'> Zadanie textu   </font>

Pre kreslenie textu do obrázku je určený príkaz v tvare 

    "text"  at location [position];
    
        locatiom - poloha stredu renderovaného textu

        position - relatívna poloha voči location
            ljust      horizontálne zarovnanie vlavo
            rjust      horizontálne zarovnanie vpravo
            above      vertikálne zarovnanie nahor
            belov      vertikálne zarovnanie nadol

Textový reťazec ohraničený obyčajnými uvodzovkami je pri spracovaní odoslaný na renderovanie do LateX-u a umiestnený (ako obrázok) do polohy *location*. Poloha textu môže byť zadaná absolútnou pozíciou, referenciou na objekt alebo odkazom na posledný použitý komponent (*last line*, *last box*, *last text* ...). Vlastná veľkosť textu (ohraničenia) **nie je** známa, pretože samotný text je vytváraný až pri renderovaní a jeho veľkosť závisí od typu a veľkosti fontu. Relatívne umiestnenie voči tejto polohe je možné upraviť pomocou parametra *position*, jeho použitie ukazuje nasledujúci obrázok

    BX: box wid 4.5 ht 1.5 at (0,0);
    LL: line from (-1,0) to (1,0);
        "rjust" at LL.start  rjust;
        "ljust" at LL.end ljust;
        "above" at LL.center above;
        "below" at LL.center below;

        "rjust" at BX.w rjust;
        "ljust" at BX.e ljust;
        "above" at BX.n above;
        "below" at BX.s below;

        "ljust above" at last box.ne ljust above;
        "ljust below" at last box.se ljust below;
        "rjust below" at last box.sw rjust below;
        "rjust above" at last box.nw rjust above;

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
Origin: Here 
BX: box wid 4.5 ht 1.5 at (0,0);
LL: line from (-1,0) to (1,0);
"rjust" at LL.start  rjust;
"ljust" at LL.end ljust;
"above" at LL.center above;
"below" at LL.center below;

"rjust" at BX.w rjust;
"ljust" at BX.e ljust;
"above" at BX.n above;
"below" at BX.s below;

"ljust above" at last box.ne ljust above;
"ljust below" at last box.se ljust below;
"rjust below" at last box.sw rjust below;
"rjust above" at last box.nw rjust above;
'''
_ = cm_compile('cm_0130a', data, dpi=600)   
```

```{figure} ./src/cm_0130a.png
:width: 400px
:name: cm_0130a

[Relatívne](./src/cm_0130a.ckt) umiestnenie textu voči zadanej polohe.
```
    
Text modifikuje globálnu premennú `Here`, po vykreslení textu je nová hodnota poloha `Here` v geometrickom strede textu.

## <font color='teal'>  Farba textu  </font>

Pre nastavenie farby je možné použiť 

* pre globálne nastavenie farby vrátane textov sú makrá *rgb()* resp. preddefinované pomenované farby zadefinované v súbore [lib_color.ckt](./src/lib_color.ckt) v tvare *color_<meno_farby>*. 

        ...
        color_red;
        color_green;
        ...
    
* pre lokálne nastavenie farby textu je možné použiť v zadaní textu prostredie *color* z LaTexu v tvare *\color{<farba>}*

        "\color{red} červený text" at (1, 1); 
        
Vyššiu prioritu má nastavenie lokálnej farbu textu.
        
        BOX: box wid 3 ht 2 at (5,4);
            "stred boxu" at BOX.c;                     dot;
            "\color{red} červený text" at BOX.n above; dot;
            
            color_dark_orange;                               # globalne
            "\color{blue} text vpravo" at BOX.e ljust; dot;  # lokalne
            "text vlavo dole" at BOX.sw rjust below;   dot;

            color_blue;
        LL: line from (2, 1.5) right_ 6;
            "stred čiary" at last line.c above;        dot;
        
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

Origin: Here 
Grid(10,5);


BOX: box wid 3 ht 2 at (5,3);
    "stred \,\,\,  boxu" at BOX.c;             dot;
    "\color{red} červený text" at BOX.n above; dot;
    
    color_dark_orange;
    "\color{blue} text vpravo" at BOX.e ljust; dot;
    "text vlavo dole" at BOX.sw rjust below;   dot;

    color_blue;
LL: line from (2, 0.5) right_ 6;
    "stred čiary" at last line.c above;        dot;
'''

_ = cm_compile('cm_0130b', data, dpi=600 )   
```

```{figure} ./src/cm_0130b.png
:width: 500px
:name: cm_0130b

[Pozícia](./src/cm_0130b.ckt) a farby textu
```

## <font color='teal'>  Matematické výrazy  </font>

Pre zobrazenie matematických výrazov sa používa štandardné formátovanie LaTeX-u. Matematický vzťah alebo matematický text sa korektne zobrazí len pri renderovaní pomocou nainštalovaného LaTeX-u.

Funkcia `sprintf` pre konverziu čísla na formátovaný reťazec akceptuje formatovacie znaky *%e, %f, %g*.

    T: "$\sqrt{\sin(\alpha^2) + \cos(\beta^2)}$" at (5, 0.5);    

       "$f(a)+\frac {f'(a)}{1!} (x-a) + 
       \frac{f''(a)}{2!} (x-a)^2 + 
       \frac{f^{(3)}(a)}{3!}(x-a)^3 + \cdots$" at (5,3);   
        
       color_red;
       sprintf("Formatovany text $x=%2.3f$ \,\, $y=%2.3f $", T.x, T.y) at (5, 1.5);


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

Origin: Here 
Grid(10, 4);

T: "$\sqrt{\sin(\alpha^2) + \cos(\beta^2)}$" at (5, 0.5);    

"$f(a)+\frac {f'(a)}{1!} (x-a) + 
       \frac{f''(a)}{2!} (x-a)^2 + 
       \frac{f^{(3)}(a)}{3!}(x-a)^3 + \cdots$" at (5,3);   

color_red;
sprintf("Formatovany text $x=%2.3f$ \,\,  $y=%2.3f $", T.x, T.y) at (5, 1.5);
'''

_ = cm_compile('cm_0130c', data, dpi=600)   
```

```{figure} ./src/cm_0130c.png
:width: 600px
:name: cm_0130c

[Použitie](./src/cm_0130c.ckt) matematických výrazov
```

## <font color='teal'>  Formátovanie textu pomocou LaTeX-u  </font>

Jaxyk `dpic` poskytuje len obmedzené možnosti formátovania textu. Ak je pre renderovanie použitý LaTeX, je možné používať pre úpravu textu príkazy z jeho prostredia, tieto sú súčasťou textu v úvodzovkách. Možnosti úpravy textu sú v LaTeXe rozsiahle, podrobnosti sú popísané v jeho [dokumentácii](https://www.latex-project.org/help/documentation/fntguide.pdf).

Pre prepínanie typu fontu sú v LaTeX-e definované 3 základné skupiny príkazov pre výber kolekcie textu, fomátovania a tvaru textu v rámci kolekcie. Príkazy sa môžu vzťahovať na vybranú časť textu uzatvorenú v zložených zátvorkách `{...}` alebo na na celý text. Výber z LaTeX príkazov pre formátovanie textu 

**Výber kolekcie fontov**

    font Roman        \rmfamily  \rm   \textrm{...}
    font Sans Serif   \sffamily  \sf   \textsf{...}
    font Typewriter   \fffamily  \tt   \texttt{...}
    
**Forma textu**

    tučný text       \bfseries   \bf   \textbf{...}
 
 **Tvar textu v kolekcii**
     
    šikmý text       \itshape    \it   \textit{...}
    naklonený text   \slshape    \sl   \textsl{...}
    malé písmená     \scshape    \sc   \textsc{...}

**Velkosť písma**

    \tiny     \scriptsize    \footnotesize   \small   \normalsize 
    \large    \Large         \LARGE          \huge    \Huge   
    
**Rotácia textu**
    
    \rotatebox{angle}{text}
    
Poloha otočeného textu je vždy v jeho strede, pridávanie medzier na začiatok alebo koniec textu neposunie stred textu.

**Podčiarknutý text**

    \underline{Underline}
    
Príklad formátovania textu s použitím príkazov LaTex-u:

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
Grid(10.5,5);


"\textit{Italic 123}" at (1.5, 0.5);
"\textbf{Bold 123}" at (1.5, 1.0);
"\textsc{SmallCaps 123}" at (1.5, 1.5);
"\textsl{Slanted 123}" at (1.5, 2);
"\textrm{Roman 123}" at (1.5, 3.5);
"\textsf{Sans Serif 123}" at (1.5, 4);
"\texttt{Typewriter 123}" at (1.5, 4.5);

for i=0 to 300 by 60 do {
  move to ( 5 + 1*cos(i/180*pi), 2.5 + 1*sin(i/180*pi) );
  sprintf("\rotatebox{%g}{Text %g}", i,i );
}

"\tiny  tiny  \scriptsize scriptsize \footnotesize footnotesize" at (8.5, 4.5);
" \small small \normalsize normalsize " at (8.5,4)
"\large large  \Large Large " at (8.5,3.25)
"\LARGE LARGE" at (8.5,2.5)
"\huge huge" at (8.5, 1.5)
"\Huge Huge" at (8.5, 0.5)
'''

_ = cm_compile('cm_0130d', data, dpi=600)   
```

```{figure} ./src/cm_0130d.png
:width: 600px
:name: cm_0130d

[Formátovanie](./src/cm_0130d.ckt) textu pomocou príkazov LaTeX-u
```


