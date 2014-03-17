from django.http import HttpResponseRedirect
from django.views import generic
from incident.models import Incident
from incident.forms import UpdateFormSet, IncidentUpdateForm


class IncidentDetailView(generic.DetailView):
    model = Incident


class IncidentListView(generic.ListView):
    model = Incident
    paginate_by = 25


class IncidentCreateView(generic.CreateView):
    model = Incident


class IncidentUpdateView(generic.UpdateView):
    template_name = 'incident/incident_update.html'
    model = Incident
    form_class = IncidentUpdateForm

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        update_form = UpdateFormSet()
        return self.render_to_response(
            self.get_context_data(form=form, update_form=update_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        update_form = UpdateFormSet(self.request.POST)
        if (form.is_valid() and update_form.is_valid()):
            return self.form_valid(form, update_form)
        else:
            return self.form_invalid(form, update_form)

    def form_valid(self, form, update_form):
        self.object = form.save()
        update_form.instance = self.object
        update_form.save()
        return HttpResponseRedirect(self.object.get_absolute_url())

    def form_invalid(self, form, update_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, update_form=update_form))
