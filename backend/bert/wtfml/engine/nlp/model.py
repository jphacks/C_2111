import torch
import torch.nn as nn
import torch.nn.functional as F
import transformers


class BERTBaseClassifier(nn.Module):
    def __init__(
        self,
        num_classes: int = 4,
        pretrain_model_name: str = "cl-tohoku/bert-base-japanese-whole-word-masking",
    ):
        super().__init__()
        self.bert = transformers.BertModel.from_pretrained(pretrain_model_name)
        self.bert_drop = nn.Dropout(0.3)
        self.out = nn.Linear(768, num_classes)

    def forward(self, ids, mask, token_type_ids):
        output = self.bert(ids, attention_mask=mask, token_type_ids=token_type_ids)
        bo = self.bert_drop(output.pooler_output)
        output = self.out(bo)
        return output

    def get_features(self, ids, mask, token_type_ids):
        output = self.bert(ids, attention_mask=mask, token_type_ids=token_type_ids)
        return output.pooler_output


class DistilBERTBaseClassifier(nn.Module):
    def __init__(
        self,
        num_classes: int = 4,
        pretrain_model_name: str = "bandainamco-mirai/distilbert-base-japanese",
    ):
        super().__init__()
        self.backborn= transformers.AutoModel.from_pretrained("bandainamco-mirai/distilbert-base-japanese")
        # transformers.DistilBertTokenizer.from_pretrained(pretrain_model_name)
        self.bert_drop = nn.Dropout(0.3)
        self.out = nn.Linear(768, num_classes)

    def forward(self, ids, mask): #, token_type_ids
        output = self.backborn(ids, attention_mask=mask) #, token_type_ids=token_type_ids)
        hidden_state = output[0]
        pooler = hidden_state[:, 0]
        bo = self.bert_drop(pooler)
        output = self.out(bo)
        return output


    def get_features(self, ids, mask): #, token_type_ids
        output = self.backborn(ids, attention_mask=mask) #, token_type_ids=token_type_ids)
        hidden_state = output[0]
        pooler = hidden_state[:, 0]
        return pooler

class LaboroBERTBaseClassifier(nn.Module):
    def __init__(
        self,
        num_classes: int = 4,
        pretrain_model_name: str = "laboro-ai/distilbert-base-japanese",
    ):
        super().__init__()
        self.backborn= transformers.AutoModel.from_pretrained("laboro-ai/distilbert-base-japanese")
        # transformers.DistilBertTokenizer.from_pretrained(pretrain_model_name)
        self.bert_drop = nn.Dropout(0.3)
        self.out = nn.Linear(768, num_classes)

    def forward(self, ids): # , mask): #, token_type_ids
        output = self.backborn(ids) #, attention_mask=mask) #, token_type_ids=token_type_ids)
        hidden_state = output[0]
        pooler = hidden_state[:, 0]
        bo = self.bert_drop(pooler)
        output = self.out(bo)
        return output


    def get_features(self, ids): # , mask): #, token_type_ids
        output = self.backborn(ids) #, attention_mask=mask) #, token_type_ids=token_type_ids)
        hidden_state = output[0]
        pooler = hidden_state[:, 0]
        return pooler


class TextCNNFeature(nn.Module):
    def __init__(self, embed_dim, kernel_sizes, input_channel=1, kernel_num=100):
        super().__init__()
        self.convs1 = nn.ModuleList(
            [nn.Conv2d(input_channel, kernel_num, (k, embed_dim)) for k in kernel_sizes]
        )

    def forward(self, x):
        x = x.unsqueeze(1)  # (N,Ci,W,D)
        x_list = [
            F.relu(conv(x)).squeeze(3) for conv in self.convs1
        ]  # [(N,Co,W), ...]*len(Ks)
        x_list = [
            F.max_pool1d(i, i.size(2)).squeeze(2) for i in x_list
        ]  # [(N,Co), ...]*len(Ks)
        x = torch.cat(x_list, 1)
        return x


class TextCNN(nn.Module):
    """
    text CNN model
    """

    kernel_sizes = [3, 4, 5]

    def __init__(
        self,
        class_num,
        embed_dim,
        input_channel=1,
        kernel_num=100,
        dropout_rate=0.3,
        kernel_sizes=[3, 4, 5],
    ):
        super().__init__()
        self.features = TextCNNFeature(
            embed_dim, kernel_sizes, input_channel, kernel_num
        )
        self.classifier = nn.Sequential(
            nn.Dropout(dropout_rate),
            nn.Linear(len(self.kernel_sizes) * kernel_num, class_num),
        )

    def forward(self, x):
        # x = x.unsqueeze(1)  # 64 * 1 * 144 * 300
        x = self.features(x)
        x = self.classifier(x)
        return x
