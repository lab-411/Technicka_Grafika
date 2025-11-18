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

    sinusoid(amplitude, frequency, phase, tmin, tmax, linetype)


```{code-cell} ipython3 
:tags: ["remove-cell"]
import os
from cm.utils import *
cwd = os.getcwd()
data = r'''
include(`''' + cwd + '/cm/base.ckt' + r'''')

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

_ = cm_compile('./img/cm_035', data,  dpi=600 )   
```

```{figure} ./img/cm_035.png
:width: 600px
:name: cm_035

Makro sinusoid()
```

    rand()
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]
import os
from cm.utils import *
cwd = os.getcwd()
data = r'''
include(`''' + cwd + '/cm/base.ckt' + r'''')

Origin: Here 
Grid(10, 1);

move to (0,0.5);
for x = 0 to 10  by 0.05 do { line to (x, rand()*0.2 + 0.4); } 
'''

_ = cm_compile('./img/cm_036', data,  dpi=600)   
```


```{figure} ./img/cm_036.png
:width: 600px
:name: cm_036

Makro rand()
```

    shadebox(box attributes, shade width)
    
    
```{code-cell} ipython3 
:tags: ["remove-cell"]
import os
from cm.utils import *
cwd = os.getcwd()
data = r'''
include(`''' + cwd + '/cm/base.ckt' + r'''')

Origin: Here 
Grid(5, 3);

move to (0,0);
shadebox(B:box wid 3 ht 1 with .sw at (1,1), 2) 
"text" at B.c;
'''

_ = cm_compile('./img/cm_037', data, dpi=600)   
```


```{figure} ./img/cm_037.png
:width: 300px
:name: cm_037

Makro shadebox()
```

    hatchbox()


```{code-cell} ipython3 
:tags: ["remove-cell"]
import os
from cm.utils import *
cwd = os.getcwd()
data = r'''
include(`''' + cwd + '/cm/base.ckt' + r'''')

Origin: Here 
Grid(5, 3);

move to (1,1.5);
linethick_(0.8);
hatchbox(wid 3 ht 2, ,dashed,angle=125 ); 
'''

_ = cm_compile('./img/cm_038', data,  dpi=600)   
```


```{figure} ./img/cm_038.png
:width: 300px
:name: cm_038

Makro hatchbox()
```
