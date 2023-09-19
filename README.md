# slackbot
A proof of concept command line application that analyzes prompts as if they were Slack messages where sensitive contents have to be redacted out. The interesting part of this PoC is inverting the usage of a question answering model, where the questions are fixed and used to analyse messages on the fly. The set of questions can be expanded, made configurable, etc ...

## Install

```
pip install -r requirements.txt
```

## Usage

```
python slackbot.py
```

You can then write arbitrary messages on the prompt, and the bot will answer with a redacted version where passwords have been substituted.
