from django.db import models

class Notes(models.Model):
    note_content = models.CharField(max_length=300, blank=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'notes'
        app_label = 'todo_app'

    def __unicode__(self):
        return u'{}:{}'.format(self.pk, self.note_content, self.created, self.modified)