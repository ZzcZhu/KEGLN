# 环境设置 （Environment settings）：
python 3.6
torch==1.0.1
pytorch-pretrained-bert==0.6.2


# 数据集 (Datasets)：
用于训练此模型的数据集是一个真实的数据集，受医院保护，因此只能提供参考示例。（The dataset used to train this model is a real-world dataset, which is protected by the hospital, hence only a reference example can be provided.）


# 运行 (Code running)：
python run.py


# 说明（Explanation）：
    此文件夹用于存放下载好的pytorch版的BERT预训练模型。（This folder is designated for storing the downloaded PyTorch version of the BERT pre-trained model.）
    包括：（Including：）
        pytorch_model.bin  
        bert_config.json  
        vocab.txt  
    BERT预训练模型下载地址：(Download link for the BERT pre-trained model: )  
        bert_Chinese: https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese.tar.gz
        bert_English（英文数据实验需要替换为此模型（For experiments with English data, it is necessary to switch to this one））: https://huggingface.co/google-bert/bert-base-uncased

# 论文原文：
    使用此代码请引用此篇论文：（To use this code, please cite the following paper：）
    Wang, J., Li, J., Zhu, Z., Zhao, Q., Yu, Y., Yang, L., & Xu, C. (2021). Joint Extraction of Events in Chinese Electronic Medical Records. 2021 IEEE 45th Annual Computers, Software, and Applications Conference (COMPSAC), 1924-1929.
