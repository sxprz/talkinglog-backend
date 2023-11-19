# Hackathon Loganalysis Tum 2023 11

Welcome to the "Hackathon Loganalysis Tum 2023 11" repository. This project is part of a broader initiative to develop log analysis tools, as part of a competition hosted by Rohde & Schwarz.
 
## Motivation:

In today's data-driven world, handling and understanding large log files is a significant challenge. This hackathon aims to leverage transformer models to simplify this process. The goal is to create a solution that can summarize these log files and provide a user-friendly QA system to interact with the summarized data.
Furthermore, by linking the answers back to the original log lines, we aim to maintain data credibility and provide a verification method. This hackathon is an opportunity to contribute to a solution that can revolutionize how organizations interact with their log data, leading to more efficient data handling and informed decision-making.

## Virtual Machine for Hackathon Teams
To support all hackathon teams, we will provide a Virtual Machine (VM) that is enabled with a GPU. This VM will also have the capability to broadcast a frontend application (see README.md inside "streamlit" folder), such as Streamlit, which will allow teams to present their results effectively. This setup will ensure that all teams have the necessary computational resources and presentation tools to excel in the hackathon.
 
## Task Description:
In this hackathon challenge, your task is to develop a two-step solution using transformer models for handling large log files.

### Data
Inside the "data" folder you find three log files. Files starting with "test*" are given to you for testing the system you develop. The "final_log.out" file is the log you should consider in your final presentation (see below).

### Step 1: Summarization of Log Files
Your first task is to create a algorithm, using for example transformer models, that can effectively summarize large log files. The model should be able to parse through the log files, understand the context, and generate a concise summary of the logs. The goal is to distill the essential information from the logs into a format that is easily understandable and manageable.

### Step 2: QA with Summarized Context
Once the summarization is done, your next task is to use another transformer model to perform a QA (Question-Answering) task with the summarized context or the full log if you are able to do so. The user should be able to ask questions related to the log files, and the transformer model should provide answers.

### Additional Requirement: Traceability of Answers
An additional requirement for this challenge is to maintain the traceability of the answers given by the QA transformer. This means that for every answer provided by the transformer, there should be a way to link it back to the original log lines used for the summarization. This will help in ensuring the credibility of the answers and provide a way for users to verify the information if required.
The solution should be efficient, scalable, and robust, capable of handling log files of varying sizes and complexity.

Tipp: Due to the content of the logs you find in "data", we are mostly interessted in topics around ssh!​
- Is there a not authorized ssh login try?​
- Where are the lines in the log for that?​
- Which addresses tried to login?​

### Measurement of Success:
As a part of the hackathon, you are also required to devise a method to measure the success of your solution. This could be based on the accuracy of the summarization, the relevance of the answers provided by the QA transformer, and the effectiveness of the traceability feature.


### Super Challenge Dynamic Summarization:
A very usefull feature would be a dynamic summarization that allows for the creation of summaries that adapt to the context and content interacting with the user.
Instead of a static summary, the dynamic summarization process continually updates and refines the summary based on new input given by the user.

1. Dialog with User: The system engages in a dialog with the user to better understand their needs and preferences. This interactive process ensures that the final output is tailored to the user’s specific requirements and interests.

2. Summarize What Fits Best to User Question: The system focuses on summarizing information that is most relevant to the user’s query. By prioritizing content that directly addresses the user’s question, the system ensures that the summary is concise, relevant, and useful.

3. Allow to Remove Content for Summary That Users are Not Interested In: The system provides users with the option to exclude certain content from the summary. For example, if a user specifies “remove layer rspias-daemon”, the system will ignore messages with this context. This feature allows users to customize the summary according to their preferences.

4. Sequential Summarization: This approach involves adjusting the summary step by step based on user input. As the user provides more information or clarifies their needs, the system refines the summary accordingly. This iterative process ensures that the final summary accurately reflects the user’s intent and information needs.

A frontend and backend allowing to get a dynamic summarization would be a very useful feature.

## **Final Submission:**


1. **10:00 Sunday**: The final project submission is scheduled for 10:00 on Sunday. This is the deadline for all project-related submissions.

2. **Final Project Submission**: All components of the final project must be submitted by this deadline. This includes all code, documentation, and related materials into the hackathon related gitrepos (see email).

3. **Code in Repo**: The code for the project should be properly organized and uploaded to the designated repository (see email). This ensures that the code is easily accessible for review and evaluation.

4. **Pitch about...**: As part of the submission, a pitch presentation is required. This should for succinctly explain the project, its objectives, the approach taken (showing parts of the source code), and the results achieved presented on the "data/final_log.out" file.

5. **1st & 2nd Place Will Maybe Need a Frontend Check**: The projects that secure the 1st and 2nd places may require a frontend check. This involves a live test with the frontend to ensure that the project functions as expected in a real-world scenario.


## Prepaired Tools, Snippets and Tutorials

### Install requirements

First, install with the python interpreter of your choice the "requirements.txt" file via pip, i.e. "pip install requirements.txt"

### Streamlit as possible frontend

Inside the "streamlit" folder, you will find Python code snippets to help you develop a frontend for your hackathon project with Streamlit. Streamlit is a powerful tool that allows you to turn data scripts into shareable web apps in just a few minutes.

### Tutorial to NLP and Log files

Inside the ‘tutorial’ folder, you will find some snippets and explanations related to the hackathon and NLP tools that might be useful. These tutorials are designed to help you understand the basics of Natural Language Processing (NLP) and how to work with log files.
