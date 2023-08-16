FROM python:3

WORKDIR /usr/src/app

# достаточно копирования 3х файлов (csv.py, data.tgz, requirements.txt)
COPY requirements.txt csv_sum.py data.tgz ./

#для увеличения производительности передадим выполнение команд в один RUN
#можно добавить очистку кэша apt, путем /var/lib/apt/lists его удаления уменьшается размер изображения, поскольку кэш apt не хранится в слое
#добавить аргумент -y в команду apt-get install, для исключения ручного вмешательства
#для получения актуальных версий сразу же в run добавим apt-get update

RUN pip install -r requirements.txt \
    && apt-get update \
    && apt-get install -y tar \
    && rm -rf /var/lib/apt/lists/* \ 
    && tar zxfv data.tgz
