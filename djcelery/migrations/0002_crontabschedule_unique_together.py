from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("djcelery", "0001_initial")]

    operations = [
        migrations.AlterUniqueTogether(
            name="crontabschedule", unique_together=("minute", "hour", "day_of_week", "day_of_month", "month_of_year")
        )
    ]
