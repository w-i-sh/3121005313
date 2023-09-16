import jieba
from collections import Counter
import math


class Compare:
    def __init__(self,text1,text2):
        self.text_1 = str(text1)
        self.text_2 = str(text2)
# 将文本分词并转化为词汇列表
    def tokenize(self):
        self.tokens_1 = jieba.cut(self.text_1)
        self.tokens_2 = jieba.cut(self.text_2)
        self.token_1 = [token for token in self.tokens_1]
        self.token_2 = [token for token in self.tokens_2]
        return self.token_1,self.token_2


# 计算词频向量
    def get_vector(self):
        self.token_counts_1 = Counter(self.token_1)
        self.token_counts_2 = Counter(self.token_2)
        return self.token_counts_1,self.token_counts_2


# 计算余弦相似性
    def cosine_similarity(self):
        dot_product = sum(self.token_counts_1[token] * self.token_counts_2[token] for token in self.token_counts_1 if token in self.token_counts_2)

        norm_vec1 = math.sqrt(sum(self.token_counts_1[token] ** 2 for token in self.token_counts_1))
        norm_vec2 = math.sqrt(sum(self.token_counts_2[token] ** 2 for token in self.token_counts_2))

        similarity = dot_product / (norm_vec1 * norm_vec2)

        return similarity
