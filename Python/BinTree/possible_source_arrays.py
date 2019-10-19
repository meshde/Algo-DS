from tests import get_bst

def func(arr, index, options, final_list):
    if (len(options) == 0):
        final_list.append(arr.copy())
        return

    for option in options:
        arr[index] = option.get_value()
        opts = options.copy()
        opts.remove(option)

        if option.has_left_child():
            opts.append(option.get_left_child())

        if option.has_right_child():
            opts.append(option.get_right_child())

        func(arr, index + 1, opts, final_list)


def get_all_source_arrays(root, count):
    final_list = []
    arr = [0] * count
    arr[0] = root.get_value()
    opts = []

    if root.has_left_child():
        opts.append(root.get_left_child())

    if root.has_right_child():
        opts.append(root.get_right_child())

    func(arr, 1, opts, final_list)
    return final_list

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        vals = [50, 20, 60, 10, 25, 70, 5, 15, 65, 80]
        root = get_bst(vals)
        final_list = get_all_source_arrays(root, len(vals))

        for ans in final_list:
            assert get_bst(ans) == root

    elif sys.argv[1] == 'time':
        import time
        import random

        for power in [5, 6, 7, 8, 9, 10, 11, 12, 13]:
            limit = 10 ** power

            arr = [random.randint(1, power) for _ in range(power)]
            root = get_bst(arr)

            start = time.process_time()
            get_all_source_arrays(root, len(arr))
            print('Time taken by ' + str(limit) + ' is ' + str(time.process_time() - start))
