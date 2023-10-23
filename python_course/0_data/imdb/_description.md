# IMDB reviews dataset

## Summary

This is a dataset for binary sentiment classification. It provides 25,000 highly polar
movie reviews for training and 25,000 additional reviews for testing.

## Variables

After cleansing the data, the dataset will containt these columns:

1. `id` ID for the review (int).
2. `dataset` : Dataset that contained the review; `Train` or `Test` (string).
3. `label` : Sentiment of the review; `Positive` or `Negative` (string).
4. `rating`: Star rating given to the movie 1-10 (int).
5. `content`: Full text of the review (string).

## Source

Downloaded from: https://ai.stanford.edu/~amaas/data/sentiment/
Direct download link: https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz

## Reference

Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher
Potts. (2011). Learning Word Vectors for Sentiment Analysis. The 49th Annual Meeting of
the Association for Computational Linguistics (ACL 2011).
