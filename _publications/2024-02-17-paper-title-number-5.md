---
title: "Honest AI: Fine-Tuning "Small" Language Models to Say "I Don't Know", and Reducing Hallucination in RAG"
collection: publications
category: conferences
permalink: https://ieeexplore.ieee.org/document/8310067
excerpt: 'This paper is about fixing template issue #693.'
date: 2018-03-12
venue: '2024 KDD Cup Workshop for Retrieval Augmented Generation at the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining'
paperurl: ''
citation: #''
---

Hallucination is a key roadblock for applications of Large Language Models (LLMs), particularly for enterprise applications that are sensitive to information accuracy. To address this issue, two general approaches have been explored: Retrieval-Augmented Generation (RAG) to supply LLMs with updated information as context, and fine-tuning the LLMs with new information and desired output styles. In this paper, we propose Honest AI: a novel strategy to fine-tune "small" language models to say "I don't know" to reduce hallucination, along with several alternative RAG approaches. The solution ranked 1st in Task 2 for the false premise question. The alternative approaches include using RAG with search engine and knowledge graph results, fine-tuning base LLMs with new information and combinations of both approaches. Although all approaches improve the performance of the LLMs, RAG alone does not significantly improve the performance and fine-tuning is needed for better results. Finally, the hybrid approach achieved the highest score in the CRAG benchmark. In addition, our approach emphasizes the use of relatively small models with fewer than 10 billion parameters, promoting resource efficiency.