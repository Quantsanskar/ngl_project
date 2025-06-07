from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Question

def get_client_ip(request):
    """Get the client's IP address"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    """Main page with question form"""
    return render(request, 'questions/index.html')

@csrf_exempt
@require_http_methods(["POST"])
def submit_question(request):
    """Handle question submission"""
    try:
        data = json.loads(request.body)
        question_text = data.get('question', '').strip()
        name = data.get('name', '').strip()
        is_anonymous = data.get('is_anonymous', True)
        
        if not question_text:
            return JsonResponse({'success': False, 'error': 'Question cannot be empty'})
        
        # Get client IP
        ip_address = get_client_ip(request)
        
        # Create question
        question = Question.objects.create(
            question_text=question_text,
            ip_address=ip_address,
            name=name if not is_anonymous and name else None,
            is_anonymous=is_anonymous
        )
        
        return JsonResponse({
            'success': True, 
            'message': 'Question submitted successfully!'
        })
        
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def view_questions(request):
    """Admin page to view all questions"""
    questions = Question.objects.all()
    return render(request, 'questions/view_questions.html', {'questions': questions})
