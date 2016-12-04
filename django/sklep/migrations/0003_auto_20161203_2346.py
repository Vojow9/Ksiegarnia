from django.db import models, migrations

def combine_names(apps, schema_editor):
  
    Book = apps.get_model("sklep", "Book")
    for book in Book.objects.all():
        book.variations = "%s %s" % (book.variations)
        book.save()

class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]