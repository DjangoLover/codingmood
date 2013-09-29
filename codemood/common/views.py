from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView

from badges.models import Badge
from commits.forms import RepositoryForm
from commits.models import Repository, Commit
from social.models import Post


class Index(TemplateView):
    """
    Return different view to authenticated and not.
    """
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            return AuthenticatedIndex.as_view()(self.request)
        else:
            return NotAuthenticatedIndex.as_view()(self.request)


class AuthenticatedIndex(FormView):
    """
    View to authenticated user
    """
    template_name = 'index/authorized.html'
    form_class = RepositoryForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AuthenticatedIndex, self).get_context_data(**kwargs)
        user = self.request.user

        #TODO: Add filtering by user
        context['git_activity_list'] = Commit.objects.all()
        context['repositories_list'] = Repository.objects.all()
        
        context['fb_activity_list'] = Post.objects.filter(user=user).order_by('created')
        context['badge_list'] = Badge.objects.filter(badgeuser__user=user).distinct()[:4]
        return context

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return redirect(self.get_success_url())


class NotAuthenticatedIndex(TemplateView):
    """
    View to NOT authenticated user
    """
    template_name = 'index/not-authorized.html'
