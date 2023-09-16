import jieba
from collections import Counter
import math
import sys

#读取文件中的文本
def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File not found in: {file_name}")
        sys.exit(1)


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


#从控制台给出的文件路径读取文本

text1 = read_file(sys.argv[1])
text2 = read_file(sys.argv[2])

# 分词并获取词频向量
tokens1 = tokenize(text1)
tokens2 = tokenize(text2)

vector1 = get_vector(tokens1)
vector2 = get_vector(tokens2)

# 计算余弦相似性
similarity_1_2 = cosine_similarity(vector1, vector2)
print(type(similarity_1_2))

try:
    with open(sys.argv[3], 'w') as file:
        # 将 float 变量转换为字符串，并写入文件
        file.write(str(similarity_1_2))
    print(f"成功将 查重率 写入到文件中")
except Exception as e:
    print(f"写入文件时发生错误: {str(e)}")