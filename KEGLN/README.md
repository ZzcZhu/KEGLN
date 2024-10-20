# 1 环境配置（Environment settings）
```shell
conda create -n test python=3.6
conda activate test
pip install -r requirements.txt
```

# 2 代码运行（Code Running）
```shell
python train.py
```

# 3 数据 （Data）
## 数据集：（Datasets）
真实数据受合作医院保护，暂无法提供，请见谅，我们在与医院积极协商，获得权限后会第一时间公开。（Real-world data is safeguarded by our collaborating hospitals and is currently not accessible; please understand. We are in active discussions with the hospitals and will disclose the data promptly once permissions are granted.）  

中文公开数据可在https://github.com/YangzlTHU/C-EMRs上公开可用。（Chinese public data is publicly available at https://github.com/YangzlTHU/C-EMRs for anyone to access and use.）  

英文公开数据MIMIC-III需要在官网（https://physionet.org/content/mimiciii/1.4/）申请。（To access the publicly available English dataset MIMIC-III, an application must be submitted through the official website at https://physionet.org/content/mimiciii/1.4/.）

## 数据样例：（Data examples）
datasets提供了训练数据样例，包括temp，temp.cites和description三个必要文件。（The datasets offer sample training data, comprising three essential files: temp, temp.cites, and description. ）

其中temp为抽取好的医学事件数据，这些医学事件基于Medi_EE模型提取得到。（The “temp” includes the extracted medical event data, which is obtained through the Medi_EE model.）

temp.cites为医学事件之间的关系链接数据，这些关系由Event_relation方法构建。（The "temp.cites" contains the relational link data between medical events, constructed using the Event_relation method.）

description为实体描述数据样例，描述的长度需要根据需求预先裁剪好。我们未在代码中设置读取长度的原因，是因为医院提供的描述质量较高，而百科全书提供的描述非常冗长且具有噪声。因此，在我们的方法中，医院提供的描述我们全部采纳，而百科全书提供的我们只取前100个词。在代码中设定长度参数容易导致医院提供的描述被切割破坏。请谅解，实体描述同样是合作医院整理的宝贵资源，目前无法公开提供，但您可通过百度百科、药物百科等资源中自行获取。（The “description” file is a sample of entity description data, where the length should be pre-trimmed according to the requirements. We do not set a length parameter in the code because the descriptions provided by hospitals are of high quality, whereas those from encyclopedias are often lengthy and noisy. Therefore, in our method, we fully utilize the descriptions provided by hospitals, while for encyclopedia entries, we only take the first 100 words. Setting a length parameter in the code could easily result in the truncation and degradation of the descriptions provided by hospitals.Please be understanding that these entity descriptions, like the rest of the valuable resources compiled by our partner hospitals, are not currently available for public dissemination. However, similar information can be independently sourced from resources such as Baidu Encyclopedia and Drug Encyclopedia.）

# 4 论文 ：(Cite)
Zhu, Zhichao, Jianqiang Li, Chun Xu, Jingchen Zou, Qing Zhao. A knowledge-guided event-relation graph learning network for patient similarity with Chinese electronic medical records. IEEE Transactions on Big Data (2024): n. pag.

# 补充说明：（Supplementary explanation）
KEGLN模型原本采用了HRR、IRDM、P、R、F1五种评估指标，但HRR和IRDM对数据的要求比较苛刻（必须具备患者的“出院日期”和“死亡日期”两个字段），公开数据并不适用。为了保证各位同行能够顺利运行程序，同时考虑到私密数据相关内容无法公开的问题，此公开代码为KEGLN模型在P、R、F1三个评估指标上的代码，对所有数据都适用（只要有类别标签即可），而且此代码足够验证我提出的KEGLN方法的有效性（私密数据的实验，我也采用了P、R、F1这三个指标进行了评估）。关于用HRR和IRDM评估的更多代码，待得私密数据获得公开授权后，我会第一时间在代码库中公开，请您见谅。（The KEGLN model originally employed five evaluation metrics: HRR, IRDM, Precision (P), Recall (R), and F1-score. However, HRR and IRDM are quite demanding in terms of data requirements (must have the patient's "discharge date" and "death date" fields), which are not available in public datasets. To ensure that you can run the program smoothly and considering the issue of private data related content not being accessible, the provided public code includes the evaluation of the KEGLN model based on P, R, and F1. This code is applicable to all datasets as long as category labels are proviede. Moreover, this code is sufficient to validate the effectiveness of the KEGLN method I propose (the experiment involving private data, I also utilized the P, R, and F1 metrics for evaluation). Regarding the additional code for evaluation using HRR and IRDM, I will make it publicly available in the code repository as soon as the private data is authorized for release. Please accept my apologies for any inconvenience caused.）
    
