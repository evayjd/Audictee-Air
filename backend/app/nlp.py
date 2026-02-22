import spacy

nlp = spacy.load("fr_core_news_sm")

def analyze_sentences(sentences):
    """
    给每个sentence添加tokens信息～
    """
    
    for sentence in sentences:
        doc=nlp(sentence["text"])
        
        tokens=[]
        for token in doc:
            if token.is_space:
                continue
            #目前只做词汇统计
            tokens.append({
                "text":token.text,
                "lemma":token.lemma_,
                "pos":token.pos_,
            })
            
        sentence["tokens"]=tokens
    return sentences