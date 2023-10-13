## Задание 8

Задание предполагает использование комбинаторной библиотеки itertools.

Функции библиотеки:

> <code>product(множество, [repeat=кол_во_повторений_множества])</code>\
> Функция, возвращающая декартово произведение множеств.

> <code>combinations(множество, длина)</code>\
> Функция, возвращающая комбинации из элементов, длина которых указана во втором параметре.\
> Комбинации составляются из элементов, отсортированных лексикографически (по алфавиту).

> <code>permutations(множество, [длина_элемента])</code>\
> Функция, возвращает перестановки элементов, длина которых указана в параметре.\
> Элементы множества не повторяются. \
> Если длина не указана, то размер элементов равен размеру множества.

> <code>combinations_with_replacement(множество, длина_элемента)</code>\
> Функция похожа на обычный <code>combinations</code>, но значения в элементах повторяются. 

<br>

<table class="docutils align-default">
    <thead>
        <tr class="row-odd">
            <th class="head">Пример</th>
            <th class="head">Результат работы</th>
        </tr>
    </thead>
    <tbody>
        <tr class="row-even"><td><code><span>product('ABCD',</span> <span >repeat=2)</span></code></td>
        <td><code><span>AA</span> <span >AB</span> <span >AC</span> <span >AD</span> <span >BA</span> <span >BB</span> <span >BC</span> <span >BD</span> <span >CA</span> <span >CB</span> <span >CC</span> <span >CD</span> <span >DA</span> <span >DB</span> <span >DC</span> <span >DD</span></code></td>
        </tr>
        <tr class="row-odd"><td><code ><span >permutations('ABCD',</span> <span >2)</span></code></td>
        <td><code ><span >AB</span> <span >AC</span> <span >AD</span> <span >BA</span> <span >BC</span> <span >BD</span> <span >CA</span> <span >CB</span> <span >CD</span> <span >DA</span> <span >DB</span> <span >DC</span></code></td>
        </tr>
        <tr class="row-even"><td><code ><span >combinations('ABCD',</span> <span >2)</span></code></td>
        <td><code ><span >AB</span> <span >AC</span> <span >AD</span> <span >BC</span> <span >BD</span> <span >CD</span></code></td>
        </tr>
        <tr class="row-odd"><td><code ><span >combinations_with_replacement('ABCD',&nbsp;2)</span></code></td>
        <td><code ><span >AA</span> <span >AB</span> <span >AC</span> <span >AD</span> <span >BB</span> <span >BC</span> <span >BD</span> <span >CC</span> <span >CD</span> <span >DD</span></code></td>
        </tr>
    </tbody>
</table>

<br>

> **Пример задания**\
> Борис составляет 6-буквенные коды из букв Б, О, Р, И, С.
> Буквы Б и Р нужно обязательно использовать ровно по одному разу,
> букву С можно использовать один раз или не использовать совсем,
> буквы О и И можно использовать произвольное количество раз или не использовать совсем.
> Сколько различных кодов может составить Борис?
>
> ```python
> import itertools
> # itertools - библиотека для работы с комбинаторикой
> # product() - функция, получающая все возможные перестановки элементов длины repeat из букв, которые в неё переданы
> listString = itertools.product('БОРИС', repeat=6)
> count = 0
> for str in listString:
>     # join() - функция соединяющая массив строк в одну строку при помощи разделителя, который указан до точки
>     line = ''.join(str)
>     # count() - строковая функция, которая определяет кол-во вхождений букв или слов в строку
>     if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
>         count += 1
> print(count)
> ```
> 
> Ответ: 1440