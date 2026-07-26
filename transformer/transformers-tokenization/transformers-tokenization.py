import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        
        self.id_to_word [0] =self.pad_token
        self.id_to_word[1]= self.unk_token
        self.id_to_word[2] = self.bos_token
        self.id_to_word[3] = self.eos_token
        self.word_to_id[self.pad_token] = 0
        self.word_to_id[self.unk_token]=1
        self.word_to_id[self.bos_token]=2
        self.word_to_id[self.eos_token]=3
        self.vocab_size = 4
        texts = [text.lower() for text in texts]
        all_words = [word for text in texts for word in text.lower().split()]
        texts= sorted(set(all_words))
        for text in texts:
            self.word_to_id[text]=self.vocab_size
            self.id_to_word[self.vocab_size]=text
            self.vocab_size+=1
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        encoded=[]
        for t in text.split():
            encoded.append(self.word_to_id.get(t.lower(),1))
        return encoded
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        string =[]
        for i in ids:
            string.append(self.id_to_word.get(i,self.unk_token))
        return " ".join(string)
        
