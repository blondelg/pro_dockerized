from django.db import models

ORDER = [(a,a) for a in range(1,21)]

# Create your models here.
class About(models.Model):
    abo_icon = models.CharField(max_length=60)
    abo_title = models.CharField(max_length=30)
    abo_description = models.TextField()
    abo_order = models.IntegerField(choices=ORDER, default=20)
    abo_display = models.BooleanField(default=False)

    class Meta:
        verbose_name = "About"
        ordering = ['abo_order']

    def __str__(self):
        return self.abo_title

class Experience(models.Model):
    exp_compagny_name = models.CharField(max_length=30)
    exp_geo = models.CharField(max_length=30)
    exp_poste = models.CharField(max_length=60, default="")
    exp_start = models.DateField()
    exp_stop = models.DateField()
    exp_order = models.IntegerField(choices=ORDER, default=20)
    exp_display = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Experience"
        ordering = ['exp_order']

    def __str__(self):
        return self.exp_compagny_name

class Projet(models.Model):
    pro_title = models.CharField(max_length=30)
    pro_description = models.TextField()
    pro_github = models.CharField(max_length=100,null=True)
    pro_skill = models.CharField(max_length=100,null=True)
    pro_order = models.IntegerField(choices=ORDER, default=20)
    pro_display = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Projet"
        ordering = ['pro_order']

    def __str__(self):
        return self.pro_title

class Skill(models.Model):
    ski_name = models.CharField(max_length=30)
    ski_level = models.IntegerField(default=0)
    ski_order = models.IntegerField(choices=ORDER, default=20)
    ski_display = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Skill"
        ordering = ['ski_order']

    def __str__(self):
        return self.ski_name

class Study(models.Model):
    stu_str_date = models.CharField(max_length=30)
    stu_description = models.CharField(max_length=100,null=True)
    stu_organisme = models.CharField(max_length=100,null=True)
    stu_order = models.IntegerField(choices=ORDER, default=20)
    stu_display = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Study"
        ordering = ['stu_order']

    def __str__(self):
        return self.stu_description

class Reference(models.Model):
    ref_description = models.CharField(max_length=300,null=True)
    ref_auteur = models.CharField(max_length=100,null=True)
    ref_order = models.IntegerField(choices=ORDER, default=20)
    ref_display = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Reference"
        ordering = ['ref_order']

    def __str__(self):
        return self.ref_auteur
