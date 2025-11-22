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
# <font color='navy'> Makrá  </font>

Prostredie `CircuitMacros` je rozšírením programovacieho jazyka `dpic` určeného pre kreslenie diagramov a grafov (staršia verzia je označovaná ako `gpic`) pomocou súboru **makier** pre makroprocesor **m4**. Makrá môžeme považovať za malé programy alebo skripty, ktorými sú nahradzované ich mená pri ich použití v hlavnom programe. Pomocou rozšírenia jazyka `dpic` makrami je možné vytvárať elektrické zapojenia a schémy, zároveň je možné v nich používať aj grafické prvky jazyka `dpic`.

```{admonition} Makroprocesor m4

Makroprocesor je univerzálny program pre spracovanie makier široko využívaný v programátorskej praxi najmä pri jazykoch nižšej úrovne a assembleroch. Makrá nachádzajú uplatnenie v rôznych implementáciách aj v textových a tabulkových procesoroch. Makroprocesor kopíruje vstupný text zo vstupu na výstup a popritom prí nájdení mena vopred definovaného makra

* nahrádza meno makra textom z definície makra
* nahrádza parametre makra ich hodnotami
* vkladá súbory
* prevádza manipulácie s textovými reťazcami
* vyhodnocuje podmienky
* vyhodnocuje aritmetické výrazy

Referenčnou implementáciou makroprocesora **m4** je [GNU M4](https://www.gnu.org/software/m4/manual/m4.html). 
```

Makrá definované v knižniciach `CircuitMacros` expandujú značky elektronických prvkov do množiny príkazov jazyka `dpic`, z vytvoreného programu je pomocou interpreteru príkazov vygenerovaný výsledný obrázok vo zvolenom rastrovom alebo vektorovom formáte. 

```{code-cell} ipython3 
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
command "\sf"
include(lib_base.ckt)
include(lib_color.ckt)

Origin: Here 

shadebox(B1: box wid 2 ht 1 with .w at (1,3), 2) 
"Program" at B1.c above; 
"*.ckt" at B1.c below; 
line -> from B1.e right_ 1 then down_ 0.5 then right_ 1;

shadebox(B2: box wid 2 ht 1 with .w at (1,1.5), 2) 
"Knižnice" at B2.c above; 
"*.m4" at B2.c below; 
line -> from B2.e right_ 1 then up_ 0.5 then right_ 1;

color_red;
boxrad=.1;
B3: box wid 2 ht 1.5 with .nw at (5,3)
"Makro" at B3.c above; 
"procesor" at B3.c below; 
color_black;

line -> from B3.e right_ 1;

color_blue;
boxrad=.1;
B4: box wid 2 ht 1.5 
"dpic" at B4.c above; 
"Interpreter" at B4.c below; 
color_black;

line from B4.e right_ 1;
D1: dot;
line -> up_ 2.25 then right_ 1; 
shadebox(B5: box wid 2 ht 1, 2); 
"Image" at B5.c above; 
"*.png" at B5.c below;

line -> from D1 up_ 0.75 then right_ 1; 
shadebox(B6: box wid 2 ht 1, 2); 
"Image" at B6.c above; 
"*.jpeg" at B6.c below;

line -> from D1 down_ 0.75 then right_ 1; 
shadebox(B7: box wid 2 ht 1, 2); 
"Image" at B7.c above; 
"*.svg" at B7.c below;

line -> from D1 down_ 2.25 then right_ 1; 
shadebox(B7: box wid 2 ht 1, 2); 
"Makro" at B7.c above; 
"*.tikz" at B7.c below;

color_dark_orange;
line <- from B1.n up_ 0.5;
B8: box wid 2  ht 1
"Editor" at B8.c above; 
"pycirkuit" at B8.c below;
'''

_ = cm_compile('./src/cm_0165a', data, dpi=600)   
```

```{figure} ./src/cm_0165a.png
:width: 650px
:name: cm_0165a

Postup generovania obrázkov.
```



```{warning}

Kódy makier sú v podstate pomenované textové reťazce, ktorými nahrádza makrorocesor pred samotným spracovaním zdrojového kódu  **všetky** časti zdrojového kódu zhodné s menom makra. Táto substitúcia je čisto mechanická, bez ohľadu na kontext v ktorom sa text zhodný s menom makra vyskytuje. Toto môže spôsobiť pri interpretácii kódu chybu, ktorá je spôsobená substitúciou makra na nevhodnom mieste a to aj napriek tomu, že kód programu je formálne syntakticky správny.

    R1: resistor;
    "terminal resistor" at R1.c above;   # chyba, substitucia v texte

Pre odstránenie tejto chyby je potrebné vhodným spôsobom pozmeniť text tak, aby makroprocesor text nenahrádzal, napríklad

    "terminal res\\istor" at R1.c above; # dve lomítka \\ sú pri zobrazení ignorované 
    
```

## <font color='teal'> Použitie makier  </font>

Makrá sa definujú podľa syntaxe makroprocesora **m4**. Všeobecný tvar makra je

    define (name, [expansion])
    
Reťazec *name* je nahradený reťazcom *expansion*, typ úvodzoviek v makre je dôležitý. Príklad

    define(`foo', `Hello world.')

po spracovaní dostaneme

    foo
    Hello world.
    
```{admonition} Poznámka

Substitučné reťazce v makrách `m4` začínajú znakom spätného apostrofu `chr(96)` a končia znakom apostrofu `chr(39)`. Textové reťazce v jazyku `dpic` začínajú a končia úvodzovkami `"`.
```

Makro môže mať argumenty, tieto sú označované ako \$1, \$2 ... , špeciálny význam má argument označený ako \$0, ktorý obsahuje meno makra. Príklad makra, ktoré vymení poradie argumentov

    define(`exch', `$2, $1')
  
po spracovaní dostaneme

    exch(`arg1', `arg2')
    arg2, arg1

    
Nasledujúci príklad ukazuje použitie makier.

    # definicia makier 
    #--------------------------------------------
    define(`text', `klukata ciara');
    define(`zigzac', `[line up_ $1 right_ $1 then down_ $1 right_ $1 then up_ $1 right_ $1]' )

    # pouzitie
    #--------------------------------------------
        move to (0.5,0.5); dot;
    ZG: zigzac(0.5); zigzac(1);
        "text" at ZG.n above;

Makro **text** je jednoducha nahrada reťazca. Makro **zigzac** má jeden parameter a pri jeho použití je jeho meno nahradené príkazom, argument je nahradený jeho hodnotou. Uzatvorenie príkazov do hranatých zátvoriek [...] znamená, že obsah príkazov v zátvorkách bude pokladaný za jeden zložený objekt. 
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
include(lib_base.ckt)

Origin: Here 

Grid(6,1.5)

define(`text', `klukata ciara');
define(`zigzac', `[line up_ $1 right_ $1 then down_ $1 right_ $1 then up_ $1 right_ $1]' )

move to (0.5,0.5);
dot;
ZG: zigzac(0.5); zigzac(1);
"text" at ZG.n above;
'''

_ = cm_compile('./src/cm_0165b', data, dpi=600)   
```

```{figure} ./src/cm_0165b.png
:width: 400px
:name: cm_0165b

[Príklad](./src/cm_0165b.ckt) použitia makier
```
    
## <font color='teal'> Vytvorenie makra  </font>

Pri tvorbe  makier pre kreslenie vlastných prvkov zapojenia môžeme využiť nasledujúci vzor, v ktorom sú v makre vyhodnotené dva parametre
 
    #----------------------------------------------
    # vzor(n, c) - template pre makro
    # n - numericky parameter
    # c - znakovy parameter L|R|U|P
    #----------------------------------------------
    define(`vzor',`[
        # kontrola existencie numerickeho parametra
        # pri chybajucom parametri nahradenie default hodnotou
        
        ifelse(defn(`par1'),  $1, par1=1,  par1=$1)    

        # vyber indexu 0...3 z preddefinovanej množiny parametrov L R U P 
        # pri neexistujucej ma index hodnotu -1
        
        par2 = index(`LRUD', $3)

        # vyhodnotenie pre hodnoty parametra podla hodnoty indexu
        if <= 0 then  { line -> left_  par1; } 
        if == 1 then  { line -> right_ par1; }
        if == 2 then  { line -> up_    par1; } 
        if == 3 then  { line -> down_  par1; } 
    ]')

Makro *defn()* v predlohe vytvorí premennú *par1* a skontroluje existenciu  argumentu \$1, ak tento neexistuje, *ifelse* priradí *par1=1*, ak existuje, tak potom jej priradí hodnotu *par1=\$1*. Premenná *par2* je inicializovaná hodnotou indexu z poľa dovolených parametrov. Makro pri použití pokrýva nasledujúce prípady
    
    vzor;        -> vzor(1,L)
    vzor();      -> vzor(1,L)
    vzor(2);     -> vzor(2,L)
    vzor(3,R);   -> vzor(3,R)
    vzor(,X);    -> vzor(1,L)
    vzor(,);     -> vzor(1,L)     


Nižšie je uvedené makro pre zobrazenie spínača s parametrami dĺžka spínača a 'stav (ON, OFF) spínača. Aby bol komponent presne umiestnený v mriežke bez ohľadu na jeho aktuálne grafické zobrazenie, je vhodné ho umiestniť do neviditeľného boxu s fixnými rozmermi. Pre vonkajší box potom platia štandardné atribúty *w,e,s,n,nw ...*.  



### <font color='brown'> Implementácie makra </font>

Nasledujúci príklad implementuje zobrazenie spínača s dvoma parametrami - dĺžka spínača a stavu zopnutia (ON, OFF) spínača. Aby bol komponent presne umiestnený v mriežke bez ohľadu na jeho aktuálne grafické zobrazenie, je vhodné ho umiestniť do neviditeľného boxu s fixnými rozmermi. Pre vonkajší box potom platia štandardné atribúty *w,e,s,n,nw ...*.  

Pre ilustráciu je zobrazený vonkajší box, ktorý umožňuje ukladanie komponentu v rastri, parameter *invis* spôsobi skrytie obrysu.

    # horizontal switch
    # usage:
    #     swh(length, ON | OFF );
    define(`swh',`[

        B:  box ht 1 wid $1 dotted 0.04 #invis;   # vonkajsi okraj pola 1. parametra
            rr = 0.15;
            p = 1.5; 
        
        C1: circle diameter rr at  B.c + (rr/2 - p/4, 0)
        C2: circle diameter rr at  B.c + (-rr/2 + p/4, 0) fill 0;
            line from C1.w to B.w
            line from C2.e to B.e
            ifinstr($2,OFF,                        # kontrola hodnoty 2. parametra
                {   # stav OFF
                    line from C2.c to C1.c + (0, p/4)
                },
                {   # stav ON
                    line from C2.c to C1.c 
                }
            );
    ]')

Vytvorené makro požívame ako akýkoľvek iný príkaz pre kreslenie prvkov zapojenia. Príklad použitia implmentovaného spínača je v nasledujúcom kóde, pre názornosť je ponechané zobrazenie vonkajšieho obrysu prvku. 

    move to (0.5, 2); right_; 
    swh(1, OFF);
    line 0.5;
    swh(1, ON);
    line 0.5;
    swh(2, OFF);
    dot;
    { line up_   1; right_; S1: swh(2,  ON); "$S_1$" at S1.n; }
    { line down_ 1; right_; S2: swh(2, OFF); "$S_2$" at S2.n; }



```{code-cell} ipython3 
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
include(lib_base.ckt)

# horizontal switch
# usage:
#     swh(length, ON | OFF );
define(`swh',`[

    B: box ht 1 wid $1 dashed 0.04 #invis;  # vonkajsi okraj
    rr = 0.15;
    p = 1.5; 
    
    C1: circle diameter rr at  B.c + (rr/2 - p/4, 0)
    C2: circle diameter rr at  B.c + (-rr/2 + p/4, 0) fill 0;
    line from C1.w to B.w
    line from C2.e to B.e
    ifinstr($2,OFF,
            {   
                line from C2.c to C1.c + (0, p/4)
            },
            {
                line from C2.c to C1.c 
            }
        );
]')


Origin: Here 
Grid(9,4);

move to (0.5, 2); right_; 
swh(1, OFF);
line 0.5;
swh(1, ON);
line 0.5;
swh(2, OFF);
dot;
{ line up_   1; right_; S1: swh(2,  ON); "$S_1$" at S1.n; }
{ line down_ 1; right_; S2: swh(2, OFF); "$S_2$" at S2.n; }
'''

_ = cm_compile('./src/cm_0165c', data, dpi=600)   
```

```{figure} ./src/cm_0165c.png
:width: 450px
:name: cm_0165c

[Implementácia](./src/cm_0165c.ckt) makra pre zobrazenie spínača a jeho použitie
```

## <font color='teal'> Modifikácia makra </font>

V niektorých prípadoch nepotrebujeme vytvárať nové makro, ale len rozšíriť existujúce makro o ďalši popis alebo grafiku. V niektoých zapojeniach napríklad je značka rezistora doplnená o označenie jeho výkonovej straty, ktorá môže súvisieť s jeho typom púzdra.

    define(`res_025w', `[
        R: resistor($1,$2,$3);
        dx = 0.065*linewid;
        line from R.c+(dx,-dx) to R.c+(-dx,dx);
    ]')
    

```{code-cell} ipython3 
:tags: ["remove-cell"]

from cm.utils import *

data = r'''
include(lib_base.ckt)

define(`res_05w', `[
    R: resistor($1,$2,$3);
       dx = 0.18*linewid;
       line from R.c+(-dx,0) to R.c+(dx,0);
]')


define(`res_025w', `[
    R: resistor($1,$2,$3);
       dx = 0.065*linewid;
       line from R.c+(dx,-dx) to R.c+(-dx,dx);
]')

define(`res_0125w', `[
    R: resistor($1,$2,$3);
       dx = 0.065*linewid;
       ds = 0.06
       line from R.c+(dx + ds,-dx) to R.c+(-dx + ds,dx);
       line from R.c+(dx - ds,-dx) to R.c+(-dx - ds,dx);
]')

define(`res_005w', `[
    R: resistor($1,$2,$3);
       dx = 0.065*linewid;
       ds = 0.1
       line from R.c+(dx + ds,-dx) to R.c+(-dx + ds,dx);
       line from R.c+(dx,-dx) to R.c+(-dx,dx);
       line from R.c+(dx - ds,-dx) to R.c+(-dx - ds,dx);
]')

define(`res_1w', `[
    R: resistor($1,$2,$3);
       dx = 0.065*linewid;
       line from R.c+(0, dx) to R.c+(0,-dx);
]')

define(`res_2w', `[
    R: resistor($1,$2,$3);
       dx = 0.065*linewid;
       ds = 0.05
       line from R.c+( ds,-dx) to R.c+(  ds,dx);
       line from R.c+(-ds,-dx) to R.c+( -ds,dx);
]')

define(`res_5w', `[
    R: resistor($1,$2,$3);
       dx = 0.065*linewid;
       ds = 0.05
       line from R.c+( 0,-dx) to R.c+(  ds,dx);
       line from R.c+(-ds, dx) to R.c+( 0, -dx);
]')

include(lib_base.ckt)
#Grid(10,5);
move to (3,1); "\textit{resi\\stor(2,,E)}" rjust;
resistor(2,,E); llabel(,R_1,); "$P_s$ nedefinovaý" ljust;


move to (3,2); "\textit{re\\s\_05w(2,,E)}" rjust;
res_05w(2,,E); llabel(,R_2,); "$P_s = 0.5W$" ljust;

move to (3,3); "\textit{re\\s\_025w(2,,E)}" rjust;
res_025w(2,,E); llabel(,R_3,); "$P_s = 0.25W$" ljust;

move to (3,4); "\textit{re\\s\_0125w(2,,E)}" rjust;
res_0125w(2,,E); llabel(,R_4,); "$P_s = 0.125W$" ljust;

move to (3,5); "\textit{re\\s\_005w(2,,E)}" rjust;
res_005w(2,,E); llabel(,R_5,);  "$P_s = 0.05W$" ljust;

move to (3,6); "\textit{re\\s\_1w(2,,E)}" rjust;
res_1w(2,,E); llabel(,R_6,);  "$P_s = 1W$" ljust;

move to (3,7); "\textit{re\\s\_2w(2,,E)}" rjust;
res_2w(2,,E); llabel(,R_7,);  "$P_s = 2W$" ljust;

move to (3,8); "\textit{re\\s\_5w(2,,E)}" rjust;
res_5w(2,,E); llabel(,R_8,);  "$P_s = 5W$" ljust;

'''

_ = cm_compile('./src/cm_0165d', data, dpi=600)   
```

```{figure} ./src/cm_0165d.png
:width: 400px
:name: cm_0165d

[Príklad](./src/cm_0165d.ckt) použitia modifikovaných makier.
```
    


