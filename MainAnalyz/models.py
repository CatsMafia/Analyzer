from django.db import models

POS = (
    ('FH','Forehead'),
    ('NS','Nose'),
    ('TE','Teeth'),
    ('CH', 'Chest'),
    ('AR','Arm'),
    ('ST', 'Stomach'),
    ('RS','Rightside'),
    ('LS', 'Leftside'),
    ('GR','Groin'),
    ('KN','Knees'),
    ('AK','Ankle'),

)


INTEN = {
    ('M','Mild'),
    ('A','Average'),
    ('S','Strong'),
    ('T','Terrible'),
}


TYPE_MEDICINE = {
    ('PO','Powders'),
    ('TB','Granules'),
    ('OM','Ointment'),
    ('SP','Suppository'),
    ('PL','Plasters'),
    ('LQ','LiquidPrepartions'),
}


class Symptom(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=2,choices=POS)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=2,choices=POS)
    intensive = models.CharField(max_length=1,choices=INTEN)
    symptom = models.ManyToManyField(Symptom)

    def __str__(self):
        return self.name



class Medicine(models.Model):
    name = models.CharField(max_length=30)
    activeSubstance = models.CharField(max_length=30)
    type = models.CharField(max_length=2,choices=TYPE_MEDICINE)
    amountOfSubstance = models.FloatField()
    disease = models.ManyToManyField(Disease)
    age = models.IntegerField()
    sex = models.IntegerField()
    def __str__(self):
        return self.name
