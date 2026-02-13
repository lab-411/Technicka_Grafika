# <center> <font color='navy'>  <b> Programová tvorba technickej grafiky </b> </font> </center> 

<center> 
<h3> <font color='brown'>  <b> Lenka Bartošová, Peter Fabo, Michal Kuba </b> </font> </h3>
</center> 


```{figure} ./img/heatkit.png
:width: 800px
:name: cm_116
```

<center> 
<h3> <font color='brown'>  <b> LAB - 411 Production </b> </font>       </h3>
<h3> <font color='brown'>  <b> Verzia 0.55 / Feb. 2026 </b> </font>  </h3>
</center> 

----------------

## <font color='teal'>  Obsah </font>  

%```{contents} Table of Contents
%:depth: 2
%```


```{toctree}
:titlesonly: True
:caption: Úvod
0010_uvod.md
0012_instalacia.md
0013_terminologia.md
0014_zaklady.md
```

```{toctree}
:titlesonly: True
:caption: Prvky zapojenia
0100_cm_dvojpoly.md
0102_cm_mnohopoly.md
0106_cm_prepojenia.md
0140_cm_konektor.md
0110_cm_grafika.md
0130_cm_text.md
0104_cm_upravy.md
```

```{toctree}
:titlesonly: True
:caption: Programovanie
0160_cm_syntax.md
0165_cm_makra.md
0175_cm_funkcie.md
0180_cm_prostredie.md
```

```{toctree}
:titlesonly: True
:caption: Príklady
0200_ex_jednoduche.md
0202_ex_tranzistor.md
0204_ex_opamp.md
0207_ex_integrovane_obvody.md
0206_ex_logicke_obvody.md
0208_ex_vyvojove_diagramy.md
0210_ex_katalog.md
```

```{toctree}
:titlesonly: True
:caption: Prílohy
0905_priloha_farby.md
0900_priloha_cli.md
0915_priloha_editor.md
0910_priloha_odkazy.md
```

## <font color='teal'> Anotácia / Annotation </font>   


## <font color='teal'> Autori/ Authors </font>  

### <font color='brown'> Ing. Lenka Bartošová, PhD. </font>

### <font color='brown'> RNDr. Peter Fabo, PhD. </font>

### <font color='brown'> Ing. Michal Kuba, PhD. </font>


## <font color='teal'> Vydal / Published by </font> 

    Vydalo roku 2026 

    LAB - 411 Production
    FŠT-TNUNI
    Ku kyselke 469
    911 06 Trenčín
    Slovensko

    ISBN: xxx-xx-xxxxxx-x
    

### <font color='brown'> Citovanie / How to cite</font>

    ZENODO Record

    
### <font color='brown'> Preklady / Translations </font>

Preklady do iných jazykov sú možné v zmysle licencie MIT uvedenej nižšie. V zmysle nariadenia Európskeho parlamentu a Rady (EÚ) 2024/1689 z 13. júna 2024 autori tohoto diela **nepovolujú** využitie tohoto diela a ani jeho častí pre použitie v oblasti umelej inteligenice žiadnym aktuálnym ako aj budúcim spôsobom. 

Translations into other languages ​​are possible under the terms of the MIT license listed below. In accordance with Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024, the authors of this work **do not** authorize the use of this work or any part of it for use in the field of artificial intelligence in any current or future manner.


### <font color='brown'> Titulný obrázok / Cover Image </font>

Titulný obrázok je vygenerovaný na základe podkladov uvedených ako príklad použitia v distribúcii programu *Circuit Macros*

The cover image is generated based on the materials provided as an example of use in the distribution of the *Circuit Macros* program.


## <font color='teal'>  Licencie / Licenses </font>  


### <font color='brown'> Zdrojové kódy / Source code </font>

Zdrojové kódy sú dostupné pod licenciou MIT uvedenou nižšie na URL adrese / The source codes are available under the MIT license at the URL below

    https://github.com/lab-411/Technicka_Grafika


### <font color='brown'> Publikácia </font>  

Publikácia **Programová tvorba technickej grafiky** je vydaná pod licenciou MIT

    Copyright © 2026 LAB-411 Team

    Permission is hereby granted, free of charge, to any person obtaining a copy 
    of this software and associated documentation files (the “Software”), to deal 
    in the Software without restriction, including without limitation the rights 
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
    copies of the Software, and to permit persons to whom the Software is furnished 
    to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all 
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
    INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR 
    A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
    OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


### <font color='brown'> Použité programové vybavenie / Software </font> 

Publikované na platforme *Sphinx* s využitím jazyka *MyST Markdown*, prostredia *CircuitMacros* a programovacieho jazyka *Python* v znení licencií uvedených nižšie.

Published on the *Sphinx* platform using the *MyST Markdown* language, the *CircuitMacros* environment, and the *Python* programming language under the terms of the licenses listed below.

Licencia k distribúcii programu **CircuitMacros**


    * Circuit_macros Version 10.9, copyright (c) 2025 J. D. Aplevich under     *
    * the LaTeX Project Public Licence in file Licence.txt. The files of       *
    * this distribution may be redistributed or modified provided that this    *
    * copyright notice is included and provided that modifications are clearly *
    * marked to distinguish them from this distribution.  There is no warranty *
    * whatsoever for these files.
    

Licencia k distribúcii programu **Sphinx**

    Copyright (c) 2007-2025 by the Sphinx team (see AUTHORS file). All rights reserved.

    Redistribution and use in source and binary forms, with or without modification, 
    are permitted provided that the following conditions are met:

        Redistributions of source code must retain the above copyright notice, this list 
        of conditions and the following disclaimer.
        Redistributions in binary form must reproduce the above copyright notice, this list 
        of conditions and the following disclaimer in the documentation and/or other 
        materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
    EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
    OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT 
    SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
    INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
    PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF 
    THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Citácia **MyST Markdown**

    Rowan Cockett, Franklin Koch, Steve Purves, Angus Hollands, Yuxi Wang, Chris Holdgraf, 
    Dylan Grandmont, Stefan van der Walt, Andrea, Jan-Hendrik Müller, Spencer Lyon, 
    Cristian Le, Jim Madge, Thierry Parmentelat, wwx, Sugan Reden, Yuanhao Geng, Ryan Lovett, 
    Mikkel Roald-Arbøl,Nicolas M. Thiéry. 
    (2025). jupyter-book/mystmd: mystmd@1.6.0. Zenodo. 10.5281/ZENODO.14805610


### <font color='brown'> Kontakt na autorov, diskusia a pripomienky <br>Contact the autors, discussion and comments </font>

    https://github.com/lab-411/Technicka_Grafika/discussions


## <font color='teal'> Poďakovanie/ Acknowledgements </font>  

Táto publikácia bola vytvorená s podporou grantovej agentúry VEGA, projekt pod názvom "Interpretácia periodických a neperiodických deformácií zemskej kôry v oblasti Západných Karpát na základe paralelných meraní horizontálnych posunutí."  (projekt číslo 2/0013/25).

This publication was supported by the VEGA grant agency, project under the name "Interpretation of periodic and non-periodic deformations of the Earth's crust in the Western Carpathians based on parallel measurements of horizontal displacements." (project number 2/0013/25).
