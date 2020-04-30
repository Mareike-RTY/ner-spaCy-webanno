# ner_lyrics
<h4>Scripts for detecting named entities in German lyrics by updating a German NER model by spaCy.</h4>

__Script 1: Change OTH labels to MISC labels__ 
<br>Since the WebAnno annotation label for the _miscellaneous_ named entity category (_OTH_) does not match with the respective spaCy annotation label (_MISC_), the OTH strings in the annotated data need to be replaced by MISC strings in a first step.</br>

__Script 2: Prepare date for spaCy__
<br>Since spaCy cannot process the JSON data exported from WebAnno, it is necessary to adjust the format.</br>

__Script 3: Test updated spaCy model__
<br>After updating the spaCy model via the command line interface, the model is tested on all songtext files at once, whereas the named entities included are counted and visualized within the text.</br>
<hr></hr>
<b>Methods:</b>
<br>Programming language: Python 3</br>
Annotation tool: WebAnno (v 3.6.4), https://webanno.github.io/webanno/
<br>NLP software library: spaCy (v 2.2.3), https://spacy.io/models/de#de_core_news_sm</br>
Linguistic resource: Songkorpus, www.songkorpus.de
