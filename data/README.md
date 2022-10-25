# Datasets
To demonstrate our ideas for optimization better, we have prepared two Information Retrieval datasets.

## Validation dataset based on Stanford SwiftUI lectures
**Link to Lectures:** [Stanford SwiftUI courses](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtTj9oywMWoBx0dCGd51_yG)

**Link to Lectures' license:** [Stanford SwiftUI licence](https://cs193p.sites.stanford.edu/about-cs193p)

**License** 
The lectures have been released under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. 
As our validation dataset is a derivative, we also release it under the same licence.

**Full license text:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

**Content:** Transcripts from recorded lectures. Text is often not straight to the point, often containing many unrelated sentences when a lecturer is talking about a something different to the main topic.

The second benchmark is our customly prepared one and much smaller. The dataset is based on transcriptions from Stanford University lectures regarding SWIFT UI course. We’ve split the first 7 lectures into 185 smaller ones, 25-sentenced documents with 5 sentences overlapping. We have also prepared 184 questions with multiple possible answers.

We provide the following subsets of the dataset:
 - SwiftUI as is,
 - SwiftUI containing additional fields,
 
## Validation dataset based on Squad 2.0

**Link to the dataset:** [SQUAD 2.0 dataset](https://rajpurkar.github.io/SQuAD-explorer/)

**License** 
The SQUAD 2.0 has been released under Creative Commons Attribution-ShareAlike 4.0 International(CC BY-SA 4.0) license. 
As our validation dataset is a derivative, we release it under the same licence.

**Full license text:** [ CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode)

**Content:** Extracted paragraphs from wikipedia articles. Text is well structured and contains no typos. Usually contains no bloating or unnecessary words.

The first one is based on SQUAD 2.0 - a Question Answering benchmark that can be used for the IR validation as well, when adjusted properly. We’ve extracted 10.000 random documents and 1.000 random questions referring to them. We treat each SQUAD paragraph as a separate index’es document.

We provide the following subsets of the dataset:
 - full train set,
 - full dev set,
 - 10.000 documents with 1.000 questions,
 - 1.000 documents with 500 questions,
 - 1.000 documents with 100 questions,
 - 10.000 documents with 1.000 questions, containing additional fields,

