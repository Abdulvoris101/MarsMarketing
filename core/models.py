from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Company(models.Model):
    image = models.ImageField(upload_to='companies/')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


    def __str__(self):
        return self.image.name

class Project(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    image = models.ImageField(upload_to='projects/', verbose_name='Rasm')
    category = models.ManyToManyField(Category, related_name='projects')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='image_projects/', blank=True, null=True)


    class Meta:
        ordering = ('id', )
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'


    def __str__(self):
        return f'{self.id}-{self.project.title}'


class Result(models.Model):
    experience = models.IntegerField('Tajriba')
    clients = models.IntegerField('Mijozlar')
    projects = models.IntegerField('Proyektlar')
    team = models.IntegerField('Jamoa Soni')

class SmmProject(models.Model):
    image = models.ImageField(upload_to='smm_projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.image.name}'

class ReceiveContact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ism')
    email = models.EmailField(max_length=255)
    company = models.CharField(max_length=255, verbose_name='Kompaniya nomi')
    phone = models.CharField(max_length=255, verbose_name='Telefon Nomer')
    message = models.TextField(verbose_name='Xabar', blank=True, null=True)

    def __str__(self):
        return f'Request-{self.name}'

class ContactUs(models.Model):
    address = models.CharField(verbose_name='Address', max_length=255, blank=True)
    email_address = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=255, verbose_name='Phone', blank=True)
    working_hours = models.CharField(max_length=255, verbose_name='Ish vaqti')
    
    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Infos'
    
    def __str__(self):
        return self.address