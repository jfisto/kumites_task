class KumiteArray:
    def find_array(self, arr_first, arr_second):
        return [arr_first[i] for i in arr_second if i < len(arr_first)]

    def solve(self,word):
        import re
        return max([sum([ord(letter) - ord('a') + 1 for letter in consOnly]) for consOnly in re.split("a|e|i|o|u", word)])



if __name__ == '__main__':
    obj = KumiteArray()
    # print(obj.solve(1))
    print(obj.find_array([0, 3, 4], [2, 6]))
