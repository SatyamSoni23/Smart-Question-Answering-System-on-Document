# Smart-Question-Answering-System-on-Document
It's Smart-Question Answering System on short as well as long documents. It can automatically find answers to matching questions directly from documents. The deep learning language model converts the questions and documents to semantic vectors to find the matching answer.

## Approches:
- Question Answering System Using Simple Split and Cosine Similarity (Naive Approach)
- Question Answering System Using Word2Vec Embedding Technique
- Question Answering System Using Glove Embedding Technique
- Question Answering System with Fine-Tuned BERT Technique
- Question Answering System Using CDQA on Multiple Pdf Files

## Challenges
- Bert is a really powerful model for tackling a question-answering problem. However, it comes up with the limitation of 512 tokens and the documents were really longer than 512 tokens. In order to handle this limitation I wrote the function "expand_split_sentences", which split and expand sentences i.e., it makes paragraphs with lesser than 512 tokens and makes data frames of that paragraph. In this, more than one data frame contains the correct answer so we will find the best answer by finding the max start score.

## Pretrained Model and Dataset Used
- word2vec
- glove
- bert-large-uncased-whole-word-masking-finetuned-squad
- bert-squad_1.1


## Reference
- https://arxiv.org/pdf/1805.08092.pdf
- https://ieeexplore.ieee.org/abstract/document/9079274
- https://arxiv.org/pdf/1707.07328.pdf
- https://arxiv.org/pdf/1810.04805.pdf
- https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf
- https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html
- https://nlp.seas.harvard.edu/2018/04/03/attention.html
- http://jalammar.github.io/illustrated-transformer/
- http://jalammar.github.io/illustrated-bert/
- https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/
- https://www.coursera.org/learn/nlp-sequence-models
- https://www.youtube.com/playlist?list=PLam9sigHPGwOBuH4_4fr-XvDbe5uneaf6

## Deployment
- ### Method Selection
![alt text](https://github.com/SatyamSoni23/Smart-Question-Answering-System-on-Document/blob/main/Screenshots/1.JPG)
- ### File Uploading
![alt text](https://github.com/SatyamSoni23/Smart-Question-Answering-System-on-Document/blob/main/Screenshots/2.JPG)
- ### Ask Question
![alt text](https://github.com/SatyamSoni23/Smart-Question-Answering-System-on-Document/blob/main/Screenshots/3.JPG)
- ### Processing Answer Using BERT
![alt text](https://github.com/SatyamSoni23/Smart-Question-Answering-System-on-Document/blob/main/Screenshots/4.JPG)
- ### Processing Answer Using Fine-tuning BERT
![alt text](https://github.com/SatyamSoni23/Smart-Question-Answering-System-on-Document/blob/main/Screenshots/5.JPG)
