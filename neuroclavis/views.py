from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Paciente, SessaoJogo, RegistroLog
from .services import gerar_laudo_com_ia
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class SessaoJogoAPI(APIView):
    # LIGA O ESCUDO DO JWT E DESLIGA O CSRF!
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        try:
            dados = request.data
            paciente_id = dados.get('paciente')
            paciente = Paciente.objects.get(id=paciente_id)

            # Cria a sessão
            sessao = SessaoJogo(
                paciente=paciente,
                tempo_primeira_acao=dados.get('tempo_primeira_acao'),
                tempo_total=dados.get('tempo_total'),
                cliques_falsos=dados.get('cliques_falsos'),
                solturas_erradas=dados.get('solturas_erradas'),
                qtd_quedas=dados.get('qtd_quedas'),
                tempo_segurando_peca=dados.get('tempo_segurando_peca'),
                cliques_frustracao=dados.get('cliques_frustracao'),
                tempo_congelado_pos_erro=dados.get('tempo_congelado_pos_erro')
            )

            # Chama a IA do Google
            sessao.laudo_ia = gerar_laudo_com_ia(sessao)
            sessao.save()

            # Registra no Log
            RegistroLog.objects.create(
                nivel='INFO',
                acao=f"Sessão registrada para {paciente.nome}",
                detalhes="Dados recebidos via Unity/API"
            )

            # Retorna o JSON de sucesso
            return Response({
                "mensagem": "Sessão salva com sucesso!",
                "laudo_ia": sessao.laudo_ia
            }, status=status.HTTP_201_CREATED)

        except Paciente.DoesNotExist:
            return Response({"erro": "Paciente não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)