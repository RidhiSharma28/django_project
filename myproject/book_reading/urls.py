from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bookreading_home'),  # Home page for book reading
    path('FamilyBusiness.html', views.family_business, name='family_business'),  # Family Business page
    path('1984.html', views.book_1984, name='book_1984'),  # 1984 book page
    path('LoveAtWildHarbour.html', views.love_at_wild_harbour, name='love_at_wild_harbour'),
    path('TheGreatGatsby.html', views.great_gatsby, name='great_gatsby'),
    path('ToKillAMockingbird.html', views.to_kill_mockingbird, name='to_kill_mockingbird'),
    path('StoneRaidersReturn.html', views.stone_raiders_return, name='stone_raiders_return'),
    path('TheBicycleBookClub.html', views.bicycle_book_club, name='bicycle_book_club'),
    path('TheKingsStone.html', views.kings_stone, name='kings_stone'),
    # Chapter URLs
    path('1c1.html', views.chapter_1, name='chapter_1'),
    path('1c2.html', views.chapter_2, name='chapter_2'),
    path('1c3.html', views.chapter_3, name='chapter_3'),
    path('1c4.html', views.chapter_4, name='chapter_4'),
    path('1c5.html', views.chapter_5, name='chapter_5'),
]
