## Inspiration
Analysis of large data streams has become more and more accessible - especially language processing got easier than ever before, thanks to huge progress with large language models and the ability for everyone to access those via APIs.

Retrieving valuable Information out of large Logfiles, on the other hand, is a difficult task that in many cases still isn't really automated, and for many owners of a server, it is still common practice to manually check Logfiles for notable events and for debugging errors.
So now, at the end of 2023, the year of the rise of Generative AI especially Large Language Models, we are able to stop this Logfile-Madness and use cutting-edge language processing technologies to help each and everyone to gain a better understanding of one's Server's Logfiles.

## What it does
As simple as it sounds: It enables you to chat with your Logfiles.
You can ask of any occurrences of any notable event and it will give you a short summary of where in the Logfile this event is occurring.

## How we built it
The tech stack consists of 3 major parts:
### The Frontend
TypeScript + Vite + React: The powerful Trio for agile Web deployment.

### Backend Part 1 - Web Backend
A Python Django web backend with a simple SQLite Database provides a small API for the frontend to access the model while preserving multiprocessing so there are no long loading times.

### Backend Part 2 - Model
The model is an advanced k-means Algorithm which under unsupervised learning firstly clusters chunks of the logfile and then detects which chunks are relevant for the given prompt.

## Challenges we ran into
A wild mix of indecisiveness, bad time management, and long waiting periods due to model training challenged us from the beginning. But when on Saturday night at 11 pm, every single team member was already stressed out, our Virtual Machine Provided by Rhode & Schwarz decided that it needed a little rest. As there was nobody from R&S still online to wake our VM up again and weren't in the mood to go to sleep, we decided to shift the whole infrastructure partly to Google Colab and partly to our Laptops, from where we were eventually able to deploy our Proof-of-Concept Application.

## Accomplishments that we're proud of
When team members work on different tasks - everyone does what he is best at - then it can be quickly difficult to overlook everything that is happening and that needs to happen. But when (a couple of hours before the deadline) everything comes together and you see a working application, then that the happy feeling of knowing what you have built in the last 36 hours.

## What's next for Talking Log
Our Model is good at quickly detecting occurrences of a specific topic of a prompt in large logfiles, but it is not really able to formulate sentences.
While an LLM could process a whole log file in sufficient time, our algorithm is best at filtering relevant regions from a log file. In the future, you could pass those regions together with the prompt into a Large Language Model to receive longer text answers in whole sentences.
