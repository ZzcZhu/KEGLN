import torch


def dis(p1, p2):
    return torch.norm(p2 - p1)


def ps_loss(feature, label, l=torch.tensor(0.1, requires_grad=True)):
    batch_size, total = feature.shape[0], torch.tensor(0.0, requires_grad=True)
    for i in range(batch_size):
        for j in range(i+1, batch_size):
            p1, p2 = feature[i], feature[j]
            y = 1.0 if label[i] == label[j] else 0.0
            tt = dis(p1, p2)
            value = (y * dis(p1, p2)) / 2 + (torch.max(torch.tensor(0), l-dis(p1, p2)) ** 2) / 2
            total = total + value
    return total


