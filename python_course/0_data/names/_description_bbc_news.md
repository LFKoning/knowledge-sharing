# BBC news dataset

## Summary

This dataset contains news articles originating from BBC News. The original data is provided as separate text files. These files have been processed into a single CSV file. Then Named Entity Recognition (NER) was performed to identify any persons mentioned in the article's text. If multiple persons were detected, multiple records were created for the same article.

## Variables

The dataset contains the following variables:

1. `filename` Original filename of the article (string)
2. `title` : Title of the article (string)
3. `artice` : Text of the article (string)
4. `person`: Name of the person detected (string)

## Source

Downloaded from: http://mlg.ucd.ie/datasets/bbc.html
Direct download link: http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip

## Reference

D. Greene and P. Cunningham. "Practical Solutions to the Problem of Diagonal Dominance in Kernel Document Clustering", Proc. ICML 2006. [PDF] [BibTeX].
