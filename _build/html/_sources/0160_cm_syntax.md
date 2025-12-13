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

Programovací jazyk `dpic` bol špeciálne vytvorený na kreslenie grafov a diagramov s možnosťou ich exportu ako obrázkov alebo vkladania do textových dokumentov. Obsahuje príkazy pre kreslenie lineárnych objektov ako čiara, šipka, krivka, ako aj plošné objekty ako pravouholník, kružnica, elipsa, oblúk a umožňuje vytváranie zložených objektov. Zložitejšie grafických objekty ktoré sa v obrázkoch vyskytujú častejšie, ako sú značky elektronických súčiastok, je možné v `dpic` kresliť pomocou makier, ktoré obsahujú kód pre nakreslenie objektu. `CircuitMacros` je rozšírením `dpic` o knižnice makier pre kreslenie elektronických obvodov a zapojení. Podrobný popis syntaxe jazyka `dpic` je v [dokumentácii](./data/dpic-doc.pdf). 


```{admonition} Programovací jazyk *dpic*
Programovací jazyk `dpic` historicky vychádza z jazyka [pic](./data/pic.pdf) vytvoreného Brian W. Kernighan-om v roku 1991.  Z programátorského hľadiska `dpic` patrí do skupiny tzv. *mini-jazykov*, ([DSL](https://en.wikipedia.org/wiki/Domain-specific_language)) ktoré sú vytvorené pre nejaký konkrétny učel na rozdiel od *všeobecne použiteľných jazykov* ([GPL](https://en.wikipedia.org/wiki/General-purpose_language)). Syntax jazyka `dpic` je veľmi jednoduchá, okrem príkazov na kreslenie grafických objektov má aj základné jazykové konštrukcie na riadenie toku programu ako je podmienkové vetvenie a cyklus. Nie je v ňom možné ale vytvárať funkcie, ktorú sú formálne nahradené makrami. Makrá obsahujú kód pre kreslenie zložitejších objektov a pri ich použití kompilátor nahradí v programe meno makra týmto kódom. 
```


## <font color='teal'> Program </font>

Program je tvorený textovým súborom, ktorý začína znakmi **.PS** a končí znakmi **.PE**. Príkaz na riadku je ukončený bodkočiarkou `;` alebo ukončenim riadku (neviditeľný znak `\n`). Bodkočiarka na ukončenie príkazu nie je povinná, na rozdiel napr. od jazyka `C`, ale  využijeme  ju vtedy, ak budeme do jedného riadku zadávať niekoľko príkazov. 

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


    # toto je jednoriadkovy komentar
    # toto je dvojriadkovy komentar        \\
      a jeho pokracovanie na dalsom riadku

```{warning} 
White-space (tabulátory, medzery, znak nového riadku) sú vo v argumentoch makier ignorované **pred** argumentom, nie ale **za** argumentom. 

    name( x,
    y, z )
        
    je ekvivalent

    name(x,y,z )
```
        
### <font color='brown'> Hodnoty </font>

Jazyk *dpic* pozná len **numerické** hodnoty ktoré môžu byť zapísané v desatinnom tvare alebo môžu byť vo vedeckom formáte. Všetky numerické hodnoty sú interne uchovávané vo formáte *floating-point*. Všetky grafické prvky ako aj texty sú pokladané za objekty na ploche a sú reprezentované súradnicami polohy ich geometrického stredu. 

### <font color='brown'> Premenné </font>

Meno premennej  musí začínať písmenom nasledovaným ľubovolným počtom alfanumerických znakov. Premenné sa vytvoria pri ich definícii, musia byť inicializované **numerickou** hodnotou a sú globálne t.j. majú platnosť v celom zdrojovom kóde. 


    d  = 2;
    pi = 3.14159265359;
    q  = 2*pi*8;

Pre premenné sú definované numerické a logické operácie

    binárne aritmetické oprácie
    +   -   *   /   %   ^
    
    unárne aritmetické operácie
    +=   -=   *=   /=   %=
    
    relačné operácie 
    !=   ==   <   >   >=   <=   ||   &&
    
    
### <font color='brown'> Súradnice </font>
    
Súradnice bodov sú reprezentované ako dvojice (x,y) a **nemôžu** byť použité ako hodnoty premennej, môžu ale byť reprezentované referenciou. Špeciálny význam má pomenovaná súadnica `Here`, ktorá obsahuje súradnice posledného vykresleného bodu. Súradnice majú preddefinované atribúty *.x*, *.y*, ktoré reprezentujú numerické hodnoty zložiek polohy. Pre prácu so súradnicami sú definované vektorové operácie.

#### <font color='purple'> Vytvorenie súradnice </font>

Novú súradnicu je možné vytvárať z numerických hodnôt ako aj pomocou iných súradníc.

    P1: (3,4);      # vytvorenie súradnice bodu
    p1 = (3,4);     # chyba   
    
    
    a = 1; b = 2;   # konverzia numerických hodnôt na súradnice 
    P2: (a, b);
    P3: (a, 0);     # bod na osi x
    
                    # prístup k zložkám súradnice
    px = P1.x       # numerická hodnota x-ovej súradnice
    py = P1.y       # numerická hodnota y-ovej súradnice
    nx = Here.x     # hodnoty aktuálnej pozície
    ny = Here.y
    
    P4: (P1, P2)    # ekvivalent (P1.x, P2.y)
    P5: P4          # nová súradnica 
    P5: P1          # redefinícia súradnice
    
    
```{admonition} Poznámka
Je možné používať súradnice zapísané aj bez zátvoriek v tvare *x*, *y*, ale z dôvodu možných konfliktov pri expanzii makier je vhodnejší prehľadnejší zápis so zátvorkami *(x, y)*.

    line to 1,1
    line to (1,1);
```
   
#### <font color='purple'> Vektorové operácie </font>

Výsledkom vektorovej operácie nad súradnicami je zase súradnica. Pre násobenie a delenie je platná len post-multiplikacia.
    
    S1: (a,b) + (c,d)      # súčet   
    S2: P1 + P2
    S3: P1 + (c,d)
    S4: Here + (dx,dy)     # offset k aktuálnej polohe
    
    D1: (a,b) - (c,d)      # rozdiel 
    D2: P1 - P2
    D3: P1 - (c,d)
    
    M1: (a,b)*k            # násobenie, k - numerická hodnota alebo premenná
    M2: P1*k
    M3: k*P1               # chyba
    
    Q1: (a,b)/k            # delenie       
    Q2: P1/k


#### <font color='purple'> Poloha medzi dvoma bodmi </font>

Pri kreslení zapojení často potrebujeme určiť polohu medzi dvoma bodmi, v *dpic* môžeme použiť konštrukciu *between*

    PB: k between P1 and P2  
    
Hodnota *k* určuje relatívnu vzdialenosť ku koncovým bodom, *k=0.5* je stredom, *k=0* a *k=1* sú polohy koncových bodov. Pri hodnote *k* mimo intervalu *0...1* leží za krajnými bodmi *P1* a *P2*.

```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

Grid(7,3.5)
P1: (1, 0.5)
P2: (5,2)
D1: dot(at P1) "\small \sf P1" above;
D2: dot(at P2) "\small \sf P2" above;
line from P1 to P2
color_red;
X1: 0.5 between P1 and P2; dot(at X1) "\small \sf 0.5 between P1 and P2" ljust below
color_blue;
X2: 0.75 between P1 and P2; dot(at X2) "\small \sf 0.75 between P1 and P2" rjust above
color_dark_cyan;
X3: 1.35 between P1 and P2; dot(at X3) "\small \sf 1.35 between P1 and P2" rjust above
'''

_ = cm_compile('cm_0160k', data,  dpi=600)   
```

```{figure} ./src/cm_0160k.png
:width: 450px
:name: cm_0160k

Použitie konštrukcie *between*.
```


    
### <font color='brown'> Textové reťazce </font>
    
Text je postupnosť znakov definované v obyčajných úvodzovkách a **nemôže** byť použitý ako hodnota premennej. Súradnice geometrického stredu zobrazeného textu ale môže byť reprezentovaná referenciou.  


    str = "Toto je text"          # chyba   
    T1: "Toto je text" at (1,1);  # ok, stred textu je v bode (1,1)
    

### <font color='brown'> Inštrukcie </font>

Inštrukcia je jeden alebo viacej príkazov jazyka *dpic* končiacich znakom bodkočiarky *;* alebo znakom konca riadku. Je vhodné implicitne používať znak konca riadku vždy, pri prípadnom dopĺňaní príkazu sa týmto obmedzí vznik chýb. Pretože v jazyku *dpic* nie je možné vytvárať funkcie a podprogramy, sú skupiny príkazov zoskupené do makier pomocou ktorých sa vykreslujú zložitejšie objekty. V `CircuitMacros` je program tvorený inštrukciami ktoré sú makrami ako aj samotnými príkazmi jazyka `dpic`. Formát inštrukcie v má tvar

    [referencia:] objekt [ atributy] [ umiestnenie ] [ text ]

Príklady

    line from (1,1) to (2,2)           # inštrukcia jazyka dpic
    resistor(,,E);                     # makro inštrukcia končí znakom ;
    capacitor()                        # makro inštrukcia končí \n
    resistor() rlabel(,R2,)            # chyba, neoddelene inštrukcie
    line to Here + (2,0); resistor()   # dpic a makro inšrukcia 


### <font color='brown'> Referencie </font>

Každý zobrazený objekt v môže byť označený referenciou, ktorá reprezentuje polohu jeho geometrického stredu. Pomocou referncie je možné odkazovať sa aj na atribúty objektu. Referencie musí začínať veľkým písmenom nasledovaným ľubovolným počtom alfanumerických znakov. 


        L1: line from Here to Here + (2,2);
        R1: resistor();
         S: (5,6);
         
        P1: R1.start     # suradnica
        P2: L1.end
        
        px = R1.end.x    # numericka hodnota


Referencie sú globálne, referencia definovaná v bloku alebo vetve je viditeľná v celom programe. Nové priradenie mena referencie inému objektu pôvodnú referenciu prepíše. Pri kreslení zapojení sa stáva, že musíme presne spojiť dva body zapojenia, ktorých absolútnu polohu nepoznáme. Využitím vektorvých operácií s referenciami na objekty získame spojenie, ktoré sa nepreruší ani pri dodatočnej uprave polohy objektov.

```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

    line 0.5 dotted;
LL: line right_ 2;
    dot;
    # {"\textsf{ast line}" at last line.c above;}
    line <- from LL.end + (.1,.1) up_ .5 right_ .5 dotted;
    "\textsf{Here}" at last line.end ljust above;
    
    move to LL.end+(0.8,-1.5);
    dot;
R4: resistor(right_ 2 ,,E);
    llabel(,R4,);
    line 0.5 dotted;
    line <- from R4.start - (.1,.1)   down_ .5 left_ .5 dotted;
    "\textsf{R\\4.start}" at last line.end rjust below;

move to LL.end;
linethick = 1.5;
color_red;
line from Here down_ (Here.y - R4.start.y) \
     then to R4.start;

"\textsf{line from Here down\_ (Here.y - R4.start.y)}" at (LL+R4)/2 + (-0.5,0.1) rjust;
"\textsf{then to R4.start;}" at (LL+R4)/2 + (-0.5,-0.1) rjust below;
'''

_ = cm_compile('cm_0160c', data,  dpi=600)   
```

```{figure} ./src/cm_0160c.png
:width: 500px
:name: cm_0160c

[Použitie](./src/cm_0160c.ckt) referencií pre výpočtu koncového bodu čiary.
```


### <font color='brown'>  Vetvy  </font>

Vetva je tvorená kódom uzatvoreným do zložených zátvoriek `{...}`. Vetva umožňuje vytváranie časti obvodu alebo umiestnenie iných komponentov relatívne k poslednej hodnote `Here`, vo vetve sa vytvorí lokálna kópia `Here`. S výhodou ich použijeme v prípade, keď potrebujeme nakresliť samostatnú časť obvodu (vetvu) a potom pokračovať v kreslení zapojenia od pôvodnej pozície.

Uzatvorenie kódu do vetvy `{...}` neovplyvňuje viditeľnosť premenných. Vetvy je možné do seba vnárať.  

```{code-block}
d=3;
R1: resistor(right_ d,);        # d -> 3
DT: dot;
   {      d = 2;                # Here -> DT
      R2: resistor(down_ d,);   # Here -> R2.end
          ground(at Here, T);   
          d=1.5;
   }

   {  R3: resistor(up_ d,);     # d -> 1.5   Here -> R3.end
          tconn(0.5,O);         
          d=2.5;
   }
                                # Here -> DT
R4: resistor(right_ d);         # d -> 2.5   Here -> R4.end
```


```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

d=3;
resistor(right_ d,); llabel(,R1,); dot;
{ 
  color_red;
  d = 2;
  resistor(down_ d,);llabel(,R2,);
  ground(at Here, T);
  d=1.5;
}

{ 
  color_blue;
  resistor(up_ d,);llabel(,R3,);
  tconn(0.5,O);
  d=2.5
}

color_black;
resistor(right_ d); llabel(,R4,);
'''

_ = cm_compile('cm_0160f', data, dpi=600)   
```

```{figure} ./src/cm_0160f.png
:width: 300px
:name: cm_160f

Použitie vetiev na kreslenie častí obvodu.
```

Vetvy s výhodou využijeme pri popise prvkov zapojenie. Zobrazenie textu mení rovnako ako každý nový element zapojenia hodnotu `Here`, ak chceme v kreslení pokračovať s pôvodnou súradnicou, uzatvoríme text do vetvy. Príkazy pre popis dvojpólov (*llabel ...*) hodnotu `Here` nemenia.

    line -> 1;
    box wid 2 ht 1;     
    {
        "top of box" at last box.n above; 
        "bottom of box" at last box.s below;
        line from last box.nw to last box.se; 
        line from last box.sw to last box.ne; 
    }
    line -> 1;     
    box wid 2 ht 1; 
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
Origin: Here 
line -> 1;
box wid 2 ht 1; 
{
    "top of box" at last box.n above; 
    "bottom of box" at last box.s below;
    line from last box.nw to last box.se; 
    line from last box.sw to last box.ne; 
}
line -> 1;
box wid 2 ht 1; 
'''

_ = cm_compile('cm_0160e', data, dpi=600)   
```

```{figure} ./src/cm_0160e.png
:width: 400px
:name: cm_0160e

[Lokálne](./src/cm_0160e.ckt) súradnice vo vetve.
```




### <font color='brown'> Bloky a zložené objekty</font>

Časť kódu uzatvorená v hranatých zátvorkách `[...]` predstavuje blok alebo zložený objekt. Program v bloku má vlastnú absolútnu súradnicovú sústavu a po vytvorení má vlastnosti plošného objektu. Premenné v bloku sú rovnako ako vo vetve lokálne, vnútorné referencie vytvorené v bloku sú prístupné pomocou referencie na celý blok.

       w=2;
       move to (1,1.5);                  # poloha zloženého objektu
    A:[                                  # blok s absolutnymi suradnicami  
         rr=0.25;                        # inicializácia vnútorných premenných 
         h=w/2; w=w+1/2;                 # použitie vonkajšej premennej  
     B:  box at (0,0) wid w ht h; 
     C1: circle at (0, 0.5) rad rr; 
     C2: circle at (0,-0.5) rad rr;
     C3: circle at B.w rad  rr;
     C4: circle at B.e rad rr;
    ] 

Pre zložený objeky sú automaticky vypočítané vonkajšie rozmery a sú mu priradené štandardné atribúty 

    .s   .n   .w   .e   .c
    .sw  .se  .nw  .ne
    .wid_     .ht_
    
Pre ukladanie a použitie zloženého objektu na ploche platia rovnaké pravidlá ako pre každý iný plošný objekt.

    r = A.rr;                            # chyba, premenná rr nie je viditeľná
    r = A.C1.rad                         # použitie vnútorných referncií
    line <- from A.B.nw left_ 1 up_ 1; 
    line <- from A.ne right_ 1 up_ 1;    # použitie vonkajších referencií a atribútov
    right_; box at A.c wid A.wid_ ht A.ht_ dashed;

    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)
Grid(5,3);

    w=2;
    move to (1,1.5);                  # poloha zloženého objektu
A:[                                # blok s absolutnymi suradnicami  
        rr=0.25;                      # vnutorne premenne
        h=w/2; w=w+1/2;
    B:  box at (0,0) wid w ht h; 
    C1: circle at (0, 0.5) rad rr; 
    C2: circle at (0,-0.5) rad rr;
    C3: circle at B.w rad  rr;
    C4: circle at B.e rad rr;
] 

color_red;
r = A.C1.rad
line <- from A.B.nw left_ 1 up_ 1; "\sf A.B.nw" above;
line <- from A.ne right_ 1 up_ 1; "\sf A.ne" above;

right_; box at A.c wid A.wid_   ht A.ht_ dashed;
'''

_ = cm_compile('cm_0160d', data, dpi=600)   
```

```{figure} ./src/cm_0160d.png
:width: 350px
:name: cm_0160d

Blok reprezentujúci zložený objekt a jeho vonkajší obrys.
```


       
## <font color='teal'> Riadenie toku  </font>

Jazyk *dpic* obsahuje základnú konštrukciu pre cuklus a podmienkové vetvenie toku programu. 

### <font color='brown'>  Cyklus  </font>

Formát príkazu pre cyklu

    for variable = expr to expr [by [*] incr ] do { anything }.

Jednoduchý cyklus s premennou $x$ má tvar

    for x = 0 to 200  do { line from (rand(), rand())*5 to (rand(),rand())*5; }

kde v zložených zátvorkách je telo cyklu, toto má vlastnosti bloku s relatívnymi súradnicami vztiahnutými k začiatku cyklu. Cykly sa môžu vnárať, počet vnorených cyklov nie je obmedzený. Pri opakovanom prechode telom cyklu sa hodnota kurzoru `Here` zachováva, čo je zrejmé zo zjednodušeného zápisu kódu 

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
