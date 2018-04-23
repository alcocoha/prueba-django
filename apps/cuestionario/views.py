from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from apps.cuestionario.models import Pregunta, Respuesta
import time
import json

class CuestionarioView(TemplateView):
    preguntas = Pregunta.objects.all()
    template_name = "cuestionario/index.html"

    def get_context_data(self, *args, **kwargs):
        id_user = int(time.time())
        return {'id_user': id_user, 'preguntas' : self.preguntas}

class GuardarCuestionario(TemplateView):
    
    # AQUÍ TENGO UN ERROR NO ME LLEGAN LOS DATOS LIMPIOS PARA PODER ALMACENARLOS

    def post(self, request, *args, **kwargs):
        # return HttpResponse(request.body)
        return request.body['id_user']
        
        for r in request.POST.get('respuestas'):
            print (r)
            Respuesta.objects.create(id_usuario=request.id_user, id_pregunta=r.id, respuesta=r.respuesta)
