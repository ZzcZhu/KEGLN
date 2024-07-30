# 说明（Explanation）：
这是一个用于医学文本事件抽取模型，需要根据实际需求使用特定数据先进行模型训练，输出的模型会被保存在models文件夹下，通过调用训练好的模型可以用于对新医学文本进行事件抽取。（This is a model designed for medical text event extraction, which requires pre-training with specific data based on actual needs. The trained model will be saved in the “models” folder. By invoking the pre-trained model, it can be utilized to perform event extraction on new medical texts.）
### 注意：（Note:）
预测时要以单个患者的数据作为输入。需要预测的数据仍需要保持训练数据的格式，即example.json所示的格式，但entity，trigger和arguments可以为空，这时输出预测的结果即为标注后的数据。（When making predictions, using a single patient as input.The data to be predicted must maintain the format of the training data, as shown in “example.json”. However, the fields for entity, trigger, and arguments can be left empty. In this case, the output of the prediction will be the annotated data.）

此外，data_convert.py是一个独立存在，需要预测完成后独立运行，其用于将事件抽取模型预测的结果数据，转换为可供“关系构建”（即步骤2）可读取的标准化数据格式。（Additionally, data_convert.py is an independent script that needs to be run separately after prediction is completed. It is used to convert the prediction results from the event extraction model into a standardized data format that can be read by the “relationship construction” process (i.e., step （2）).）


# 环境设置 （Environment settings）：
    python 3.6
    torch==1.0.1
    pytorch-pretrained-bert==0.6.2


# 数据集(Datasets)：
用于训练此模型的数据集及产出的模型涉及真实的电子病历数据，受医院保护，因此只能提供参考示例。（The datasets used to train this model and the output model involves the real-world EMRs, which is protected by the hospital, hence only a reference example can be provided.）


# 运行 (Code running)：
    python run.py


# 论文原文（Paper, Cite）：
Wang, J., Li, J., Zhu, Z., Zhao, Q., Yu, Y., Yang, L., & Xu, C. (2021). Joint Extraction of Events in Chinese Electronic Medical Records. 2021 IEEE 45th Annual Computers, Software, and Applications Conference (COMPSAC), 1924-1929.
