# models.py
from django.db import models

class FormSubmission(models.Model):
    """
    Model representing a form submission.

    Attributes:
        full_name (CharField): The full name of the submitter.
        email (EmailField): The email address of the submitter.
        phone_number (CharField): The phone number of the submitter.
        comments (TextField): Additional comments provided by the submitter.

    Methods:
        __str__(): String representation of the model.
    """

    full_name = models.CharField(max_length=100, help_text='Enter your full name')
    email = models.EmailField(help_text='Enter your email address')
    phone_number = models.CharField(max_length=20, help_text='Enter your phone number')
    comments = models.TextField(help_text='Enter any additional comments')

    def __str__(self):
        """
        String representation of the FormSubmission object.

        Returns:
            str: The full name of the submitter.
        """
        return self.full_name
