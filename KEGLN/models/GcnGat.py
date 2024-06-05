import torch
import torch.nn as nn
from models.GCN import GCN
from models.GAT import GAT


class GcnGat(nn.Module):
    def __init__(self, n_layers=2, n_features=256, hidden_dim=256,
                 dropout=0.3, alpha=0.1, heads=8):
        super(GcnGat, self).__init__()

        self.gcn = GCN(n_layers=n_layers, n_features=n_features, hidden_dim=hidden_dim, dropout=dropout,
                       n_classes=n_features)
        self.gat = GAT(nfeat=n_features, nhid=hidden_dim, nclass=n_features, dropout=dropout, alpha=alpha,
                       nheads=heads)

    def forward(self, feature, adj):
        adj = adj.to_sparse()
        feature = self.gcn(feature, adj)
        adj = adj.to_dense()
        feature = self.gat(feature, adj)

        return feature, adj


if __name__ == '__main__':
    feature = torch.rand(size=(20, 256)).to('cuda')
    adj = torch.randint(0, 2, size=(20, 20), dtype=torch.float).to('cuda')

    model = GcnGat().to('cuda')
    output, _ = model(feature, adj)
    print(output.shape)
    print(output)
