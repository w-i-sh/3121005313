from test import Compare
import unittest

class test_simi(unittest.TestCase):
    def setUp(self):
        print('test start')

    def test_0(self):
        text = Compare("这是一个测试","这是一个测试")
        # 分词并获取词频向量
        tokens1,tokens2 = text.tokenize()
        vector1,vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 =text.cosine_similarity()
        self.assertAlmostEqual(similarity_1_2, 1, places=7,msg='失败！')

    def test_1(self):
        text = Compare("这是一个测试_0", "这是一个测试_0")
        # 分词并获取词频向量
        tokens1, tokens2 = text.tokenize()
        vector1, vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 = text.cosine_similarity()
        self.assertAlmostEqual(similarity_1_2, 1, places=7, msg='失败！')

    def test_2(self):
        text = Compare("这是一个简单的测试", "这是一个测试")
        # 分词并获取词频向量
        tokens1, tokens2 = text.tokenize()
        vector1, vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 = text.cosine_similarity()
        self.assertLess(similarity_1_2, 1, msg='失败！')

    def test_3(self):
        text = Compare("111", "111")
        # 分词并获取词频向量
        tokens1, tokens2 = text.tokenize()
        vector1, vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 = text.cosine_similarity()
        self.assertAlmostEqual(similarity_1_2, 1, places=7, msg='失败！')

    def test_4(self):
        text = Compare("机器学习是一个复杂的领域。", "复杂的机器学习领域有很多挑战。")
        # 分词并获取词频向量
        tokens1, tokens2 = text.tokenize()
        vector1, vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 = text.cosine_similarity()
        self.assertLess(similarity_1_2, 1, msg='失败！')

    def test_5(self):
        text = Compare("1", "复杂的机器学习领域有很多挑战。")
        # 分词并获取词频向量
        tokens1, tokens2 = text.tokenize()
        vector1, vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 = text.cosine_similarity()
        self.assertAlmostEqual(similarity_1_2, 0, places=7, msg='失败！')

    def test_6(self):
        text = Compare("猫喜欢抓老鼠。", "老鼠被猫抓住了。")
        # 分词并获取词频向量
        tokens1, tokens2 = text.tokenize()
        vector1, vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 = text.cosine_similarity()
        self.assertLess(similarity_1_2, 1, msg='失败！')

    def test_7(self):
        text = Compare("今天是晴天。明天可能会下雨。", "明天可能会下雨。今天是晴天。")
        # 分词并获取词频向量
        tokens1, tokens2 = text.tokenize()
        vector1, vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 = text.cosine_similarity()
        self.assertAlmostEqual(similarity_1_2, 1, places=7, msg='失败！')

    def test_8(self):
        text = Compare("这是一个数字", "我喜欢看小说")
        # 分词并获取词频向量
        tokens1, tokens2 = text.tokenize()
        vector1, vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 = text.cosine_similarity()
        self.assertAlmostEqual(similarity_1_2, 0, places=7, msg='失败！')

    def test_9(self):
        text = Compare("a", "a")
        # 分词并获取词频向量
        tokens1, tokens2 = text.tokenize()
        vector1, vector2 = text.get_vector()
        # 计算余弦相似性
        similarity_1_2 = text.cosine_similarity()
        self.assertAlmostEqual(similarity_1_2, 1, places=7, msg='失败！')

    def setDown(self):
        print('test end')

if __name__ == "__main__":
    # 构造测试集

    suite = unittest.TestSuite()

    suite.addTest(test_simi('test_simi'))

    # 执行测试集合

    runner = unittest.TextTestRunner()

    runner.run(suite)

