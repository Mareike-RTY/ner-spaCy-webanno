# ner_lyrics
<h4><FONT COLOR="000099">Scripts for detecting named entities in German lyrics by updating a German NER model by spaCy.</FONT></h4>

<ul>
  <li><i>Script 1: Change OTH labels to MISC labels</i></li>
  Since the WebAnno annotation label for the miscellaneous named entity category (OTH) does not match with the
  respective spaCy annotation label (MISC), the OTH strings in the annotated data need to be replaced by MISC strings
  in a first step.</ul>

<ul>
  <li><i>Script 2: Prepare data for spaCy</i></li>
  Since spaCy cannot process the JSON data exported from WebAnno, it is necessary to adjust the format.</ul>

<ul>
  <li><i>Script 3: Test updated spaCy model</i></li>
  After updating the spaCy model via the command line interface, the model is tested on all songtext files at once,
  whereas the named entities included are counted and visualized within the text.</ul>
<hr></hr>
<b>Resources used:</b>
<ul>
  <li>Programming language: Python 3</li>
  <li>Annotation tool: WebAnno (v 3.6.4), https://webanno.github.io/webanno/</li>
  <li>NLP software library: spaCy (v 2.2.3), https://spacy.io/models/de#de_core_news_sm</li>
  <li>Linguistic resource: Songkorpus, www.songkorpus.de</li></ul>
