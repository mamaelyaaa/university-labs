from time import time
from random import randint


class Sorting:
    """Методы сортировки"""

    n: int = 10000
    array = list(randint(-25000, 25000) for _ in range(n))

    def __init__(self):
        self.sorted_array = Sorting.array
        self.size = len(self.sorted_array)

    def get_sorted_arr(self):
        return f'Отсортированный массив: {self.sorted_array}'

    @staticmethod
    def counting_time(func):
        def inner(*args, **kwargs):
            start = time()
            func(*args, **kwargs)
            finish = time()

            delta = finish - start
            return f'Время выполнения алгоритма: {delta:.5f} секунд'

        return inner

    @counting_time
    def bubble_sort(self) -> None:
        count: int = 1

        while count > 0:
            count = 0
            for i in range(self.size - 1):
                if self.sorted_array[i] > self.sorted_array[i + 1]:
                    self.sorted_array[i], self.sorted_array[i + 1] = self.sorted_array[i + 1], self.sorted_array[i]
                    count += 1

    @counting_time
    def simple_sort(self) -> None:

        for i in range(self.size - 1):
            min_el = self.sorted_array.index(min(self.sorted_array[i:]))
            if self.sorted_array[i] > min_el:
                self.sorted_array[i], self.sorted_array[min_el] = self.sorted_array[min_el], self.sorted_array[i]

    @counting_time
    def comb_sort(self) -> None:

        fact: float = 1.247
        step: float = self.size - 1

        while step >= 1:
            for i in range(int(self.size - step)):
                if self.sorted_array[i] > self.sorted_array[int(i + step)]:
                    self.sorted_array[i], self.sorted_array[int(i + step)] = self.sorted_array[int(i + step)], \
                        self.sorted_array[i]

            step /= fact

    @counting_time
    def shaker_sort(self) -> None:

        p_left: int = 0
        p_right: int = self.size - 1
        flag: int = 1

        while p_left < p_right and flag:
            flag = 0

            for i in range(p_left, p_right):
                if self.sorted_array[i] > self.sorted_array[i + 1]:
                    self.sorted_array[i], self.sorted_array[i + 1] = self.sorted_array[i + 1], self.sorted_array[i]
                    flag = 1
            p_right -= 1

            for i in range(p_right, p_left, -1):
                if self.sorted_array[i] < self.sorted_array[i - 1]:
                    self.sorted_array[i], self.sorted_array[i - 1] = self.sorted_array[i - 1], self.sorted_array[i]
                    flag = 1
            p_left += 1

            if not flag:
                break
