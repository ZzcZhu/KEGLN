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
    datasets提供了训练数据样例，包括temp，temp.cites和description三个必要文件,其中temp为抽取好的医学事件数据（这些医学事件基于Medi_EE模型提取得到），temp.cites为医学事件之间的关系链接数据这些关系由Event_relation方法构建），description为实体描述数据样例，长度需要事先裁剪好。请谅解，实体描述同样是合作医院整理的宝贵资源，目前无法公开提供，但可通过百度百科、药物百科等资源中自行获取。（The datasets offer sample training data, comprising three essential files: temp, temp.cites, and description. The “temp” includes the extracted medical event data, which is obtained through the Medi_EE model. The "temp.cites" contains the relational link data between medical events, constructed using the Event_relation method. The “description” file is a sample of entity description data, which needs to be pre-truncated to an appropriate length. Please be understanding that these entity descriptions, like the rest of the valuable resources compiled by our partner hospitals, are not currently available for public dissemination. However, similar information can be independently sourced from resources such as Baidu Encyclopedia and Drug Encyclopedia.）

## 对比方法的复现代码：（The replication code for the comparative methods）
    关于文章中提到的几种对比方法，鉴于这些方法是其他作者团队的辛勤研究成果，出于对知识产权的尊重，我必须先行获得对方的同意，才能进行公开。我会积极与作者团队进行联系和协商，若获得许可，复现代码将会逐步在代码库中更新。（Regarding the comparative methods mentioned in the article, as these methods represent the hard-earned research outcomes of other author teams, out of respect for intellectual property rights, I must first obtain their consent before making them public. I will actively engage in communication and negotiation with the author teams. Should permission be granted, the replication code will be gradually updated in this code database.）


# 4 论文 (Paper)
    A knowledge-guided event-relation graph learning network for patient similarity with Chinese electronic medical records

# 补充说明（Supplementary explanation）
    由于真实数据受保护的原因，因此与其相关的内容也暂时无法提供。此代码为KEGLN模型在公开数据集上的评估代码。真实数据获得权限后，相关内容会在第一时间公开。（Due to the protected nature of the real data, related content is temporarily unavailable. This code serves as an evaluation of the KEGLN model on public datasets. Once access to the real data is granted, relevant content will be released promptly.）