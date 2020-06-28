from django.shortcuts import render
from pro_app.models import *

# Create your views here.
def home(request):
    """ Display home page """

    # load about
    about = []
    for elt in About.objects.filter(abo_display=True).order_by('abo_order'):
        temp = []
        temp.append(elt.abo_icon)
        temp.append(elt.abo_title)
        temp.append(elt.abo_description)
        about.append(temp)

    # load experience
    experience = []
    for elt in Experience.objects.filter(exp_display=True).order_by('exp_order'):
        temp = []
        temp.append(elt.exp_start.strftime('%b %Y'))
        temp.append(elt.exp_stop.strftime('%b %Y'))
        temp.append(elt.exp_poste)
        temp.append(elt.exp_compagny_name)
        temp.append(elt.exp_geo)
        experience.append(temp)

    # load project
    project = []
    row = []
    nb_pro = 0
    for elt in Projet.objects.filter(pro_display=True).order_by('pro_order'):
        temp = []
        temp.append(elt.pro_title)
        temp.append(elt.pro_description)
        temp.append(elt.pro_github)
        temp.append(elt.pro_skill)
        row.append(temp)
        nb_pro += 1
        if nb_pro == 2:
            nb_pro = 0
            project.append(row)
            row = []

    if nb_pro == 1:
        project.append(row)

    # load skills
    skill = []
    for elt in Skill.objects.filter(ski_display=True).order_by('ski_order'):
        temp = []
        temp.append(elt.ski_name)
        temp.append(elt.ski_level)
        skill.append(temp)

    # load study
    study = []
    for elt in Study.objects.filter(stu_display=True).order_by('stu_order'):
        temp = []
        temp.append(elt.stu_str_date)
        temp.append(elt.stu_description)
        temp.append(elt.stu_organisme)
        study.append(temp)

    # load references
    ref = []
    for elt in Reference.objects.filter(ref_display=True).order_by('ref_order'):
        temp = []
        temp.append(elt.ref_description)
        temp.append(elt.ref_auteur)
        ref.append(temp)

    return render(request, 'home.html', {'about': about, \
    'experience': experience, \
    'project': project, \
    'skill': skill, \
    'study': study, \
    'ref': ref})

def coming_soon(request):
    """ Display coming_soon page """
    return render(request, 'coming_soon.html')
