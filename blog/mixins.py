from django.shortcuts import redirect


class LoginRequestMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:login")
        return super(LoginRequestMixin, self).dispatch(request, *args, **kwargs)
