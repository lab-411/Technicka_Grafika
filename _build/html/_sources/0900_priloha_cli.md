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


# <font color='navy'> Export obrázkov </font>

Pre vytváranie jednotlivých obrázkov v bežnej praxi vyhovuje exportovanie obrázkov priamo v programe **PyCirkuit**. Pokiaľ budeme používať vlastný editor pre písanie skriptov alebo potrebujeme generovať súbor obrázkov, napríklad pre publikácie alebo knihy, je vhodnejšie použiť programové prostriedky.

## <font color='teal'> PyCirkuit </font>

Program **PyCirkuit** umožňuje generovanie obrázkov v móde CLI (*Command Line Input*), výpis parametrov programu získame príkazom:

    pycirkuit --help

Nastavenie parametrov pre generovanie obrázkov vo formáte PNG v rozlíšení 600 dpi získame príkazom:
    
    pycirkuit --links --overwrite --dpi 600 -p <file_name>.ckt


## <font color='teal'> Shell skript </font>

Zdrojové súbory obrázkov môžeme konvertovať do publikácií v rôznych formátoch. Nižšie popísaný skript pre OS Linux využíva programy:

    m4     - štandardná súčasť operačného systému
    dpic   - kompilátor   
    latex  - systém na sadzbu textu 
    dvips  - konvertor DVI->PS, sučasť distribúcie LaTeX
    gs     - konvertor PS->PNG, súčasť distribúcie ghostscript
    
    
Tieto nainštalujeme do systému (Debian, Ubuntu) pomocou príkazov:

    sudo apt-get install dpic
    sudo apt-get install texlive texstudio texlive-plain-generic texlive-latex-extra \
                 texlive-lang-czechslovak texlive-lang-greek texlive-font-utils
    sudo apt-get install ghostscript

Postup generovania obrázkov z `CircuitMacros` je potom nasledovný:

* v textovom editore vytvoríme zdrojový text obrázku, 
* pomocou makroprocesora **m4** a knižníc makier expandujeme makrá do jazyka *dpic*,
* kompilátorom **dpic** preložíme makrá do skriptov *tikz* pre sadzací systém *LaTex*,
* vložíme skript *tikz* do pomocného konfiguračného súboru a pomocou  systému *LaTeX* ho preložíme do súboru *.dvi*. V prípade potreby môžeme vygenerovaný skript priamo používať v zdrojových kódoch publikácií bez potreby ďalších konverzií,
* pomocou programu **dvips** konvertujeme obrázok do vektorového formátu *.eps*, 
* pomocou konvertoru **gs** prevedieme vektorový obrázok do rastrového formátu *.png*. V konfigurácii konvertoru môžeme nastaviť rozlíšenie obrázku a orezanie prázdnych okrajov.
     
Na prvý pohľad postup vyzerá komplikovaný, ale poskytuje kontrolu nad každým krokom konverzie. Celý postup je implementovaný v nasledujúcom skripte [cmc.sh](./src/cmc.sh) pre príkazový interpreter *bash*. Konfiguračný súbor pre systém LaTeX *template.tex* generuje skript. V prípade potreby môžete pomocný konfiguračný súbor upraviť, napríklad ak potrebujete v systéme LaTeX doplniť ďaľšie prostredie a pod.
 
```{code-block} bash
:caption: Skript *cmc.sh* 
#!/bin/bash

echo '% LaTeX template file
\documentclass{article}
\usepackage{amsmath}
\usepackage{pst-plot, pst-eps, tikz}
\pagestyle{empty}

\begin{document}
\begin{TeXtoEPS}
    \input{data.tex}
\end{TeXtoEPS}

\end{document}' > template.tex

# cesta ku M4 knizniciam CircuitMacros (libcct.m4 ... )
CIRCUIT_MACROS='./cm/'

# expadovanie makier do formatu TIKZ
m4 -I $CIRCUIT_MACROS pgf.m4  $1 | dpic -g > data.tex

# kompilacia latex suboru
latex template.tex > latex.log
dvips -q* -E template.dvi -G0 -o $(basename $1 .ckt).eps > dvips.log

# konverzia *.eps -> *.png, parameter r-rozlisenie v dpi
gs -dSAFER -dEPSCrop -r600 -sDEVICE=pngalpha -dALLOWPSTRANSPARENCY -o $(basename $1 .ckt).png $(basename $1 .ckt).eps > gs.log

# zmazanie docasnych suborov
rm dvips.log
rm latex.log
rm $(basename $1 .ckt).eps
rm data.tex
rm template.tex
rm template.dvi
rm template.aux
rm template.log
```

## <font color='brown'> Použitie  </font>
    
Skript uložte do adresáru so zdrojovými kódmi obrázkov. V skripte upravte premennú *CIRCUIT_MACROS* podľa aktuálnej konfigurácie adresárov s knižnicami `CircuitMacros`. Nasledujúcim príkazom v konzole nastavte skript ako spustiteľný program:

    chmod +x cmc.sh

Konverziu zdrojového kódu *<meno_suboru>.ckt* na obrázok *.png* spustíme z konzoly príkazom: 

    ./cmc.sh <meno_suboru>.ckt
    
    
## <font color='teal'> Python skript </font>

Pre generovanie obrázkov v prostredí Python, ako je napríklad *Jupyter Lab*, je možné využiť funkciu *cm_compile()* implementovanú v súbore [cmc.py](./src/cmc.py). Funkcia volá rovnaké programy ako shell-skript uvedený v predchádzajúcej časti:

```{code-block} python
:caption: Skript *cmc.py* 
import os

CIRCUIT_MACROS_PATH = './cm'

def cm_compile(file_name, cm_data='', dpi=300):

    fp = open( file_name + '.ckt', 'w'); 
    fp.write(cm_data);
    fp.close()
        
    os.system( 'm4 -I %s pgf.m4  %s > data.dpc'%(CIRCUIT_MACROS_PATH, file_name+'.ckt') )
    os.system( 'dpic -g data.dpc > data.tex') 
    
    temp = r'''
    \documentclass{article}
    \usepackage{amsmath}
    \usepackage{pst-plot, pst-eps, tikz}
    \pagestyle{empty}

    \begin{document}
        \begin{TeXtoEPS}
        \input{data.tex}
        \end{TeXtoEPS}
    
    \end{document}
    '''

    f = open('template.tex', 'w' ) 
    f.write(temp)
    f.flush()
    f.close()
    
    os.system( 'latex template.tex > latex.log')   
    os.system( 'dvips -q* -E template.dvi -G0 -o %s > dvips.log '%(file_name+'.eps') )        
    os.system('gs -dSAFER -dEPSCrop -r600 -sDEVICE=pngalpha -dALLOWPSTRANSPARENCY -o %s %s > gs.log'%(file_name+'.png', file_name+'.eps'))
    
    os.system( 'rm *.dvi' )
    os.system( 'rm *.aux' )
    os.system( 'rm *.log' )
    os.system( 'rm *.tex' )
    os.system( 'rm *.eps' )
    os.system( 'rm *.dpc' )
    return file_name + '.ckt'
```

### <font color='brown'> Použitie </font>

Vytvoríme program v Pythone, v ktorom v textovom (*raw*) reťazci definujeme skript pre generovanie obrázku. Obrázok vygenerujeme vyvolaním funkcie *cm_compile()* :


```{code-block} python
:caption: Generovanie obrázkov v prostredí Pythonu 

dat a = r'''
.PS
scale = 2.54     
maxpswid = 30   
maxpsht = 30           
cct_init              

R1: resistor(2,,E); llabel(,R_1,); 
    dot; 
    { 
       R3: resistor(down_ 1.5,,E); rlabel(,R_3,);
    }
    capacitor(right_ 1.5,,E); llabel(,C_1,); rlabel(,10 \mu F,);
.PE
'''
cm_compile('obr_010', data)
```

Skript môžeme používať aj na generovanie obrázkov priamo v prostredí *Jupyter Lab*, {numref}`cm_0900a`.

```{figure} ./img/jupyter.png
:width: 700px
:name: cm_0900a

Použitie skriptov z *CircuitMacros* v prostredí *Jupyter Lab*.
```


