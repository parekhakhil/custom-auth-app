from django.shortcuts import render,redirect
from .forms import UserAdminCreationForm
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.
'''
class RegisterView(TemplateView):
    class Meta:
        model = get_user_model()
        form_class = UserAdminCreationForm
        template_name = 'accounts/register.html'
        
    def post(self,request):
        post_data = request.POST or None

        form_class = UserAdminCreationForm(post_data,instance=request.user)

        if form_class.is_valid():
            form_class.save()
            messages.success(request,'Welcome {} {}, your profile is successfully created'.format(user.first_name,user.last_name))
            return HttpResponseRedirect(reverse_lazy('users:register'))
        else:
            messages.error(request,'User already exists, please login')
            return HttpResponseRedirect(reverse_lazy('users:register'))

        context = self.get_context_data(form_class=form_class)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request,*args, **kwargs)
'''
def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Signup sucess')
            return redirect('users:register')
    return render(req, 'accounts/register.html', {'form': form})