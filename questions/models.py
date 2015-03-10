from django.db import models

# Python classes used to defined the models
# Each model defines the table and data to be stored in the DB

# Defines a 'Question' Model and gives two pieces data which will be stored in the DB 
class Question(models.Model):
	# question is a Character Field with a max length of 200
	# and will hold the text of questions
	question = models.CharField(max_length=200)
	# pub_date is Date Time Field which will store the time and date
	# the question was created
	pub_date = models.DateTimeField('date published')

	# Allows us to call to the class as an object
	def __str__(self):
		return self.question

	# A method that determine if the question was recently created.
	def was_published_recently(self):
		# returns the publish 
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = "Published recently?"

# Defines a 'Comment' Model and gives data to be stored in the DB
class Comment(models.Model):
	# question is a Foreign Key, which allows the model to relate the comment to a question
	question = models.ForeignKey(Question)
	# comment is a Character Field with a max length of 200
	comment = models.CharField(max_length=200)

	# Allows us to call to the class as an object
	def __str__(self):
		return self.comment
