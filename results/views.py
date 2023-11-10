from django.shortcuts import render, redirect
from .models import AnnouncedPUResult, PollingUnit, Lga, Party, Result
from .forms import ResultForm
from django.db.models import Sum
from django.views import View

# create your views

def get_all_results(request):
    # Query all results from the AnnouncedPuResult model
    results = AnnouncedPUResult.objects.all()

    # You can now pass the 'results' queryset to your template
    return render(request, 'result.html', {'results': results})


def get_polling_unit_results(request, polling_unit_uniqueid):
    # Query results for the specified polling unit
    results = AnnouncedPUResult.objects.filter(polling_unit_uniqueid=polling_unit_uniqueid)

    # Check if the polling unit exists; return a 404 response if not
    if not results.exists():
        return render(request, 'polling_unit_not_found.html')  # Create a template for this case if needed

    # You can now pass the 'results' queryset and 'polling_unit_uniqueid' to your template
    return render(request, 'eachresult.html', {'results': results, 'polling_unit_uniqueid': polling_unit_uniqueid})


def local_government_result(request):
    lgas = Lga.objects.all()
    selected_lga_id = request.GET.get('lga', None)

    if selected_lga_id:
        selected_lga = Lga.objects.get(lga_id=selected_lga_id)
        polling_units = PollingUnit.objects.filter(lga_id=selected_lga_id)
        total_votes = polling_units.aggregate(Sum('polling_unit_id'))['polling_unit_id__sum']
    else:
        selected_lga = None
        polling_units = None
        total_votes = None

    context = {
        'lgas': lgas,
        'selected_lga': selected_lga,
        'polling_units': polling_units,
        'total_votes': total_votes,
    }

    return render(request, 'lgasum_result.html', context)


# def result_entry(request):
#     selected_party_ids = None  # Default value

#     if request.method == 'POST':
#         form = ResultEntryForm(request.POST)
#         if form.is_valid():
#             # Process the form data and save results to the database
#             polling_unit_number = form.cleaned_data['polling_unit_number']
#             selected_party_ids = form.cleaned_data['party_results']

#             # Assuming selected_party_ids is a list of party IDs
#             selected_parties = Party.objects.filter(id__in=selected_party_ids)

#             # Save the results to the database (you need to implement this part)
#             for party in selected_parties:
#                 Result.objects.create(
#                     polling_unit_number=polling_unit_number,
#                     party=party,
#                     # Add any other fields you need to save
#                 )

#             # Extract the partyids from the list of Party objects
#             selected_party_ids = [str(party.partyid) for party in selected_parties]

#             # Join the partyids into a comma-separated string
#             party_ids_str = ','.join(selected_party_ids)

#             return redirect('success_page', selected_parties=selected_parties)

#     else:
#         form = ResultEntryForm()

#     return render(request, 'result_entry.html', {'form': form, 'selected_party_ids': selected_party_ids})


# def success_page(request, selected_parties=None):
#     selected_parties = selected_parties.split(',')
#     results = Result.objects.filter(party__partyid__in=selected_parties)
#     return render(request, 'success_page.html', {'selected_parties': selected_parties})



class AddResultsView(View):
    template_name = 'add_results.html'

    def get(self, request, polling_unit_id):
        parties = Party.objects.all()
        polling_units = PollingUnit.objects.filter(polling_unit_id=polling_unit_id)

        # Handle the case where there are multiple polling units with the same ID
        if polling_units.exists():
            polling_unit = polling_units.first()
        else:
            # Handle the case where no polling unit with the given ID is found
            # You might want to customize this part based on your specific requirements
            return render(request, 'polling_unit_not_found.html', {'polling_unit_id': polling_unit_id})

        form = ResultForm()
        return render(request, self.template_name, {'parties': parties, 'polling_unit': polling_unit, 'form': form})

    def post(self, request, polling_unit_id):
        form = ResultForm(request.POST)

        if form.is_valid():
            result = form.save(commit=False)
            result.polling_unit = PollingUnit.objects.get(polling_unit_id=polling_unit_id)
            result.save()
            return redirect('success_page')

        parties = Party.objects.all()
        polling_unit = PollingUnit.objects.get(polling_unit_id=polling_unit_id)
        return render(request, self.template_name, {'parties': parties, 'polling_unit': polling_unit, 'form': form})
