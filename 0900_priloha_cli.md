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

Pre vytváranie jednotlivých obrázkov v bežnej praxi vyhovuje exportovanie obrázkov z programu **PyCirkuit** tak ako je to uvedené v úvode tejto publikácie. Pokiaľ budeme používať vlastný editor pre písanie skriptov alebo potrebujeme generovať súbor obrázkov napríklad pre publikácie alebo knihy, je vhodnejšie použiť programové prostriedky.

## <font color='teal'> CLI PyCirkuit </font>

Program **PyCirkuit** umožňuje generovanie obrázkov v móde CLI (Command Mode Input), výpis parametrov programu získame príkazom

    pycirkuit --help

Nastavenie parametrov pre generovanie obrázkov vo formáte PNG v rozlíšení 600 dpi
    
    pycirkuit --links --overwrite --dpi 600 -p <file_name>.ckt


## <font color='teal'> Shell skript </font>

Skript pre OS Linux využíva programy

    m4     - štandardná súčasť operačného systému
    dpic   - kompilátor   
    latex  - systém na sadzbu textu 
    dvips  - konvertor DVI->PS, sučasť distribúcie LaTeX
    gs     - konvertor PS->PNG, súčasť distribúcie ghostscript
    
    
Inštalácia programov

    sudo apt-get install dpic
    sudo apt-get install texlive texstudio texlive-plain-generic texlive-latex-extra \
                 texlive-lang-czechslovak texlive-lang-greek texlive-font-utils
    sudo apt-get install ghostscript

Pre konverziu generovaných sriptov v LateXe potrebujeme pomocný súbor *template.tex* s obsahom

    \documentclass{article}
    \usepackage{pst-plot, pst-eps, tikz}
    \pagestyle{empty}

    \begin{document}
        \begin{TeXtoEPS}
            \input{temp_data.tex}
        \end{TeXtoEPS}
    \end{document}
    
    
Shell skript *cmc.sh*, ktorý generuje obrázky vo formáte PNG má potom tvar 

    #!/bin/bash
    # cesta ku M4 knizniciam CircuitMacros (libcct,m4 ... )
    CIRCUIT_MACROS='./cm/'

    # expadovanie makier do formatu TIKZ
    m4 -I $CIRCUIT_MACROS pgf.m4  $1 | dpic -g > temp_data.tex

    # kompilacia latex suboru
    latex template.tex > latex.log
    dvips -q* -E template.dvi -G0 -o $(basename $1 .ckt).eps > dvips.log

    # konverzia *.eps -> *.png, parameter r-rozzlisenie v dpi
    gs -dSAFER -dEPSCrop -r600 -sDEVICE=pngalpha -dALLOWPSTRANSPARENCY -o $(basename $1 .ckt).png $(basename $1 .ckt).eps

    # zmazanie docasnych suborov
    rm temp_data.tex
    rm dvips.log
    rm latex.log
    rm $(basename $1 .ckt).eps
    rm template.dvi
    rm template.aux
    rm template.log

V skripte upravte premennú podľa aktuálnej konfigurácie adresárov. Nastavte skript ako spustiteľný

    chmod +x cmc.sh


Skript spustíte z konzoly príkazom 

    ,/cmc.sh <meno_suboru>.ckt
    
    
## <font color='teal'> Python skript </font>

Pre generovanie obrázkov v prostredí Pythonu je možné využiť funkciu s volaniami externých programov

    import os
    import sys
    
    def cm_compile(file_name, cm_data='', dpi=300):
    
        CIRCUIT_MACROS_PATH = './cm'
    
        os.system( 'm4 -I %s pgf.m4  %s > data.dpc'%(CIRCUIT_MACROS_PATH, file_name+'.ckt') )
        os.system( 'dpic -g data.dpc > data.tex') 
        
        temp = r'''
        \documentclass{article}
        \usepackage{pstricks,pst-plot, pst-eps, tikz}
        \pagestyle{empty}
        \begin{document}
        \begin{TeXtoEPS}
        \input{temp_data.tex}
        \end{TeXtoEPS}
        \end{document}
        '''
    
        f = open('template.tex', 'w' ) 
        f.write(temp)
        f.flush()
        f.close()
        
        os.system( 'latex template.tex > latex.log')   
        os.system( 'dvips -q* -E template.dvi -G0 -o %s > dvips.log '%(file_name+'.eps') )
        os.system('gs -dSAFER -dEPSCrop -r600 -sDEVICE=pngalpha -dALLOWPSTRANSPARENCY -o %s %s >null'%(file_name+'.png', file_name+'.eps'))
        
        os.system( 'rm *.dvi' ) 
        os.system( 'rm *.aux' ) 
        os.system( 'rm *.log' ) 
        os.system( 'rm *.tex' ) 
        os.system( 'rm *.eps' ) 
        os.system( 'rm *.dpc' ) 
        return file_name + '.ckt'

Použitie skriptu

    data = r'''
    .PS
    scale=2.54
    cct_init

    resistor(,,E); rlabel(,R_1,);
    .PE
    '''

    cm_compile('obr_01', data, dpi=600) 


