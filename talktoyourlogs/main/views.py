from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
from django.core.files.base import ContentFile
import itertools
import json
from openai import OpenAI
import os


# Create your views here.

    
def model_kickoff(prompt, session):
    session.task = "waiting"
    session.save()

    os.system(f'sudo python3.9 main/ai-model/test.py "{prompt}" "/Users/timruppert/PycharmProjects/hackathon1/talktoyourlogs/{session.path}" "{session.session_id}" &')


def internal_endpoint(request):
    if not (request.get_host().startswith("localhost") or request.get_host().startswith("127.0.0.1")):
        return HttpRespone(status=403)

    data = request.GET["data"]
    session = Session.objects.get(session_id=request.GET["session"].split("---")[0])

    if not session.task.startswith('{"'):
        session.task = data
        session.save()

        c = ChatHistory.objects.get(session=session)
        c.content += f"\nMODEL: {data}"
        c.save()

    else:
        session.task += f'"{request.GET["session"].split("---")[1]}": "{data}", '
        session.save()

    return HttpResponse(status=200)


def check_for_result(request):
    body = request.POST

    session = Session.objects.get(session_id=body["session"].split("---")[0])

    if not session.task.startswith('{"'):
        res = str(session.task)
    else:
        res = str(session.task) + "}}"

    if res != "waiting" and res != "empty":
        session.task = "empty"
        session.save()

    return HttpResponse(res)


def _lines_from_session(session):
    lines = []

    with open(session.path, "r") as f:
        lines += f.readlines()
            
    return lines

def upload(request):
    if request.method == "GET":
        return HttpResponse('''
            <form action="/upload" method="POST" enctype="multipart/form-data">
                <input type="file" name="logfile" multiple>
                <input type="submit">
            </form>
        ''')
    

    files = [file.read().decode() for file in request.FILES.getlist("logfile")]
    



    s = Session.objects.create(path="..")

    s.path = f"temp/{s.session_id}"
    s.save()

    with open(f"temp/{s.session_id}", "w+") as f:
        f.write("\n".join(files))

    ChatHistory.objects.create(session=s, content="")

    return HttpResponse(str(s.session_id))


def demo(request):
    s = Session.objects.create(path=f"temp/final_log.out")

    ChatHistory.objects.create(session=s, content="")
    
    return HttpResponse(str(s.session_id))


def chat(request):
    body = request.POST
    
    if not "session" in body:
        return HttpResponse(status=403)
    
    session = Session.objects.get(session_id=body["session"])
    
    c = ChatHistory.objects.get(session=session)
    c.content += f"\nUSER: {body['prompt']}"
    c.save()

    model_kickoff(body["prompt"], session)

    return HttpResponse(status=200)


def get_history(request):

    body = request.POST
    session = Session.objects.get(session_id=body["session"])
    return HttpResponse(ChatHistory.objects.get(session=session).content)


def close_session(request):
    body = request.POST

    session = Session.objects.get(session_id=body["session"])

    for file in os.listdir("temp"):
        filename = os.fsdecode(file)
        if filename.startswith(session.session_id):
            os.remove(os.path.join("temp", filename))

    session.delete()

    return HttpResponse("Bye!")


def get_categories(request):
    return HttpResponse(",".join(map(str, DefaultCategory.objects.all())))


def category(request, category):
    body = request.POST
    
    session = Session.objects.get(session_id=body["session"])

    category = DefaultCategory.objects.get(name=category)

    session.task = '{"chart_type": "'+ category.chart_type +'", "prompts": {'
    session.save()

    for prompt in category.prompts.all():
        model_kickoff(prompt.prompt, session + "---" + prompt.prompt)
        
    return HttpResponse(status=200)


def suggest_similar(request):

    with open("main/key", "r") as f:
        openai = OpenAI(api_key=str(f.read()))
    body = request.POST

    session = Session.objects.get(session_id=body["session"])

    last_message = ChatHistory.objects.get(session=session).content.split("USER:")[-1].split("MODEL:")[0]

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Suggest exaclty 5 similar questions to ask about server logfiles, and every question should be seperated by '---'."},
            {"role": "user", "content": last_message}
        ]
    )

    res = HttpResponse(json.dumps([i for i in (completion.choices[0].message.content.replace("\n", "").split("---")) if len(i)>0]))


    del openai

    return res




