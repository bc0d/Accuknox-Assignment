
# `Question 2:` 
By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# `Answer:`
By default the django signals run in the same database transaction as the caller.
Because of thet when a signal is triggered during a db operation and if the transaction roll backed, the signal function also roll back.

To prove this we can use the try block and first trigger the signal and make transaction then raise an exception.
Also inside the signal function need to create a entry to temp model.
By doing this we can identify that after the roll back temp model entry is roll backed.

Signals.py :
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Temp

@receiver(post_save, sender=User)
def reg_name_signal(sender, instance, **kwargs):
    print("Signal function started")
    Temp.objects.create(message=f"Saved User with ID {instance.id}")
    print("Temp entry added.")
```

View.py :
```python
from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Temp

def reg_name(request):
    try:
        instance = MyModel.objects.create(name="Ram")
        print("Before exception.")
        raise Exception("Rolled backed.")
    except Exception as e:
        print(e)
    is_temp = Temp.objects.exists()
    return HttpResponse(f"Is Temp has value : {is_temp}")
```