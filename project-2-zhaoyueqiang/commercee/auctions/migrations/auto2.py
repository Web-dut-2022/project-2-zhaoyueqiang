
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', 'auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(),
        ),
    ]
