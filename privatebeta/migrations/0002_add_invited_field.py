
from south.db import db
from django.db import models
from privatebeta.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'InviteRequest.invited'
        db.add_column('privatebeta_inviterequest', 'invited', orm['privatebeta.inviterequest:invited'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'InviteRequest.invited'
        db.delete_column('privatebeta_inviterequest', 'invited')
        
    
    
    models = {
        'privatebeta.inviterequest': {
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        }
    }
    
    complete_apps = ['privatebeta']
