# chinese-event-extraction-pytorch
一个简单的用pytorch实现中文事件抽取的代码。

# 环境
python 3.6

torch==1.0.1

pytorch-pretrained-bert==0.6.2

# 数据集
数据是私密的，只能提供示例供参考。

# 运行
运行 run.py

# 预训练语言模型
bert模型放在bert_pretain目录下，三个文件：

pytorch_model.bin

bert_config.json

vocab.txt

预训练模型下载地址：

bert_Chinese: 模型 https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese.tar.gz

词表 https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese-vocab.txt

来自[这里](https://github.com/huggingface/pytorch-transformers)

