## Телеграм бот.

### Установка 
    
    git clone git@github.com:zdimon/tbot.git
    cd tbot
    virtualenv -p python3 venv
    . ./venv/bin/activate
    pip install -r requirements.txt
    
### Запуск демона.

    ./run.py
    
## Настройки

### Ручная

В папке source создать папку по имени бота.
В ней создать файл key где прописать ключ.

### Автоматическая

    ./install.py

## Наполнение бота.

В корне создать папку index куда положить файл message.txt.

    <message>Hello! Welcome</message>
    <button value="path_to_one_step">
        Do you want to see the catalog?
    </button>

    <button value="path_to_second_step">
       No thank you
    </button>
    
В этом файле описать сообщение и кнопки с указанием пути (value) который указывает на каталог относительно корня в который зайдет 
бот и будет там искать опять файл message.txt.

Любое изображение с именем image.png будет показано перед сообщением.


