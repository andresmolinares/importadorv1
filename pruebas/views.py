from django.shortcuts import render
from tablib import Dataset
# Create your views here.
from pruebas.resource import PersonResource


def importer(request):
    # template = loader.get_template('export/importar.html')
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        print(dataset)
        new_persons = request.FILES['xlsfile']
        print(new_persons)
        imported_data = dataset.load(new_persons.read())
        print(dataset)
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
        person_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'export/index.html')
