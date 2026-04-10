import uuid  # para valores hexadecimais aleatórios

from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


'''Está função cria um nome de hexadecimal para fazer o upload de fotos no sistema
   Em StdImageField('Image', upload_to=get_file_path, >> como visto no exemplo upload_to chama a função 
sem executar, ou seja sem o parentese
'''


class Base(models.Model):
    # só coloca valor ao criar
    created = models.DateField('Date of creation', auto_now_add=True)
    # atualiza valor ao atualizar objeto
    modify = models.DateField('Updated', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Services(Base):
    ICON_CHOISES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    service_title = models.CharField('Service', max_length=100)
    description = models.TextField('Description', max_length=300)
    icon = models.CharField('Icon', max_length=12, choices=ICON_CHOISES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service_title


class Position(Base):
    position = models.CharField('position', max_length=100)

    class Meta:
        verbose_name = 'position'
        verbose_name_plural = 'positions'

    def __str__(self):
        return self.position


class Member(Base):
    name = models.CharField('name', max_length=100)
    position = models.ForeignKey(
        'core.Position', verbose_name='Position', on_delete=models.CASCADE)  # remoção em cascata
    bio = models.TextField('Bio', max_length=300)
    image = StdImageField('Image', upload_to=get_file_path, variations={
                          # 480 é o tamanho da img do template já
                          'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    linkedin = models.CharField('LinkedIn', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.name

# Desafio de implementar as fetures


class Features(Base):
    ICON_CHOISES = (
        ('lni-rocket', 'Rocket'),
        ('lni-laptop-phone', 'Responsive'),
        ('lni-cog', 'Gear'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Layers'),
    )

    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', max_length=300)
    icon = models.CharField('Icon', max_length=16, choices=ICON_CHOISES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.name
