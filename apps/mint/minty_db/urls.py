from django.urls import path

from . import views

app_name = "minty_db"

urlpatterns = [
    # Landing page
    path("", views.landing, name="landing"),
    # Items
    path("items/", views.ItemListView.as_view(), name="item_list"),
    path("items/<uuid:uuid>/", views.ItemDetailView.as_view(), name="item_detail"),
    # Mobs
    path("mobs/", views.MobListView.as_view(), name="mob_list"),
    path("mobs/<uuid:uuid>/", views.MobDetailView.as_view(), name="mob_detail"),
    # Classes
    path("classes/", views.ClassListView.as_view(), name="class_list"),
    path("classes/<uuid:uuid>/", views.ClassDetailView.as_view(), name="class_detail"),
    # Jobs
    path("jobs/", views.JobListView.as_view(), name="job_list"),
    path("jobs/<uuid:uuid>/", views.JobDetailView.as_view(), name="job_detail"),
    # Skills
    path("skills/", views.SkillListView.as_view(), name="skill_list"),
    path("skills/<uuid:uuid>/", views.SkillDetailView.as_view(), name="skill_detail"),
    # NPCs
    path("npcs/", views.NPCListView.as_view(), name="npc_list"),
    path("npcs/<uuid:uuid>/", views.NPCDetailView.as_view(), name="npc_detail"),
    # Quests
    path("quests/", views.QuestListView.as_view(), name="quest_list"),
    path("quests/<uuid:uuid>/", views.QuestDetailView.as_view(), name="quest_detail"),
    # Maps
    path("maps/", views.MapListView.as_view(), name="map_list"),
    path("maps/<uuid:uuid>/", views.MapDetailView.as_view(), name="map_detail"),
]
