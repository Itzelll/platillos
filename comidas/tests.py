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

CREATE_COMIDA_MUTATION = '''
  mutation createComidaMutation(
    $nombre: String, 
    $tipoPlatillo: String, 
    $calorias: Float, 
    $proteinas: Float, 
    $paisOrigen: String, 
    $ingredientes: String, 
    $saludable: String, 
    $tiempoCoccion: Int, 
    $dificultadPreparacion: Int, 
    $utensiliosRequeridos: String
    ){
      createComida(
        nombre: $nombre, 
        tipoPlatillo: $tipoPlatillo, 
        calorias: $calorias, 
        proteinas: $proteinas, 
        paisOrigen: $paisOrigen, 
        ingredientes: $ingredientes, 
        saludable: $saludable, 
        tiempoCoccion: $tiempoCoccion, 
        dificultadPreparacion: $dificultadPreparacion, 
        utensiliosRequeridos: $utensiliosRequeridos
        ){
        
          nombre
          saludable
          
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
        print ("query comidas results ")
        print (content)
        assert len(content['data']['comidas']) == 2


    def test_createComida_mutation(self):

        response = self.query(
            CREATE_COMIDA_MUTATION,
            variables={
              'nombre': 'kimchi coreano', 
              'tipoPlatillo': 'guarnicion',
              'calorias': 23,
              'proteinas': 2,
              'paisOrigen': 'Corea del sur',
              'ingredientes': 'col china, nabo, harina de arroz, ajo, jengibre, sal, azucar, pimienta, agua, salsa de soja, chile en polvo',
              'saludable': 'Si',
              'tiempoCoccion': 150,
              'dificultadPreparacion': 2,
              'utensiliosRequeridos': 'manos, cucharas, contenedor grande'
            }
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createComida": {"nombre": "kimchi coreano", "saludable": "Si"}}, content['data'])
        
