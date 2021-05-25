from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.template import RequestContext

from characters.forms.powers_form import Power_form
from characters.models import Powers


def set_power(request, _id):

    return