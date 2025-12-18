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


# <font color='navy'> Blokové diagramy</font> 

Elektronické zariadenia v súčasnej dobe sú komplexné systémy, ktorých dokumentácia si vyžaduje hierarchický prístup, v ktorom na najvyššej úrovni dokumentujeme jednotlivé funkčné celku a vzťahy medzi nimi. Diagramy majú často tvar hybridných zapojení, kde pre väčšiu názornosť kombinujeme bloky s diskrétnymi komponentami reprezentujúcimi funkčnosť vybraných častí zariadenia.

Na obrázku je blokové zapojenie zariadenia pre testy mechanických vlastností 3D tlačených materiálov. Zariadenie obsahuje centrálny mikrokontrolér a analógové a digitálne periférie, ktoré sú riadené prostredníctvom rozhraní mikrokontroléra. Prepojenia medzi jednotlivými funkčnými časťami sú realizované pomocou označených zberníc (*SPI*, *I2C*) ako aj vodičmi, ktoré môžu byť jednotlivé alebo v skupine (*pulse*, *switch* ...). Pre lepšiu prehľadnosť je v zapojení označené, z koľkých vodičov zbernica alebo skupina vodičov pozostáva.



```{figure} ./src/exam_02_trhacka.png
:width: 700px
:name: img_0208a

[Blokové](./src/exam_02_trhacka.ckt) zapojenie zariadenia pre testy 3D tlačených materiálov.
```
