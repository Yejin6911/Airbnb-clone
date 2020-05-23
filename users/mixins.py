from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin

#로그아웃 한 사람만 볼 수 있음
class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page not found"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("core:home")