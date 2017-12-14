from django.db.models import Q
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import StaffProfile
from django.shortcuts import render, get_object_or_404, redirect
from .forms import StaffProfileCreateForm
from django.urls import reverse_lazy


class StaffListView(ListView):
    def get_queryset(self):
        return StaffProfile.objects.all()


class StaffCreateView(CreateView):
    form_class = StaffProfileCreateForm
    template_name = "staff/form.html"

    def form_valid(self, form):
        instance = form.save()
        instance.save()
        return super(StaffCreateView, self).form_valid(form)


class StaffUpdateView(UpdateView):
    form_class = StaffProfileCreateForm
    template_name = "staff/detail-update.html"
    queryset = StaffProfile.objects.all()


class StaffDeleteView(DeleteView):
    model = StaffProfile
    template_name = "staff/detail-update.html"
    success_url = reverse_lazy("staff:list")






# def staff_delete(request, slug):
#     staffemp = get_object_or_404(StaffProfile, slug=slug)
#
#     staffemp.delete()
#
#     return redirect("staff:list")




# contact is purely for practice


# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#
#         context = {}
#         return render(request, "contact.html", context)


# to just render a template page

# def staff_listview(request):
#     template_name = "contact.html"
#     queryset = StaffProfile.objects.all()
#     context = {}
#     return render(request, template_name, context)


# class ContactTemplateView(TemplateView):
#     template_name = "contact.html"
#
#     def get_context_data(self, *args, **kwargs):        # this is called a overriding method
#         context = super(ContactTemplateView, self).get_context_data(*args, **kwargs)
#         name = "Vincent's Template View using get_context_data"
#         context = {"name_for_temp": name}
#         print(context)
#         return context


# class ContactListView(ListView):
#     queryset = StaffProfile.objects.all()
#     template_name = "contact.html"
#
#
# class FirstNameListView(ListView):
#     queryset = StaffProfile.objects.filter(first_name__iexact="James")
#     template_name = "contact.html"
#
#
# class LastNameListView(ListView):
#     queryset = StaffProfile.objects.filter(last_name__iexact="Benns")
#     template_name = "contact.html"
#
#
# class SearchContactListView(ListView):
#     template_name = "contact.html"
#
#     def get_queryset(self):
#         print(self.kwargs)
#         slug = self.kwargs.get("slug")
#         if slug:
#             queryset = StaffProfile.objects.filter(
#                 Q(first_name__iexact=slug) |
#                 Q(first_name__icontains=slug)  #this gets real specific.
#
#
#             )
#         else:
#             queryset = StaffProfile.objects.none()
#         return queryset
#
#
# class SearchContactDetailView(DetailView):
#     pass



