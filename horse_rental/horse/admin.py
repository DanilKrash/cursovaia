from django.contrib import admin
from horse.models import Complexity, Types_of_training, Training, Trainer, Horse, Route, Services, Comments, User, \
    Order, Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'elect')
    search_fields = ('user',)
    list_filter = ('date', 'elect')
    readonly_fields = ('date', 'user')
    list_editable = ('elect',)
    fields = ('user', 'date', 'text', 'elect')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Complexity)
class ComplexityAdmin(admin.ModelAdmin):
    list_display = ('complexity_name',)
    search_fields = ('complexity_name',)


@admin.register(Types_of_training)
class Types_of_trainingAdmin(admin.ModelAdmin):
    list_display = ('types_training_name',)
    search_fields = ('types_training_name',)


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('training_name',)
    search_fields = ('training_name',)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'sername', 'lastname', 'is_busy', 'date_of_employment', 'image')
    search_fields = ('name', 'sername')
    list_filter = ('date_of_employment',)
    list_editable = ('is_busy',)


@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('horse_name', 'breed', 'is_busy')
    search_fields = ('horse_name', 'breed')
    list_filter = ('birthday',)
    list_editable = ('is_busy',)
    filter_horizontal = ('trainer',)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'length', 'description')
    search_fields = ('route_name',)
    list_filter = ('length',)
    list_editable = ('length', 'description')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'get_trainer', 'get_horse')
    search_fields = ('service_name',)
    filter_horizontal = ('trainer', 'horse')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'services')
    search_fields = ('user',)
    list_filter = ('date', 'services')
    readonly_fields = ('date', 'user')
    fields = ('user', 'date', 'text', 'services')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_of_create', 'user', 'date_start', 'time_start', 'services', 'status']
    search_fields = ('user', 'services')
    list_filter = ['date_start', 'date_of_create', 'status']
    readonly_fields = ('date_of_create', 'user')
    list_editable = ('status',)
    fields = ('user', 'date_of_create', 'date_start', 'time_start', 'services', 'status')


