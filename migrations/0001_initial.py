# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Incident'
        db.create_table('incident_incident', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_resolved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('severity_level', self.gf('django.db.models.fields.IntegerField')(max_length=1, default=0)),
        ))
        db.send_create_signal('incident', ['Incident'])

        # Adding model 'Update'
        db.create_table('incident_update', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('incident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['incident.Incident'])),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('incident', ['Update'])


    def backwards(self, orm):
        # Deleting model 'Incident'
        db.delete_table('incident_incident')

        # Deleting model 'Update'
        db.delete_table('incident_update')


    models = {
        'incident.incident': {
            'Meta': {'object_name': 'Incident', 'ordering': "['date_time']"},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_resolved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'severity_level': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incident.update': {
            'Meta': {'object_name': 'Update', 'ordering': "['incident', 'date_time']"},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incident': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['incident.Incident']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['incident']