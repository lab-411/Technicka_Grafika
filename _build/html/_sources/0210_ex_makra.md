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

# <font color='navy'> Užitočné makrá  </font>

## <font color='teal'> Pracovná plocha  </font>

%========================================================================
% SHADEBOX
%------------------------------------------------------------------------

````{tab-set}

```{tab-item} Grid()
   Obrazok
```

```{tab-item} Popis  
        Grid(x,y)
        
        Vykreslenie pomocnej mriežky na ploche pre jednoduchšiu rozmiestňovanie prvkov.
        Mierka mriežky je v centimetroch.
        
```

```{tab-item} Príklad
        include(lib_base.ckt)
        Grid(10,5)
```
````

## <font color='teal'> Grafické objekty  </font>

%========================================================================
% SHADEBOX
%------------------------------------------------------------------------

````{tab-set}

```{tab-item} shadebox()
   Obrazok
```

```{tab-item} Popis  
   popis
```

```{tab-item} Príklad
        linethick_(0.8);
        hatchbox(wid 3 ht 2, ,dashed,angle=125 ); 
```

````

%========================================================================
% HATCHBOX
%------------------------------------------------------------------------

````{tab-set}

```{tab-item} hatchbox()
   obrazok
```

```{tab-item} Popis   
   popis
```

```{tab-item} Príklad
        shadebox(B:box wid 3 ht 1 with .sw at (1,1), 2) 
```

````


## <font color='teal'> Doplnky </font>

%========================================================================
% SINUSOID
%------------------------------------------------------------------------

```{code-cell} ipython3 
:tags: ["remove-cell"]

from src.utils import *

data = r'''
include(lib_base.ckt)
include(lib_color.ckt)

Origin: Here 

move to (0,1); 
ampl = 1;  freq = 2;  t_min = 0;  t_max = 10;  phase = -pi_/2;
sinusoid(ampl, twopi_*freq/t_max, phase, t_min , t_max);

move to (0,1); 
color_blue;
ampl = 1;  freq = 6;  t_min = 0;  t_max = 10;  phase = pi_/2;
sinusoid(ampl, twopi_*freq/t_max, phase, t_min , t_max, dashed);

move to (0,1); 
color_red;
ampl = 1;  freq = 3;  t_min = 0;  t_max = 10;  phase = 0;
sinusoid(ampl, twopi_*freq/t_max, phase, t_min , t_max, dotted);
'''

_ = cm_compile('cm_0210a', data,  dpi=600 )   
```

%-------------------------------------------------------------------------

````{tab-set}

```{tab-item} sinusoid()
<img src="./src/cm_0210a.png" width="600px" class="center">
```

```{tab-item} Popis
    Zobrazenie harmonického priebehu
    
    sinusoid(ampl, freq, phase, t_min, t_max)
    
      ampl  - amplitúda
      freq  - frekvencia
      phase - fáza
      t_min - začiatok časovej osi
      t_max - koniec časovej osi
```


```{tab-item} Príklad
    Origin: Here;
    sinusoid(1.0, twopi_*2/10,-pi_/2, 0, 10) at Origin;
    sinusoid(1.0, twopi_*6/10, pi_/2, 0, 10, dashed) at Origin;
    sinusoid(0.5, twopi_*3/10,     0, 0, 10, dotted) at Origin;
```

````

%========================================================================
% RAND, RANDN
%------------------------------------------------------------------------

```{code-cell} ipython3 
:tags: ["remove-cell"]
from src.utils import *

data = r'''
#include(lib_base.ckt)
#include(lib_color.ckt)

Origin: Here 
#Grid(10, 1);

move to (0,0.5);
for x = 0 to 10  by 0.05 do { line to (x, rand()*0.25); } 
'''

_ = cm_compile('cm_0210b', data,  dpi=600)   
```

%-------------------------------------------------------------------------


````{tab-set}

```{tab-item} rand(), randn()
<img src="./src/cm_0210b.png" width="600px" class="center">
```

```{tab-item} Popis    
    rand(), randn()
```


```{tab-item} Príklad
    for x = 0 to 10  by 0.05 do { line to (x, rand()*0.25); } 
    
    stddev = 0.25
    n=100
    randn(z,n,0,stddev) 
    m = 0
    for i=1 to n-1 by 2 do { m +=1; x[m] = z[i]; y[m] = z[i+1]
        dot(at (x[m],y[m]))
    }
```

````





