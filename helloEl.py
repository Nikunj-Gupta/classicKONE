import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import ConversationV1
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import alsaaudio, time, audioop
import scipy.io.wavfile
import numpy
#lights on 1
#lights off 0
#fans on 2
#fans off 3
import serial
import sys
import pyaudio  
import wave  


'''
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)

#audio_input = []
audio_input = numpy.zeros(shape=(100,2))
i = 0
while i <= 100:
	l,data = inp.read()
	if l:
		audio_input[i][0] = audioop.max(data, 2)
	i = i + 1
	time.sleep(.001)
	    
wav_input = scipy.io.wavfile.read(audio_input)
''' 
    

speech_to_text = SpeechToTextV1(
    username='d9770911-5622-42e9-9e8a-87748b1943eb',
    password='3SFcWLaNtpYj',
    x_watson_learning_opt_out=False
)

with open(join(dirname(__file__), sys.argv[1]),
          'rb') as audio_file:
          
	parsed_json = json.loads(json.dumps(speech_to_text.recognize(audio_file, content_type='audio/wav', timestamps=True, word_confidence=True), indent=2))
	print parsed_json['results'][0]['alternatives'][0]['transcript']








conversation = ConversationV1(
    username='cb3a69c8-05eb-47eb-9f7c-e3af70df9b90',
    password='l5zwTQTECNmc',
    version='2016-09-20')

# replace with your own workspace_id
workspace_id = '5fc02fa2-bdfd-4e2a-8147-95f87cea437e'

response = conversation.message(workspace_id=workspace_id, message_input={
    'text': parsed_json['results'][0]['alternatives'][0]['transcript'] })
#print(json.dumps(response, indent=2))

newResponse = response["output"]["text"][0]


'''
for key, value in response["output"]["text"].items():
	print("Key:")
	print(key)
'''


'''
newResponse = response['output']['text']
print newResponse
'''

'''
parsed_json = json.loads(json.dumps(speech_to_text.recognize(audio_file, content_type='audio/wav', timestamps=True, word_confidence=True), indent=2))
	print parsed_json['results'][0]['alternatives'][0]['transcript']
'''


# When you send multiple requests for the same conversation, include the
# context object from the previous response.
# response = conversation.message(workspace_id=workspace_id, message_input={
# 'text': 'turn the wipers on'},
#                                context=response['context'])
# print(json.dumps(response, indent=2))












# coding=utf-8
text_to_speech = TextToSpeechV1(
    username='af1d35c6-c311-46d8-8200-f05b711ff723',
    password='j5VWWJHYBnoi',
    x_watson_learning_opt_out=True)  # Optional flag

#print(json.dumps(text_to_speech.voices(), indent=2))

print newResponse
with open(join(dirname(__file__), 'output.wav'),
          'wb') as audio_file: audio_file.write(text_to_speech.synthesize(newResponse, accept='audio/wav', voice="en-US_AllisonVoice"))


#define stream chunk   
chunk = 1024  
#open a wav format music  
f = wave.open(r"output.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  
#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  
#stop stream  
stream.stop_stream()  
stream.close()  
#close PyAudio  
p.terminate()  

if ("Lights" in newResponse and "on" in newResponse):
	ser = serial.Serial('/dev/ttyACM1', 9600)
	while (True):
		ser.write('1')

if ("lights" in newResponse and "off" in newResponse):
	ser = serial.Serial('/dev/ttyACM1', 9600)
	while (True):
		ser.write('0')







'''
for key, value in parsed_json.items():
	print("Key:")
	print(key)

for key, value in parsed_json.iteritems():
	print("Key:")
	print(key)
	print "Value:"
	print (value)
'''
'''
def get_keys(dl, keys_list):
	if isinstance(dl, dict):
 	    keys_list += dl.keys()
	    map(lambda x: get_keys(x, keys_list), dl.values())
	elif isinstance(dl, list):
	    map(lambda x: get_keys(x, keys_list), dl)

keys = []
get_keys(parsed_json, keys)

print(keys)
# [u'a', u'inLanguage', u'description', u'priceCurrency', u'geonames_address', u'price', u'title', u'availabl', u'uri', u'seller', u'publisher', u'a', u'hasIdentifier', u'hasPreferredName', u'uri', u'fallsWithinState1stDiv', u'score', u'fallsWithinCountry', u'fallsWithinCountyProvince2ndDiv', u'geo', u'a', u'hasType', u'label', u'a', u'label', u'a', u'uri', u'hasName', u'a', u'label', u'a', u'uri', u'hasName', u'a', u'label', u'a', u'uri', u'lat', u'lon', u'a', u'address', u'a', u'name', u'a', u'description', u'a', u'name', usury']

#print(list(set(keys)))    # unique list of keys
'''
