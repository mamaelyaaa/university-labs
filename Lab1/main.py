from Lab1.sorting import Sorting


def main():
    with open('time.txt', 'w') as file:
        print(f'{Sorting().simple_sort()} (Simple sort)', file=file)
        print(f'{Sorting().bubble_sort()} (Bubble sort)', file=file)
        print(f'{Sorting().comb_sort()} (Comb sort)', file=file)
        print(f'{Sorting().shaker_sort()} (Shaker sort)', file=file)

    print(f'{Sorting().get_sorted_arr()}')


if __name__ == '__main__':
    main()
