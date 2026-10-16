import logging
from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def send_new_testimonial_email(testimonial , cfg):
    if not cfg or not cfg.notify_email:
        return
    status = "منتشر شد" if testimonial.is_published else "در انتظار تأیید شما"
    subject = f"نظر جدید از {testimonial.name}"
    body = (
        f"نام: {testimonial.name}\n"
        f"موضوع: {testimonial.subject.title if testimonial.subject else '-'}\n"
        f"امتیاز: {testimonial.rating} از 5\n"
        f"وضعیت: {status}\n\n"
        f"متن نظر:\n{testimonial.text}\n"
    )
    try:
        send_mail(subject , body , settings.DEFAULT_FROM_EMAIL , [cfg.notify_email])
    except Exception:
        logger.exception("ارسال ایمیل نظر جدید ناموفق بود")