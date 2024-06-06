import torch
from torch.utils.data import Dataset
from utils.embedding import Embedding
import scipy.sparse as sp
import numpy as np
import os


class GraphDataset(Dataset):
    def __init__(self, data_path, bert_pretrained_path, mode='train', ratio=0.8):
        self.data_path = data_path
        self.mode = mode
        self.ratio = ratio
        self.idx_features_labels = np.genfromtxt(data_path, dtype=np.dtype(str), encoding='utf-8')
        self.bv = Embedding(bert_pretrained_path)  # Bert Vector
        self.desc_vector ,self.desc_info = self.description()
        self.cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
        self.child_adj, self.child_features, self.labels = self.build_child_graph()
        self.father_adj = self.build_father_graph()
        self.data = [self.child_features, self.child_adj, self.father_adj, self.labels]

        assert self.child_adj.shape[0] == self.father_adj.shape[0]
        split = int(self.child_adj.shape[0] * ratio)

        for i in range(len(self.data)):
            if mode == 'train':
                self.data[i] = self.data[i][:split]
            else:
                self.data[i] = self.data[i][split:]

    def description(self):
        desc_vector = []
        with open(os.path.join(os.path.dirname(self.data_path), 'description'), 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                desc_vector.append(self.bv.toVector(line))

        return desc_vector, lines

    def similarityCalculate(self, sentence):
        max_similarity, result = 0, ''
        sentence_vector = self.bv.toVector(sentence)
        for vector in self.desc_vector:
            ans = self.cos(sentence_vector, vector)
            if max_similarity < ans:
                max_similarity, result = ans, vector
        return sentence_vector[0] + result[0]
    
    # 构建元素关系图
    def build_child_graph(self):
        name_map = dict()
        labels = []
        for item in self.idx_features_labels:
            if item[1] not in name_map:
                name_map[item[1]] = []
                labels.append(int(float(item[-1])))
            name_map[item[1]].append(list(item[3:-1]))
        name_map = dict(sorted(name_map.items()))

        size = len(name_map['10002013'][0])
        edges = np.array([[i, j] for i in range(size) for j in range(size)])

        child_features, child_adj = [], []
        for key, value in name_map.items():
            temp_features, temp_adj = [], []
            for sentence in value:
                word2vec = []
                for word in sentence:
                    word2vec.append(list(self.similarityCalculate(word)))
                word2vec = np.array(word2vec)
                features = sp.csr_matrix(word2vec, dtype=np.float32)
                temp_features.append(features.toarray())
                temp_adj.append(sp.coo_matrix((np.ones(edges.shape[0]), (edges[:, 0], edges[:, 1])),
                                              shape=(size, size), dtype=np.float32).toarray())  # 构建邻接矩阵
            child_features.append(temp_features)
            child_adj.append(temp_adj)

        child_features = np.array(child_features)
        child_adj = np.array(child_adj)

        return child_adj, child_features, labels
    
    # 构建事件关系图
    def build_father_graph(self):
        infos = self.idx_features_labels[:, 0:2]
        infos_map = dict()
        for info in infos:
            event, body = info[0], info[-1]
            if body not in infos_map:
                infos_map[body] = []
            infos_map[body].append(event)

        for k in infos_map.keys():
            infos_map[k] = sorted(infos_map[k])

        infos_map = dict(sorted(infos_map.items()))

        rev_map = dict()
        for idx, (k, v) in enumerate(infos_map.items()):
            for event in v:
                rev_map[event] = idx

        edges_unordered = np.genfromtxt(os.path.join(os.path.dirname(self.data_path), 'temp.cites'),
                                        dtype=np.str_)

        connection = dict()
        for edges in edges_unordered:
            idx = rev_map[edges[0]]
            if idx not in connection:
                connection[idx] = []
            connection[idx].append([int(item.split('-')[-1])-1 for item in edges])

        father_adj, size = [], 4
        for idx, (k, v) in enumerate(connection.items()):
            edges = np.array(connection[idx])
            temp = sp.coo_matrix((np.ones(edges.shape[0]), (edges[:, 0], edges[:, 1])),
                                       shape=(size, size), dtype=np.float32)
            father_adj.append(temp.toarray())

        father_adj = np.array(father_adj)
        return father_adj

    def __len__(self):
        return self.data[0].shape[0]

    def __getitem__(self, idx):
        # a, b, c = self.child_adj[idx], self.child_features[idx], self.father_adj[idx]
        c_f, c_a, f_a = self.data[0][idx], self.data[1][idx], self.data[2][idx]
        label = self.data[-1][idx]

        # a (3, 4, 20, 20)
        # b (3, 4, 20, 768)
        # c (3, 4, 4)
        return torch.tensor(c_f), torch.tensor(c_a), torch.tensor(f_a), torch.tensor(label)


if __name__ == '__main__':
   dataset = GraphDataset(data_path=r'../datasets/temp', bert_pretrained_path=r'../configs/bert-base-chinese',
                          mode='train')
   print(len(dataset))
   print(dataset[0])