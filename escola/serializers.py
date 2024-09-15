from rest_framework import serializers
from .models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    turno = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'turno']

    def get_turno(self, obj):
        return obj.get_turno_display()


class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome']
