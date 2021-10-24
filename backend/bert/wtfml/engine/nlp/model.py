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
