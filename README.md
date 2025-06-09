# Transform of the tensor products of the 1D scaling signal and the 1D wavelet

## Описание
Вычислены тензорные произведения масштабирующих векторов и вейвлет-векторов в их различных комбинациях. Результаты построены в виде 2D-картинок.

Рассмотрены вейвлет преобразования тензорных произведений. Подтвержден факт - результатом вейвлет преобразования является матрица, состоящая из нулей, за исключением одного элемента - один элемент равен единице.

Координаты  единичного элемента однозначно определяются:
1. Составом векторов в комбинации ${(V_m \otimes V_n}$, ${V_m \otimes W_n}$, ${W_m \otimes V_n}$ или ${W_m \otimes W_n)}$.
2. Номерами m,n векторов согласно таблице ниже:

|         | **m=1**  | **m=2**  |
|---------|----------|----------|
| **n=2** | m=1, n=2 | m=2, n=2 |
| **n=1** | m=1, n=1 | m=2, n=1 |

Рассмотренная задача соответствует упражнению 4.1.C из книги [1].

<img src='readme_img/fig_4_2.png' alt='Figure 4.2' style='width:70%; height:auto;'>

Результат тензорного произведения:

<img src='readme_img/tensors.png' alt='User tensors' style='width:70%; height:auto;'>

## Примечания
Результат упражнения 4.1.C из книги [1] не совпадает с картинкой в части отступов по краям. Вероятно, в [1] вставлен вырезанный фрагмент полной картинки.

## Схема преобразования
В качестве базовой принята схема преобразований из книги [1].

<img src='readme_img/f_transformed.png' alt='Alt Text' style='width:20%; height:auto;'>

Эта схема отличается от реализованной в [PyWavelets](https://pywavelets.readthedocs.io/en/latest/)

<img src='readme_img/layout.png' alt='PyWavelets data layout' style='width:60%; height:auto;'>

## Перечень основных файлов
- [pixel.ipynb](pixel.ipynb) - основной блокнот с результатами исследований.
- [tensors.py](tensors.py) - скрипт построения графиков, соответствующих Figure 4.2 упражнения 4.1.C из книги [1].
- [pixel_pywt.py](pixel_pywt.py) - скрипт реализации упражнения 4.1.C из книги [1] с использованием [PyWavelets](https://pywavelets.readthedocs.io/en/latest/)


## Пользовательские функции
- [split_matrices.py](/Functions/split_matrices.py) - расчленяет исходную матрицу симметрично на 4 составляющие cA, cH, cV, cD, в соответствии со схемой из книги [1].
- [combine_matrices.py](/Functions/combine_matrices.py) - объединяет cA, cH, cV, cD в единую матрицу в соответствии со схемой из книги [1].
- [vwHaar.py](/Functions/vwHaar.py) - определяет масштабирующие векторы и вейвлет векторы Хаара-преобразования первого уровня.
- [mtrxHaar.py](/Functions/mtrxHaar.py) - определяет масштабирующие векторы и вейвлет векторы Хаара-преобразования заданного уровня, используя результаты функции [vwHaar.py](/Functions/vwHaar.py).

## Reference
1. James S. Walker. A Primer on Wavelets and Their Scientific Applications. 2nd Edition. 2008.
2. [2D Forward and Inverse Discrete Wavelet Transform](https://pywavelets.readthedocs.io/en/latest/ref/2d-dwt-and-idwt.html)