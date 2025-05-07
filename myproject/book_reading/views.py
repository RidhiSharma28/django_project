from django.shortcuts import render

# Define the index view
def index(request):
    return render(request, 'secondapptemplates/bookreading_home.html')

def family_business(request):
    return render(request, 'secondapptemplates/FamilyBusiness.html')

def book_1984(request):
    return render(request, 'secondapptemplates/1984.html')

def love_at_wild_harbour(request):
    return render(request, 'secondapptemplates/LoveAtWildHarbour.html')

def great_gatsby(request):
    return render(request, 'secondapptemplates/TheGreatGatsby.html')

def to_kill_mockingbird(request):
    return render(request, 'secondapptemplates/ToKillAMockingbird.html')

def stone_raiders_return(request):
    return render(request, 'secondapptemplates/StoneRaidersReturn.html')

def bicycle_book_club(request):
    return render(request, 'secondapptemplates/TheBicycleBookClub.html')

def kings_stone(request):
    return render(request, 'secondapptemplates/TheKingsStone.html')

# Chapter views
def chapter_1(request):
    return render(request, 'secondapptemplates/1c1.html')

def chapter_2(request):
    return render(request, 'secondapptemplates/1c2.html')

def chapter_3(request):
    return render(request, 'secondapptemplates/1c3.html')

def chapter_4(request):
    return render(request, 'secondapptemplates/1c4.html')

def chapter_5(request):
    return render(request, 'secondapptemplates/1c5.html')
