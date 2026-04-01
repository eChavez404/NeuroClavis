from rest_framework import serializers
from .models import SessaoJogo

class SessaoJogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessaoJogo
        
        fields = [
            'id', 'paciente', 'tempo_primeira_acao', 'tempo_total', 
            'cliques_falsos', 'solturas_erradas', 'qtd_quedas', 
            'tempo_segurando_peca', 'cliques_frustracao', 'tempo_congelado_pos_erro',
            'laudo_ia', 'created_at'
        ]
        
        read_only_fields = ['id', 'laudo_ia', 'created_at']