import string


class KumiteCryptography:
    # def keyword_cipher(a, b):
    #     return a.lower().translate(str.maketrans(ascii_lowercase, "".join(dict.fromkeys(b + ascii_lowercase))))

    def keyword_cipher(self, original_text:str, private_key:str):
        original_text, private_key = original_text.lower(), private_key.lower()
        cypher_text = ""
        private_key: str = "".join(sorted(set(private_key), key=private_key.index))
        abc = [chr(i) for i in range(97,123)]
        key = list(map(str, private_key)) + [leteral for leteral in abc if leteral not in private_key]
        for _char in original_text:
            if _char == " ":
                cypher_text = cypher_text + " "
            else:
                cypher_text = cypher_text + key[abc.index(_char)]
        return cypher_text


if __name__ == '__main__':
    obj = KumiteCryptography()
    print(obj.keyword_cipher("Test", "unBuntu"))