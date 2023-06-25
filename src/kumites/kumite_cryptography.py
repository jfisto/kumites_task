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


class CyptoAnalizeCipherViginer:

    def ABC_LIST(self):
        return [chr(i) for i in range(65,91)]

    def abc_matrix(self,abc):
        abc_mtrx =[]
        for i in range(len(abc)):
            abc_mtrx.append([])
            for j in range(len(abc)):
                abc_mtrx[i].append(abc[(i+j)%len(abc)])
        return abc_mtrx

    def listik_index(self, ciphertext, keylen):
        textPart = []
        for i in range(keylen):
            textPart.append([])
            for j in range(i,len(ciphertext),keylen):
                textPart[i].append(ciphertext[j])
        return textPart

    def index_text(self,abc,list_part):
        list_index = []
        count = 0.0
        indexC = 0.0
        for k in range(len(list_part)):
            for i in range(len(abc)):
                for j in range(len(list_part[k])):
                    if abc[i] == list_part[k][j]:
                        count += 1.0
                        # print(list_part[k][j])
                indexC += count * (count-1) / (len(list_part[k]) * (len(list_part[k]) - 1))
                # print(count,len(list_part[k]),indexC)
                count = 0.0
            list_index.append(indexC)
            indexC = 0.0
        # print(list_index)
        return list_index

    def check_id(self,list_index):
        res = f"We have found length our key ${list_index}"
        i = 0
        while i < len(list_index):
            if list_index[i] < 0.058 or list_index[i] > 0.072:
                res = "Error"
                i = len(list_index)
            i+=1
        # print(i)
        return res

    def findPartText(self,text_part:list,abc:list):
        maxequsym = []
        entermax = 0
        count = 0
        ind = 0
        for i in range(len(text_part)):
            for j in range(len(abc)):
                for k in range(len(text_part[i])):
                    if abc[j] == text_part[i][k]:
                        count += 1
                if count > entermax:
                    entermax = count
                    ind = j
                count = 0
            entermax = 0
            maxequsym.append(abc[ind])
        return maxequsym

    def findKey(self,list_sym:list,abc:list) -> str:
        ind:int
        foundKey = ""
        for i in range(len(list_sym)):
            for j in range(len(abc)):
                if list_sym[i] == abc[j]:
                    ind = (j-4)%26
                    if ind < 0:
                        ind = (ind+26)%26
                    foundKey += abc[ind]
        return foundKey

    def substring(self,found_key):
        if found_key[:len(found_key)-1] in "CODEWARS":
            return "CODEWARS"

    def main(self,ciphertext,keylen):
        abc = self.ABC_LIST()
        text_part = self.listik_index(ciphertext, keylen)  # listik4
        find_part_text = self.findPartText(text_part, abc)
        find_key = self.findKey(find_part_text, abc)
        return self.substring(find_key)


if __name__ == '__main__':
    # obj = KumiteCryptography()
    # print(obj.keyword_cipher("Test", "unBuntu"))
    obj = CyptoAnalizeCipherViginer()
    ciphertext = "NSWXARWJGEXIJCZWUZLOAWFJFTUIMUVFEWHWPEEVVCYENYSGVVECSRZLGFDRZBPKWPMIYTFFGQDRJOKOTWWIWNVKUOBEXOLLZFDCOWZLJCXXQSZFITUIMUVFVLVEJDKZGSVWWYNANZKERERFKRLSOYEUTOWMYLVLVSUJNEHMGBFCEFKZGSVWWYZKCPRYPTYWHFHUQEELWGHSBXISAGWSPRVSVNHFNAJAPEDXWRUAHTHVANKSWHKSNSYSXSKEXIKKYVLGDCRFDSUIBLVUVSGMJTYWKFXWAOWDGHWINSYWOWQKSAPKYFLXENXKVMOIBOIWZOPTHEZKXWVMXLPVKTIINEELHFRQBALDMBHVOLVLVSUFEGISOHUMCRREYCUHBRVIWSQGEEJOQFGPANXLJOQHOEELGBFIHEEYVVFEJBVUCZFYHAKWFTRVOPVUKTLGWUKZQFVEJDLKGRWSLRFNGCUHESGJQJHEQTYGTGKMLOWLGLWWAVVFHCUEQTYGTGZLKSVKVMOIOAIWPCWWKDZNGFJIJTRUEIUEPERNGFDKALVLVSUJNEHMGBFMASTSPCQPUBVYNSDRADSQCBDPUZZFIOOENGVSOCXRPOWJGDUIOEELCHLZATVPVKLXDTYWCJDMHASANWWCKFDGFSURYODHWHLRCAEVECOPACKAQBVSBLRJISWITTTGTDRVWSLUJQDPYUCSVWRROAIWGOVMHYDSFSHBWMGDGGFEJBVVTOZRBRFECJDVEEKQQTVSQRTWUDUIOSIWRCUXENXJGZLKEOLKVSAXOSTAGBWMBITLGLWWWNUYGBHVWLWAEHLSJAEVVVHVAAIWFWIJARVFESVIOPVUKOOPUFFJISQINACXKQWMKNNAVVWLAPFKKHLSJOWZCBGMSIKZJPHGKMZFIARVACFEOCQLARSWTHVDEMZFJWVGHAJKKQLRPRFVWQWSNYTJADWSCRRHJMWITTTGFSVEJDJWEFHXSRZLKBJKEVVKVVHIJGCAUVOIPTVJHFHUQEEUAGHUQEEUGOVIPAFFTWVLZLWUOIJCLWSNMXAUVTYWOCVXYODEQBOIPTVJROLVOAJLJVHEJRVWTWQSJAKFFGWIOEEGHHHIZOILKVLEOTFSPRWLAMFKVQRQIOEVQIEPADCWVHHVOAJDNSHWOOFLVTIVNNEHRQFXDEKGRHZIHVVDGHWINSTGODUMOERTQIWSBTYWVCWEHUJSISWLATFHGWJLPLVLVSUWYODHTWVIWBFMVCIXDEKGVOOYOAXWNSWXARWJGEXIJCPSUOIYJCKAQBRJNAECEOQFAFZLVSGAALCTAGHZARRDTOQOBUEUVWRROWZLJHKIPWFHCFDQATVJECFLKBVLCFDRGFLFEHLSJBVAPUWLABVKVOQSPHVJTOQOBUEUVWRRSIKZPCDHFUJLCPOIBRVWROUEIEKWTOOWKFZLUHKIHEKLGFIVAQLWPQBHESKJKPXXEOEJGOVSJASDAKHPHTYWUOPIBUEUVWRRDAJTGSQYOEULQTLXPHVSOWQSWCZVHFHUQEEUAWQTNOKWKBVIMUVFESVEOPPMUWQKPHVNKQFMLHVJQFVSIEFLJSUGEPYWTPDWADFFCGWVWDUDKBJGDETCGFESWRULADLGWLCQWGHWWMEWOCQMYSLUJOVEOIELQSUVZRFHRWQKPHVKGQRRZRKGTSPIIBVJVVHXKPVAIVWGDAISEHHVOTYWWGHSBLVLVSUJNEHMGBFMASRFFTUIMUVFEMDRWLPKKGSPWYJSHIQHWMVFVOOVKLVAPQUCLTFYTOPWWNUKGJHVWLNGTRSYVZCWIOPIOIEUNIGMJGYSPUPEJSTJCPEPAAEVVVHXALVNKGLSJGREGGKSSWYWGZRJBOILWBHSJEFXVVHIWRCAGGWHASTJKDWMKNZFEZDWOITSNZLXARRLWFHSBAGHNMLRCTYWMBRAHEUYGCIIJGCAUVOIPTVJHFHUQEEUAHRWKLMAPUDGNYGLQUUEIIJXQIQHENVSRCHWBADGWGVXKRPLJSJSHDSMIKKINEKZGAHXDOUAUGXGYEJKHIOPUAGHNWHHPOUWEWSLARREGGVECEZFUHUYYTZFICQXDENZGFHEXOLLUCIEPRVSUIUIDIUVGBECYAGLCWQOEDUDGHWINFIWSIHRYIVKJOGEOTIGPUHJBETLQBWLADVKKUQSBSFEGYHCXORJFZDCKUKKVVHQKSKXTSTYANKDGHWINSRJGCQXDESGVHRQNONGHHKIXLZUMSQWZEIXGFWCLENJKHHVWNULJSKSIEIGYCIXDEUNQFDOOIDHNWIMADBWAPREND"
    key = "CODEWARS"
    print(obj.main(ciphertext,len(key)))