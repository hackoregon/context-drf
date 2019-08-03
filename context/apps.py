from os import listdir, getcwd, path
from django.apps import AppConfig
from .context import parse

class ContextConfig(AppConfig):
    name = 'context'
    verbose_name = "Context"
    data_sources = dict()

    def ready(self):
      prefix = './context/context_sources'
      filenames = listdir(prefix)
      filenames = [x for x in filenames if x.endswith('.context.yml')]
      print("\nLoading context files...")
      for f in filenames:
        slug = f.split('.context.yml')[0]
        with open(path.join(prefix, f)) as ctx:
          record = parse(ctx.read())
          self.data_sources[slug] = record
          print("  => %s" % f)
      print("")

    def source(self, slug):
      return self.data_sources[slug]
      # apps.get_app_config('context').source(:slug)

    def all(self):
      return self.data_sources