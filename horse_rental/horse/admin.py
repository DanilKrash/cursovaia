from django.contrib import admin
from horse.models import Complexity, Types_of_training, Training, Trainer, Horse, Route, Services, Comments, User, Order


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
    list_display = ('name', 'sername', 'lastname', 'date_of_employment', 'image')
    search_fields = ('name', 'sername')
    list_filter = ('date_of_employment',)


@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('horse_name', 'breed', 'status', 'birthday', 'horse_img')
    search_fields = ('horse_name', 'breed')
    list_filter = ('birthday',)
    list_editable = ('status', )
    filter_horizontal = ('trainer',)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'length', 'description')
    search_fields = ('route_name',)
    list_filter = ('length',)
    list_editable = ('length', 'description')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_img', 'get_trainer', 'get_horse')
    search_fields = ('service_name',)
    filter_horizontal = ('trainer', 'horse')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'text', 'services')
    search_fields = ('user',)
    list_filter = ('date',)
    readonly_fields = ('date',)
    list_editable = ('text',)
    fields = ('user', 'date', 'text', 'services')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_of_create', 'user', 'date_start', 'services']
    search_fields = ('user', 'services')
    list_filter = ['date_start', 'date_of_create']
    readonly_fields = ('date_of_create',)
    fields = ('user', 'trainer', 'horse', 'date_of_create', 'date_start', 'services')
