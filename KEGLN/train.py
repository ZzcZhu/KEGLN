# author: Zhichao Zhu 
# 2024/06/07
from torch.utils.data import DataLoader
from utils.dataload import GraphDataset
from utils.metrics import getMetrics
from utils.random_state import RandomState
from models.Merge import MergeModel
from utils.psloss import ps_loss
import torch.nn as nn
from tqdm import tqdm
import torch
import os


def train(model, epoch, train_loader, valid_loader, criterion, optimizer, device, pth_save_path, accumulation_steps,
          alpha):
    best_metrics = {'acc': 0}

    for i in range(epoch):
        model.train()
        train_loss_list, train_acc_list = [], []
        train_y_true, train_y_pred = [], []
        for count, (child_feature, child_adj, father_adj, label) in tqdm(enumerate(train_loader)):
            child_feature, child_adj, father_adj, label = child_feature.to(device), child_adj.to(device), \
                father_adj.to(device), label.to(device)
            output, feature = model(child_feature, child_adj, father_adj)
            adloss = criterion(output, label) / accumulation_steps
            psloss = ps_loss(feature, label)
            loss = adloss + alpha * psloss
            train_loss_list.append(loss.item())
            loss.backward()
            output = output.argmax(axis=1)
            train_y_pred.extend(output.cpu().numpy().tolist())
            train_y_true.extend(label.cpu().numpy().tolist())

            if (count + 1) % accumulation_steps == 0:
                optimizer.step()
                optimizer.zero_grad()

        train_loss = sum(train_loss_list) / len(train_loss_list)
        train_metrics = getMetrics(train_y_true, train_y_pred)
        train_metrics['loss'] = train_loss
        print('train | loss={:.3f} | acc={:.3f} | precision={:.3f} | recall={:.3f} | f1={:.3f}'.format(
            train_metrics['loss'], train_metrics['acc'], train_metrics['precision'],
            train_metrics['recall'], train_metrics['f1']))

        validation_metrics = validation(model, valid_loader, criterion, device)

        if validation_metrics['acc'] > best_metrics['acc']:
            torch.save(model.state_dict(), os.path.join(pth_save_path, "epoch{}_acc{:.6}.pt"
                                                        .format(i, validation_metrics['acc'])))
            best_metrics = validation_metrics

    return best_metrics


def validation(model, valid_loader, criterion, device):
    model.eval()
    validation_loss_list, validation_acc_list = [], []
    validation_y_true, validation_y_pred = [], []
    with torch.no_grad():
        for child_feature, child_adj, father_adj, label in tqdm(valid_loader):
            child_feature, child_adj, father_adj, label = child_feature.to(device), child_adj.to(device), \
                father_adj.to(device), label.to(device)
            batch_size = child_feature.shape[0]
            assert batch_size == 1
            output, feature = model(child_feature, child_adj, father_adj)
            loss = criterion(output, label)
            validation_loss_list.append(loss.item())
            output = output.argmax(axis=1)

            output = output.cpu().numpy().tolist()
            label = label.cpu().numpy().tolist()

            validation_y_pred.extend(output)
            validation_y_true.extend(label)

    validation_loss = sum(validation_loss_list) / len(validation_loss_list)
    validation_metrics = getMetrics(validation_y_true, validation_y_pred)
    validation_metrics['loss'] = validation_loss
    print('valid | loss={:.3f} | acc={:.3f} | precision={:.3f} | recall={:.3f} | f1={:.3f}'.format(
        validation_metrics['loss'], validation_metrics['acc'], validation_metrics['precision'],
        validation_metrics['recall'], validation_metrics['f1']))

    return validation_metrics


if __name__ == '__main__':
    configs = {
        'dataset_path': r'./datasets/temp',
        'bert_pretrained_path': r'./configs/bert-base-chinese',
        'device': torch.device('cuda' if torch.cuda.is_available() else 'cpu'),
        'lr': 1e-4,
        'epoch': 200,
        'batch_size': 32,
        'accumulation_steps': 2,
        'pth_save_path': r'./pths',
        'seed': 8866,
        'alpha': 1.0,       
    }

    # fixed random seed
    randomState = RandomState(seed=configs['seed'])

    # load dataset
    train_dataset = GraphDataset(data_path=configs['dataset_path'], bert_pretrained_path=configs['bert_pretrained_path'],
                                 mode='train')
    valid_dataset = GraphDataset(data_path=configs['dataset_path'], bert_pretrained_path=configs['bert_pretrained_path'],
                                 mode='valid')
    train_loader = DataLoader(dataset=train_dataset, batch_size=configs['batch_size'], shuffle=True)
    valid_loader = DataLoader(dataset=valid_dataset, batch_size=configs['batch_size'], shuffle=False)

    model = MergeModel(n_layers=2, child_features=768, father_features=768, hidden_dim=256, dropout=0.5, alpha=0.2,
                       heads=8, n_classes=2).to(configs['device'])

    # define loss function
    criterion = nn.CrossEntropyLoss()

    # define optimization
    optimizer = torch.optim.Adam(params=model.parameters(), lr=configs["lr"])

    # training
    best_metrics = train(model=model, epoch=configs['epoch'], train_loader=train_loader, valid_loader=valid_loader,
          criterion=criterion, optimizer=optimizer, device=configs['device'], pth_save_path=configs['pth_save_path'],
                         accumulation_steps=configs['accumulation_steps'], alpha=configs['alpha'])

    print('best_metrics'.center(80, '-'))
    print(best_metrics)
