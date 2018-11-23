# coding=utf-8
import nltk
import spacy
import json

nlp = spacy.blank("en")

def word_tokenize(sent):
  doc = nlp(sent)
  return [token.text for token in doc]

def gener_dict(inputfile):
  word_to_id = {}
  with open(inputfile,"r") as rf:
    lines = rf.readlines()
    for line in lines:
      word_tok = word_tokenize(line)[:-1]
      for item in word_tok:
        if item not in word_to_id:
          word_to_id[item] = len(word_to_id)
  return word_to_id


def gener_bigram(inputfile):
  word_to_id = gener_dict(inputfile)
  relation = []
  bi_list = []
  word_count_list = []
  word_count_all = {}
  with open(inputfile,'r') as rf:
    lines = rf.readlines()
    for line in lines:
      word_ = word_tokenize(line)[:-1]
      for it in range(len(word_)-1):
        item = []
        item.append(word_[it])
        item.append(word_[it + 1])
        bi_list.append(item)
  for word_key in word_to_id:
    word_count_list = []
    word_count = {}
    item_word_all = []
    for item in bi_list:
      # word_count_list = []
      if word_key == item[0]:
        # word_count = {}
        if item[1] not in word_count:
          word_count[item[1]] = 1
        else:
          word_count[item[1]] += 1
        # item_count = []
        # item_count.append(word_count.keys())
        # item_count.append(word_count.values())
        # word_count_list.append(word_count)
        # print("word)uot{}:", word_count_list)
      else:
        pass
      # sorted(word_count.items(), key=lambda x: x[1], reverse=True)
      word_count_list.append(word_count)
      # word_count_list.append(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
      # print("word)uot{}:", word_count_list)
    # for k,v in word_count_list[0].items():
    #   kv = []
    #   kv.append(word_to_id[k])
    #   kv.append(v)
    #   item_word_all.append(kv)
    num_dict = {}
    for k, v in word_count_list[0].items():
      num_dict[word_to_id[k]] = v
    # print("{0}:", sorted(num_dict.items(), key=lambda x: x[1], reverse=True))
    # word_count_all[word_to_id[word_key]] = word_count_list[0]
    # word_count_all[word_to_id[word_key]] = item_word_all
    # word_count_all[word_to_id[word_key]] = word_count_list[0]
    word_count_all[word_to_id[word_key]] = sorted(num_dict.items() ,key=lambda x:x[1],reverse=True)
  with open("bigram_emnlptxt2.json","w") as wf:
    json.dump(word_count_all,wf)
  print("word_count[word_key]:", word_count_all)
  print("len word_to_id:",len(word_to_id))

def te(nums):
  li = []
  word_dict = {"a":0,"b":1,"c":2,"d":3}
  word_count_alls = {}
  word_count_all = {}
  word_count_all_num = {}
  for i in range(len(nums)-1):
    item = []
    item.append(nums[i])
    item.append(nums[i+1])
    li.append(item)
    # print(nums[i],nums[i+1])
  for word_key in word_dict:
    word_count_list = []
    word_count = {}
    item_list = []
    item_word_all = []
    for item in li:
      # word_count_list = []
      if word_key == item[0]:
        # word_count = {}
        if item[1] not in word_count:
          word_count[item[1]] = 1
        else:
          word_count[item[1]] += 1
        # item_count = []
        # item_count.append(word_count.keys())
        # item_count.append(word_count.values())
        # word_count_list.append(word_count)
        # print("word)uot{}:",word_count_list)
      else:
        pass
      # sorted(word_count.items(), key=lambda x: x[1], reverse=True))
      word_count_list.append(word_count)
      # word_count_list.append(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
      print("word)uot{}:", word_count_list)

    for k,v in word_count_list[0].items():
      kv = []
      kv.append(word_dict[k])
      kv.append(v)
      item_word_all.append(kv)

    # word_count_alls[word_key] = word_count_list[0]
    word_count_alls[word_key] = word_count_list[0]
    num_dict = {}
    for k,v in word_count_list[0].items():
      num_dict[word_dict[k]] = v
    print("[0]:",word_count_list[0])
    print("[0}:",sorted(word_count_list[0].items(), key=lambda x: x[1],reverse=True))
    ss = sorted(num_dict.items(),key=lambda x:x[1],reverse=True)
    print("{0}:",type(ss[0][0]))
    # sorted(dict1.items(), key=lambda x: x[1],reverse=True
    word_count_all[word_dict[word_key]] = item_word_all
    word_count_all_num[word_dict[word_key]] = sorted(num_dict.items(),key=lambda x:x[1],reverse=True)
  print("word_count[word_key]s:",word_count_alls)
  print("word_count[word_key] :",word_count_all)
  print("word_count[word_key]nums:",word_count_all_num)
  print("li",li)
if __name__ == "__main__":
  # gener_dict("emnlp10.txt")
  te(['a','b','a','c','a','d','a','b','a','d','b','d','b','a','c','a','c','b'])
  # gener_bigram("emnlp10.txt")
  # num = {"a":0,"b":1,"c":2,"d":3}
  # dict1 = {'a': 2, 'b': 3, 'c': 8, 'd': 4}
  # di ={}
  # for k,v in dict1.items():
  #   di[num[k]] = v
  # print("di:",di)
  # list1 = sorted(di.items(), key=lambda x: x[1],reverse=True)
  # list2 = sorted(dict1.items() ,key=lambda x: x[1],reverse=True)
  # # list2 = sorted(dict1.values())
  # print("list2",list1)


