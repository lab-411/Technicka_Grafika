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


    
# <font color='navy'> Prepojenia </font>

V `CircuitMacros` sú prepojenia medzi prvkami zapojenia zobrazené pomocou príkazu *line*, parametre a možnosti kreslenia štandardných prepojovacích vodičov sú popísané v kapitole [Grafika](./0110_cm_grafika.md). Tvar a forma zobrazenia prepojení medzi prvkami sa v čase s vývojom techniky menila. V minulosti sa pri prepojeniach kládol dôraz aj na formu zobrazenia ich fyzickej realizácie, ako vidíme na nasledujúcom obrázku, kde je znázornené križovanie neprepojených vodičov oblúkom a zvýraznená spoločná zem, ktorá bývala realizovaná masívnym kovovým rámom zariadenia, táto je zobrazená hrubou čiarou.  

```{figure} ./img/radio_r731.jpg
:width: 600px
:name: cm_0106a

Zapojenie elektrónkového rádia, [zdroj](https://archive.org/details/ABC_Radiocostruzioni_R731_R841).
```
Pre kreslenie takejto formy zapojenia môžeme využť makro *crossover()*

    crossover(linespec, [L|R][:line_attributes], Linename1, Linename2, . . .)
    
    parametre:
    
        linespec           - začiatok a koniec prepojenia
        [L|R]              - smer oblúka
        [:line_attributes] - doplnkové atrubúty (dashed ...)
        Linename1          - referencie na spoje, nad ktorými prechádza prepojenie 
        Linename2
        
        
Pre nakreslenie hrubšieho zemného vodiča a pripojovacích bodov si vytvoríme vlastné makrá *gnd_line()* a *gnd_dot()*, použitie makier zobrazuje nasledujúci príklad

```{code-block}
define(`gnd_line',`[ move to ($1,0); linethick_(5);
    L: line to Here + ($1,0); linethick_(); ]')

define(`gnd_dot',`[ C:circle at Here rad 0.09 fill 1; ]')

P1:(1,0.5);    P2:(1,1);   P3:(1,1.5);   DX:(0.5,0)
P4:(0.5, 2.5); P5:(1,2.5); P6:(1.5,2.5); DY:(0,0.5)

LA: line from P1 to P3; 
    crossover(from P2-DX to P2+DX,,LA)

LC: line from P4 to P6; 
    crossover(from P5-DY to P5+DY,R,LC)

GL:  gnd_line(4) at (3, 0.5);  
Q1: line from (3, 1.0) right_ 4; 
Q2: line from (3, 1.5) right_ 4; 

CR: crossover(from (4,.5) to (4, 2),L,Q1, Q2); { gnd_dot() at CR.s }
TR:  transformer(up_ 1.5,R,4,W,4) with .P1 at CR.n; line from TR.S2 to (TR.S1, TR.P2)
     crossover(from TR.S1 to (TR.S1, (Q2.start+Q1.start)/2),R,Q2);
     line to (TR.S1, Q1.start); dot;
```


```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
Grid(8,4);

define(`gnd_line',`[
    move to ($1,0);
    linethick_(5);
    L: line to Here + ($1,0);
    linethick_();
]')

define(`gnd_dot',`[ C:circle at Here rad 0.09 fill 1; ]')

P1:(1,0.5);    P2:(1,1);   P3:(1,1.5);   DX:(0.5,0)
P4:(0.5, 2.5); P5:(1,2.5); P6:(1.5,2.5); DY:(0,0.5)

LA: line from P1 to P3; "\sf LA" ljust;
    crossover(from P2-DX to P2+DX,,LA)

LC: line from P4 to P6; "\sf LC" ljust;
    crossover(from P5-DY to P5+DY,R,LC)


GL:  gnd_line(4) at (3, 0.5);  "\sf GL" ljust
Q1: line from (3, 1.0) right_ 4; "\sf Q1" ljust
Q2: line from (3, 1.5) right_ 4; "\sf Q2" ljust

CR: crossover(from (4,.5) to (4, 2),L,Q1, Q2); { gnd_dot() at CR.s }
TR:  transformer(up_ 1.5,R,4,W,4) with .P1 at CR.n; line from TR.S2 to (TR.S1, TR.P2)
     crossover(from TR.S1 to (TR.S1, (Q2.start+Q1.start)/2),R,Q2);
     line to (TR.S1, Q1.start); dot;
'''

_ = cm_compile('cm_0106b', data, dpi=600)   
```

```{figure} ./src/cm_0106b.png
:width: 500px
:name: cm_0106b

[Vykreslenie](./src/cm_0106b.ckt) časti zapojenia so starším prevedením križovania vodičov.
```

Pre vykreslenie štandarného spojenie vodičov použijeme makro *dot()*. Pokiaľ nie je križovanie vodičov nijako označené, predpokladáme že sú nespojené. Parametrami makra môžeme upraviť veľkost spoja, makro bez parametrov vykreslí bod spojenia v preddefinovanom tvare.

    dot(at location,radius|keys,fill)
    
    parametre:
    
        at location  - umiestnenie spojenia
        radius|keys  - parametre spoja, priemer vonkajšej kružnice
        fill         - hodnota 0...1 výplne, 0-čierna, 1-biela

Polohu prepojenia môžeme využiť aj na vyznačenie eletrických veličín v uzle zapojenia.

```{code-block}
:emphasize-lines: 2
resistor(2,,E); llabel(,\sf R_1,)
dot "\sf 3.3V" above; 
{resistor(down_ 2 ,,E);  llabel(,\sf R_3,)}
resistor(right_ 2,,E);  llabel(,\sf R_2,)
```

```{code-cell} ipython3  
:tags: ["remove-cell"]

from src.utils import *

data = r'''
resistor(2,,E); llabel(,\sf R_1,)
dot "\sf 3.3V" above; {resistor(down_ 2 ,,E);  llabel(,\sf R_3,)}
resistor(right_ 2,,E);  llabel(,\sf R_2,)
'''

_ = cm_compile('cm_0106c', data, dpi=600)   
```

```{figure} ./src/cm_0106c.png
:width: 250px
:name: cm_0106c

Zobrazenia napätia v uzle zapojenia.
```
