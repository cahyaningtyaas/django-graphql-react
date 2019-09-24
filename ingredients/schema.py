# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from .models import Dish #, Chef, Customer


class DishType(DjangoObjectType):
    class Meta:
        model = Dish


# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient
#
#
class Query(object):
    all_dish = graphene.List(DishType)
    # all_ingredients = graphene.List(IngredientType)

    def resolve_all_dish(self, info, **kwargs):
        return Dish.objects.all()

    # def resolve_all_ingredients(self, info, **kwargs):
    #     # We can easily optimize query count in the resolve method
    #     return Ingredient.objects.select_related('category').all()