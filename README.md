># Проект "homework_13_2"
___
>## Содержание
- [Описание проекта](#описание-проекта-)
- [Требования к окружению](#требования-к-окружению-)
- [Установка проекта](#установка-проекта--)
- [Установка зависимостей из `requirements.txt`](#установка-зависимостей-из-requirementstxt--)
- [Запуск программы `main.py` в корне проекта](#запуск-функций-в-файле-mainpy-в-корне-проекта--)
- [Запуск функций в файле `main_demo.py` в корне проекта](#запуск-функций-в-файле-mainpy-в-корне-проекта--)
- [Тестирование](#тестирование-)
- [JSON-файл](#json-файл--)
- [CSV- и XLSX-файлы](#csv--и-xlsx-файлы--)
- [Логгирование](#логгирование--)


___
- [Пример работы функций в модуле `masks.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-maskspy--p)
  - [Функция `get_mask_card_number`](#функция-get_mask_card_number)
  - [Функция `get_mask_account`](#функция-get_mask_account)
- [Пример работы функций в модуле `widget.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-widgetpy--p)
  - [Функция `mask_account_card`](#функция-mask_account_card)
  - [Функция `get_date`](#функция-get_date)
- [Пример работы функций в модуле `processing.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-processingpy--p)
  - [Функция `filter_by_state`](#функция-filter_by_state)
  - [Функция `sort_by_date`](#функция-sort_by_date)
- [Пример работы функций в модуле `generators.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-generatorspy--p)
  - [Функция `filter_by_currency`](#функция-filter_by_currency)
  - [Функция `transaction_descriptions`](#функция-transaction_descriptions)
  - [Функция `card_number_generator`](#функция-card_number_generator)
- [Пример работы функций в модуле `decorators.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-decoratorspy--p)
  - [Функция декоратор `log`](#функция-декоратор-log)
- [JSON-файл. Пример работы функций в модулях `utils` и `external_api`:](#p-stylecolorsteelblue-json-файл-пример-работы-функций-в-модулях-utils-и-external_api--p)
  - [Функция `read_json_file`](#функция-read_json_file)
  - [Функция `api_convert_currency`](#функция-api_convert_currency)
- [CSV- и XLSX-файлы. Пример работы функций в модуле `finance_reader.py`:](#csv--и-xlsx-файлы-пример-работы-функций-в-модуле-finance_readerpy--)
  - [Функция `read_transactions_from_csv`](#функция-read_transactions_from_csv)
  - [Функция `read_transactions_from_excel`](#функция-read_transactions_from_excel)
- [Пример работы функции в модуле `search_and_count.py`](#пример-работы-функций-в-модуле-search_and_countpy--)
  - [Функция `search_operations_by_description`](#функция-search_operations_by_description)
  - [Функция `count_operations_by_category`](#функция-count_operations_by_category)
>___




## Описание проекта [⮭](#содержание)

Проект "homework_13_2" реализованный в модуле `main.py` является заврешающей работой над виджетом банковских операций клиента, 
с применением функционала, который уже был реализован в предыдущих проектах:

`homework_9_1`, `homework_9_2`, `homework_10_1`, `homework_10_2`, `homework_11_1`, `homework_11_2`, `homework_12_1`, 
`homework_12_2`, `homework_13_1`. 

В качестве входных данных для многих функций используются данные, полученные из JSON-файла, CSV- и XLSX-файлов.


<details><summary>**program preview**
</summary>

```bash
Привет! Добро пожаловать в программу работы с банковскими транзакциями.

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
>>> 3

Для обработки выбран XLSX-файл.

Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

>>> CANCELED

Операции отфильтрованы по статусу "CANCELED"

...
...
...
```
</details>




___

## Требования к окружению [⮭](#содержание)

- Версия Python: 
```
Python 3.8+
```
- Версия Pycharm:
```
pycharm-community-2024.2.2
 ```

___

## Установка проекта [⮭](#содержание) 

1. Клонируйте репозиторий:
```bash
git clone git@github.com:viktorbarabash85/homework_10_1.git
```
2. Перейти в директорию проекта:
```bash
 cd homework_11_2
```
3. (Если требуется) Активируйте виртуальное окружение:
```bash
source .venv/bin/activate  # или .venv\Scripts\activate для Windows
```

___

## Установка зависимостей из `requirements.txt` [⮭](#содержание) 
```bash
pip install -r requirements.txt
```
___

##  Запуск программы в файле `main.py` в корне проекта [⮭](#содержание) 
В командной строке выполните команду:
```bash
poetry run python .\main.py
```


___

##  Запуск функций в файле `main_demo.py` в корне проекта [⮭](#содержание) 
В командной строке выполните команду:
```bash
poetry run python .\main_demo.py
```
___

## Тестирование [⮭](#содержание)

Тесты написаны ко всем функциям проекта в модулях: `test_masks.py`, `test_widjet.py`, `test_processing.py`,
`test_generators.py`, `test_decorators.py`, `conftest.py`, `test_external_api.py`, `test_utils.py`, 
`test_finance_reader.py`, `test_search_operations_by_description`, `test_count_operations_by_category` и `test_main.py`.  

Все тесты расположены в папке `tests\`.

Для их запуска необходимо установить `pytest`, выполнив команду:
```bash
# Установка через Poetry
poetry add --group dev pytest
```
Проект покрыт тестами на `100%`.
Запустите тестирование выполнив команду:
```bash
pytest
# или
pytest --cov
```
В репозитории есть папка `html.cov` с отчетом покрытия тестами в формате `index.html`
```bash
# Создание отчета покрытия программы тестами в формате `index.html`
pytest --cov=src --cov-report=html
```

___

## JSON-файл [⮭](#содержание) 
<details><summary>  Описание обработки JSON-файла:
 </summary>

1. Файл с банковскими операциями размещен в директории `data` в корне проекта.
2. Создан модуль `utils` в пакете `src`.
3. Реализована функция чтения JSON-файла в модуле `utils`.
4. Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента.
5. Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях.
6. Если JSON-файл пустой, содержит не-список или не найден, возвращается пустой список.
</details>


___

## CSV- и XLSX-файлы [⮭](#содержание) 
<details><summary>  Описание обработки CSV- и XLSX-файлов:
 </summary>

1. Файлы  `transactions.csv` и `transactions_excel.xlsx` размещены в директории `data` в корне проекта.
2. Создан модуль `finance_reader.py` в пакете `src`.
3. Реализована функция чтения CSV- и XLSX-файла в модуле `finance_reader.py`.
4. Функция чтения CSV- и XLSX-файла принимает путь к файлу JSON в качестве аргумента.
5. Функция чтения CSV- и XLSX-файла возвращает список словарей с данными финансовых операций.
6. .
</details>












___

## Логгирование [⮭](#содержание)  
<details><summary>  Описание логгирования:
 </summary>

1. Созданы логеры для перечисленных модулей: 
- `masks`
- `utils`
2. Реализована запись логов в файл. Логи записываться в папку `logs` в корне проекта. 
Файлы логов имеют расширение `.log`.
3. Формат записи лога в файл включает:
- `метку времени`, 
- `название модуля`, 
- `уровень серьезности`
- `сообщение, описывающее событие или ошибку, которые произошли`.
4. Лог перезаписываться при каждом запуске приложения.
</details>



___
> ___
___


## Пример работы функций в модуле `masks.py`: [⮭](#содержание)  

___
### Функция `get_mask_card_number`
<details><summary> Пример работы функции: </summary>

```bash
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
```
</details>

___
### Функция `get_mask_account`
<details><summary> Пример работы функции: </summary>

```bash
73654108430135874305  # входной аргумент
**4305  # выход функции
```
</details>

___

## Пример работы функций в модуле `widget.py`: [⮭](#содержание) 

___
### Функция `mask_account_card`
<details><summary> Пример работы функции: </summary>

```bash
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```
</details>

<details><summary> Примеры входных данных для проверки функции: </summary>

```bash
Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305
```
</details>

___
### Функция `get_date`
<details><summary> Пример работы функции: </summary>

```bash
# Пример для карты
"2024-03-11T02:26:18.671407"  # входной аргумент
"11.03.2024"  # выход функции в формате "ДД.ММ.ГГГГ"
```
</details>








___

##  Пример работы функций в модуле `processing.py`: [⮭](#содержание)  

___

### Функция `filter_by_state`
<details><summary> Пример работы функции: </summary>

В модуле `processing.py` функция [filter_by_state](#функция-filter_by_state), которая принимает список словарей 
и опционально значение для ключа 
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению.

В том же модуле функция [sort_by_date](#функция-sort_by_date), которая принимает список словарей и необязательный 
параметр, задающий порядок 
сортировки (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате (date).


```bash
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
</details>

<details><summary> Пример входных данных для проверки функции: </summary>

```bash
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
</details>


___

### Функция `sort_by_date`
<details><summary> Пример работы функции: </summary>

```bash
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
</details>

<details><summary> Пример входных данных для проверки функции </summary>

```bash
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
</details>

___

## Пример работы функций в модуле `generators.py`: [⮭](#содержание) 

___

### Функция `filter_by_currency`
<details><summary> Пример использования функции: </summary>

```bash
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
</details>

___

### Функция `transaction_descriptions`
<details><summary> Пример использования функции: </summary>

```bash
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
</details>


___

<details><summary> Пример входных данных для проверки функций 
filter_by_currency и transaction_descriptions: </summary>

```bash
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
```
</details>

___

### Функция `card_number_generator`
<details><summary> Пример использования функции: </summary>

```bash
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```
</details>

___

## Пример работы функций в модуле `decorators.py`: [⮭](#содержание) 

___

### Функция декоратор `log`
<details><summary> Описание декоратора: </summary>

Декоратор `log` автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
Декоратор принимает необязательный аргумент `filename`, который определяет, куда будут записываться логи 
(в файл или в консоль):

- Если `filename` задан, логи записываются в указанный файл.
- Если `filename` не задан, логи выводятся в консоль.

Логирование включает:
- Имя функции и результат выполнения при успешной операции.
- Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
</details>

<details><summary> Пример использования декоратора: </summary>

```bash
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
```
Ожидаемый вывод в лог-файл `mylog.txt` при успешном выполнении:
```bash
my_function ok
```
Ожидаемый вывод при ошибке:
```bash
my_function error: тип ошибки. Inputs: (1, 2), {}
```
Где `тип ошибки` заменяется на текст ошибки.

</details>


##  JSON-файл. Пример работы функций в модулях `utils` и `external_api`: [⮭](#содержание)  

___

### Функция `read_json_file`
<details><summary> Описание функции: </summary>

- Функцию размещена в модуле `utils`.
- Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. 
- Если файл пустой, содержит не список или не найден, функция возвращает пустой список. 
- Файл с данными о финансовых транзациях помещается в `operations.json` в директорию `data/` в корне проекта.

 Ссылка на файл: [operations.json](https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view).
</details>

### Функция `api_convert_currency`
<details><summary> Описание функции: </summary>

- Функция-конвертация размещена в модуле `external_api`.
- Функция принимает на вход транзакцию и возвращает сумму транзакции (`amount`) в `рублях`, тип данных — 
`float`. 
- Если транзакция была в `USD` или `EUR`, происходит обращение к внешнему API для получения текущего курса 
валют и конвертации суммы операции в рубли. 
- Для конвертации валюты применяется `Exchange Rates Data API`:
https://apilayer.com/exchangerates_data-api.
</details>

___


##  CSV- и XLSX-файлы. Пример работы функций в модуле `finance_reader.py`: [⮭](#содержание)  

___
Скачайте файлы [transactions.csv](https://github.com/skypro-008/transactions/blob/main/transactions.csv) 
и [transactions_excel.xlsx](https://github.com/skypro-008/transactions/blob/main/transactions_excel.xlsx) 
для работы над задачами и разместите их в папку `data` в корне проекта (если их там еще нет).

Пример использования

```python
csv_file_path = 'data/transactions.csv'
excel_file_path = 'data/transactions_excel.xlsx'
print(read_transactions_from_csv(csv_file_path, nrows=2))
print(read_transactions_from_excel(excel_file_path, nrows=2))
```
или
```python
csv_file_path = read_transactions_from_csv('data/transactions.csv')
excel_file_path = read_transactions_from_excel('data/transactions_excel.xlsx')
```

### Функция `read_transactions_from_csv`
<details><summary> Описание функции: </summary>

- Читает транзакции из файла CSV
- Параметры:
  - `file_path` (str): Путь к файлу CSV, который необходимо прочитать.
  - `nrows` (int, optional): Количество строк для чтения из файла. Если не указано, читаются все строки.
  - `delimiter` (str, optional): Символ, используемый для разделения значений в CSV файлелч (по умоанию запятая).
- Возвращает: 
  - Список словарей, где каждый словарь представляет собой строку данных из файла. 
  - Если файл пуст или не содержит данных, возвращает пустой список.
- Исключения:
  - `FileNotFoundError`: Выбрасывается, если указанный файл не найден.
  - `Exception`: Выбрасывается для других ошибок, связанных с чтением файла.
 </details>

### Функция `read_transactions_from_excel`
<details><summary> Описание функции: </summary>

- Читает транзакции из файла Excel.
- Параметры:
  - `file_path` (str): Путь к файлу Excel, который необходимо прочитать.
  - `nrows` (int, optional): Количество строк для чтения из файла. Если не указано, читаются все строки.
- Возвращает:
  - Список словарей, где каждый словарь представляет собой строку данных из файла. 
  - Если файл пуст, возвращает пустой список.
- Исключения:
  - `FileNotFoundError`: Выбрасывается, если указанный файл не найден.
  - `Exception`: Выбрасывается для других ошибок, связанных с чтением файла.
</details>



___


## Пример работы функций в модуле `search_and_count.py`: [⮭](#содержание)  

___
### Функция `search_operations_by_description`
<details><summary> Пример работы функции: </summary>

Функция для поиска операций по описанию с использованием регулярных выражений.

**:param operations:** Список словарей с данными о банковских операциях.

**:param search_term:** Строка для поиска в описании операций.

**:return:** Список словарей из категорий, у которых в описании есть введенное слово или строка.

```bash
# входой аргумент
search_operations_by_description(
    [
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Закрытие вклада"},
        {"description": "Открытие вклада"},
        ], "перевод"))     

# выход функции
[
{'description': 'Перевод с карты на карту'}, 
{'description': 'Перевод с карты на карту'}, 
{'description': 'Перевод организации'}, 
{'description': 'Перевод организации'}, 
{'description': 'Перевод со счета на счет'}
]
```
</details>

___
### Функция `count_operations_by_category`
<details><summary> Пример работы функции: </summary>

Функция для подсчета количества операций по категориям.

**:param operations:** Список словарей с данными о банковских операциях.

**:param category_count:** Словарь для подсчета транзакций по описанию (по умолчанию None).

**:return:** Словарь, где ключи — это названия категорий, а значения — количество операций в каждой категории.


```bash
# входной аргумент
(count_operations_by_category(
    [
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Закрытие вклада"},
        {"description": "Открытие вклада"},
        ], ))
        
# выход функции
{'Перевод с карты на карту': 2,
'Перевод организации': 2, 
'Перевод со счета на счет': 1, 
'Закрытие вклада': 1, 
'Открытие вклада': 1}

```
</details>

___


