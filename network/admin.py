from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html
from network.models import BusinessUnit, Product


@admin.register(BusinessUnit)
class BusinessUnitAdmin(admin.ModelAdmin):
    """
    Класс для управления моделью BusinessUnit в административной панели Django.
    Отображает список бизнес-единиц, позволяет фильтровать по городу и обнулять задолженности.
    """
    list_display = ['title', 'email', 'country', 'city', 'unit_type', 'supplier_link', 'debt']
    list_display_links = ['title']
    list_filter = ['city']
    actions = ['clear_debt']

    @admin.display(description='Поставщик')
    def supplier_link(self, obj):
        """
        Возвращает HTML-ссылку на страницу поставщика для объекта BusinessUnit.
        """
        if obj.supplier:
            link = reverse("admin:network_businessunit_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier.title)
        return "-"

    def clear_debt(self, request, queryset):
        """
        Обнуляет задолженность для выбранных бизнес-единиц.
        """
        count = queryset.update(debt=0)
        self.message_user(request, 'Задолженность успешно очищена для {} объект(ов).'.format(count), messages.WARNING)

    clear_debt.short_description = 'Очистить задолженность'


admin.site.register(Product)  # Регистрация модели продукта
