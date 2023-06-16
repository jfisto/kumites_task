class KumiteArray:
    def find_array(self, arr_first, arr_second):
        return [arr_first[i] for i in arr_second if i < len(arr_first)]


if __name__ == '__main__':
    obj = KumiteArray()
    print(obj.find_array([0, 3, 4], [2, 6]))
