from django.contrib import admin

from .user import UserAdmin
from ..models import User

admin.site.register(
    User,
    UserAdmin,
)
