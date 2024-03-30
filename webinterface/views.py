# webinterface/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .calculate import calculate_values
from django.views.generic import TemplateView
from django.contrib import messages

class DemandGenerationView(TemplateView):
    template_name = 'webinterface/demand_generation.html'

def success_view(request):
    # Render a success page or return an HttpResponse
    return render(request, 'webinterface/success.html')

def generate_demand(request):
    if request.method == "POST":
        # Call the function to calculate values
        branch_calculations = calculate_values(request.POST)
        
        # Now branch_calculations contains all your xbr* variables
        # Do something with the results, like storing them in the database
        
        # For now, let's redirect to a success page
        messages.success(request, 'Form submitted successfully!')
        return render(request, 'webinterface/demand_generation.html')
    else:
        # If it's not a POST request, just render the form
        return render(request, 'webinterface/demand_generation.html')
