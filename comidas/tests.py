from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from comidas.schema import schema
from comidas.models import Comida

COMIDAS_QUERY = '''
 {
   comidas {
     id
     nombre
     tipoPlatillo
     calorias
     proteinas
     paisOrigen
     ingredientes
     saludable
     tiempoCoccion
     dificultadPreparacion
     utensiliosRequeridos
   }
 }
'''

class ComidaTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.comida1 = mixer.blend(Comida)
        self.comida2 = mixer.blend(Comida)
        
    def test_comidas_query(self):
        response = self.query(
            COMIDAS_QUERY,
        )

        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query link results ")
        print (content)
        assert len(content['data']['comidas']) == 2