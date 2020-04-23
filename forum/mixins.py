from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixing(UserPassesTestMixin):
  # only the staff can create new sections
  def test_func(self):
    return self.request.user.is_staff
