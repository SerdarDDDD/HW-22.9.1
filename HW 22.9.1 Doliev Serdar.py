def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
            return False
    middle = (right + left) // 2
    if element == array[middle]:
        if array[middle - 1] < element:  # если элемент в середине,
            return False
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
    elif element == array[middle - 1]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)
array = list(map(int, input().split()))
element = int(input())
sorted(array)
left = int(array[0])
right = int(array[-1])
# запускаем алгоритм на левой и правой границе
if element < left or element > right:
    print('Числа нет в диапазоне')
print(array)
print(binary_search(array, element, left, right))

