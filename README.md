# Transform of the tensor products of the 1D scaling signal and the 1D wavelet

## Описание
Рассматриваются тензорные произведения масштабирующих векторов и вейвлет-векторов в их различных комбинациях, а также вейвлет преобразование тензорного произведения. Подтвержден факт - результатом вейвлет преобразования является матрица, состоящая из нулей, за исключением одного элемента - он равен единице.

Координаты этого единичного элемента однозначно определяются:
1. составом векторов в комбинаци (${V_m \otimes V_n}$, ${V_m \otimes W_n}$, ${W_m \otimes V_n}$ или ${W_m \otimes W_n}$),
2. номерами m,n векторов.

|         | **m=1**  | **m=2**  |
|---------|----------|----------|
| **n=2** | m=1, n=2 | m=2, n=2 |
| **n=1** | m=1, n=1 | m=2, n=1 |

## Перечень основных файлов
- pixel.ipynb - основной блокнот с результатами исследований.
- tensors.py - скрипт построение графиков, соответствующих Figure 4.2 упражнения 4.1.C из [1].
- pixel_pywt.py - дополнительный скрипт с реализацией упражнения 4.1.C. из [1] с использованием [PyWavelets](https://pywavelets.readthedocs.io/en/latest/)

![Figure 4.2](/readme_img/fig_4_2.png)

## Пользовательские функции
- split_matrices.py
- combine_matrices.py
- mtrxHaar.py
- vwHaar.py

## Примечания
1. Отличия схем преобразования

### Схема преобразований в [1]

![f_transformed](/readme_img/f_transformed.png)

### Схема преобразований в [PyWavelets](https://pywavelets.readthedocs.io/en/latest/)

![data layout](/readme_img/layout.png)


2. Результат упражнения 4.1.C из [1] все равно не совпадает с картинкой в части отступов по краям. Вероятно, в [1] вставлен вырезанный фрагмент полной картинки.

## Reference
1. James S. Walker. A Primer on Wavelets and Their Scientific Applications. 2nd Edition. 2008.
2. [2D Forward and Inverse Discrete Wavelet Transform](https://pywavelets.readthedocs.io/en/latest/ref/2d-dwt-and-idwt.html)