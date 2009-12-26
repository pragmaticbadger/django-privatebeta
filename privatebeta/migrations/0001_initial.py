
from south.db import db
from django.db import models
from privatebeta.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'InviteRequest'
        db.create_table('privatebeta_inviterequest', (
            ('id', orm['privatebeta.InviteRequest:id']),
            ('email', orm['privatebeta.InviteRequest:email']),
            ('created', orm['privatebeta.InviteRequest:created']),
        ))
        db.send_create_signal('privatebeta', ['InviteRequest'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'InviteRequest'
        db.delete_table('privatebeta_inviterequest')
        
    
    
    models = {
        'privatebeta.inviterequest': {
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['privatebeta']
