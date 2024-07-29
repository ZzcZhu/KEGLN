# author: Zhichao Zhu
import json
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.util import bigrams
import math
from itertools import combinations

nltk.download('punkt')

def calculate_cpmi(corpus, word1, word2):
    tokens = word_tokenize(corpus.lower())
    
    freq_dist = FreqDist(tokens)
    
    bigram_freq_dist = FreqDist(bigrams(tokens))
    
    total_words = len(tokens)
    total_bigrams = len(list(bigrams(tokens)))
    
    freq_word1 = freq_dist[word1]
    freq_word2 = freq_dist[word2]
    
    freq_bigram = bigram_freq_dist[(word1, word2)]
    
    if freq_word1 == 0 or freq_word2 == 0 or freq_bigram == 0:
        return 0.0
    
    p_word1 = freq_word1 / total_words
    p_word2 = freq_word2 / total_words
    p_bigram = freq_bigram / total_bigrams
    
    cpmi_value = math.log2(p_bigram / (p_word1 * p_word2))
    return cpmi_value

def calculate_average_cpmi_between_sentences(sentence1, sentence2):
    tokens1 = word_tokenize(sentence1.lower())
    tokens2 = word_tokenize(sentence2.lower())
    
    all_cpmi_values = []
    
    for word1 in tokens1:
        for word2 in tokens2:
            cpmi_value = calculate_cpmi(sentence1 + " " + sentence2, word1, word2)
            all_cpmi_values.append(cpmi_value)
    
    return sum(all_cpmi_values) / len(all_cpmi_values) if all_cpmi_values else 0

def main(topk, patient_id):

    input_filename = 'Event_relation\\event_example.json'

    with open(input_filename, 'r', encoding='utf-8') as infile:
        input_data = json.load(infile)

    
    output_data = []
    event_id_counter = 1

    for item in input_data:
        event_content = [entity['text'] for entity in item['entity'] if entity['role'] != 'NONE']
        output_data.append({
            "event_id": str(f"{event_id_counter}"),
            "event_content": list(event_content)
        })
        event_id_counter += 1

    

    output_filename = 'Event_relation\\event_output.json'
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, indent=4, ensure_ascii=False)


    with open(output_filename, 'r', encoding='utf-8') as f:
        events = json.load(f)

    event_contents = {i['event_id']: ' '.join(i['event_content']) for i in events}
    
    event_ids = list(event_contents.keys())
    event_pairs = combinations(event_ids, 2)
    
    results = {}
    
    for event_id1, event_id2 in event_pairs:
        sentence1 = event_contents[event_id1]
        sentence2 = event_contents[event_id2]
        
        average_strength = calculate_average_cpmi_between_sentences(sentence1, sentence2)
        
        if event_id1 not in results:
            results[event_id1] = []
        if event_id2 not in results:
            results[event_id2] = []
        
        results[event_id1].append((event_id2, average_strength))
        results[event_id2].append((event_id1, average_strength))
    

    top_relationships = []
    

    for event_id in results:
        sorted_related_events = sorted(results[event_id], key=lambda x: x[1], reverse=True)[:topk]
        for related_event, strength in sorted_related_events:
            top_relationships.append((str(patient_id) + "-" + str(event_id), str(patient_id) + "-" + str(related_event)))
    
    print(top_relationships)

    with open('Event_relation\\temp.cites', 'w', encoding='utf-8') as f:
        for event_id1, event_id2 in top_relationships:
            f.write(event_id1 + "\t" + event_id2 + "\n")

if __name__ == "__main__":
    topk = 4  # 邻居数量
    patient_id = "id"  # 患者实际ID，根据实际数据情况替换
    main(topk, patient_id)