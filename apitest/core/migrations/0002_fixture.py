from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_endpoint_project'),
    ]

    def generate_projects(apps, schema_editor):
        Project = apps.get_model("core", "Project")
        Endpoint = apps.get_model("core", "Endpoint")

        test_project = Project(
            name="Test", base_url="localhost:8000", slug="test",
            desc="Test project"
        )
        test_project.save()
        best_project = Project(
            name="Best", base_url="localhost:9000", slug="best",
            desc="Best project"
        )
        best_project.save()

        Endpoint(name="login", url="/api/login", project=test_project).save()
        Endpoint(name="logout", url="/api/logout", project=test_project).save()

        Endpoint(name="login", url="/api/login", project=best_project).save()
        Endpoint(name="logout", url="/api/logout", project=best_project).save()

    operations = [
        migrations.RunPython(generate_projects),
    ]
