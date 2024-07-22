# 说明（Explanation）：
    这是一个用于医学文本事件抽取模型，需要根据实际需求使用特定数据先进行模型训练，输出的模型会被保存在models文件夹下，通过调用训练好的模型可以用于对新医学文本进行事件抽取。（This is a model designed for medical text event extraction, which requires pre-training with specific data based on actual needs. The trained model will be saved in the “models” folder. By invoking the pre-trained model, it can be utilized to perform event extraction on new medical texts.）

# 环境设置 （Environment settings）：
    python 3.6
    torch==1.0.1
    pytorch-pretrained-bert==0.6.2


# 数据集 (Datasets)：
    用于训练此模型的数据集涉及真实的电子病历数据，受医院保护，因此只能提供参考示例。（The dataset used to train this model involves the real-world EMRs, which is protected by the hospital, hence only a reference example can be provided.）


# 运行 (Code running)：
    python run.py


# 论文原文（Paper）：
    使用此代码请引用此篇论文：（To use this code, please cite the following paper：）
    Wang, J., Li, J., Zhu, Z., Zhao, Q., Yu, Y., Yang, L., & Xu, C. (2021). Joint Extraction of Events in Chinese Electronic Medical Records. 2021 IEEE 45th Annual Computers, Software, and Applications Conference (COMPSAC), 1924-1929.
