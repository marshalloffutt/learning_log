from django.contrib import admin
from learning_logs.models import Topic, Entry

# Tells Django to manage our model through the admin site
admin.site.register(Topic)
admin.site.register(Entry)