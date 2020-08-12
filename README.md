# Language Identification

The goal is to identify the language in which a document, message, or sentence is written. To achieve this goal, I propose the following methodology. First, to transform a text into character n-gram features. Second, to build a machine-learned classifier to predict the language in which a text is written, using those character n-gram features to support the predictive power. Last, to evaluate the performance of the approach proposed here on a variety of datasets and against some of the most popular language identification libraries in the Python ecosystem.

Moreover, it is worth making clear that the language identification system will be limited to 14 out of 24 official languages of the European Union, namely:

1. Czech
2. Danish
3. Dutch
4. English
5. Finnish
6. French
7. German
8. Hungarian
9. Italian
10. Polish
11. Portuguese
12. Romanian
13. Spanish
14. Swedish

The above languages were chosen due to data availability matters, but mostly because their alphabet is based on modern Latin.

## Further Reading

The entire solution approach is available as a [Jupyter notebook](https://nbviewer.jupyter.org/github/jacerong/language-identification/blob/master/langid.ipynb). The notebook shows the source code and a more detailed description of the experimentation. Likewise, the author invites the reader to visit [this](https://jacerong.com/blog/language-identification.html) short description of the proposed approach to language identification.
