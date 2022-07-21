from rest_framework import serializers
from tracking.models import Category, Spending


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", "name_category", "is_active", "fk_user")


class SpendingSerializer(serializers.ModelSerializer):
    name_category = serializers.SerializerMethodField('get_name_category')

    def get_name_category(self, fk):
        return fk.fk_category.name_category

    class Meta:
        model = Spending
        fields = ("id", "amount", "comment", "date_time_created", "name_category", "fk_category", "fk_user")
