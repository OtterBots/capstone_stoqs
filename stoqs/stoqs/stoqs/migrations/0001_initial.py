# Generated by Django 4.2.2 on 2023-07-06 22:47

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import stoqs.stoqs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(max_length=256)),
                ('comment', models.TextField(max_length=2048)),
                ('startdate', models.DateTimeField()),
                ('plannedstartdate', models.DateTimeField(null=True)),
                ('enddate', models.DateTimeField(null=True)),
                ('plannedenddate', models.DateTimeField(null=True)),
                ('num_measuredparameters', models.IntegerField(null=True)),
                ('loaded_date', models.DateTimeField(null=True)),
                ('maptrack', django.contrib.gis.db.models.fields.LineStringField(null=True, srid=4326)),
                ('plannedtrack', django.contrib.gis.db.models.fields.LineStringField(null=True, srid=4326)),
                ('mappoint', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('mindepth', models.FloatField(null=True)),
                ('maxdepth', models.FloatField(null=True)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='ActivityParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('number', models.IntegerField(null=True)),
                ('min', models.FloatField(null=True)),
                ('max', models.FloatField(null=True)),
                ('mean', models.FloatField(null=True)),
                ('median', models.FloatField(null=True)),
                ('mode', models.FloatField(null=True)),
                ('p025', models.FloatField(null=True)),
                ('p975', models.FloatField(null=True)),
                ('p010', models.FloatField(null=True)),
                ('p990', models.FloatField(null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activity')),
            ],
            options={
                'verbose_name': 'Activity Parameter',
                'verbose_name_plural': 'Activity Parameter',
            },
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'Activity Type',
                'verbose_name_plural': 'Activity Types',
            },
        ),
        migrations.CreateModel(
            name='AnalysisMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(db_index=True, max_length=256, unique=True)),
                ('uristring', models.CharField(max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Analysis Method',
                'verbose_name_plural': 'Analysis Methods',
            },
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(db_index=True, max_length=128, unique_for_date='startdate')),
                ('startdate', models.DateTimeField(null=True)),
                ('enddate', models.DateTimeField(null=True)),
                ('description', models.CharField(blank=True, max_length=4096, null=True)),
            ],
            options={
                'verbose_name': 'Campaign',
                'verbose_name_plural': 'Campaigns',
            },
        ),
        migrations.CreateModel(
            name='InstantPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timevalue', models.DateTimeField(db_index=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activity')),
            ],
            options={
                'unique_together': {('activity', 'timevalue')},
            },
        ),
        migrations.CreateModel(
            name='NominalLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth', models.FloatField(db_index=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activity')),
            ],
            options={
                'verbose_name': 'NominalLocation',
                'verbose_name_plural': 'NominalLocations',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('type', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('standard_name', models.CharField(max_length=128, null=True)),
                ('long_name', models.CharField(blank=True, max_length=128, null=True)),
                ('units', models.CharField(blank=True, max_length=128, null=True)),
                ('origin', models.CharField(blank=True, max_length=256, null=True)),
                ('domain', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), null=True, size=None)),
            ],
            options={
                'verbose_name': 'Parameter',
                'verbose_name_plural': 'Parameters',
            },
        ),
        migrations.CreateModel(
            name='ParameterGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'ParameterGroup',
                'verbose_name_plural': 'ParameterGroups',
            },
        ),
        migrations.CreateModel(
            name='PermaLink',
            fields=[
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('parameters', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('usage_count', models.IntegerField(default=0)),
                ('last_usage', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(db_index=True, max_length=128, unique=True)),
                ('color', models.CharField(blank=True, max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(db_index=True, max_length=128, unique=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('depth', models.DecimalField(db_index=True, decimal_places=30, max_digits=100)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('name', models.CharField(db_index=True, max_length=128)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('filterdiameter', models.FloatField(blank=True, null=True)),
                ('filterporesize', models.FloatField(blank=True, null=True)),
                ('laboratory', models.CharField(blank=True, max_length=128, null=True)),
                ('researcher', models.CharField(blank=True, max_length=128, null=True)),
                ('instantpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.instantpoint')),
            ],
            options={
                'verbose_name': 'Sample',
                'verbose_name_plural': 'Samples',
            },
        ),
        migrations.CreateModel(
            name='SampledParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('datavalue', models.DecimalField(db_index=True, decimal_places=30, max_digits=100)),
                ('analysismethod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stoqs.analysismethod')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.parameter')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.sample')),
            ],
            options={
                'verbose_name': 'Sampled Parameter',
                'verbose_name_plural': 'Sampled Parameter',
                'unique_together': {('sample', 'parameter')},
            },
        ),
        migrations.CreateModel(
            name='SamplePurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name': 'Sample Purpose',
                'verbose_name_plural': 'Sample Purposes',
            },
        ),
        migrations.CreateModel(
            name='SampleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'Sample Type',
                'verbose_name_plural': 'Sample Types',
            },
        ),
        migrations.CreateModel(
            name='SimpleDepthTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epochmilliseconds', models.FloatField()),
                ('depth', models.FloatField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activity')),
                ('instantpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.instantpoint')),
                ('nominallocation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stoqs.nominallocation')),
            ],
            options={
                'verbose_name': 'Simple depth time series',
                'verbose_name_plural': 'Simple depth time series',
            },
        ),
        migrations.CreateModel(
            name='SimpleBottomDepthTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epochmilliseconds', models.FloatField()),
                ('bottomdepth', models.FloatField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activity')),
                ('instantpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.instantpoint')),
                ('nominallocation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stoqs.nominallocation')),
            ],
            options={
                'verbose_name': 'Simple bottom depth time series',
                'verbose_name_plural': 'Simple bottom depth time series',
            },
        ),
        migrations.AddField(
            model_name='sample',
            name='samplepurpose',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='stoqs.samplepurpose'),
        ),
        migrations.AddField(
            model_name='sample',
            name='sampletype',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='stoqs.sampletype'),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(max_length=128, null=True)),
                ('value', models.TextField(null=True)),
                ('uristring', models.CharField(max_length=256, null=True)),
                ('resourcetype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stoqs.resourcetype')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('name', models.CharField(max_length=128)),
                ('color', models.CharField(blank=True, max_length=8, null=True)),
                ('platformtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.platformtype')),
            ],
            options={
                'verbose_name': 'Platform',
                'verbose_name_plural': 'Platforms',
            },
        ),
        migrations.CreateModel(
            name='PlannedDepthTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epochmilliseconds', models.FloatField()),
                ('depth', models.FloatField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activity')),
            ],
            options={
                'verbose_name': 'Planned depth time series',
                'verbose_name_plural': 'Planned depth time series',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth', models.FloatField(db_index=True)),
                ('bottomdepth', models.FloatField(db_index=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('instantpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.instantpoint')),
                ('nominallocation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stoqs.nominallocation')),
            ],
            options={
                'verbose_name': 'Measurement',
                'verbose_name_plural': 'Measurements',
                'unique_together': {('instantpoint', 'depth', 'geom')},
            },
        ),
        migrations.CreateModel(
            name='MeasuredParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datavalue', models.FloatField(db_index=True, null=True)),
                ('dataarray', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), null=True, size=None)),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.measurement')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.parameter')),
            ],
            options={
                'verbose_name': 'Measured Parameter',
                'verbose_name_plural': 'Measured Parameter',
                'unique_together': {('measurement', 'parameter')},
            },
        ),
        migrations.CreateModel(
            name='CampaignLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('timevalue', models.DateTimeField(db_index=True)),
                ('message', models.CharField(max_length=2048)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('depth', models.FloatField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.campaign')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.resource')),
            ],
            options={
                'verbose_name': 'Campaign Log',
                'verbose_name_plural': 'Campaign Logs',
            },
        ),
        migrations.CreateModel(
            name='ActivityParameterHistogram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('binlo', models.FloatField()),
                ('binhi', models.FloatField()),
                ('bincount', models.IntegerField()),
                ('activityparameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activityparameter')),
            ],
        ),
        migrations.AddField(
            model_name='activityparameter',
            name='parameter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.parameter'),
        ),
        migrations.AddField(
            model_name='activity',
            name='activitytype',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='stoqs.activitytype'),
        ),
        migrations.AddField(
            model_name='activity',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stoqs.campaign'),
        ),
        migrations.AddField(
            model_name='activity',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.platform'),
        ),
        migrations.CreateModel(
            name='SampleResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.resource')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.sample')),
            ],
            options={
                'verbose_name': 'Sample Resource',
                'verbose_name_plural': 'Sample Resource',
                'unique_together': {('sample', 'resource')},
            },
        ),
        migrations.CreateModel(
            name='SampleRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='stoqs.sample')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='stoqs.sample')),
            ],
            options={
                'verbose_name': 'Sample Relationship',
                'verbose_name_plural': 'Sample Relationships',
                'unique_together': {('parent', 'child')},
            },
        ),
        migrations.CreateModel(
            name='SampledParameterResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activity')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.resource')),
                ('sampledparameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.sampledparameter')),
            ],
            options={
                'verbose_name': 'SampledParameter Resource',
                'verbose_name_plural': 'SampledParameter Resource',
                'unique_together': {('sampledparameter', 'resource')},
            },
        ),
        migrations.CreateModel(
            name='ResourceResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('fromresource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toresource', to='stoqs.resource')),
                ('toresource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromresource', to='stoqs.resource')),
            ],
            options={
                'verbose_name': 'Resource Resource',
                'verbose_name_plural': 'Resource Resource',
                'unique_together': {('fromresource', 'toresource')},
            },
        ),
        migrations.CreateModel(
            name='PlatformResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.platform')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.resource')),
            ],
            options={
                'verbose_name': 'Platform Resource',
                'verbose_name_plural': 'Platform Resource',
                'unique_together': {('platform', 'resource')},
            },
        ),
        migrations.CreateModel(
            name='ParameterResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.parameter')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.resource')),
            ],
            options={
                'verbose_name': 'Parameter Resource',
                'verbose_name_plural': 'Parameter Resource',
                'unique_together': {('parameter', 'resource')},
            },
        ),
        migrations.CreateModel(
            name='ParameterGroupParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.parameter')),
                ('parametergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.parametergroup')),
            ],
            options={
                'verbose_name': 'ParameterGroup Parameter',
                'verbose_name_plural': 'ParameterGroup Parameter',
                'unique_together': {('parametergroup', 'parameter')},
            },
        ),
        migrations.CreateModel(
            name='MeasuredParameterResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activity')),
                ('measuredparameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.measuredparameter')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.resource')),
            ],
            options={
                'verbose_name': 'MeasuredParameter Resource',
                'verbose_name_plural': 'MeasuredParameter Resource',
                'unique_together': {('measuredparameter', 'resource')},
            },
        ),
        migrations.CreateModel(
            name='CampaignResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.campaign')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.resource')),
            ],
            options={
                'verbose_name': 'Campaign Resource',
                'verbose_name_plural': 'Campaign Resource',
                'unique_together': {('campaign', 'resource')},
            },
        ),
        migrations.CreateModel(
            name='ActivityResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', stoqs.stoqs.models.UUIDField(editable=False, max_length=32)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.activity')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoqs.resource')),
            ],
            options={
                'verbose_name': 'Activity Resource',
                'verbose_name_plural': 'Activity Resource',
                'unique_together': {('activity', 'resource')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='activityparameter',
            unique_together={('activity', 'parameter')},
        ),
    ]
