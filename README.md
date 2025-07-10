# mini-wikipedia

Консольный клиент для быстрого поиска статей в Википедии прямо из терминала. Весит всего **1 КБ** и работает без графического интерфейса.

## 📦 Установка

```bash
pkg update -y && pkg install -y git python && git clone https://github.com/d1ezz9/mini-wikipedia.git && cd mini-wikipedia && pip install requests && echo '#!/bin/bash
cd ~/mini-wikipedia
python mini-wikipedia.py' > mini-wiki && chmod +x mini-wiki && echo 'alias mini-wiki="~/mini-wikipedia/mini-wiki"' >> ~/.bashrc && source ~/.bashrc && echo -e "\n\033[1;32mГотово! Теперь используйте \033[1;33mmini-wiki\033[1;32m для запуска.\033[0m"
```

*требуется python:*

```bash
pkg install python
```

## 🚀 Использование

После установки просто запустите команду:
```bash
mini-wiki
```

### Пример работы:
```text
> Python

Найдено:
1. Python
2. Python (programming language)
3. Pythonidae

№: 2

Python (programming language)
==================================================
Python — высокоуровневый язык программирования общего назначения...
```

## 🔧 Особенности
- Поиск по русской Википедии (можно модифицировать для других языков)
- Вывод краткого содержания статьи
- Простой интерфейс с нумерацией результатов
- Работает даже на слабых устройствах

## ⚙️ Технические детали
- Использует официальный [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)
- Зависимости: `requests`.
- Вес основного кода: **22 строки**
