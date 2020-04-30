# ner_lyrics
Scripts for detecting named entities in German lyrics by updating a German NER model by spaCy.
**change OTH labels to MISC labels: since the WebAnno annotation label for the _miscellaneous_ named entity category (_OTH_) does not match with the respective spaCy annotation label (_MISC_), the OTH strings in the annotated data need to be replaced by MISC strings in a first step.
**prepare date for spaCy: 
**test updated spaCy model: on all data files at once

Programming language: Python 3
Annotation tool: WebAnno (v 3.6.4)
NLP software library: spaCy (v 2.2.3)
