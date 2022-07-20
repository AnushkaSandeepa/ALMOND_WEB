from django.contrib import admin

from v_stream.models import Session
from .models import Session
from .models import Measurements
from .models import ModelInfo

# Register your models here.

admin.site.register(Session)
admin.site.register(Measurements)
admin.site.register(ModelInfo)