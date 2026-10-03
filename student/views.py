from django.shortcuts import render

def student_form(request):
    majors = ['Computer Science', 'Information Systems', 'Software Engineering', 'Cybersecurity', 'Data Science']
    standings = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#']

    if request.method == 'POST':
        name = request.POST.get('student_name', '').strip()
        student_id = request.POST.get('student_id', '').strip()
        
        errors = []
        if not name:
            errors.append("Student Name is required.")
        if not student_id:
            errors.append("Student ID is required.")
        
        if errors:
            return render(request, 'student/form.html', {
                'majors': majors,
                'standings': standings,
                'languages': languages,
                'errors': errors,
                'data': request.POST
            })
        
        context = {
            'student_name': name,
            'student_id': student_id,
            'major': request.POST.get('major'),
            'standing': request.POST.get('standing'),
            'prog_languages': request.POST.getlist('languages'),
            'grad_year': request.POST.get('grad_year'),
            'comments': request.POST.get('comments'),
        }
        return render(request, 'student/result.html', context)

    return render(request, 'student/form.html', {
        'majors': majors,
        'standings': standings,
        'languages': languages,
    })