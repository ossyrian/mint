from django.shortcuts import render
from django.views.generic import ListView, DetailView

from minty_db.models import Item, Mob, MapleClass, Job, Skill, NPC, Quest, Map


def landing(request):
    """Landing page for MintyDB"""
    return render(request, "minty_db/landing.html")


# Item Views
class ItemListView(ListView):
    model = Item
    template_name = "minty_db/items/list.html"
    context_object_name = "items"
    paginate_by = 24


class ItemDetailView(DetailView):
    model = Item
    template_name = "minty_db/items/detail.html"
    context_object_name = "item"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


# Mob Views
class MobListView(ListView):
    model = Mob
    template_name = "minty_db/mobs/list.html"
    context_object_name = "mobs"
    paginate_by = 24


class MobDetailView(DetailView):
    model = Mob
    template_name = "minty_db/mobs/detail.html"
    context_object_name = "mob"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


# Class Views
class ClassListView(ListView):
    model = MapleClass
    template_name = "minty_db/classes/list.html"
    context_object_name = "classes"
    paginate_by = 24


class ClassDetailView(DetailView):
    model = MapleClass
    template_name = "minty_db/classes/detail.html"
    context_object_name = "class"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


# Job Views
class JobListView(ListView):
    model = Job
    template_name = "minty_db/jobs/list.html"
    context_object_name = "jobs"
    paginate_by = 24


class JobDetailView(DetailView):
    model = Job
    template_name = "minty_db/jobs/detail.html"
    context_object_name = "job"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


# Skill Views
class SkillListView(ListView):
    model = Skill
    template_name = "minty_db/skills/list.html"
    context_object_name = "skills"
    paginate_by = 24


class SkillDetailView(DetailView):
    model = Skill
    template_name = "minty_db/skills/detail.html"
    context_object_name = "skill"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


# NPC Views
class NPCListView(ListView):
    model = NPC
    template_name = "minty_db/npcs/list.html"
    context_object_name = "npcs"
    paginate_by = 24


class NPCDetailView(DetailView):
    model = NPC
    template_name = "minty_db/npcs/detail.html"
    context_object_name = "npc"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


# Quest Views
class QuestListView(ListView):
    model = Quest
    template_name = "minty_db/quests/list.html"
    context_object_name = "quests"
    paginate_by = 24


class QuestDetailView(DetailView):
    model = Quest
    template_name = "minty_db/quests/detail.html"
    context_object_name = "quest"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


# Map Views
class MapListView(ListView):
    model = Map
    template_name = "minty_db/maps/list.html"
    context_object_name = "maps"
    paginate_by = 24


class MapDetailView(DetailView):
    model = Map
    template_name = "minty_db/maps/detail.html"
    context_object_name = "map"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"
