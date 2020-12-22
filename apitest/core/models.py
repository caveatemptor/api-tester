from django.db import models


class Project(models.Model):
    """All endpoints grouped"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    base_url = models.URLField(max_length=255)

    def __str__(self):
        return f"<Project: {self.name}>"


class Endpoint(models.Model):
    """URL resource to test"""
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="endpoints")

    def __str__(self):
        return f"<Endpoint: {self.name}:{self.url}>"
