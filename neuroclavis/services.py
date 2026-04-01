import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def gerar_laudo_com_ia(dados_sessao):
    try:
        token = os.getenv("GITHUB_TOKEN")
        
        if not token:
            return "Erro: O Token do GitHub não foi encontrado no arquivo .env"

        client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=token,
        )
        
        # PROMPT RECALIBRADO: Eliminação de viés e reconhecimento de Padrão Normativo
        prompt = f"""
        Atue como um Especialista Sênior em Neuropsicologia Clínica e Avaliação do Neurodesenvolvimento Infantil.
        Analise a telemetria comportamental extraída de um jogo terapêutico e redija uma Impressão Clínica Preliminar.
        
        CRÍTICO: Evite viés diagnóstico unificado (não associe tudo a desatenção ou hiperatividade). É imperativo que você avalie a possibilidade de um perfil NEUROTÍPICO (desenvolvimento normativo) caso os dados demonstrem eficiência.

        DADOS DA SESSÃO:
        - Latência de Resposta Inicial: {dados_sessao.tempo_primeira_acao} seg
        - Tempo Total de Execução: {dados_sessao.tempo_total} seg
        - Falha de Inibição (Cliques no vazio): {dados_sessao.cliques_falsos}
        - Praxia Visuoespacial (Erros de encaixe): {dados_sessao.solturas_erradas}
        - Destreza Motora Fina (Quedas de peça): {dados_sessao.qtd_quedas}
        - Tempo de Planejamento (Segurando peça): {dados_sessao.tempo_segurando_peca} seg
        - Desregulação Emocional (Cliques rápidos de frustração): {dados_sessao.cliques_frustracao}
        - Tempo Refratário (Congelamento pós-erro): {dados_sessao.tempo_congelado_pos_erro} seg

        DIRETRIZES CLÍNICAS DE CRUZAMENTO DE DADOS:
        1. PADRÃO PRESERVADO (NEUROTÍPICO): Se os índices de erros, quedas e frustrações forem baixos, ateste que as funções executivas, controle inibitório e regulação emocional estão preservados.
        2. PERFIL ANSIOSO / RIGIDEZ COGNITIVA: Alta latência inicial, alto tempo de planejamento e longo congelamento pós-erro (traços comuns em quadros de ansiedade de performance ou inflexibilidade do TEA).
        3. PERFIL DISPRÁXICO / MOTOR: Alto índice de quedas de peça e erros de encaixe, porém com baixa impulsividade (cliques falsos baixos), sugere Transtorno do Desenvolvimento da Coordenação.
        4. PERFIL IMPULSIVO: Alto índice de cliques falsos aliados a frustração rápida, sugerindo falha no controle inibitório.

        REGRAS DE FORMATAÇÃO:
        - Redija um único parágrafo contínuo (máximo 6 linhas).
        - Utilize terminologia neurocientífica rigorosa (ex: "praxia construtiva preservada", "sugere perfil normativo", "indicativo de disfunção executiva").
        - Não dê um diagnóstico fechado. Conclua apontando os domínios cognitivos que estão adequados e/ou os que exigem maior investigação empírica.
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um Doutor em Neurociência Cognitiva que realiza análises frias, imparciais e baseadas puramente nos dados métricos, reconhecendo tanto patologias quanto o desenvolvimento típico."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2, # Reduzido ainda mais para evitar alucinações e focar na regra matemática do prompt
            max_tokens=250
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Erro ao gerar laudo via IA: {str(e)}"