from django.contrib import admin
from .models import Article         # Uses a relative import with the dot (.) prefix
                                    # Specifies should be imported from the same directory as the module in
# Register your models here.

admin.site.register(Article)