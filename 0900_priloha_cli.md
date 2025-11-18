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


# <font color='navy'> Kompilácia skriptov </font> 

Proces vytvárania zapojenia, jeho kompilácie a konverzie do výsledného grafického formátu môžeme urobiť aj ručne priamo z konzoly systému. V nasledujúcom texte sú použité označenia

    PATH_TO_CM_MACROS - cesta k inštalácii circuit-macros
    SOURCE_FILE       - zdrojový textový súbor s vytvoreným zapojením
    PIC_FILE          - vystupny subor predpropcesora m4 s prikazmi gpic       
    PSTRICK_FILE      - kompilovanu subor s prikazmi pre pstricks
    LATEX_FILE        - finalny LaTeX súbor

## <font color='teal'> Preklad a kompilácia s využitím LaTex-u </font> 


Najprv uvedieme komplikovanejší postup s využitím renderovania textov v LaTex-e a s využitím makier PSTricks, predpokladáme, že LaTex s príslušnými modulmi máte už nainštalovaný. V prvom kroku preložíme naše zapojenie pomocou makroprocesora do príkazov jazyka PIC

    m4 -I PATH_TO_CM_MACROS pstricks.m4 SOURCE_FILE > PIC_FILE

v príkaze zadefinujeme cestu k adresáru, kde sme rozbalili makrá z archívu, náš zdrojový súbor so zapojením a zvolíme meno súboru, do ktorého sa uložia príkazy v PIC. *pstricks.m4* obsahuje sadu pomocných makier pre finálny výstup. 

V druhom kroku súbor v jazyku PIC do sady makier *pstricks* preložíme pomocou

    dpic -p PIC_FILE > PSTRICK_FILE

Výsledkom prekladu je zdrojový text pre LaTexu-u s príkazmi pre *pstricks*, ktorý má štandardný tvar

    \begin{pspicture}  ...  \end{pspicture}

Skompilovaný súbor už môžeme vložiť do dokumentu v LaTex-u a ďalej s ním pracovať. Pretože pri kreslení schém potrebuje priebžne sledovať výsledok práce, pre renderovanie obrázku zapojenia do postscriptu môžeme použiť krátky dokument (LATEX_FILE)

    \documentclass{article}
    \usepackage{times,pstricks,pst-eps,pst-grad}
    \usepackage{graphicx}
    \begin{document}
    \begin{TeXtoEPS}
    ...
    \input PSTRICK_FILE        <- menu skompilovaneho suboru bez pripony
    ...
    \end{TeXtoEPS}\end{document}



ktorý preložíme 

    latex LATEX_FILE      <- bez pripony .tex
    dvips -E LATEX_FILE   <- bez pripony .aux
    
Výsledkom prekladu je obrázok vo formáte postscript. Aj keď uvedený postup vyzerá komplikovane, jednoduché skripty v pythone alebo shell-e problém vyriešia. 


## <font color='teal'> Preklad a kompilácia bez využitia LaTex-u </font> 


Pri jednoduchšom spôsobe grafický súbor vygeneruje priamo kompilátor *dpic*, samozrejme ale bez renderovania textov LaTex-om.

    m4 -I PATH_TO_CM_MACROS postscript.m4 SOURCE_FILE | dpic -r > PS_FILE




