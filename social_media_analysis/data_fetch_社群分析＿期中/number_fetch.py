def fetch_data(source,name):
    global all_count
    all_count = all_count  +1
    global all_data
    all_data["data_"+ name] = {}
    new_id = list()
    reply_num = 0
    reactions = 0
    like_num = 0
    love_num = 0
    haha_num = 0
    wow_num = 0
    sad_num = 0
    angry_num = 0
    share_num = 0
    count = 0

    with open(source,"r") as csvfile:
        file_data = csv.DictReader(csvfile)
        for row in file_data:
            if row["大類別"] == "post":
                seg_list = jieba.cut(row["post_message"])
                for words in seg_list:
                    if(words=="世大運"):
                        reply_num = reply_num + int(row["留言數"])
                        reactions = reactions + int(row["總回應數(Reactions)"])
                        like_num = like_num + int(row["like"])
                        love_num = love_num + int(row["love"])
                        haha_num = haha_num + int(row["haha"])
                        wow_num = wow_num + int(row["wow"])
                        sad_num = sad_num + int(row["sad"])
                        angry_num = angry_num + int(row["angry"])
                        share_num = share_num + int(row["分享數"])
                        new_id.append(row['postID'])
                        count = count + 1
                        break;

    all_data["data_"+ name]["留言數"] = reply_num
    all_data["data_"+ name]["回應數"] = reactions
    all_data["data_"+ name]["讚數"] = like_num
    all_data["data_"+ name]["愛心"] = love_num
    all_data["data_"+ name]["好笑"] = haha_num
    all_data["data_"+ name]["哇哦"] = wow_num
    all_data["data_"+ name]["難過"] = sad_num
    all_data["data_"+ name]["生氣"] = angry_num
    all_data["data_"+ name]["分享數"] = share_num

import csv,json,jieba,facebook
from collections import OrderedDict
token="EAACEdEose0cBADey7QQz2kZAbsNnFZBGZB8cWY5kfD2LuHu86Ncg2krF3AbL2WZClA7QTQ5UwmZBqOuHTsLrzJKYGrgJjuVNpIFDUeEs2s3JdEcJ \
    jjUWbYfZC3x4AUKVZBZAdNQMg99vcPVs9VftJuq67lVcNq05FJMxFbTXmpZBZCY6YRMOtI0GpVSkVHgeyoZA2MG6hDPXU2xkAZDZD"
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
all_data = dict()
all_count = 0
for i in range(len(file_set)):
    fetch_data(file_set[i],file_name[i])

with open("data_number.json","w") as f:
    f.write(json.dumps(all_data,ensure_ascii=False,indent=4))
    f.close()
