# <font color='navy'> Katalóg </font> 
 Katalóg obsahuje najčastejšie používané prvky zapojení. 

## <font color='teal'> Pasívne prvky </font> 

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/comp_0.png
:width: 120px
```
:::

:::{grid-item}
:columns: 7

    resistor(,E);llabel(,R_1,);rlabel(,10k,)
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/comp_1.png
:width: 120px
```
:::

:::{grid-item}
:columns: 7

    resistor(,E);llabel(,R_1,);
	b_current(i);
	rarrow(u);
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/comp_2.png
:width: 120px
```
:::

:::{grid-item}
:columns: 7

    resistor(,E);variable(,A,,elen_*0.65);
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/comp_3.png
:width: 120px
```
:::

:::{grid-item}
:columns: 7

    capacitor(,,,0.55,0.15); 
	llabel(,C_1,);rlabel(,100 nF,);
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/comp_4.png
:width: 120px
```
:::

:::{grid-item}
:columns: 7

    capacitor(,K+,,0.55, 0.18); 
	llabel(,C_1,);rlabel(,10 \mu F,)
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/comp_5.png
:width: 120px
```
:::

:::{grid-item}
:columns: 7

    inductor(,L,6); 
	llabel(,L_1,);rlabel(,100 \mu H,);
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/comp_6.png
:width: 140px
```
:::

:::{grid-item}
:columns: 7

    L1:[Q: inductor(,L,6); linethick_(2); 
	line dimen_*0.7 at Q.c + (0,0.25);];          
	"$L_1$" at L1.n above;
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/comp_7.png
:width: 120px
```
:::

:::{grid-item}
:columns: 7

    TR:[Q:transformer(down_ 1.5,L,6,W,4); 
	 line from Q.S1 to (Q.S1,Q.P1);         
	 line from Q.S2 to (Q.S2,Q.P2)]; 
	 "$L_1$" at TR.w rjust; "$L_2$" at TR.e ljust;
:::
::::
## <font color='teal'> Grafické prvky </font> 

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/graph_0.png
:width: 380px
```
:::

:::{grid-item}
:columns: 7

    sinusoid(1.0, pi_*4/10,-pi_/2, 0, 10);
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/graph_1.png
:width: 150px
```
:::

:::{grid-item}
:columns: 7

    hatchbox(wid 3 ht 1.5,,dashed,angle=125 );
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/graph_2.png
:width: 150px
```
:::

:::{grid-item}
:columns: 7

    shadebox(box wid 3 ht 1.5 "text", 2);
:::
::::

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/graph_3.png
:width: 380px
```
:::

:::{grid-item}
:columns: 7

    for x = 0 to 10  by 0.05 do 
	   { line to (x, rand()*0.25); } ;
:::
::::
## <font color='teal'> Pracovná plocha </font> 

::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/space_0.png
:width: 300px
```
:::

:::{grid-item}
:columns: 7

    Grid(5,2);
:::
::::
