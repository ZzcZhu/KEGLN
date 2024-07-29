# author: Zhichao Zhu

import json

def extract_text_from_entities(data):
    text_list = []
    
    for entity in data.get("entity", []):
        if 'text' in entity:
            text_list.append(entity['text'])

    return text_list

def merge_values_and_match_concepts(parsed_data, concepts, dictionary):
    
    word_list = parsed_data["word"]
    postag_list = parsed_data["postag"]
    
    merged_results = []
    i = 0

    while i < len(word_list):
        if postag_list[i] == "m" and i + 1 < len(word_list) and postag_list[i + 1] == "q":
            new_value = word_list[i] + word_list[i + 1]
            merged_results.append((i, new_value))  
            i += 2  
        elif postag_list[i] == "m":
            new_value = word_list[i]
            merged_results.append((i, new_value))
            i += 1
        else:
            i += 1

    attributes = []
    used_concepts = set()
    used_values = set()
    for concept in concepts:
        concept_index = word_list.index(concept) if concept in word_list else -1
        if concept_index != -1 and concept not in used_concepts:
           
            if concept_index + 1 < len(word_list):
                next_word = word_list[concept_index + 1]
                if next_word in dictionary:
                    attributes.append((concept, next_word))
                    used_concepts.add(concept)
                    continue
            
            nearest_value = None
            nearest_distance = float('inf')

            for idx, merged_value in merged_results:
                distance = abs(idx - concept_index)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_value = merged_value
            if nearest_value and nearest_value not in used_values:
                attributes.append((concept, nearest_value))
                used_concepts.add(concept)
                used_values.add(nearest_value)
    
    return attributes




with open("Attribute_value\input_data.json", 'r', encoding='utf-8') as f:
    data_list = json.load(f)

with open("Attribute_value\parsed_data.json", 'r', encoding='utf-8') as f:
    parsed_data_list = json.load(f)

with open('Attribute_value\dictionary.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()


dictionary = {}

for line in lines:
    line = line.strip()
    dictionary[line] = line

results = []

origin_data = []

event_type = []

for each in data_list:
    event_type.append(each["trigger"][0]["event_type"])

for idx, data in enumerate(data_list):
    parsed_data = parsed_data_list[idx]
    concepts = extract_text_from_entities(data)
    origin_data.append(concepts)
    result = merge_values_and_match_concepts(parsed_data, concepts, dictionary)
    results.append(result)

element_lists = []

for s_list, d_list in zip(origin_data, results):

    temp_list = []
    for s_item in s_list:
     
        for d_item in d_list:
            if s_item == d_item[0]:
                temp_list.append(s_item + d_item[1])
                break
        else:
            
            temp_list.append(s_item)
            
    element_lists.append(temp_list)

patient_id = "id"  # 患者实际ID，根据实际数据情况替换
label = "type"  # 患者类别信息，一般是诊断结果，0，1.0,2.0等等多种，需要根据实际情况替换
output_file = "temp"  
with open("Attribute_value\\" + output_file, "w", encoding="utf-8") as f:
    for i in range(len(element_lists)):
        j = 0  # 一个事件中最多包含20个事件元素，多裁少补
        s = str(patient_id) + "-" + str(i+1) + "\t" + str(patient_id) + "\t" + event_type[i] 
        for each in element_lists[i]:
            if j<20:
                s += "\t" + str(each)
                j+=1
            else:
                break
        while j<20:
            s += "\t" + "0"
            j += 1
        s = s + "\t" + str(label)  
        f.write(s)
        f.write("\n")

