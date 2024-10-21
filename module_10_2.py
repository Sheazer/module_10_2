# from threading import Thread
# import requests
#
# THE_URL = 'http://binaryjazz.us/wp-json/genrenator/v1/genre'
#
# class Getter(Thread):
#     res = []
#     def __init__(self, url):
#         self.THE_URL = url
#         super().__init__()
#
#     def run(self):
#         response = requests.get(self.THE_URL)
#         Getter.res.append((response.json()))
#
#
# threads = []
# num_of_genres = 10
#
# for i in range(num_of_genres):
#     thread = Getter(THE_URL)
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# print(Getter.res)
# assert len(Getter.res) == num_of_genres


from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали!')
        enemy = 100
        x = 0
        while enemy > 0:
            x += 1
            sleep(0.3)
            enemy -= self.power
            if enemy <= 0:
                print(f'{self.name} сражается {x} дней, осталось 0 воинов."')
                print(f'{self.name} одержал победу спустя {x} дней!')
                return
            print(f'{self.name} сражается {x} дней, осталось {enemy} воинов."')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
