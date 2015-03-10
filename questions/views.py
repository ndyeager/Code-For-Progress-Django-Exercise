from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Loads form Class from the form.py file
from .forms import CommentForm
# Loads the Comment and Question models for the models.py file
from .models import Comment, Question

# Creates the view for the homepage
def home(request):
	# creates a variable to hold all the questions from the Questions model
	# and order them decending
	question_list = Question.objects.order_by('-pub_date')[:5]
	# Assigns home.html as the template for this view
	template = "home.html"
	# Takes the varible above and allows it to be injected into the template
	context = {'question_list': question_list}
	# Renders the template and passes the question_list variable into the page
	return render(request, template, context)

# Create the view for the question details page
def detail(request, question_id):
	# Assigns the the questions Primary Key to the the variable "question"
	question = get_object_or_404(Question, pk=question_id)
	# Assigns the CommentForm from the CommentForm Class to the "form" if theres
	# input. If not, will flash error message in view.
	form = CommentForm(request.POST or None)
	# Checks if form is valid
	if form.is_valid():
		# If form is valid then comment is saved to database using the 'question' variable
		# assigned earlier to insure comment is assigned to appropiate question
		comment = question.comment_set.create(comment=request.POST['comment'])
		# Redirects user to the current page, essentially reloading the page
		return HttpResponseRedirect(reverse('questions.views.detail', args=(question.id,)))
	# Assigns "detail.html" as the template for the view
	template = "detail.html"
	# Takes the 'form' and 'question' and injects them into the page
	context = {"form": form, 'question': question}
	# Renders the template and passes the "CommentForm" and "question" variable
	return render(request, template, context)
