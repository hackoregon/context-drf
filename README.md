# context-drf

#### _An implementation of the Context spec for Django REST Framework_

The Context spec serves to capture metadata about a dataset to contextualize any usage of said data. No data is "raw", no data is "pure", it all comes from somewhere, and the more we understand the source, the better we can analyze and challenge any reporting thereof.

## Using Context with Django REST Framework

The `context-drf` addon will automatically load context files from the `context_sources` directory when your Django app starts. The Context spec requires that every context source is individually addressable, so the Context URLs will need to be added to your Django app. This will add endpoints for requesting, one, many, or all context sources as JSON.

Next, context files need to be associated with your Django models via a new `Context` class in the model class.

```py
from django.db import models


class Rides(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    segment = models.CharField(max_length=256, blank=True, null=True)
    trips = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rides'

    class Context:
        sources = [ 'scooters' ]
```

Note that since a single model can be the result of many data sources, `sources` is a list.

Once a context file is associated with a class, you can use a Context mixin to automatically annotate a `ViewSet` with compliant Context metadata, including links directly to the API endpoints for the associated context sources.

## Customizing API Responses

THe Context spec has strict requirements for how context sources need to be laid out in API responses, so it's strongly encouraged to stick with the Context mixins, but in the event that the mixins do not suffice, context source files can be retrieved as `dict`s from the Context app config.

```py
from django.apps import apps

slug = 'context_file_name'
file_contents = apps.get_app_config('context').source(slug)
```
