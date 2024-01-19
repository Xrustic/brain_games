### Hexlet tests and linter status:
[![Actions Status](https://github.com/Xrustic/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Xrustic/python-project-49/actions)

### Maintainability Badge
<a href="https://codeclimate.com/github/Xrustic/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/368258a69f6567c3d242/maintainability" /></a>

# Первый проект для Хекслет
Этот проект запускает определенные игры на математические знания. В нем содержаться такие игры как: Проверка на четность, калькулятор, НОД (Наибольший общий делитель), арифметическая прогрессия и "Простое ли число?".

## Технологии
Для создания данного проекта использовался Python версии 3.10. Чтобы установить последнюю версию нужно использовать команду:
```sh
sudo apt install python3
```

Так же в проекте используется pip 19 версии и выше. Чтобы установить pip нужно использовать команду:
```sh
sudo apt -y install python3-pip
```

Если необходимо обновить pip введите команду:
```sh
python3 -m pip install --upgrade --user pip
```

Ещё в проекте используется poetry 1.2.0 версии и выше. Для установки poetry необходимо ввести команду:
```sh
pipx install poetry
```

Так же вам потребуется установленная библиотека prompt. Для установки введите команду:
```sh
pip install prompt
```

## Использование
Чтобы запустить игры на вашем компьютере необходимо сначала установить все, что прописано выше, а после в командной строке написать необходимую команду для запуска игры:

Калькулятор
```sh
brain-calc
```

Проверка на четность
```sh
brain-even
```

НОД(наибольший общий делитель)
```sh
brain-gcd
```

"Простое ли число?"
```sh
brain-prime
```

Арифметическая прогрессия
```sh
brain-progression
```

### Установка и билд
После изменения файлов с играми, вы можете проверить линтером:
```sh
make lint
```

Так же необходимо пересобрать весь проект с помощью команд: 
```sh
make build

make publish

make package-install
```

### Аскинема
5 часть проекта (Проверка на чётность): <a href="https://asciinema.org/a/obHxxrgc3T9z7GS8cpLtmQBDN" target="_blank"><img src="https://asciinema.org/a/obHxxrgc3T9z7GS8cpLtmQBDN.svg" /></a>

6 часть проекта (Калькулятор): <a href="https://asciinema.org/a/xBSGXxrO6VyVGaPGLJAY7rjGg" target="_blank"><img src="https://asciinema.org/a/xBSGXxrO6VyVGaPGLJAY7rjGg.svg" /></a>

7 часть проекта (НОД): <a href="https://asciinema.org/a/J73DtlQpf76fRiEUIByLmRE6q" target="_blank"><img src="https://asciinema.org/a/J73DtlQpf76fRiEUIByLmRE6q.svg" /></a>

8 часть проекта (Арифметическая прогрессия): <a href="https://asciinema.org/a/db5smOJSP1JBBVGBvZmBSPZZS" target="_blank"><img src="https://asciinema.org/a/db5smOJSP1JBBVGBvZmBSPZZS.svg" /></a>

9 часть проекта (Простое ли число?): <a href="https://asciinema.org/a/qs1jGWqSPG3Rt9Zz75jub45bR" target="_blank"><img src="https://asciinema.org/a/qs1jGWqSPG3Rt9Zz75jub45bR.svg" /></a>

## Команда проекта
Автор:
- [Ольга Сесюнина] (https://<github.com/Xrustic>)
