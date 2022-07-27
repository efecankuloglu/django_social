from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from .models import Post, Profile, User
from .forms import PostModelForm, CustomUserCreationForm


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class MainPageView(generic.View):
    def get(self, request):
        form = PostModelForm(initial={"user": request.user})
        post_qs = Post.objects.all()
        user_qs = User.objects.all().exclude(is_staff=True)
        context = {
            "form": form,
            "post_qs": post_qs,
            "user_qs": user_qs,
        }
        return render(request, "main_page.html", context=context)

    def post(self, request):
        form = PostModelForm(request.POST)
        post = form.save(commit=False)
        post.user = request.user
        form.save()
        return redirect("social:main-page")


# class ProfileView(generic.ListView):
#     template_name = "profile_page.html"
    
#     def get_queryset(self):
#         user = self.request.user
#         return Post.objects.filter(user=user)

def profile_view(request, slug):
    user = User.objects.get(slug=slug)
    profile = Profile.objects.get(user=user)
    qs = Post.objects.filter(user=user)
    context = {
        "qs": qs,
        "profile": profile,
    }
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "profile_page.html", context=context)