# author: Zhichao Zhu
import torch.nn.functional as F
from models.GcnGat import GcnGat
import torch.nn as nn
import torch


class MergeModel(nn.Module):
    def __init__(self, n_layers=2, child_features=256, father_features=256, hidden_dim=256,
                 dropout=0.3, alpha=0.1, heads=8, n_classes=2):
        super(MergeModel, self).__init__()
        self.fc = nn.Linear(in_features=768, out_features=child_features)
        self.child_layer = GcnGat(n_layers=n_layers, n_features=child_features, hidden_dim=hidden_dim,
                 dropout=dropout, alpha=alpha, heads=heads)

        self.father_layer = GcnGat(n_layers=n_layers, n_features=father_features, hidden_dim=hidden_dim,
                 dropout=dropout, alpha=alpha, heads=heads)

        self.biLSTM = nn.LSTM(
            input_size=child_features,
            hidden_size=hidden_dim,
            num_layers=1,
            bidirectional=True,
            batch_first=True)   # BiLSTM

        self.classifier = nn.Linear(in_features=hidden_dim * 2, out_features=n_classes)

    def forward(self, child_feature_batch, child_adj_batch, father_adj_batch):

        batch_size, predict, feature = child_feature_batch.shape[0], [], []
        for i in range(batch_size):
            child_feature, child_adj, father_adj = child_feature_batch[i], child_adj_batch[i], father_adj_batch[i]
            child_feature = self.fc(child_feature)
            event_num = child_feature.shape[0]
            for i in range(event_num):
                child_feature[i], child_adj[i] = self.child_layer(child_feature[i], child_adj[i])

            father_feature = torch.mean(child_feature, dim=1)

            father_feature, father_adj = self.father_layer(father_feature, father_adj)
            x = father_feature.unsqueeze(0)
            x, (hn, cn) = self.biLSTM(x)

            x, _ = scaled_dot_product_attention(x, x, x)
            x = torch.mean(x, dim=1)
            feature.append(x)
            x = self.classifier(x)
            predict.append(x)

        predict = torch.stack(predict)
        feature = torch.stack(feature)

        return predict.squeeze(1), feature.squeeze(1)


def scaled_dot_product_attention(query, key, value):
    """
    计算缩放点积注意力
    query, key, value: 输入张量，形状为 (batch_size, seq_len, d_k)
    mask: 掩码张量，形状为 (batch_size, seq_len, seq_len)
    """
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    attention_weights = F.softmax(scores, dim=-1)
    output = torch.matmul(attention_weights, value)
    return output, attention_weights


if __name__ == '__main__':
    child_feature = torch.rand(size=(4, 20, 256)).to('cuda')
    child_adj = torch.randint(0, 2, size=(4, 20, 20), dtype=torch.float).to('cuda')
    father_adj = torch.rand(size=(4, 4)).to('cuda')

    model = MergeModel(father_features=256).to('cuda')
    output = model(child_feature, child_adj, father_adj)
    print(output.shape)