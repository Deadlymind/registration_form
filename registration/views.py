# views.py
from django.shortcuts import render, redirect
from .forms import SubmissionForm
from django.core.mail import send_mail
from django.conf import settings


def submit_form(request):
    """
    View function for handling form submissions.

    If the request method is POST:
        - Validates the form data.
        - Saves the form data to create a new FormSubmission object.
        - Sends an email notification using send_notification_email.
        - Redirects to the success page if the form submission is successful.
    
    If the request method is GET:
        - Renders the form to be filled by the user.

    Args:
        request: The HTTP request.

    Returns:
        Rendered HTML page.
    """
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            send_notification_email(submission)  # Send email notification
            return redirect('success_page')  # Change 'success_page' to your actual success page URL
    else:
        form = SubmissionForm()

    return render(request, 'registration/register.html', {'form': form})


def success_page(request):
    """
    View function for rendering the success page.

    Args:
        request: The HTTP request.

    Returns:
        Rendered HTML success page.
    """
    return render(request, 'registration/success.html')


def send_notification_email(submission):
    """
    Sends an email notification with form submission details.

    Args:
        submission: FormSubmission object containing user details.
    """
    subject = 'New Registration Submission'
    message = f'''Hi, a new registration was submitted.

Details:
Name: {submission.full_name}
Email: {submission.email}
Phone: {submission.phone_number}
Comments: {submission.comments}
'''
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['oussamaayari2014@gmail.com']  # replace with your email

    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email notification. Error: {e}")
