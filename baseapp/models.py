from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Member(models.Model):
    # null=False, blank = False by default
    # addedByUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    # addressStreet = models.CharField(max_length=100, null=True, blank=True)
    addressLocation = models.CharField(
        max_length=100)
    # state = models.CharField(max_length=100, null=True, blank=True)
    # country = models.CharField(max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)  # stores date & time
    isOrganizationMember = models.BooleanField(default=False)
    bloodGroup = models.CharField(max_length=100, null=True, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)

    # updatedAt = models.DateTimeField()  #stores date & time
    # AssignedActivity = models.ForeignKey(
    #     OrganizationPosts, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['createdAt']


class Organization(models.Model):
    # null=False, blank = False by default
    # addedByUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    # addressStreet = models.CharField(max_length=100, null=True, blank=True)
    addressLocation = models.CharField(
        max_length=100)
    # state = models.CharField(max_length=100, null=True, blank=True)
    # country = models.CharField(max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)  # stores date & time
    isOrganizationMember = models.BooleanField(default=True)
    yearOfEstablishment = models.DateField(null=True, blank=True)
    chairman = models.CharField(max_length=100, null=True, blank=True)
    # updatedAt = models.DateTimeField()  #stores date & time
    # Activities = models.ForeignKey(
    #  OrganizationPosts, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email


class OrganizationPosts(models.Model):
    # null=False, blank = False by default
    postedByOrganization = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    postedByOrganizationEmail = models.CharField(
        max_length=100)
    MemberSelected = models.ForeignKey(
        Member, on_delete=models.SET_NULL, null=True, blank=True)
    requirementInformation = models.CharField(max_length=100)
    # addressStreet = models.CharField(max_length=100, null=True, blank=True)
    addressLocation = models.CharField(
        max_length=100)
    # state = models.CharField(max_length=100, null=True, blank=True)
    # country = models.CharField(max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)  # stores date & time
    # updatedAt = models.DateTimeField()  #stores date & time

    def __str__(self):
        return self.requirementInformation

    class Meta:
        ordering = ['createdAt']


class VideoPosts(models.Model):
    # null=False, blank = False by default
    postedByOrganization = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, null=True)
    # _id = models.AutoField(primary_key=True, editable=False)
    postedByOrganizationEmail = models.CharField(
        max_length=100, null=True, blank=True)
    MemberSelected = models.ForeignKey(
        Member, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    # addressStreet = models.CharField(max_length=100, null=True, blank=True)
    # addressLocation = models.CharField(
    #     max_length=100)
    # state = models.CharField(max_length=100, null=True, blank=True)
    # country = models.CharField(max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)  # stores date & time
    # updatedAt = models.DateTimeField()  #stores date & time

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['createdAt']
