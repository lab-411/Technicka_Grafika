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


## <font color='teal'> Knižnica *log* </font> 


```{code-cell} ipython3  
:tags: ["remove-cell"]
from src.utils import *

data = r'''
log_init

command "\sf"

define(`SPI_Master', `[
  BX: box wid 2.5 ht 7*lg_pinsep;

      lg_pin(BX.ne - (0, 1*lg_pinsep),  SCLK, Pin8, e,,0 );
      lg_pin(BX.ne - (0, 2*lg_pinsep),  MOSI, Pin7, e,,0 );
      lg_pin(BX.ne - (0, 3*lg_pinsep),  MISO, Pin6, e,,0 );
      lg_pin(BX.ne - (0, 4*lg_pinsep),  lg_bartxt(CS1), Pin5, e,,0 );
      lg_pin(BX.ne - (0, 5*lg_pinsep),  lg_bartxt(CS2), Pin4, e,,0 );
      lg_pin(BX.ne - (0, 6*lg_pinsep),  lg_bartxt(CS3), Pin3, e,,0 );

]')

define(`SPI_Slave', `[
  BX: box wid 2 ht 5*lg_pinsep;

      lg_pin(BX.nw - (0, 1*lg_pinsep),  SCLK, Pin1, w,,0);
      lg_pin(BX.nw - (0, 2*lg_pinsep),  MOSI, Pin2, w,, 0);
      lg_pin(BX.nw - (0, 3*lg_pinsep),  MISO, Pin3, w,, 0);
      lg_pin(BX.nw - (0, 4*lg_pinsep),  lg_bartxt(CS), Pin4, w,,0 );
]')

M: SPI_Master(); "SPI" at M.c +(-0.3,0) above; "Master" at M.c +(-0.3,0) below;
   line from M.Pin8 right 1.5;  DT1: dot; 
   line from M.Pin7 right 1.25; DT2: dot; 
   line <-from M.Pin6 right 1.;   DT3: dot;

   line from DT1-> right 1;
S1: SPI_Slave() with .Pin1 at last line .end; 
    "SPI" at S1.c +(0.3,0) above; "Slave" at S1.c +(0.3,0) below;
    line -> from DT2 to S1.Pin2
    line from DT3 to S1.Pin3
    line -> from M.Pin5 to S1.Pin4

    line from DT1 down_ 2.5; DT5: dot;line -> to (S1.Pin1, Here)
    right_
S2: SPI_Slave() with .Pin1 at last line .end
    "SPI" at S2.c +(0.3,0) above; "Slave" at S2.c +(0.3,0) below;
    line from DT2 to (DT2, S2.Pin2); DT6: dot;line -> to S2.Pin2
    line from DT3 to (DT3, S2.Pin3); DT7: dot;line -> to S2.Pin3

    line from DT5 down_ 2.5; ;line -> to (S1.Pin1, Here)
    right_
S3: SPI_Slave() with .Pin1 at last line .end
    "SPI" at S3.c +(0.3,0) above; "Slave" at S3.c +(0.3,0) below;
    line from DT6 to (DT6, S3.Pin2); line -> to S3.Pin2
    line from DT7 to (DT7, S3.Pin3); line -> to S3.Pin3

X:  0.3 between M.Pin4 and S2.Pin4;
    line -> from M.Pin4 to (X, M.Pin4) then to (X, S2.Pin4) then to S2.Pin4

Y:  0.2 between M.Pin3 and S3.Pin4;
    line -> from M.Pin3 to (Y, M.Pin3) then to (Y, S3.Pin4) then to S3.Pin4 
'''

_ = cm_compile('img_0208a', data,  dpi=600)   
```

```{figure} ./src/img_0208a.png
:width: 350px
:name: img_0208a

Blokové [zapojenie](./src/img_0208a.ckt) SPI rozhrania 
```
