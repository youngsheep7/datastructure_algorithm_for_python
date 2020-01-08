"""
seek duplicate element in an array
"""


class Array(object):
    def __init__(self, *args):
        self.elms = args
        self.xor_val = self.xor()

    def xor(self):
        """calculate the xor result of array"""
        r = 0
        for elm in self.elms:
            r ^= elm
        return r


def main():
    array2 = Array(1, 2, 3, 4, 5, 6, 2)
    array1 = Array(1, 2, 3, 4, 5, 6)  # 构造
    r = array1.xor_val ^ array2.xor_val
    print(f"数组的重复元素{r}")


if __name__ == "__main__":
    main()
