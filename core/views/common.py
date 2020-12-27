from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from users.appvars import LAWYER, CUSTOMER
from core.models import Appointment
from core.forms.common import AppointmentCreateForm
from users.models import User


class HomeView(TemplateView):

    template_name = "core/home.html"


def dashboard(request):

    if request.user.is_authenticated:
        if request.user.user_type == LAWYER:
            return redirect('core:lawyer_dashboard')

        elif request.user.user_type == CUSTOMER:
            return redirect('core:customer_dashboard')

    # If user is not authenticated
    return render(request, 'core:home')


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentCreateForm

    template_name = 'core/appointment.html'

    def form_valid(self, form):
        # We have accepted a value as pk in the url.
        pk = self.kwargs['pk']

        # Selecting the user with the pk as the lawyer
        lawyer = User.objects.get(pk=pk)
        form.instance.lawyer = User.objects.get(pk=pk)

        # Saving the fee of the lawyer as the fee of this appointment
        form.instance.fee = lawyer.lawyerprofile.fee

        # Selecting the present user as the customer
        form.instance.customer = self.request.user
        return super().form_valid(form)
