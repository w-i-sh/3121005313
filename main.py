import re
import jieba
from collections import Counter
import math


# 将文本分词并转化为词汇列表
def tokenize(text):
    tokens = jieba.cut(text)
    return [token for token in tokens]


# 计算词频向量
def get_vector(tokens):
    token_counts = Counter(tokens)
    return token_counts


# 计算余弦相似性
def cosine_similarity(vec1, vec2):
    dot_product = sum(vec1[token] * vec2[token] for token in vec1 if token in vec2)

    norm_vec1 = math.sqrt(sum(vec1[token] ** 2 for token in vec1))
    norm_vec2 = math.sqrt(sum(vec2[token] ** 2 for token in vec2))

    similarity = dot_product / (norm_vec1 * norm_vec2)

    return similarity


# 示例汉字文本
with open("E:\Python\PycharmProjects\personalHomework\测试文本\orig.txt","r",encoding="utf-8") as file:
    text1 = file.read()
with open("E:\Python\PycharmProjects\personalHomework\测试文本\orig_0.8_add.txt","r",encoding="utf-8") as file:
    text2 = file.read()

# 分词并获取词频向量
tokens1 = tokenize(text1)
tokens2 = tokenize(text2)

vector1 = get_vector(tokens1)
vector2 = get_vector(tokens2)

# 计算余弦相似性
similarity_1_2 = cosine_similarity(vector1, vector2)

print("两个文本的重复率是:", similarity_1_2)
