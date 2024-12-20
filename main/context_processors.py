from .models import ContactInfo


def contact_info(request):
    data = ContactInfo.objects.first()

    return {
        'city': data.city_address,
        'street': data.street_address,
        'phone_number': data.phone_number,
        'email': data.email,
        'opening_hours': data.opening_hours,

        'facebook': data.facebook_link,
        'x': data.x_link,
        'instagram': data.instagram_link,
        'linkedin': data.linkedin_link,
    }