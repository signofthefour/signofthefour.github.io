---
layout: post
title:  "Overview of Attention in Deep Learning"
author: sotf
categories: [ deeplearning, speech processing ]
image: assets/images/attentionindeeplearning/6.png
beforetoc: "When reading about the tacotron, I get very confused about attention. What is it, what does it do, and how does it work?"
toc: true
---

Attention is considered a strong and popular technique of Deep Learning in recent times. It is based on a sense of focus on basic information that is important as we learn and access new information.

This seemingly simple idea is of great help in developing not only the field of Natural Language Processing (NLP) but also issues such as image processing, speech processing, medical advice...

Before going into content, I write this article for the purpose of learning and sharing learning. I am not an author and the knowledge I have referenced may not be correct. Please review carefully and read other documents, if possible please share with me.

## History

Attention was first proposed in the NLP field and continues to be researched and developed today:

* Seq2Seq, or RNN Encoder-Decoder [Cho et al. (2014)](http://emnlp2014.org/papers/pdf/EMNLP2014179.pdf), [Sutskever et al. (2014)](https://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf)
* Alignment models [Bahdanau et al. (2015)](https://arxiv.org/pdf/1409.0473.pdf), [Luong et al. (2015)](https://arxiv.org/pdf/1508.04025.pdf)
* Visual attention [Xu et al. (2015)](http://proceedings.mlr.press/v37/xuc15.pdf)
* Hierarchical attention [Yang et al. (2016)](https://www.aclweb.org/anthology/N16-1174.pdf)
* Transformer [Vaswani et al. (2017](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)

## Sequence to sequence (Seq2Seq) architecture for machine translation

Sequence to sequence (Seq2Seq) is a two-part deep learning architecture capable of associating a sequence with a sequence. Every day, we can encounter information in a lot of sequences: sound, text ... About a simple example for Seq2Seq: linking a piece of text with a sound segment (Text to Speech), Audio with text (Automatic Speech Recognition), from an English sentence to a Vietnamese sentence (Translate, Seq2Seq is recommended for this problem at first)

[Cho et al. (2014)](http://emnlp2014.org/papers/pdf/EMNLP2014179.pdf) and [Sutskever et al. (2014)](https://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf) has independently proposed a deep learning network consisting of two main parts: encoder and decoder. An encoder reads into a string with variable length, the decoder returns a string of results: (English phrase) - (encoder) -> (decoder) -> (Vietnamese phrase). Each encoder and decoder has its own RNN network with separate LSTM or GRU.
![alt text]({{base.url}}/assets/images/attentionindeeplearning/1.png "Image source: Sutskever et al. (2014)")

## Align & Translate

The possible problem with Seq2Seq is that a sequence of information cannot be fully captured by a limit vector. For example, if an RNN receives too long a sentence, it is likely that it will not be able to transmit the information until the end due to the problem of Gradient Exploding.
![alt text]({{base.url}}/assets/images/attentionindeeplearning/2.png "Image source: Bahdanau et al. (2015)")
[Bahdanau et al. (2015)](https://arxiv.org/pdf/1409.0473.pdf) proposed to use context vector solution to align input and output files. Context vector allows the characteristics of all hidden states to be captured in encoder cells, aligning them on the output. This allows the model to "focus" on important parts of the input and learn the complex relationship between input and target ouput. See also [Luong et al. (2015)](https://arxiv.org/pdf/1508.04025.pdf) about aligning techniques between input and output.

## Visual attentionn

[Xu et al. (2015)](http://proceedings.mlr.press/v37/xuc15.pdf) proposes a attention framework based on the Seq2Seq architecture. This framework tries to align between an image and words (caption assignment problem for images).
![alt text]({{base.url}}/assets/images/attentionindeeplearning/3.png "Image source: Xu et al. (2015)")
This architecture uses a convolution layer to extract the information in the image into a vector, bringing in RNN with attention. Then generate a caption that highlights the main object as shown below.
![alt text]({{base.url}}/assets/images/attentionindeeplearning/4.png "Image source: Xu et al. (2015)")

## Hierarchical attention

[Yang et al. (2016)](https://www.aclweb.org/anthology/N16-1174.pdf]) pointed out that with its hierarchical attention network (HAN), Attention can be effectively utilized in many different floors. At the same time, with HAN, we can use attention in classification problems, not just sequence problems.
![alt text]({{base.url}}/assets/images/attentionindeeplearning/5.png "Image source: Yang et al. (2016)")
The HAN consists of 2 encoder networks, one for word and one for sentence. The Word encoder processes each word one by one and arranges it into a "sentence of interest". The Sentence encoder then sorts each sentence with the final output. HAN allows to interpret the results as shown below. HAN users can know what is the important sentence and what is the important part of the sentence.
![alt text]({{base.url}}/assets/images/attentionindeeplearning/6.png "Image source: Yang et al. (2016)")

## Transformer and BERT

![alt text]({{base.url}}/assets/images/attentionindeeplearning/7.png "Image source: Vaswani et al. (2017)")
[Vaswani et al. (2017)](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf) suggests breakthrough neural network architecture in NLP. The Multi-head self-attention class of this architecture aligns the letters of this string with the letters of another string to calculate the representation of the sentence. This approach is more efficient not only in terms of representability but also more computationally efficient than convolutional and recursive computation.

![alt text]({{base.url}}/assets/images/attentionindeeplearning/8.png "Image source: Vaswani et al. (2017)")

With his ability, Transformer has promoted a lot of research towards typical self-attention-based models such as Bidirectional Encoders Representation from Transfomer (BERT) by [Devlin et al. (2019)](https://arxiv.org/pdf/1810.04805.pdf?source=post_elevate_sequence_page---------------------------) . During the 2019 period, BERT's ability is considered state-of-art in NLP thanks to significant improvements from the transfomer. Some self-attention-based models give other breakthrough results such as XLNet, RoBERTa, GPT-2 and ALBERT.
![alt text]({{base.url}}/assets/images/attentionindeeplearning/9.png "Image source: Devlin et al. (2018)")

## Other applications

Regarding the application in NLP, the overview can be seen at first through the last part of the article. Of course, today's Attention mechanism is widely used in many other fields as well:

* Heathcare: [Choi et al. (2016)](http://papers.nips.cc/paper6321-retain-an-interpretable-predictive-model-for-healthcare-using-reverse-time-attention-mechanism.pdf)
* Speech recognition: [Chorowski et al. (2015)](http://papers.nips.cc/paper/5847-attention-based-models-for-speech-recognition.pdf)
* Graph attention networks: [Velickovic´ et al. (2018)](https://arxiv.org/pdf/1710.10903.pdf)
* Recommender systems: [Seo et al. (2017)](https://dl.acm.org/doi/10.1145/3109859.3109890), [Tay et al. (2018)](https://arxiv.org/pdf/1801.09251.pdf)
* Self-driving cars: [Kim and Canny (2017)](http://openaccess.thecvf.com/content_ICCV_2017/papers/Kim_Interpretable_Learning_for_ICCV_2017_paper.pdf)

## Reference

* Seq2Seq, or RNN Encoder-Decoder [Cho et al. (2014)](http://emnlp2014.org/papers/pdf/EMNLP2014179.pdf), [Sutskever et al. (2014)](https://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf)
* Alignment models [Bahdanau et al. (2015)](https://arxiv.org/pdf/1409.0473.pdf), [Luong et al. (2015)](https://arxiv.org/pdf/1508.04025.pdf)
* Visual attention [Xu et al. (2015)](http://proceedings.mlr.press/v37/xuc15.pdf)
* Hierarchical attention [Yang et al. (2016)](https://www.aclweb.org/anthology/N16-1174.pdf)
* Transformer [Vaswani et al. (2017](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)
