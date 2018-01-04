# Image Resizer

Программа предназначена для изменения изображения согласно заданным параметрам.

 ```
 File pic_767x960.jpeg has been saved to dir/for/saving/image
 ```
# Установка

Программа требует для своей работы установленного интерпретатора Python версии 3.5.  
В программе используется сторонняя библиотека для работы с изображениями [Pillow](https://pypi.python.org/pypi/Pillow/3.3.1). 

Используйте команду pip для установки  библиотеки из файла зависимостей (или pip3 если есть конфликт с предустановленным Python 2):
```
$ pip install -r requirements.txt # В качестве альтернативы используйте pip3
```
Рекомендуется устанавливать зависимости в виртуальном окружении, используя [virtualenv](https://github.com/pypa/virtualenv), [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) или [venv](https://docs.python.org/3/library/venv.html). 

# Использование

Для просмотра вспомогаельной информации по использованию программы используйте ключ ```-h``` или ```--help```:
```
$ python3 image_resize.py -h
```
### Аргументы командной строки:
```
image_resize.py [-h] [-x WIDTH] [-y HEIGTH] [-s SCALE] [-p PATH] file
```
- <file> - Файл с исходным изображением.
- ```-h, --help``` - Вызов справки.
- ```-x, --width``` - Ширина результирующего изображения.
- ```-y, --heigth``` - Высота результирующего изображения.
- ```-s, --scale``` - Масштаб увеличения/уменьшения изображения (может быть меньше 1).
- ```-p, --path``` - Путь до директории куда следует сохранить результирующий файл.


Пример запуска в Linux(Debian), Python 3.5.2:

```
$ python image_resize.py picture.jpg -s 2
File picture_1534x1920.jpeg has been saved to dir/for/saving/image
```

# Цели проекта

Код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
