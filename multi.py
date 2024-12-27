from datetime import datetime # Для вывода времени в нужном формате (это было самым трудным)
from multiprocessing import Pool

# Это по заданию
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while file.readline():
            all_data.append(file.readline())

# Это мой вариант
# def read_info(name):
#     with open(name, 'r') as file:
#         file.readlines()


# Главная функция
def main():
    # Создаем список имен файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов функции
    start_time = datetime.now()  # Время начала
    for filename in filenames:
        read_info(filename)
    end_time = datetime.now()  # Время окончания
    print(f"{end_time - start_time} (линейный)")  # Выводим время выполнения

    # Многопроцессный вызов функции read_info
    start_time = datetime.now()  # Время начала
    with Pool() as pool:  # Пул процессов
        pool.map(read_info, filenames)
    end_time = datetime.now()  # Время окончания
    print(f"{end_time - start_time} (многопроцессный)")  # Выводим время выполнения

# Основной блок кода
if __name__ == '__main__':
    main()
