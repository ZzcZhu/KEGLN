from transformers import BertTokenizer, BertModel
import torch


class Embedding:
    def __init__(self, pretrained_path=r'../configs/bert-base-chinese'):
        # 加载预训练的 BERT 模型和分词器
        self.tokenizer = BertTokenizer.from_pretrained(pretrained_path)
        self.model = BertModel.from_pretrained(pretrained_path)

    def toVector(self, text):
        # 对输入文本进行分词
        inputs = self.tokenizer(text, return_tensors='pt')

        # 获取输入的ID和注意力掩码
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']

        # 禁用梯度计算，因为我们只需要推理
        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask=attention_mask)

        # 获取最后一层的隐藏状态
        last_hidden_states = outputs.last_hidden_state

        # 获取第一个词（CLS）的嵌入表示，通常用作句子的嵌入
        sentence_embedding = last_hidden_states[:, 0, :]

        # 获取所有词的嵌入表示
        # word_embeddings = last_hidden_states

        return sentence_embedding

    def similarity(self, sentence1, sentence2):
        sentence_embedding = (self.toVector(sentence1), self.toVector(sentence2))
        # 计算余弦相似度
        cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
        similarity = cos(sentence_embedding[0], sentence_embedding[-1])

        return similarity


if __name__ == '__main__':
    text = "你好吗？"
    ref = "我很好"
    path = r'../configs/bert-base-chinese'
    embedding = Embedding()
    vector = embedding.toVector(text)
    print(vector.shape)

    print(embedding.similarity(text, ref))
