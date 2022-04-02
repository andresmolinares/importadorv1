from import_export import resources

from pruebas.models import Person


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person