import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livo.settings')
django.setup()

from househelp.models import SkillTag
print(f"SkillTags: {SkillTag.objects.all().count()}")
for skill in SkillTag.objects.all():
    print(f"- {skill.name}")

from users.models import PreferenceTag
print(f"PreferenceTags: {PreferenceTag.objects.all().count()}")
