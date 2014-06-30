from django.db import models

#simple kinda wrapper to keep track of skills
class Skill(models.Model):
		UID = models.AutoField()
		skillName = models.CharField(max_length = 25)
		def __unicode__():
			return self.skillName
			
# IITB students who will use the portal		
class User(models.Model):
		UID = models.AutoField()
		name = models.CharField(max_length = 40) #long name for gulti junta :P
		email = models.EmailField()
		roll = models.CharField(max_length = 10) #for LDAP roll number
		skills = models.ManyToManyField(Skill)
		phone = models.CharField(max_length=14) #if someone tries to give +91 and stuff
		def __unicode__():
			return self.name

#the startups		
class Company(models.Model):
		UID = models.AutoField()
		email = models.EmailField()
		website = models.URLField()
		name = models.CharField(max_length = 20)
		founders = models.TextField()
		founderDelimiter = '`' #use backquote for delimiter, and .split('`') to get it back
		def getFounders(self):
			return founders.founders.split('`')
		chat = models.TextField() #simple way to store the chat
		def __unicode__():
			return self.name

#the jobs themselves
class Job(models.Model):
		UID = models.AutoField()
		subject = models.CharField(max_length = 100)
		description = models.TextField()
		company = models.ForeignKey(Company)
		skills = models.ManyToManyField(Skill)
		def __unicode__():
			return self.subject + self.company.name
