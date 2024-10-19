# 说明（Explanation）

一种适用于电子病历文本相似性计算的模型，可服务于临床诊断、病案归档等多种不同临床应用。(A model for calculating the similarity of electronic medical record (EMR) texts, applicable to various clinical applications such as clinical diagnosis and medical record archiving.)
    
### 代码执行顺序：(The order of code execution：)
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

### 一些解释：（Some explanations：）
由于我提出的KEGLN方法较为复杂，从而导致其对数据的格式和内容的要求也极为苛刻，涉及较为复杂的前期数据处理（上面提到的步骤（1）（2）（3）），还请见谅。为了保证各位同行能够快速上手，我目前更新的最新代码已尽可能地让每个独立部分产出的数据能够为下一步骤服务（详细说明已在相应的部分给出）。后期我会继续优化代码，以尽可能的把各自独立的部分衔接起来做成一个完备的整体。此外，由于步骤（2）和步骤（3）不涉及模型学习和训练过程，因此输出数据和预期结果之间可能存在差异，需要一定的人工校对。事实上，数据处理本身就不可避免的需要一定的人工参与以最小化外部因素对模型性能的影响。
（Due to the complexity of the proposed KEGLN method, it imposes stringent requirements on the format and content of the data, necessitating relatively complex preliminary data processing (as mentioned in steps (1), (2), and (3) above). I apologize for any inconvenience this may cause. To ensure that you can quickly get started, I have updated the latest version of the code to let the output from each independent part can serve the next step as much as possible (detailed explanations have been provided in the corresponding sections). I will continue to optimize the code to connect the independent parts as much as possible to form a complete whole. In addition, since steps (2) and (3) do not involve model learning and training processes, there may be differences between the output data and the expected results, requiring some manual proofreading. In fact, data processing itself inevitably requires some human involvement to minimize the impact of external factors on model performance.）

### 重要提示：（Important Note: ）
步骤（1）、（2）和（3）均建议按照以单个患者病历作为输入来逐一执行代码，因为本研究提出的KEGLN是基于两个各自独立的患者的事件图来计算相似性的，同时处理多个患者病历容易造成数据和图结构混乱。（Steps (1), (2), and (3) are recommended to be executed one by one using individual patient records as input, because the KEGLN proposed in this study calculates similarity based on two independently constructed patient event graphs. Processing multiple patient data simultaneously may lead to the confusion of the data and the graph structure.）

每个患者病历按照步骤（1），（2）和（3）处理完毕后，将步骤（2）和（3）产出的全部患者数据拼接在一起，即可得到最终KEGLN的训练数据。（After processing each patient's medical record according to steps (1), (2), and (3), concatenate all patient data produced from steps (2) and (3) to obtain the final KEGLN training data.）


# 论文（Paper）
Zhu, Zhichao, Jianqiang Li, Chun Xu, Jingchen Zou, Qing Zhao. A knowledge-guided event-relation graph learning network for patient similarity with Chinese electronic medical records. IEEE Transactions on Big Data (2024): n. pag.
