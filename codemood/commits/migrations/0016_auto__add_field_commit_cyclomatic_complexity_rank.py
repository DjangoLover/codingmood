# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Commit.cyclomatic_complexity_rank'
        db.add_column(u'commits_commit', 'cyclomatic_complexity_rank',
                      self.gf('django.db.models.fields.CharField')(default='A', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Commit.cyclomatic_complexity_rank'
        db.delete_column(u'commits_commit', 'cyclomatic_complexity_rank')


    models = {
        u'commits.commit': {
            'Meta': {'object_name': 'Commit'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'code_rate': ('django.db.models.fields.FloatField', [], {}),
            'commit_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'cyclomatic_complexity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'cyclomatic_complexity_rank': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messages': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'prev_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'commits'", 'to': u"orm['commits.Repository']"})
        },
        u'commits.repository': {
            'Meta': {'object_name': 'Repository'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['commits']