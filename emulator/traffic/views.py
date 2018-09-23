from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):

    s = "You are at the test Top Level Page with links to: <br /><br />"
    s = s + '<a href="test_cases">Test Case Editor...</a><br />'
    s = s + '<a href="login">Login</a><br />'
    s = s + '<a href="map">View Ongoing Tests</a><br />'
    s = s + '<a href="analysis">Test Analysis</a><br />'
    return HttpResponse(s)

def test_cases(request):
    s = "You are at the test Top Level Test Controller showing all test for the current user.<br /><br />"
    s = s + '<a href="test_edit">Add/del/edit individual test case</a><br />'
    s = s + '<a href="vehicles">Add/del/edit vehicles</a><br />'
    s = s + '<a href="drivers">Add/del/edit driver profiles</a><br />'
    s = s + '<a href="v2x_app">Register V2X apps</a><br />'        
    return HttpResponse(s)

def test_edit(request):
    s = "You are at the edit individual test. All routes will show here<br /><br />"
    s = s + '<a href="edit_route">Add/del/edit routes</a><br />'
    return HttpResponse(s)
    
def vehicles(request):
    return HttpResponse("You are at the edit vehicles page. Choosing vehicles/editing will happend here.")

def drivers(request):
    return HttpResponse("You are at the edit drivers profiles page. Choosing driver will happen here.")

def v2x_app(request):
    return HttpResponse("You are at the V2X appplication edit page. Choosing V2X connectivity will happen here.")
    
def map(request):
    return HttpResponse("You are at the map top level. Viewing Open Map magic happens here")

def analysis(request):
    return HttpResponse("You are at the test analysis view. Statistics Will Show here")
    
def edit_route(request):

    s = "You are at the route edit page.<br /><br />"
    s = s + '<a href="schedule">Set traffic schedule</a><br />'
    s = s + '<a href="vehicles">Connect Vehicles to Route</a><br />'
    s = s + '<a href="v2x_app">Connect V2X apps</a><br />'

    return HttpResponse(s)
    
def schedule(request):
    return HttpResponse("You are at the route traffic schedule.")
    
def login(request):
    return HttpResponse("You are at the login page.")    