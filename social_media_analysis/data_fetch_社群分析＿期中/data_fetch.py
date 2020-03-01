def fetch_data(source,name):
    new_data = dict()
    new_data_message = dict()
    new_id = list()
    only_message = list()
    only_second_message = list()
    count = 0
    with open(source,"r") as csvfile:
        file_data = csv.DictReader(csvfile)
        for row in file_data:
            if row["大類別"] == "post":
                seg_list = jieba.cut(row["post_message"])
                for words in seg_list:
                    if(words=="世大運"):
                        new_data["part"+str((count+1))]={}
                        new_data["part"+str((count+1))]["posts"+str(count+1)] = row
                        new_id.append(row['postID'])
                        count = count + 1
                        break;
    for i in range(0,count):
        if new_data["part"+str((i+1))]["posts"+str(i+1)] != "":
            posts = graph.get_connections(id=new_id[i],connection_name="comments?fields=like_count,message")
            new_data["part"+str((i+1))]["comment-part"] = {}
            for x in range(len(posts['data'])):
                new_data["part"+str((i+1))]["comment-part"]["comment"+str(x+1)] = posts['data'][x]
                only_message.append(posts['data'][x]["message"])
                second_comment = graph.get_connections(id=posts['data'][x]["id"],connection_name="comments")
                new_data["part"+str((i+1))]["comment-part"]["comment"+str(x+1)]["second_comment"] = {}
                for y in range(len(second_comment['data'])):
                    new_data["part"+str((i+1))]["comment-part"]["comment"+str(x+1)]["second_comment"]["second_comment"+str(y+1)] = second_comment['data'][y]
                    only_second_message.append(second_comment['data'][y]["message"])

    #with open(name+"_data.json","w") as f:
    #    f.write(json.dumps(new_data,ensure_ascii=False,indent=4))
    #    f.close()
    new_data_message["message"] = {};
    new_data_message["message"] = only_message;
    new_data_message["second_message"] = {}
    new_data_message["second_message"] = only_second_message
    print(new_data_message)
    with open(name+"_data_message.json","w") as f:
        f.write(json.dumps(new_data_message,ensure_ascii=False,indent=4))
        f.close()
import csv,json,jieba,facebook
from collections import OrderedDict
token="EAACEdEose0cBAJQC1TbtzbJVQrJARVwq2vhJnBlDCIRkb3PY9ZC8U1PjYTMucwiz2ZAwlBm4Gf4vrZA88t7OxO0ISoVqytdZBhg \
    am149ZBFGskvdAD4FPOuaowl2khL64lDCzdBp3l2DdI7TPPovKZCQnhYqsnTzI7hpyYcA9yahaFii8rIkiRIZAmhyDhshZAKXhpdgJFl7agZDZD"
graph = facebook.GraphAPI(access_token=token,version='2.7')
ardi_post = "../Downloads/1478518292360151_201711230246.csv"
walkwithpain_post = "../Downloads/344714869058361_201711230252.csv"
Monday_post = "../Downloads/498788970193926_201711230252.csv"
kissshoe_post = "../Downloads/823878360969684_201711230251.csv"
nolookwhilework_post= "../Downloads/920752461339263_201711230250.csv"
planetman_post = "../Downloads/194682774019921_201711230252.csv"
howfun_post = "../Downloads/572154239502200_201711230251.csv"
linchen_post = "../Downloads/621516664558773_201711230250.csv"
AGA_post = "../Downloads/118807651515245_201711230251.csv"
first_post = "阿滴英文"
second_post = "走路痛"
third_post = "星期天"
fourth_post = "啾啾鞋"
fifth_post = "上班不要看"
sixth_post = "囧星人"
seventh_post = "How Fun如何爽"
eighth_post = "林辰"
nineth_post = "蔡阿嘎"
file_set = [ardi_post,walkwithpain_post,Monday_post,
                    kissshoe_post,nolookwhilework_post,planetman_post,howfun_post,linchen_post,AGA_post]

file_name = [first_post,second_post,third_post,fourth_post,fifth_post,sixth_post,seventh_post,eighth_post,nineth_post]

for i in range(len(file_set)):
    fetch_data(file_set[i],file_name[i])
