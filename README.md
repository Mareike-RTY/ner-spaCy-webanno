# ner_lyrics
Scripts for detecting named entities in German lyrics by updating a German NER model by spaCy.

__Change OTH labels to MISC labels:__ 
Since the WebAnno annotation label for the _miscellaneous_ named entity category (_OTH_) does not match with the respective spaCy annotation label (_MISC_), the OTH strings in the annotated data need to be replaced by MISC strings in a first step.

__Prepare date for spaCy:__
Since spaCy cannot process the JSON data exported from WebAnno, it is necessary to adjust the format.

__Test updated spaCy model:__
After updating the spaCy model via the command line interface, the model is tested on all songtext files whereas the named entities included are counted and visualized within the text.


__Used:__
Programming language: Python 3
Annotation tool: WebAnno (v 3.6.4)
NLP software library: spaCy (v 2.2.3)
Linguistic resource: www.songkorpus.de
