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


# <font color='navy'> Inštalácia  </font> 

## <font color='teal'>  Linux </font> 

Pre systém založený na derivátoch Ubuntu je vhodné použiť inštaláciu *CircuitMacros* spolu s editorom *pycirkuit*. Pre renderovanie textov, ktoré obsahujú matematické výrazy je potrebné nainštalovať aj podporu pre *LaTeX* a *dpic* 

    sudo apt-get update
    sudo apt install python3-pip 
    sudo apt-get -y install dpic
    sudo apt-get install texlive texstudio texlive-plain-generic texlive-latex-extra \
                     texlive-lang-czechslovak texlive-lang-greek texlive-font-utils
    pip install pycirkuit --break-system-packages


## <font color='teal'>  Windows</font> 

## <font color='teal'> MAC-OS </font> 
