from django.db import models
import uuid
# Create your models here.


class Session(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    
    path = models.CharField(max_length=600)

    task = models.CharField(max_length=1000, blank=True, null=True, default="empty")


    def __str__(self):
        return str(self.session_id)


    
class ChatHistory(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=600, default="Title")
    
    content = models.CharField(max_length=5000)


class DefaultCategory(models.Model):
    name = models.CharField(max_length=100)
    prompts = models.ManyToManyField("DefaultPrompt")
    
    chart_type = models.CharField(max_length=3, choices=(
        ("PIE", "Piechart"),
        ("BAR", "Barchart"),
        ("LIN", "Linechart"),
        ("HMP", "Heatmap"),
        ("SCP", "Scatterplot"),
        ("NON", "Undefined"),
    ), default="NON")

    def __str__(self):
        return self.name
    
    

class DefaultPrompt(models.Model):
    prompt = models.CharField(max_length=900)
    
    def __str__(self):
        return self.prompt