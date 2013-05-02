from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
#from django.template import Context, loader
from django.shortcuts import render

from exam.models import UserDetail, Question
import random

question_set = []
level = 0
correct=True
MAX_LEVEL = 4

#/exam/details/True
def details(request):
    global question_set
    global level
    global correct
    if correct:
        level = level+1
        if level > MAX_LEVEL:
            context = {'question':'', 'message':'You have successfully completed the test!!'}
            return render(request, 'exam/details.html', context)
        question_set = Question.objects.filter(level=level)
        question_set = list(question_set)
        
    if not len(question_set):
        #if questions for a set finishes
        context = {'question':'', 'message':'You can still improve. Ended up at level %s!!' %(level) }
        return render(request, 'exam/details.html', context)
        
    rand = random.randint(0, len(question_set)-1)
    question = question_set[rand]
    question_set.pop(rand)
    rand = random.randint(0, 3)
    choice_set = [question.option1, question.option2, question.option3]
    choice_set.insert(rand, question.answer)
    context = {'question': question, 'choice_set': choice_set}
    return render(request, 'exam/details.html', context)
    
def check(request, ques_id):
    question = Question.objects.get(id=ques_id)
    ans = request.POST['choice']
    global correct
    if question.answer == ans:
        correct = True
        return HttpResponseRedirect(reverse('exam:details'))
    else:
        correct = False
        return HttpResponseRedirect(reverse('exam:details'))
        
def index(request):
    questions_list = Question.objects.all()
    context = {'questions_list': questions_list}
    return render(request, 'exam/index.html', context)
    #template = loader.get_template('exam/index.html')
    #context = Context({
    #    'questions_list': questions_list,
    #})
    #return HttpResponse(template.render(context))
