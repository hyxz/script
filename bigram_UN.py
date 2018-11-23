# coding=utf-8
import json
from tqdm import tqdm

def gener_bigramNU(inputfile):
  relation = []
  bi_list = []
  word_count_list = []
  word_count_all = {}
  with open(inputfile,'r') as rf:
    lines = rf.readlines()
    for line in tqdm(lines):
      line_item = [int(i)  for i in line[:-1].strip().split(' ')]
      if len(line_item) < 51:
        line_item.insert(0,5255)
        line_item.insert(line_item.index(5254),5256)
      else:
        line_item.insert(0,5255)
        line_item.insert(52,5256) 
      # print("lines:",line_item)
  #   for line in lines:
  #     print(line)
  #     # word_ = word_tokenize(line)[:-1]
      for it in tqdm(range(len(line_item)-1)):
        item = []
        item.append(line_item[it])
        item.append(line_item[it + 1])
        bi_list.append(item)
  for word_key in tqdm(range(5257)):
    word_count_list = []
    word_count = {}
    item_word_all = []
    for item in tqdm(bi_list):
      # word_count_list = []
      if word_key == item[0]:
        # word_count = {}
        if item[1] not in word_count:
          word_count[item[1]] = 1
        else:
          word_count[item[1]] += 1
      else:
        pass
      # sorted(word_count.items(), key=lambda x: x[1], reverse=True)
      word_count_list.append(word_count)

    num_dict = {}
    for k, v in word_count_list[0].items():
      num_dict[k] = v
    word_count_all[word_key] = sorted(num_dict.items() ,key=lambda x:x[1],reverse=True)
  with open("bigram_emnlpNU.json","w") as wf:
    json.dump(word_count_all,wf)
  # print("word_count[word_key]:", word_count_all)

def load_word_to_dict(file):
  with open(file,"r") as rf:
    line = json.load(rf)
    return line

def te(nums):
  li = []
  nums.insert(0,5455)
  nums.append(5256)
  # word_dict = {"a":0,"b":1,"c":2,"d":3}
  # word_dict = load_word_to_dict("word_index_dict.json")
  word_count_alls = {}
  word_count_all = {}
  word_count_all_num = {}
  for i in range(len(nums)-1):
    item = []
    item.append(nums[i])
    item.append(nums[i+1])
    li.append(item)
    # print(nums[i],nums[i+1])
  for word_key in nums:
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
      kv.append(k)
      kv.append(v)
      item_word_all.append(kv)

    # word_count_alls[word_key] = word_count_list[0]
    word_count_alls[word_key] = word_count_list[0]
    num_dict = {}
    for k,v in word_count_list[0].items():
      num_dict[k] = v
    print("[0]:",word_count_list[0])
    print("[0}:",sorted(word_count_list[0].items(), key=lambda x: x[1],reverse=True))
    ss = sorted(num_dict.items(),key=lambda x:x[1],reverse=True)
    # print("{0}:",type(ss[0][0]))
    # sorted(dict1.items(), key=lambda x: x[1],reverse=True
    word_count_all[word_key] = item_word_all
    word_count_all_num[word_key] = sorted(num_dict.items(),key=lambda x:x[1],reverse=True)
  print("word_count[word_key]s:",word_count_alls)
  print("word_count[word_key] :",word_count_all)
  print("word_count[word_key]nums:",word_count_all_num)
  print("li",li)


if __name__ == "__main__":
  # gener_dict("emnlp10.txt")
  # te([2358 ,5080 ,3343, 1868, 4785, 2789, 4773,2789,4773,2358,5080,3343,2789,1000,2358,4773,2789,4773,2358,5080,3343,2789,1000,2358])
  gener_bigramNU("jiak.txt")
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

