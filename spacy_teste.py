import spacy
from collections import Counter


nlp = spacy.load("pt_core_news_sm")

doc = nlp('Importante mencionar que, dentro do Processo de Recuperação Judicial 1 do agente, que tramita na Primeira Vara de Falências e Recuperações Judiciais do Tribunal de Justiça de São Paulo, foi emitida Decisão 2 , de 24 de abril de 2019, que concedeu tutela de urgência em favor do agente, impedindo que a CCEE adotasse qualquer medida em desfavor do mesmo pelo período de 5 dias. Já, em 12 de setembro de 2019, foi proferida nova decisão, que impediu a CCEE de efetuar qualquer tipo de cobrança ao agente, pelo período de seis meses. Posteriormente, em 14 de outubro de 2019, devido ao agravo de instrumento interposto pela CCEE, foi emitida nova decisão, que determinou que o fato de o agente estar em recuperação judicial não afasta o seu dever de cumprir as exigências contratuais, tais como o aporte de garantias.Importante mencionar que, dentro do Processo de Recuperação Judicial 1 do agente, que tramita na Primeira Vara de Falências e Recuperações Judiciais do Tribunal de Justiça de São Paulo, foi emitida Decisão 2 , de 24 de abril de 2019, que concedeu tutela de urgência em favor do agente, impedindo que a CCEE adotasse qualquer medida em desfavor do mesmo pelo período de 5 dias. Já, em 12 de setembro de 2019, foi proferida nova decisão, que impediu a CCEE de efetuar qualquer tipo de cobrança ao agente, pelo período de seis meses. Posteriormente, em 14 de outubro de 2019, devido ao agravo de instrumento interposto pela CCEE, foi emitida nova decisão, que determinou que o fato de o agente estar em recuperação judicial não afasta o seu dever de cumprir as exigências contratuais, tais como o aporte de garantias.')

# all tokens that arent stop words or punctuations
words = [
    token.text for token in doc
    if token.is_stop is not True
    and token.is_punct is not True
]

# noun tokens that arent stop words or punctuations
nouns = [
    token.text for token in doc if token.is_stop is not True
    and token.is_punct is not True
    and token.pos_ != "NUM"
    and token.pos_ != "PRON"
]

# five most common tokens
Word_freq = Counter(words)
common_words = Word_freq.most_common(5)
print(common_words)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(5)
print(common_nouns)
