# 说明 （Explanation）
基于LTP模型对句子进行句法分析，基于LTP模型输出结果可以实现“属性值”构建。（Utilizing the LTP model, syntactic analysis is conducted on sentences. The output from the LTP model facilitates the construction of “attribute-value” construction.）

LTP模型下载地址（Download link for the LTP Model）：https://ltp.ai/download.html

LTP Demo：https://ltp.ai/demo.html

### 数据介绍：（Data introduction:）
input_data.json为输入数据示例。（The “input_data.json” file serves as an example of the input data.）

parsed_data.json为LTP输出数据的示例。（The “parsed_data.json” file is an example of the output data from the LTP model.）

dictionary.txt为分类值字典，由于大量分类值由医院资源提供，因此也无法公开，仅能提供一些示例，请见谅。（The “dictionary.txt” file is a classification value dictionary. Since a large number of classification values are provided by hospital resources, it cannot be made public. Only some examples can be provided; we apologize for any inconvenience caused.）

temp是最终输出结果数据，已基本符合KEGLN训练数据格式，但是其中的患者ID以及对应的标签Label需要根据实际患者进行对应修改。（The “temp” file is the final output result, which basically conforms to the KEGLN training data format, but the patient ID and corresponding label need to be modified according to the actual patient.）

### 注意：（Note:）
input_data.json和parsed_data.json的数据需要按顺序一一对应。（ The data in “input_data.json” and “parsed_data.json” must correspond to each other in sequence.）

以单个患者病历作为输入。（Using a single patient's EMR as input.）

# 代码运行 （Code running）
    python Construction.py
    
    
