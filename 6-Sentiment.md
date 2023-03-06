---
title: Sentiment Analysis
layout: default
nav_order: 6
---

# What is sentiment analysis?

When humans read documents, we are able to infer the emotional valence behind words and phrases. It can be a generally negative or positive sentiment, such as: "I'm having a terrible day" or "My day was fantastic". More complex emotions can also be understood, i.e., surprise: "Oh wow!". According to Silge and Robinson (2017), sentiment analysis allows one to programmatically analyse emotional sentiments within large amounts of text, quickly and without manual input or supervision. In qualitative quantitative mixed methods studies, the application of this approach within the qualitative side may prove invaluable and significantly reduce time and resources spent. 

When sentiment analysis is performed, a lexicon is used to compare and assign emotional sentiment to the text. Three general purpose lexicons are [AFINN](http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010), [bing](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html), and [nrc](http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm). However, according to Hamilton et al. (2016), the emotional sentiment of words or phrases often varies according to the domain or context. The following figure illustrates this:

![](assets/domain_lexicon_eg.png)<!-- -->
*Figure 1*. Word sentiment differences between a sports subreddit and a subreddit dedicated to female perspectives and struggles (Hamilton et al. 2016).
# Proposed Research Questions

1. Are there differences between the domain specific lexicons of various mental health subreddit groups?

2. Do the most common positive and negative words differ between each group, i.e. Dissociation, Depression, and Substance Use?

3. Among these groups, are there differences in the most common bi-grams (two word phrases) starting with the same word, such as "like" or "feel"?

4. Do the major differences in the aspect-based sentiment analysis of each group relate to differences within DSM-V criteria?

# Description of groups of subreddits
1. **Anxiety**: Anxiety, Anxietyhelp, socialanxiety, HealthAnxiety, anxietysuccess
2. **BPD** (Borderline Personality Disorder): BPD, BPDlovedones, BorderlinePDisorder, BPD4BPD, BPDParterns
3. **Depression**: SuicideWatch, depression, depression_help
4. **Dissociation**: dpdr, dpdrhelp, Dissociation, Depersonalization, derealization, DPDRecoveryStories, OSDD, anhedonia, BrainFog
5. **NPD** (Narcissistic Personality Disorder): NarcissisticAbuse, raisedbynarcissists
6. **PTSD**: CPTSD, PTSD, Ptsdrecovery
7. **Substances**: addiction, benzorecovery, Drugs, HPPD, leaves, opiates, Psychonaut, REDDITORSINRECOVERY, zoloft

# General To do

**End product:**
1. Bar charts showing top most common positive and negative words in a subreddit, words associated with a specific word, i.e. like, feel, not, with x axis as sentiment value.
2. Charts specific to each subreddit.
3. Charts comparing the use of similar words used in different subreddits.
4. Compare sentiment lexicons/dictionaries, domain specific vs AFINN vs bing vs NRC.

**Steps:**
1. Figure out and adapt [socialsent code](https://github.com/williamleif/socialsent) example.
2. Create domain specific sentiment lexicons/dictionaries for each subreddit group.
3. Perform sentiment analysis - looking at units beyond just words, sentiment of sentence.
4. Visualize sentiment analysis output with plotnine

--------------
Sentiment Analysis Based on BERT Word Vector and Hierarchical Bidirectional LSTM

https://skimai.com/fine-tuning-bert-for-sentiment-analysis/

https://ieeexplore-ieee-org.proxy.lib.sfu.ca/document/9543231/figures#figures



# Methodology:

### A. Creating lexicons

**Tools**: socialsent library

**Steps**:
1. Figure out min dataset size required.
2. Dataset preparation: split selected dataset into *training*, *validation*, and *testing* sets.

https://pub.towardsai.net/i-fine-tuned-gpt-2-on-110k-scientific-papers-heres-the-result-9933fe7c3c26

3. Using *socialsent*, run on dataset.

### B. Fine-tune pretrained models

To perform sentiment analysis on a specific dataset, fine-tune the model on that dataset by providing it with its respective lexicon produced in **Step A**.
    - DeBERTa-v3-base-absa-v1.1: https://huggingface.co/yangheng/deberta-v3-base-absa-v1.1
    - DistilBERT
    - MobileBERT

**Tools**: Hugging Face Transformers

**Steps**:
1. Set up separate environment for each pretrained model.
2. Tokenization
3. Model Initialization: load model and initialize it with pre-trained weights
4. Add Classification Head: The classification head is a neural network layer that maps the output of the last layer of DeBERTa to a fixed number of output classes.
5. Training: feed model with training set and backpropagate errors to update model parameters
6. Evaluation: Evaluate performance of model on validation set. This helps fine-tune model hyperparameters to optimize performance
7. Testing: Test fine-tuned model on testing set to evaluate performance on unseen data.

https://www.geeksforgeeks.org/fine-tuning-bert-model-for-sentiment-analysis/

### C. Aspect Modelling in Sentiment Analysis 

Aspect Modelling in Sentiment Analysis (ABSA): 

Aspect modelling is an advanced text-analysis technique that refers to the process of breaking down the text input into aspect categories and its aspect terms and then identifying the sentiment behind each aspect in the whole text input. The two key terms in this model are:
    - Sentiments: A positive or negative review about a particular aspect
    - Aspects: the category, feature, or topic that is under observation.


**Tools**: SpaCy

**Steps**:
1. Consider the input text corpus and pre-process the dataset.
2. Create Word Embeddings of the text input. (use a fine-tuned pretrained model)
3. Aspect Terms Extraction -> Aspect Categories Model 
4. Sentiment Extraction -> Sentiment Model 
5. Combine 3 and 4 to create Aspect Based Sentiment.(OUTPUT)

https://www.geeksforgeeks.org/aspect-modelling-in-sentiment-analysis/?ref=rp



Aspect Modelling in Sentiment Analysis vs Hierarchical BiDirectional LSTM?

# References

Hamilton, W. L., Clark, K., Leskovec, J., &amp; Jurafsky, D. (2016). Inducing domain-specific sentiment lexicons from unlabeled corpora. arXiv.org. Retrieved February 13, 2023, from https://arxiv.org/abs/1606.02820 

Silge, J., &amp; Robinson, D. (2017). Text mining with R: A tidy approach. O'Reilly. 
---