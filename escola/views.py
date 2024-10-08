from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, EstudanteSerializerV2, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from .throttles import MatriculaAnonRateThrottle


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by('id')
    # serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['codigo']
    search_fields = ['codigo', 'descricao']
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    throttle_classes = [MatriculaAnonRateThrottle, UserRateThrottle]
    
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset

    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculasCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset

    serializer_class = ListaMatriculasCursoSerializer
