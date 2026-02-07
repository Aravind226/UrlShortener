import secrets
import string
from .models import URL
def create_short(long_URL):
    values = string.ascii_lowercase + string.ascii_uppercase + string.digits
    shortcode = ''.join(secrets.choice(values) for i in range(6))
    return shortcode

def generate_short(long_URL):
    url = create_short(long_URL)
    while URL.objects.filter(shortenedURL = url).exists():
        url = create_short(long_URL)
    return url