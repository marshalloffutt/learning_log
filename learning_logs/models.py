from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

# class Entry inherits from Django's base Model class
class Entry(models.Model):
    """Something specific learned about a topic."""
    # Delete topic also deletes all entries associated with that topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Without this Django would call entries 'Entrys'
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
             return self.text