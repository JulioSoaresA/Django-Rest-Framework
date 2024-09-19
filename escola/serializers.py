from rest_framework import serializers
from .models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF informado não é válido."})
        
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome': "O nome só pode conter letras."})
        
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError(
                {'celular': "O celular informado não é válido. Use o formato (XX) 9XXXX-XXXX."}
            )
        return dados


class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular']


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
