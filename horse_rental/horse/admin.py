from django.contrib import admin
from horse.models import Complexity, Types_of_training, Training, Trainer, Horse, Route, Services, Comments


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
    list_display = ('name', 'sername', 'lastname', 'date_of_employment')
    search_fields = ('name', 'sername')
    list_filter = ('date_of_employment', )


@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('horse_name', 'breed', 'status', 'birthday', 'horse_img')
    search_fields = ('horse_name', 'breed')
    list_filter = ('birthday', )
    list_editable = ('status', )


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'length', 'description')
    search_fields = ('route_name', )
    list_filter = ('length', )
    list_editable = ('length', 'description')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_img')
    search_fields = ('service_name', )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'text', 'services')
    search_fields = ('user', )
    list_filter = ('date', )
    readonly_fields = ('date', )
    list_editable = ('text', )
    fields = ('user', 'date', 'text', 'services')




