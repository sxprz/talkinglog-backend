import sys
import requests

from model_summarize import TextSummarizer

prompt, path, session = sys.argv[1:]


with open(path, "r") as f:
    context = f.read()

summarizer = TextSummarizer(
    model_name="bert-large-uncased-whole-word-masking-finetuned-squad",
    embedding_model_name="glove-wiki-gigaword-300",
    max_length=512,
    overlap=80,
    num_clusters=3
)


data = summarizer.summarize(context, prompt)


requests.get(f"http://localhost:8000/internal?session={session}&data={data}")
