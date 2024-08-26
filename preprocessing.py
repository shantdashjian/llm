import re
from SimpleTokenizerV1 import SimpleTokenizerV1

with open('the-verdict.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item for item in preprocessed if item.strip()]

all_tokens = sorted(set(preprocessed))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

vocab = {token:integer for integer, token in enumerate(all_tokens)}

print(len(vocab.items()))

tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know,", Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)

text = tokenizer.decode(ids)
print(text)
