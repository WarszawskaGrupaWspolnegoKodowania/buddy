from django.conf import settings
from django.utils.translation import ugettext_noop as _

def create_notice_types(sender, **kwargs):
    if "pinax.notifications" in settings.INSTALLED_APPS:
        from pinax.notifications.models import NoticeType
        print("Creating notices for myapp")
        NoticeType.create("friends_invite", _("Invitation Received"), _("Someone wants to code with you!"))
        NoticeType.create("friends_accept", _("Acceptance Received"), _("You can code together!"))
        NoticeType.create("someone_wants_to_join", _("I want to help in your project!"), _(
            "Someone wants to join your project"))
        NoticeType.create("you_joined_project", _("Now you can help with this project!"), _(
            "an invitation you sent has been accepted"))
    else:
        print("Skipping creation of NoticeTypes as notification app not found")
