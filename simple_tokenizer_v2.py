import re
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.token_to_id = vocab
        self.id_to_token = {i:s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.token_to_id else "<|unk|>" for item in preprocessed]
        ids = [self.token_to_id[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.id_to_token[i] for i in ids])
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text
