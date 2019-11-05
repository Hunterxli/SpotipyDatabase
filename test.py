# Imports the Google Cloud client library
from google.cloud import translate_v2 as translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = u'Hello, world!'
# The target language
target = 'en'

# Translates some text into Russian
translation = translate_client.translate(text, target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))