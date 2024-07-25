
import json, re

def remove_annotations(text):
    # 使用正则表达式匹配并删除标注
    cleaned_text = re.sub(r' B-[A-Z]-[\u4e00-\u9fa5]+| I-[A-Z]-[\u4e00-\u9fa5]+| NONE', '', text)
    return cleaned_text.strip()

def convert_to_jso(lines):
    sentence = ''.join([line.split('\t')[0] for line in lines])
    sentence = remove_annotations(sentence)
    print(sentence)
    print("----------")
    entities = []
    triggers = []
    arguments = []
    
    entity = {'text': '', 'start': -1, 'end': -1, 'role': ''}
    trigger = {'text': '', 'start': -1, 'end': -1, 'event_type': ''}
    print(lines)
    for i, line in enumerate(lines):
        word, tag1, tag2 = line.split('\t')
        if tag1.startswith('B-T-'):
            if trigger['text']:
                triggers.append(trigger)
            trigger = {'text': word, 'start': i, 'end': i, 'event_type': tag1[4:]}
        elif tag1.startswith('I-T-'):
            trigger['text'] += word
            trigger['end'] = i
        
        if tag2.startswith('B-E-'):
            if entity['text']:
                entities.append(entity)
                arguments.append({**entity, 'entity_type': entity['role']})
            entity = {'text': word, 'start': i, 'end': i, 'role': tag2[4:]}
        elif tag2.startswith('I-E-'):
            entity['text'] += word
            entity['end'] = i
    
    if trigger['text']:
        triggers.append(trigger)
    if entity['text']:
        entities.append(entity)
        arguments.append({**entity, 'entity_type': entity['role']})
    
    return {
        'sentence': sentence,
        'entity': entities,
        'trigger': triggers,
        'arguments': arguments
    }
    

def convert_to_json(data):
    sentences = data.split('[CLS]\tNONE\tNONE')
    #print(sentences)
    results = []
    
    for sentence in sentences:
        if sentence.strip():
            lines = sentence.strip().split('\n')
            result = convert_to_jso(lines)
            results.append(result)
    
    return json.dumps(results, ensure_ascii=False, indent=4)


# Read prediction document
"""
file_path = "your_file_path" # 预测结果数据文件路径, 一般位于resule_data中
with open(file_path, "r", encoding="utf-8") as f:
    S = f.readlines()
"""

# Data Examples
S = """[CLS]	NONE	NONE
患	NONE	NONE
者	NONE	NONE
突	NONE	NONE
然	NONE	NONE
出	B-T-症状	B-T-症状
现	I-T-症状	I-T-症状
腹	B-E-症状	B-E-症状
痛	I-E-症状	I-E-症状
、	NONE	NONE
恶	B-E-症状	B-E-症状
心	I-E-症状	I-E-症状
、	NONE	NONE
呕	B-E-症状	B-E-症状
吐	I-E-症状	I-E-症状
、	NONE	NONE
腹	B-E-症状	B-E-症状
泻	I-E-症状	I-E-症状
。	NONE	NONE

[CLS]	NONE	NONE
监	B-T-检查	B-T-检查
测	I-T-检查	I-T-检查
：	NONE	NONE
呼	B-E-检查	B-E-检查
吸	I-E-检查	I-E-检查
4	NONE	NONE
3	NONE	NONE
次	NONE	NONE
/	NONE	NONE
分	NONE	NONE
，	NONE	NONE
血	B-E-检查	B-E-检查
氧	I-E-检查	I-E-检查
饱	I-E-检查	I-E-检查
和	I-E-检查	I-E-检查
度	I-E-检查	I-E-检查
6	NONE	NONE
5	NONE	NONE
%	NONE	NONE
。	NONE	NONE"""

D = convert_to_json(S)
print(D)
with open("output_data", "w", encoding="utf-8") as f:
    json.dump(D, f, ensure_ascii=False, indent=4)
