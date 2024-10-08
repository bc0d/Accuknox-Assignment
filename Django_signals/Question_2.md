
# `Question 2:` 
Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# `Answer:`
In Django signals runs synchronously and it runs in the same thread as it's caller's thread.
So when a signal is triggered from a function the statements in signal method will continue to run in the same thread.
After that it continue the main execution flow.

To proving the use of same thread in  signals I'm here using threading module.

Signals.py :
```python
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def reg_name_signal(sender, instance, **kwargs):
    print(f"Signal function running thread's name: {threading.current_thread().name}")
```

View.py :
```python
import threading
from django.shortcuts import render
from .models import User

def reg_name(request):
    print(f"Main function running thread's name: {threading.current_thread().name}")
    instance = User.objects.create(name="Ram")
    return render(request, 'profil.html')
```