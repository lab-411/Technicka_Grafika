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


# <font color='navy'> Základy kreslenia</font> 

Princíp vytvárania zapojení v `CircuitMacros` spočíva v zapise príkazov do štandardného textového súboru, ktorý po kompilácii vytvára prvky zapojenia na virtuálnej ploche. Súbor s príkazmi začína  *.PS* a končí *.PE*, príkazy a texty mimo tohoto označenia sú ignorované. 

```{code-block}
:caption: Prvý program
.PS               - zaciatok postupnosti prikazov
scale=2.54        - nastavenie parametru velkosti obrazku
cct_init          - inicializacia kniznice s analogovými prvkami (rezistor, ...)

resistor;         - príkaz pre vykreslenie rezistoru

.PE               - koniec postupnosti prikazov
```

Najjednoduchším spôsobom kreslenia zapojení je použitie jednoduchého programu *PyCirkuit*, ktorý obsahuje editor diagramov, prehliadač generovaných obrázkov a umožnuje ich export do rôznych formátov. V ďaľších príkladoch v tejto publikácii budeme uvádzať len príkazy na kreslenie zapojenia bez spoločných príkazov pre formátovanie a nastavenie generovania obrázkov (*.PS*, *.PE* ...) 

```{figure} ./img/pck_01.png
:width: 500px
:name: pck01

Editácia a preklad zapojenia v programe *PyCirkuit*
```

Príkaz na riadku je ukončený bodkočiarkou `;` alebo ukončenim riadku (neviditeľný znak `\n`). Bodkočiarku využijeme aj vtedy, ak budeme do jedného riadku zadávať niekoľko príkazov. Po nakreslení zapojenia vygenerujeme obrázok tlačítkom *Export* vo vhodnom formáte, ktorý si zvolíme v konfigurácii programu.

```{figure} ./img/pck_02.png
:width: 600px
:name: pck02

Konfigurácia formátu exportovaných obrázkov v programe *PyCirkuit*
```


## <font color='teal'> Ukladanie prvkov </font> 

Každý prvok diagramu alebo schémy je vykreslený na v diagrame na 2D pozícii, ktorá je uchovávaná v virtuálnom kurzore označenom ako `Here`. Prvky v zapojení (*resistor*, *capacitor*) ukladáme za sebou v zadaných smeroch príkazmi **up_**, **down_**, **right_** a **left_** . Pri zmene smeru sa automaticku mení aj orientácia prvku. Pre zobrazenie bodu spojenia niekoľkých prvkov použijeme makro *dot* 

```{code-block}
right_;
resistor;
resistor;
dot;
down_;
capacitor;
right_;
diode;
```

    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 

right_;
resistor;
resistor;
dot;
down_;
capacitor;
right_
diode;
'''

_ = cm_compile('cm_0014a', data, dpi=600)   
```

```{figure} ./src/cm_0014a.png
:width: 300px
:name: cm_0014a

Ukladanie prvkov zapojenia na základe ich poradia v programe.
```

Po vykreslení nejakého prvku zapojenie sa hodnota kurzora `Here` posúva v smere ukladanie tak, aby prvky zapojenie na seba nadväzovali. Polohu kurzoru môžeme presunúť na novú pozíciu (x,y) pomocou príkazu 

    move to (x,y);
    
alebo vykreslením prepojovacieho vodiča alebo čiary príkazom *line*, kurzor `Here` sa po vykreslení presunie na koniec čiary

    line to (x,y);                 - vykrelenie čiary z Here do (x,y) 
    line right_ d;                 - čiara z Here zadaným smerom a dĺžkou
    line from (x1,y1) to (x2,y2);  - čiara medzi dvoma bodmi


## <font color='teal'> Referencie a atribúty </font> 
    
Každý prvok v zapojení môžeme označiť pomocou textovej referencie ukončenej znakom `:`, táto musí byť zapísaná veľkými písmenani a nesmie začínať číslicou. Po vytvorení je referencia globálna, je ju možno použiť v ktorejkolvek časti zapojenia.

    R1: resistor;       - referencia R1
    r1: resistor;       - chyba
    1R: resistor;       - chyba

K prvkom zapojenia a polohe ich častí pristupovať pomocou referencie a pomenovaných atribútov oddelených od seba bodkou `.` Skupiny prvkov, napríklad dvojpóly (*resistor* ...), majú spoločné atribúty a každý typ prvku môže mať naviac aj vlastné, špecifické atribúty. Napríklad, spoločné atribúty pre dvojpóly sú:

    .start    .s         - bod v ktorom bol začiatok kreslenia prvku
    .end      .e         - bod v ktorom skončilo kreslenie prvku
    .center   .c         - geometrický stred prvku
    
Atribút má hodnotu súradnice označenej časti prvku. Na nasledujúcom príklade je ukázané použitie referencií a atribútov v zapojení. Pomocná mriežka je vykreslená pre zobrazenie skutočných pozícií prvkov zapojenia.

```{code-block}
:emphasize-lines: 5
    move to (1,1);
R1: resistor;                 # referencia, R1.start = (1,1)
    move to (1,2)
C1: capacitor;                # referencia C1.start = (1,2)
    line from R1.start to C1.end; # spoj medzi bodmi zadanými referenciami a atribútmi
```
    
```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)

Grid(4,3);
Origin: Here 

move to (1,1);
R1: resistor
move to (1,2)
C1: capacitor;

line from R1.start to C1.end;
'''

_ = cm_compile('cm_0014b', data, dpi=600)   
```

```{figure} ./src/cm_0014b.png
:width: 250px
:name: cm_0014b

Použitie referencií pri ukladaní prvkov zapojenia.
```

## <font color='teal'> Vlastnosti prvkov </font> 

Makrá pre zobrazenie prvkov majú zvyčajne niekoľko parametrov, pomocou ktorých môžeme meniť a upravovať zobrazenie prvku v zapojení. Napríklad pre zobrazenie rezistoru má makro zo štandardnej knižnice `CircuitMacros` nasledujúci formát:

    resistor(linespec, n, chars, cycle wid)

    linespec    - dĺžka rezistoru, môže byť aj so zadaním smeru
    n           - počet cyklov v USA norme rezistoru
    chars       - typ zobrazenia rezistoru (napr. E - europske zobrazenie)
    cycle wid   - velkosť cyklov v USA norme
    
Súčasťou zapojenia elektronickéjho obvodu je textový popis prvkov, ktorý zvyčajne pozostáva z označenie prvku, napríklad $R_1$ a jeho hodnoty, napríklad $100 \Omega$. Ukladanie popisov prvkov v komplikovanejších obvodoch pomocou jednoduchých textov by bolo značne náročné, naviac s rizikom nesprávneho označenia alebo pomiešania označenia napríklad pri zmene alebo úprave polohy prvkov. Pre zjednodušenie popisu (označenie, hodnota) posledného zobrazovaného prvku typu dvojpól môžeme preto použiť makrá, ktoré zväzujú texty s označením a s príslušným prvkom. 

    llabel( slabel, xlabel, elabel )  - označenie po lavej strane v smere ukladania
    rlabel( slabel, xlabel, elabel )  - označenie po pravej strane v smere ukladanie 
  
    parametre:
    
        slabel       - označenie v bode začiatku prvku
        xlabel       - označenie v strede prvku
        elabel       - označenie v bode konca prvku
    
Použitie makier na označovanie prvkov garantuje presné a definované umiestnenie popisu voči prvku a rovnaké umiestnenie popisov pre všetky prvky v zapojení. Relatívna poloha popisu prvku sa nemení ani pri presunutí prvku do iného bodu zapojenia. Tieto vlastnosti značne uľahčujú kreslenie zapojení, pretože v zapojeniach elektronických obvodov je zvyčajne veľké množstvo textu a popisov prvkov. Nasledujúci príklad ukazuje zapojenie s označením prvkov a využitie referencie pre zadanie počiatočného bodu kreslenia prvku (*R2*). V označení prvkov zapojenia môžeme použiť syntax pre zápis matematických výrazov v LaTeX-e, napríklad R_1 = $R_1$ (vyžaduje inštaláciu LaTeX-u).

```{code-block}
    move to (0.5, 2.5);  
R1: resistor(2,,E); llabel(a,R_1,b); rlabel(,10k,);
D1: dot;
C1: capacitor(down_ 2,); rlabel(,C_1,); llabel(,10 \mu F,);
R2: resistor(from D1 right_ 2,,E); llabel(,R_2,); rlabel(,33k,);
```

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

Grid(5,3.5);
Origin: Here 

move to (0.5,2.5);
R1: resistor(2,,E); llabel(a,R_1,b); rlabel(,10k,);
D1: dot;
C1: capacitor(down_ 2,); rlabel(,C_1,); llabel(,10 \mu F,);
R2: resistor(from D1 right_ 2,,E); llabel(,R_2,); rlabel(,33k,);

'''

_ = cm_compile('cm_0014c', data, dpi=600)   
```

```{figure} ./src/cm_0014c.png
:width: 300px
:name: cm_0014c

Označenie prvkov zapojenia.
```

## <font color='teal'> Kreslenie diagramov </font> 

V `CircuitMacros` môžeme využívať  príkazy jazyka `dpic` pre kreslenie diagramov pomocou 2D objektov ako je *box*, *circle*, *ellippse*, *arc*, ako aj lineárnych objektov *line*, *arrow*, *spline* a príkaz pre presun kurzora *move*. Pre kreslenie komplikovanejších diagramov (signálové grafy, vývojové diagramy) sú v `CircuitMacros` dostupné knižnice špecializovaných makier pre zvolený typ diagramu.

    box wid 2 ht 1 "Box";
    line -> right_ 1;
    circle rad 0.5 "r=0.5";
    line -> right_ 1;
    ellipse wid 2 ht 1 "Ellipse";


```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)

#Grid(5,3.5);
Origin: Here 

box wid 2 ht 1 "Box";
line -> right_ 1;
circle rad 0.5 "r=0.5";
line -> right_ 1;
ellipse wid 2 ht 1 "Ellipse";

'''

_ = cm_compile('cm_0014d', data, dpi=600)   
```

```{figure} ./src/cm_0014d.png
:width: 400px
:name: cm_0014d

Jednoduchý [diagram](./src/cm_0014d.ckt) vykreslený pomocou príkazov *dpic*
```



