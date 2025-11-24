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

Pre systém založený na derivátoch Ubuntu je vhodné použiť inštaláciu jednoducého prostredia **PyCirkuit**, ktoré obsahuje v distribúcii aj knižnice `CircuitMacros`. Pre spracovanie skriptov je potrebné nainštalovať kompilátor **dpic** a pre renderovanie textov, ktoré obsahujú matematické výrazy aj podporu pre **LaTeX**.

    sudo apt-get update
    sudo apt install python3-pip 
    sudo apt-get -y install dpic
    sudo apt-get install texlive texstudio texlive-plain-generic texlive-latex-extra \
                     texlive-lang-czechslovak texlive-lang-greek texlive-font-utils
    pip install pycirkuit 
    
Po inštalácii spustíme prostredie **PyCirkuit**  v konzole príkazom

    pycirkuit


## <font color='teal'>  Windows</font> 

Pre inštalácia PyCirkuit pod OS Windows potrebuje nainštalovať prostredie **LaTeX**, interpreter **Python** a pomocné programy **dpic** a **m4** pre kompiláciu skriptov `CircuitMacros`. 

### <font color='brown'> Inštalácia LaTeX a Python</font>

* Vyberieme a nainštalujeme distribúciu LaTeX-u pre Windows napr. MikTeX. Túto distribúciu LaTeX-u stiahneme zo stránky [miktex.org](https://miktex.org/). Pre inštaláciu postupujeme podľa tam uvedených [pokynov](https://miktex.org/howto/install-miktex).

* Stiahneme a nainštalujeme interpreter programovacieho jazyka Python3 pre Windows. Odporúčame použitie distribúcie [WinPython](https://winpython.github.io/), ktorá umožňuje spustiť Python na akomkoľvek počítači so systémom Windows bez nutnosti inštalácie. Zo [stránky](https://sourceforge.net/projects/winpython/files/WinPython_3.13/3.13.7.0/) stiahneme súbor [WinPython64-3.13.7.0slim.exe](https://sourceforge.net/projects/winpython/files/WinPython_3.13/3.13.7.0/WinPython64-3.13.7.0slim.exe/download).

* Súbor uložíme do zvoleného adresáru, po jeho spustení sa rozbalí v danom adresári, čím vznikne v tomto adresári podadresár s názvom **WPy64-31700** so spustiteľným súborom s názvom **WinPython Command Prompt.exe**.
Po jeho spustení sa objaví okno s príkazovým riadkom systému Windows, v ktorom je možné spustiť interpreter jazyka Python3.


### <font color='brown'> Inštalácia PyCirkuit</font>

* Je vhodné program nainštalovať do virtuálneho prostredia Python-u, aby sme ho oddelili od ostatných inštalácií a knižníc Python-u, ktoré sa môžu nachádzať v operačnom systéme. Vytvoríme adresár, kam chceme PyCirkuit nainštalovať a spustíme program

      WinPython Command Prompt.exe

* Vytvoríme virtuálne prostredie Python-u pomocou príkazu a aktivujeme virtuálne prostredie

      python -m venv PyCirkuit
      cd PyCirkuit\Scripts
      activate

* Inštaláciu PyCirkuit spustíme príkazom:

      pip install pycirkuit

* Do adresára **PyCirkuit\Lib\site-packages\pycirkuit\lib** vložíme dva spustiteľné súbory **dpic.exe** a **m4.exe**, ktoré stiahneme zo stránky projektu [CircuitMacros](https://ece.uwaterloo.ca/~aplevich/dpic/Windows/index.html). Grafické rozhranie programu PyCirkuit spustíme príkazom:
        
      PyCirkuit

* Príklady obsiahnuté v distribúcii programu sa nachádzajú v adresári **PyCirkuit\Lib\site-packages\pycirkuit\examples**. Po skončení práce môžeme deaktivovať virtuálne prostredie príkazom

      deactivate



alebo jednoducho zatvoríme okno s príkazovým riadkom OS Windows, z ktorého sme spustili PyCirkuit.


### <font color='brown'> Použitie PyCirkuit</font>

V adresári s nainštalovaným programom **PyCirkuit** aktivujeme virtuálne prostredie a spustíme program 

    cd <cesta k virtuálnemu prostrediu>
    PyCirkuit\Scripts\activate
    PyCirkuit
