from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def home(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isRequestFromHome = True
    return render(request, 'IndianCollegesApp/second_base_templet.html', {'firstState': firstState, 'allCitiesList': allCitiesList, 'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates, 'isRequestFromHome': isRequestFromHome})


def state(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isRequestFromHome = False
    return render(request, 'IndianCollegesApp/second_base_templet.html', {'selectedState': selectedState, 'allCitiesList': allCitiesList, 'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates, 'isRequestFromHome': isRequestFromHome})
