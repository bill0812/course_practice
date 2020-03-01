def fetch_data(name):
    with open(name,"r") as f:
        message = json.loads(f.read())
        length_of_dict = len(message["second_message"])
        #print(message["message"])
        #print(string.punctuation)
        punctuations = '''。🤓🏻!！^___^……~，()-[]{};:'"\,<>./?@#$%^&*_~❤️😅๑・ω～♥”3😱😳😆❤😁💪🏼🤣😊😣😂💪😝😍👍👏😔01234566789'''
        for i in range(length_of_dict):
            no_punct = ""
            for char in message["second_message"][i]:
               if char not in punctuations:
                   no_punct = no_punct + char

            segment = jieba.cut(no_punct,cut_all=False)
            for x in segment:
                global read_data
                if x not in read_data:
                    read_data[x] = 1
                else:
                    count = read_data.get(x)
                    #print(x)
                    #print(count)
                    read_data[x] = count + 1

import csv,json,jieba,facebook,re
from collections import OrderedDict
token="EAACEdEose0cBAJQC1TbtzbJVQrJARVwq2vhJnBlDCIRkb3PY9ZC8U1PjYTMucwiz2ZAwlBm4Gf4vrZA88t7OxO0ISoVqytdZBhg \
    am149ZBFGskvdAD4FPOuaowl2khL64lDCzdBp3l2DdI7TPPovKZCQnhYqsnTzI7hpyYcA9yahaFii8rIkiRIZAmhyDhshZAKXhpdgJFl7agZDZD"
graph = facebook.GraphAPI(access_token=token,version='2.7')
first_post = "阿滴英文_data_message.json"
second_post = "走路痛_data_message.json"
third_post = "星期天_data_message.json"
fourth_post = "啾啾鞋_data_message.json"
fifth_post = "上班不要看_data_message.json"
sixth_post = "囧星人_data_message.json"
seventh_post = "How Fun如何爽_data_message.json"
eighth_post = "林辰_data_message.json"
nineth_post = "蔡阿嘎_data_message.json"

file_name = [first_post,second_post,third_post,fourth_post,fifth_post,sixth_post,seventh_post,eighth_post,nineth_post]
read_data = dict()
with open("data_second.json","w")as f:
    f.write(json.dumps({},ensure_ascii=False,indent=4))
    f.close()
    for i in range(9):

        fetch_data(file_name[i])

with open("data_second.json","w") as f:
    for key, value in read_data.copy().items():
        if int(value) < 5:
            del read_data[key]
    print(read_data)
    f.write(json.dumps(read_data,ensure_ascii=False,indent=4))
    f.close()
