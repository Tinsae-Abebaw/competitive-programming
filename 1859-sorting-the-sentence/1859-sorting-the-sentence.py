class Solution:
    def sortSentence(self, s: str) -> str:
        list_s = list(s)
        word = ""
        rank = 0
        count=0
        output = ""
        for p in list_s:
            if p == ' ':
                count += 1
        sentence = [0]*(count+1)
        dic = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        for i in list_s:
            if i == ' ':
                list_s.remove(i)
        for j in list_s:
            if j not in dic:
                word += j
            elif j in dic:
                rank = dic.get(j)-1
                sentence[rank] = word
                word = ''
        for m in range(0, len(sentence)):
            output += sentence[m]
            if m < len(sentence)-1:
                output += ' '
        return output