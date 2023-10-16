# Speech-to-Text (GCP)

Showcasing how to convert speech to text in GCP.

## Setup

- Create a service account in GCP
- Download the API key
- Name it `secret.json` and save it alongside this `README.md` file.

## Installation

```bash
pip install -e .
```

## Usage

```bash
s2t <audio file> <output file>
```

## Tips/Ideas

### Self-Hosting the Speech Transcription

I am using the GCP Speech-to-Text model. I'm sure it's pretty great. But it
_could_ cost a fair bit of money, given it costs about 1c per minute. Imagine
you submit 10 x 1 hour transcriptions: that's 10 hours or 600 minutes = $6. Not 
a lot, sure, but it can very quickly add up...

I know that there are alternatives to GCP. Some stuff I found:

- [VOSK](https://github.com/alphacep/vosk-api)
- [PocketSphinx](https://github.com/cmusphinx/pocketsphinx)
- [PocketSphinx example](https://stackoverflow.com/a/38877903)
- [OpenAI Whisper](https://github.com/openai/whisper)

### High-Level Framework

I am using a very low-level interface into GCP. There are frameworks for this. 
Here is one that I found that looks promising: https://github.com/Uberi/speech_recognition.

### Correcting Transcription Errors

The transcription you are returned from GCP isn't perfect. I found a really easy
way to correct these mistakes is to ask ChatGPT. I had the following prompt work
pretty well:

```
I have some text that has been transcribed. It has a few mistakes in it. Can you
identify them and correct them? Return the following message, with all the 
corrections, as a single paragraph. Don't return anything but the corrected 
paragraph.

There are a few things more important in our world than the good old fashioned 
nine to five job everywhere. You look on the internet you will be met with 
advertisers and influencers telling you how you can quit the rat race by 
starting a business retire early by Saving and investing prodigiously or telling 
your boss to shove it after Your Meme coins have mooned. It's a nice dream that 
sells well because honestly sometimes jobs can really suck. I hate my job 
commuting an hour a day to spend eight hours in an office for five days a week 
all with little to no flexibility is not
```

I was returned the following, which I think is pretty good:

```
There are a few things more important in our world than the good old-fashioned 
nine-to-five job. Everywhere you look on the internet, you will be met with 
advertisers and influencers telling you how you can quit the rat race by 
starting a business, retire early by saving and investing prodigiously, or 
telling your boss to shove it after your meme coins have mooned. It's a nice 
dream that sells well because, honestly, sometimes jobs can really suck. I hate 
my job, commuting an hour a day to spend eight hours in an office for five days 
a week, all with little to no flexibility is not.
```

I'm sure there are more efficient ways to perform this conversion (e.g. a 
self-hosted LLM, some other NLP model, etc.) but this at least worked without
much effort.