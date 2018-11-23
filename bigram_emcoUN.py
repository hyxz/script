# coding=utf-8
import json
from tqdm import tqdm

#process emnlp data
def gener_bigramNUA(inputfile):
  relation = []
  bi_list = []
  word_count_list = []
  word_count_all = {}
  with open(inputfile,'r') as rf:
    lines = rf.readlines()
    for line in tqdm(lines):
      line_item = [int(i) for i in line[:-1].strip().split(' ')]
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
  # for word_key in range(5257):
    word_count_list = []
    word_count = {}
    item_word_all = []
  same_item_dict = {}
  for items in tqdm(range(len(bi_list))):
    # word_count_list = []
    same_item = []
    # print(li[items][0],li[items + 1][0])
    if bi_list[items][0] not in same_item_dict:
      same_item.append(bi_list[items][1])
      same_item_dict[bi_list[items][0]] = same_item
    else:
      same_item_dict[bi_list[items][0]].append(bi_list[items][1])
  all_dict = {}
  for k, v in tqdm(same_item_dict.items()):
    count_fn = {}
    for item in v:
      if item not in count_fn:
        count_fn[item] = 1
      else:
        count_fn[item] += 1
    # sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
    all_dict[k] = sorted(count_fn.items(), key=lambda x: x[1], reverse=True)
  # print("coiuntfn:", all_dict)
  with open("image_cocoNUA.json","w") as wf:
    json.dump(all_dict,wf)

#process coco
def gener_bigramCONUA(inputfile):
  relation = []
  bi_list = []
  word_count_list = []
  word_count_all = {}
  with open(inputfile,'r') as rf:
    lines = rf.readlines()
    for line in tqdm(lines):
      line_item = [int(i) for i in line[:-1].strip().split(' ')]
      if len(line_item) < 37:
        line_item.insert(0,4682)
        try:
          line_item.insert(line_item.index(4681),4683)
        except:
          print("###line_item:",line_item)
          print("###line_item len:",len(line_item))
      else:
        line_item.insert(0,4682)
        line_item.insert(38,4683)
      # print("lines:",line_item)
  #   for line in lines:
  #     print(line)
  #     # word_ = word_tokenize(line)[:-1]
      for it in tqdm(range(len(line_item)-1)):
        item = []
        item.append(line_item[it])
        item.append(line_item[it + 1])
        bi_list.append(item)
  # for word_key in range(5257):
    word_count_list = []
    word_count = {}
    item_word_all = []
  same_item_dict = {}
  for items in tqdm(range(len(bi_list))):
    # word_count_list = []
    same_item = []
    # print(li[items][0],li[items + 1][0])
    if bi_list[items][0] not in same_item_dict:
      same_item.append(bi_list[items][1])
      same_item_dict[bi_list[items][0]] = same_item
    else:
      same_item_dict[bi_list[items][0]].append(bi_list[items][1])
  all_dict = {}
  for k, v in tqdm(same_item_dict.items()):
    count_fn = {}
    for item in v:
      if item not in count_fn:
        count_fn[item] = 1
      else:
        count_fn[item] += 1
    # sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
    all_dict[k] = sorted(count_fn.items(), key=lambda x: x[1], reverse=True)
  # print("coiuntfn:", all_dict)
  with open("image_cocoNUA.json","w") as wf:
    json.dump(all_dict,wf)

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

if __name__ == "__main__":
  # gener_dict("emnlp10.txt")
  # te([2358 ,5080 ,3343, 1868, 4785, 2789, 4773,2789,4773,2358,5080,3343,2789,1000,2358,4773,2789,4773,2358,5080,3343,2789,1000,2358])
  #gener_bigramNU("jiak.txt")
  #gener_bigramNUA("emnlp_news.txt")
  gener_bigramCONUA("image_coco.txt")
