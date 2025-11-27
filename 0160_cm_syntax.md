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
# <font color='navy'> Jazyk *dpic*  </font>

Programovací jazyk `dpic` bol špeciálne vytvorený na kreslenie grafov a diagramov s možnosťou ich exportu ako obrázkov alebo vkladania do textových dokumentov. Obsahuje príkazy pre kreslenie lineárnych objektov ako čiara, šipka, krivka, ako aj plošné objekty ako pravouholník, kružnica, elipsa, oblúk a umožňuje vytváranie zložených objektov. Zložitejšie grafických objekty ktoré sa v obrázkoch vyskytujú častejšie, ako sú značky elektronických súčiastok, je možné v `dpic` kresliť pomocou makier, ktoré obsahujú kód pre nakreslenie objektu. `CircuitMacros` je rozšírením `dpic` o knižnice makier pre kreslenie elektronických obvodov a zapojení. 


```{admonition} Programovací jazyk *dpic*
Programovací jazyk `dpic` historicky vychádza z jazyka [pic](./data/pic.pdf) vytvoreného Brian W. Kernighan-om v roku 1991.  Z programátorského hľadiska `dpic` patrí do skupiny tzv. *mini-jazykov*, ([DSL](https://en.wikipedia.org/wiki/Domain-specific_language)) ktoré sú vytvorené pre nejaký konkrétny učel na rozdiel od *všeobecne použiteľných jazykov* ([GPL](https://en.wikipedia.org/wiki/General-purpose_language)). Syntax jazyka `dpic` je veľmi jednoduchá, okrem príkazov na kreslenie grafických objektov má aj základné jazykové konštrukcie na riadenie toku programu ako je podmienkové vetvenie a cyklus. Nie je v ňom možné ale vytvárať funkcie, ktorú sú formálne nahradené makrami. Makrá obsahujú kód pre kreslenie zložitejších objektov a pri ich použití kompilátor nahradí v programe meno makra týmto kódom. 
```


## <font color='teal'> Program </font>

Program je tvorený textovým súborom, ktorý začína znakmi **.PS** a končí znakmi **.PE**. Príkaz na riadku je ukončený bodkočiarkou `;` alebo ukončenim riadku (neviditeľný znak `\n`). Bodkočiarka na ukončenie príkazu nie je povinná, na rozdiel napr. od jazyka `C`, ale  využijeme  vtedy, ak budeme do jedného riadku zadávať niekoľko príkazov. 

    .PS                           # zaciatok postupnosti prikazov
    scale=2.54                    # príkaz nastavenie parametrov velkosti obrazku
    cct_init                      # príkaz pre inicializaciu kniznice makier 
                                  #  s analogovými prvkami (rezistor, ...)

    line from (1,1) to (2,2)      # príkaz dpic pre vykreslenie čiary
    resistor                      # makro pre vykreslenie rezistoru
    rezistor(,,E);                # makro s parametrami
    resistor(2,,E); rlabel(,R1,); # niekolko príkazov v jednom riadku

    .PE                           # koniec postupnosti prikazov
 

Text za koncom programu je ignorovaný. Ukončenie programu môžeme prakticky využiť pri hľadaní chýb v skripte, kedy pomocou **.PE** vyradíme zbytok programu zo spracovania.
 
### <font color='brown'> Komentáre </font>

Komentáre začínajú znakom # a končia koncom riadku. Blokové komentáre nie sú definované, je ale možné použiť viacriadkové komentáre s riadkami ukončenými \\\\\\\\.

```Python
# toto je jednoriadkovy komentar
# toto je dvojriadkovy komentar        \\
  a jeho pokracovanie na dalsom riadku
```

White-space (tabulátory, medzery, znak nového riadku) sú vo výrazoch ignorované

```Python
    name( x,
    y, z )
```
        
je ekvivalent

```Python
    name(x,y,z)
```
        
### <font color='brown'> Hodnoty </font>

* Numerické hodnoty môžu obsahovať desatinnú bodku alebo môžu byť vo vedeckom formáte. Všetky numerické hodnoty sú interne uchovávané vo formáte *floating-point*.
* Polohy súradníc sú zapísané usporiadanou dvojicou *(x,y)*, každá súradnica implicitne obsahuje atribúty *.x* a *.y*.
* Textové reťazce sú zapísané pomocou úvodzoviek *"Toto je text"*

### <font color='brown'> Premenné </font>

Meno premennej  musí začínať písmenom nasledovaným ľubovolným počtom alfanumerických znakov. Premenné sa vytvoria pri ich definícii, musia byť inicializované **numerickou** hodnotou a sú globálne t.j. majú platnosť v celom zdrojovom kóde. 

```Python
d  = 2;
pi = 3.14159265359;
q  = 2*pi*8;
```    

Súradnice bodov sú reprezentované ako dvojice (x,y) a **nemôžu** byť použité ako hodnoty premennej, môžu ale byť reprezentované referenciou.

```Python
p1 = (3,4);    # chyba   
P1: (3,4);     # ok
```  

Text je postupnosť znakov definované v obyčajných úvodzovkách a **nemôže** byť použitý ako hodnota premennej. Stred zobrazeného textu ale môže byť reprezentovaný referenciou. 

```Python
str = "Toto je text"          # chyba   
T1: "Toto je text" at (1,1);  # ok, stred textu je v bode (1,1)
```    


### <font color='brown'> Makrá a príkazy </font>

Inštrukcia (*statement*) je jeden alebo viacej príkazov končiacich znakom bodkočiarky *;* alebo znakom konca riadku. Je vhodné implicitne používať znak konca riadku vždy, pri prípadnom dopĺňaní príkazu sa týmto obmedzí vznik chýb. V `CircuitMacros` je program tvorený inštrukciami ktoré sú makrami ako aj samotnými príkazmi jazyka `dpic`.

```
line from (1,1) to (2,2)           # inšrukcia jazyka dpic
resistor(,,E);                     # makro inštrukcia končí znakom ;
capacitor()                        # makro inštrukcia končí \n
resistor() rlabel(,R2,)            # chyba, neoddelene inštrukcie
line to Here + (2,0); resistor()   # dpic a makro inšrukcia 
```

```{admonition} Konflikt mien 

Používanie makrier spoločne s interpreterom môže byť niekedy zdrojom chýb. Problémom môže byť hlavne to, že o chybe spôsobenej nesprávnym použitím makie sa dozvieme až pri interpretácii kódu s expandovanými makrami, pričom sa zvyčajne nedozvieme, z ktorého makra a na ktorom riadku zdrojového kódu k chybe došlo.   

* Niektoré makrá definujú premenné a konštanty, ktoré môžu byť príčinou konfliktov. Napríklad makro *setrgb()* používa premenné *r_* , *g_*, *b_*, kde prvá premenná vytvorí konflikt s menom, ak potrebujeme napríklad označiť rezistor pomocou syntaxe v LaTex-u napr. *r_1*. V takomto prípade je potrebné v reťazci pre LaTeX použiť formálne prerušenie reťazca *r\\_1*.

* Nie je možné priamo v zobrazovanom texte použiť mená makrier, napríklad *"toto je resistor R1"*, pretože pri substitúcii dôjde k nahradeniu textu *resistor*  kódom definovanom v makre a následnej chybe pri interpretácii zdrojového kódu. Text musíme upraviť podobne ako v predchádzajúcom prípade. 

```

### <font color='brown'> Objekty a referencie </font>

Každý príkazom zobrazovaný objekt  v *dpic* môže byť označený referenciou, prostredníctvom ktorej je možné odkazovať sa na jej atribúty (ak sú definované). Referencie musí začínať veľkým písmenom nasledovaným ľubovolným počtom alfanumerických znakov. 

Formát

    [ Reference :] object [ attributes ] [ placement ] [ strings ]

Príklad použitia referencií

```
L1: line from Here to Here + (2,2);
R1: resistor();
```

Referenciou je možné označiť aj súradnice.
    
```Python
Stred: (5,6);
```    

Pomocou referencií je možné pristupovať k individuálnym atribútom komponentov, napr:

```Python
Stred.x  # má hodnotu 5
Stred.y  # má hodnotu 6
```

Referencie sú globálne, referencia definovaná v bloku je viditeľná v celom programe. Nové priradenie mena referencie inému objektu pôvodnú referenciu prepíše.


### <font color='brown'> Zložené objekty </font>

Uzatvorené v zátvorkách *[  .. ]*


### <font color='brown'>  Bloky  </font>

Premenné uzatvorené v bloku {...} majú lokálnu platnosť, v nich vytvorené  majú platnosť globálnu. Kód v bloku sa vzťahuje k poslednej aktuálnej polohe a nemení ju, je preto výhodné používať bloky na kreslenie vetiev obvodov vzľadom k referenčnej polohe.  

```
d = 2;
{
    d = 0.4;
    Q: (1,1);          # globálná definícia polohy
    ...
}
line from Q right_ d   # d má hodnotu 2
```

## <font color='teal'> Riadenie toku  </font>

Jazyk *dpic* obsahuje základnú konštrukciu pre cuklus a podmienkové vetvenie toku programu. 

### <font color='brown'>  Cyklus  </font>

Formát cyklu

    for variable = expr to expr [by [*] incr ] do { anything }.

Jednoduchý cyklus s premennou $x$ má tvar

    for x = 1 to 10 by 2 do { line from (0,0) to (5,x); }
    
kde v zložených zátvorkách je telo cyklu, toto má vlastnosti bloku s relatívnymi súradnicami vztiahnutými k začiatku cyklu. Pri opakovanom prechode telom cyklu sa hodnota kurzoru `Here` zachováva, čo je zrejmé zo zjednodušeného kódu 

    ...
    for q=0 to 2*pi by 0.1 do{
        x = r*cos(a*q);
        y = r*cos(b*q);
        line to (x,y);        <-- line from Here to (x,y); Here <- (x,y)
    }
    ...


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
boxrad = .1;

include(lib_base.ckt)
include(lib_color.ckt)

define(`mv_liss', `x = r*cos(0)+x0; y=r*sin($3)+y0; move to (x,y);' );
define(`ln_liss', `x = r*cos($1*q)+x0; y=r*sin($2*q + $3)+y0; line to (x,y);' );

r = 1.5;

x0 = 2; y0 = 2; phi = pi/4; a=1; b=2;
rgbfill(fill_light_grey, {box at (x0,y0) wid 4 ht 4} );
sprintf("$a=%2.0f \,\,\, b=%2.0f \,\,\, \phi$=%2.2f", a,b, phi) at last box .n above;
color_red;
mv_liss(a,b,phi)
for q=0 to 4*pi by 0.05 do{
  ln_liss(a,b,phi);
}
color_reset;

x0 = 7; y0 = 2; phi = pi/2; a=5; b=3;
rgbfill(fill_light_grey, {box at (x0,y0) wid 4 ht 4} );
sprintf("$a=%2.0f \,\,\, b=%2.0f \,\,\, \phi$=%2.2f", a,b, phi) at last box .n above;
color_blue; 
mv_liss(a,b,phi)
for q=0 to 2*pi by 0.05 do{
  ln_liss(a,b,phi);
}
color_reset;

x0 = 2; y0 = 7; phi = pi/3; a=2; b=3;
rgbfill(fill_light_grey, {box at (x0,y0) wid 4 ht 4} );
sprintf("$a=%2.0f \,\,\, b=%2.0f \,\,\, \phi$=%2.2f", a,b, phi) at last box .n above;
color_dark_green; 
mv_liss(a,b,phi)
for q=0 to 4*pi by 0.05 do{
  ln_liss(a,b,phi);
}
color_reset;

x0 = 7; y0 = 7; phi = 0; a=5; b=7;
rgbfill(fill_light_grey, {box at (x0,y0) wid 4 ht 4} );
sprintf("$a=%2.0f \,\,\, b=%2.0f \,\,\, \phi$=%2.2f", a,b, phi) at last box .n above;
color_red;
mv_liss(a,b,phi)
for q=0 to 4*pi by 0.01 do{
  ln_liss(a,b,phi);
}
'''

_ = cm_compile('cm_0160b', data, dpi=600)   
```


```{figure} ./src/cm_0160b.png
:width: 500px
:name: cm_0160b

[Príklad](./src/cm_0160b.ckt) použitia cyklu.
```


### <font color='brown'> Vetvenie  </font>

Formát vetvenia 

    if expression then { if-true } else { if-false }
