from __future__ import unicode_literals
from django.db import models

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

MAIL_TYPES = (
    ('mail', 'Standard Mail'),
    ('contact', 'Kontakt'),
    ('newsletter_confirm', 'Nyhedsbrev Bekræftelse'),
    ('newsletter_welcome', 'Nyhedsbrev Velkomstbesked'),
    ('order_new', 'Ordre Bekræftelse'),
    ('order_cancel', 'Ordre Annulleret'),
    ('order_processing', 'Ordre Behandler'),
    ('order_done', 'Ordre Fuldført'),
)

class Email(models.Model):

    """Model to store outgoing email information"""

    from_email = models.TextField(_("from e-mail"))
    recipients = models.TextField(_("recipients"))
    subject = models.TextField(_("subject"))
    attachment = models.TextField(null=True, blank=True)
    body = models.TextField(_("body"))
    ok = models.BooleanField(_("ok"), default=False, db_index=True)
    date_sent = models.DateTimeField(_("date sent"), auto_now_add=True, db_index=True)
    read = models.BooleanField(_('read'), default=False)
    read_timestamp = models.DateTimeField(_("read timestamp"), null=True, blank=True)
    type_of = models.CharField(_("Typeof"), max_length=100, choices=MAIL_TYPES, default=MAIL_TYPES[0])

    def __str__(self):
        return "{s.recipients}: {s.subject}".format(s=self)

    class Meta:
        verbose_name = _("e-mail")
        verbose_name_plural = _("e-mails")
        ordering = ('-date_sent',)


