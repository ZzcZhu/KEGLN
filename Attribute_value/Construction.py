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
            if nearest_value:
                attributes.append((concept, nearest_value))
                used_concepts.add(concept)

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


for idx, data in enumerate(data_list):
    parsed_data = parsed_data_list[idx]
    concepts = extract_text_from_entities(data)
    result = merge_values_and_match_concepts(parsed_data, concepts, dictionary)
    results.append(result)


output_file = "attribut_value.json"
with open("Attribute_value\\" + output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

