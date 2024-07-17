# 说明（Explanation）
    一种适用于电子病历文本相似性计算的模型，可服务于临床诊断、病案归档等多种不同临床应用。(A model for calculating the similarity of electronic medical record (EMR) texts, applicable to various clinical applications such as clinical diagnosis and medical record archiving.)
    
    代码执行顺序：(The order of code execution：)
        （1）Medi_EE（事件抽取）
        （2）Event_relation（事件关系构建）
        （3）Attribute_value（属性值构建）
        （4）KEGLN（KEGLN模型训练）
    其中（1）、（2）和（3）为数据准备阶段（即预处理），独立于核心方法（4）之外。如果您的数据已经符合（4）KEGLN模型的训练数据标准，（1）、（2）、（3）步骤可以忽略。
        (1)  Medi_EE (Event extraction)
        (2)  Event_Relation (Event relation construction)
        (3)  Attribute_value (Attribute value construction)
        (4)  KEGLN (KEGLN model training)
    Among them, (1), (2), and (3) constitute the data preparation phase (i.e., preprocessing), which is independent of the core method (4). If your data already meets the training data standards for the KEGLN model, steps (1), (2), and (3) can be omitted.

# 论文（Paper）
    A knowledge-guided event-relation graph learning network for patient similarity with Chinese electronic medical records