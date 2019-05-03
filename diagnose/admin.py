from django.contrib import admin
from .models import Diagnose, Question, SendMail, Common
import csv
import datetime
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # write the header row
    writer.writerow([field.verbose_name for field in fields])
    # write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'modified']
    list_display_links = ['name']


admin.site.register(Diagnose, DiagnosisAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'created', 'modified']
    list_display_links = ['user']
    actions = [export_to_csv]


admin.site.register(Question, QuestionAdmin)


class MailAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'created', 'modified']
    list_display_links = ['user']


admin.site.register(SendMail, MailAdmin)


class CommonAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'modified']
    actions = [export_to_csv]


admin.site.register(Common, CommonAdmin)



