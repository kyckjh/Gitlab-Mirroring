from django.shortcuts import render
from .models import Pet, PetSitter
from django.db import reset_queries, connection

def get_sql_queries(origin_func):
    def wrapper():
        reset_queries()
        origin_func()
        query_info = connection.queries
        for query in query_info:
            print(query['sql'])
    return wrapper

# Create your views here.
@get_sql_queries
def get_pet_data():
    pets = Pet.objects.all()
    for pet in pets:
        print(f"{pet.name} | 집사 : {pet.pet_sitter.first_name}")
