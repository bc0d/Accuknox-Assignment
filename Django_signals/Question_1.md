
# `Question 1:` 
 By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# `Answer:`
Signals are used in Django to perform tasks when modification happend in database.
In django, signals are executed synchronously that means when a signal is sent the handlers are executed in series and then go to the next statement in the code block.
The are 3 types like when using delete(), save() and initialising the model.

To proving the synchronous behavior of signals I'm here using timestamp.
- Here I'm using the post_save method.
- Also using the delay to show the sequential working.

Signals.py :
```python
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import User

@receiver(post_save, sender=User)
def reg_name_signal(sender, instance, **kwargs):
    print(f"Signal function started at: {now()}")
    time.sleep(5)
    print(f"Signal function finished at: {now()}")
```

View.py :
```python
from django.shortcuts import render
from django.utils.timezone import now
from .models import User

def reg_name(request):
    print(f"Time before saving model: {now()}")
    instance = User.objects.create(name="Ram")
    print(f"Time after saving model: {now()}")
    return render(request, 'profil.html')
```