class KumiteGenerate:
    # def generate_hashtag(self,string):
    #     return False if len("#"+"".join([word.capitalize() for word in string.split(" ")])) > 140 or len("#"+"".join([word.capitalize() for word in string.split(" ")])) == 1 else "#"+"".join([word.capitalize() for word in string.split(" ")])
    def generate_hashtag(self,string):
        ans = '#' + str(string.title().replace(' ', ''))
        return string and not len(ans) > 140 and ans or False

if __name__ == '__main__':
    obj = KumiteGenerate()
    print(obj.generate_hashtag("    Codewars   Codewars   "))