# 1 配置环境
```shell
conda create -n test python=3.6
conda activate test
pip install -r requirements.txt
```

# 2 运行项目
```shell
python train.py
```

# 3 数据
## 数据集：
    私密中文数据涉及信息保护，目前无法提供。  
    公开中文数据可在https://github.com/YangzlTHU/C-EMRs上公开可用。  
    公开英文数据MIMIC-III需要在官网（https://physionet.org/content/mimiciii/1.4/）申请。（注：使用英文数据训练模型需要将bert-base-chinese替换为支持英文的版本）   

## 数据样例：  
    datasets提供了训练数据样例，即temp和temp.cites,其中temp为抽取好的医学事件数据（这些医学事件基于Medi_EE模型提取得到），temp.cites为医学事件之间的关系链接数据。  
    description为实体描述数据样例。（注：实体描述是合作医院整理的宝贵资源，目前无法公开提供。但可通过百度百科、药物百科等资源中自行获取）

# 4 论文
    A knowledge-guided event-relation graph learning network for patient similarity with Chinese electronic medical records