from django.shortcuts import render

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('top')

    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS, '会員登録に成功しました')
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form) -> HttpResponse:
        messages.add_message(self.request, messages.ERROR, '会員登録に失敗しました')
        return super().form_invalid()
