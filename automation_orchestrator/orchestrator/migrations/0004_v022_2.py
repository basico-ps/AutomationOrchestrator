# Generated by Django 3.0.3 on 2020-02-27 08:03

from django.db import migrations, models
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orchestrator', '0003_v022_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filetrigger',
            name='bot',
            field=models.ForeignKey(help_text='Select the bot for this trigger.', null=True, on_delete=models.deletion.PROTECT, to='orchestrator.Bot'),
        ),
        migrations.AlterField(
            model_name='scheduletrigger',
            name='bot',
            field=models.ForeignKey(help_text='Select the bot for this trigger.', null=True, on_delete=models.deletion.PROTECT, to='orchestrator.Bot'),
        ),
        migrations.AlterField(
            model_name='emailimaptrigger',
            name='bot',
            field=models.ForeignKey(help_text='Select the bot for this trigger.', null=True, on_delete=models.deletion.PROTECT, to='orchestrator.Bot'),
        ),
        migrations.AlterField(
            model_name='emailoutlooktrigger',
            name='bot',
            field=models.ForeignKey(help_text='Select the bot for this trigger.', null=True, on_delete=models.deletion.PROTECT, to='orchestrator.Bot'),
        ),
        migrations.AlterField(
            model_name='apitrigger',
            name='bot',
            field=models.ForeignKey(help_text='Select the bot for this trigger.', null=True, on_delete=models.deletion.PROTECT, to='orchestrator.Bot'),
        ),
        migrations.AddField(
            model_name='apitrigger',
            name='bots',
            field=sortedm2m.fields.SortedManyToManyField(help_text='Select the bots for this trigger.', related_name='api_trigger_bot', to='orchestrator.Bot'),
        ),
        migrations.AddField(
            model_name='emailimaptrigger',
            name='bots',
            field=sortedm2m.fields.SortedManyToManyField(help_text='Select the bots for this trigger.', related_name='email_imap_trigger_bot', to='orchestrator.Bot'),
        ),
        migrations.AddField(
            model_name='emailoutlooktrigger',
            name='bots',
            field=sortedm2m.fields.SortedManyToManyField(help_text='Select the bots for this trigger.', related_name='email_outlook_trigger_bot', to='orchestrator.Bot'),
        ),
        migrations.AddField(
            model_name='filetrigger',
            name='bots',
            field=sortedm2m.fields.SortedManyToManyField(help_text='Select the bots for this trigger.', related_name='file_trigger_bot', to='orchestrator.Bot'),
        ),
        migrations.AddField(
            model_name='scheduletrigger',
            name='bots',
            field=sortedm2m.fields.SortedManyToManyField(help_text='Select the bots for this trigger.', related_name='schedule_trigger_bot', to='orchestrator.Bot'),
        ),
    ]
