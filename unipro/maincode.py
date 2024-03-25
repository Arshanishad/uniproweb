
import re, math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from unipro.dbconnectionnew  import *
ps = PorterStemmer()

def cb(qus):
    qus=qus.lower()
    WORD = re.compile(r'\w+')
    from collections import Counter
    def text_to_vector(text):
        words = WORD.findall(text)
        return Counter(words)

    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    text1 = sr(qus.lower())

    vector1 = text_to_vector(text1)

    res="select * from project where status='accepted'"
    sall=selectall(res)
    print("s--" ,sall)
    res = []
    pid = []
    for d in sall:

        text2 = sr(str(d['description']).lower())
        vector2 = text_to_vector(text2)
        cosine = get_cosine(vector1, vector2)
        print("eeeeeeeee",cosine)
        if cosine>.3:
            pid.append(str(d['p_id']))
            # return "0"
    print("projectid",pid)
    return pid
    # return "1"




def sr(txt):
     stop_words = set(stopwords.words('english'))

     word_tokens = word_tokenize(txt)


     filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
     filtered_sentence1=[]
     for i in filtered_sentence:
         filtered_sentence1.append(ps.stem(i))

     return ' '.join(filtered_sentence1)




















# print(cb("Crimes are a common social problem affecting"))


