from rest_framework.exceptions import ValidationError


def validate_expiration_time(time):
    if not 300 <= time <= 30000:
        raise ValidationError(
            f"Expiration time has to be a value between 300s and 3000s"
        )
