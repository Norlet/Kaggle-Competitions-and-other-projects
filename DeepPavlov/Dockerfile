FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY my_solution.py .

ENV PYTHONDONTWRITEBYTECODE=1

# Добавьте эту строку для указания скрипта для выполнения
CMD ["python", "my_solution.py"]