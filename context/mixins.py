from django.apps import apps

class ContextViewSet():
    """
    Adds the `context` root-level property to the API response
    """
    # TODO: This is a very brittle proof of concept. This needs to guard against
    # Models that don't have a Context class among other things.
    def list(self, request):
        res = super().list(self, request)
        query = self.get_queryset()
        contextConfig = apps.get_app_config('context')
        baseUrl = request.build_absolute_uri('/context/')

        sources = [{
            'name': x,
            'link': baseUrl + x,
            'source': contextConfig.source(x)
        } for x in query.model.Context.sources]

        res.data['context'] = dict({
            'sources': sources
        })

        return res

# Mixin for an individual object
# ContextResponse that takes a response and a list of classes