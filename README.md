<div align="center">
  
# 🧠 NeuroClavis
**As chaves digitais para decodificar a mente da criança.**

![Unity](https://img.shields.io/badge/Unity-6-black?style=for-the-badge&logo=unity)
![C#](https://img.shields.io/badge/C%23-Arquitetura_Orientada_a_Eventos-239120?style=for-the-badge&logo=c-sharp)
![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![OpenAI](https://img.shields.io/badge/AI_Co--Pilot-GPT--4o--mini-412991?style=for-the-badge&logo=openai)

*Uma plataforma de Digital Therapeutics (DTx) que transforma avaliações neuropsicológicas em experiências lúdicas, utilizando telemetria invisível e Inteligência Artificial para gerar laudos clínicos baseados em evidências.*

</div>

---

## 🎯 A Visão: Por que o NeuroClavis existe?
Diagnósticos de transtornos do neurodesenvolvimento (como **TDAH, TEA e Transtornos Motores**) dependem de avaliações clínicas que muitas vezes geram *ansiedade de performance* na criança. Testes de papel e caneta são frios e falham em capturar o comportamento natural do paciente.

**A nossa solução:** Criamos um ecossistema onde a criança apenas joga. O que parece ser um simples quebra-cabeça 2D esconde um **motor de telemetria de alta precisão**. Capturamos cada milissegundo de hesitação, cada movimento de frustração e cada erro motor. Esses dados são enviados para um backend robusto onde nossa **Inteligência Artificial (Co-Piloto Clínico)** analisa os padrões e entrega um relatório pré-clínico detalhado nas mãos do profissional de saúde.

---

## 🚀 O Motor da Inovação (O que construímos)

Nós não fizemos apenas um jogo ou um CRUD. Nós construímos uma ponte entre a física de um motor gráfico e a análise de dados de uma API.

### 🎮 1. Game Design Focado em Psicologia (Frontend)
- **Física Clínica (SmoothDamp):** A movimentação das peças não é rígida. Utilizamos interpolação matemática (`Vector3.SmoothDamp`) para que o objeto siga o mouse com fluidez. Isso garante que a medição da coordenação motora fina da criança seja pura, sem interferência de travamentos do jogo.
- **Filosofia do "Soft Fail":** Telas de *Game Over* geram picos de cortisol e invalidam o teste. Se a criança erra o encaixe, a peça simplesmente retorna suavemente à origem. O jogo nunca a pune, mas o sistema registra a falha silenciosamente.
- **Detecção Cirúrgica (Physics2D.OverlapBoxAll):** Rejeitamos colisões simples (*Triggers*) que podem falhar em movimentos rápidos. Construímos um sistema robusto de validação de área matemática usando máscaras de colisão (*LayerMasks*), garantindo 100% de precisão na detecção do sucesso ou erro.

### 🧠 2. O Cérebro Invisível: Telemetria Clínica
Enquanto a criança se diverte, nosso sistema `PlayerTelemetryCollector` avalia o comportamento em background, traduzindo ações do mouse em métricas psicológicas:

| Ação no Jogo (Raw Data) | O que a IA interpreta (Marcador Clínico) |
| :--- | :--- |
| **Tempo até o 1º Clique** | **Latência de Resposta:** Velocidade de processamento visual e ideação. |
| **Cliques fora do alvo** | **Controle Inibitório:** Marcador primário de impulsividade (TDAH). |
| **Cliques ultrarrápidos** | **Regulação Emocional:** Cliques repetitivos indicam frustração sob estresse. |
| **Quedas da peça** | **Praxia Visuoespacial:** Falhas na coordenação visomotora fina. |
| **Tempo de peça solta** | **Tempo Refratário:** Bloqueio cognitivo e tempo de recuperação pós-erro. |

### 🤖 3. Inteligência Artificial Generativa (Backend)
O backend não apenas salva os dados no banco. Ele utiliza o modelo **GPT-4o-mini** (via GitHub Models/OpenAI SDK) atuando como um *Co-Piloto*. A IA recebe o JSON da partida e processa os dados sob um rigoroso prompt de engenharia médica, devolvendo um laudo em linguagem natural com hipóteses clínicas para guiar o médico.

---

## 📐 Engenharia de Software Avançada (Design Patterns)

O código foi desenhado para ser escalável, manutenível e blindado contra falhas, utilizando padrões da indústria:

### No Unity (C#)
*   **Data Transfer Objects (DTOs):** A engine da Unity possui uma estrutura de dados pesada (`GameObjects`, `Transforms`). Para não poluir nossa API, aplicamos o padrão **DTO** (`DjangoPayload`). Nós "traduzimos" e empacotamos apenas os números que importam em um objeto limpo antes de serializar em JSON. A API recebe dados puros, ignorando completamente a complexidade da engine.
*   **Singleton Pattern & Persistência:** Sistemas vitais como a coleta de dados e o envio para a API (`TelemetryApiSender`) são protegidos pelo padrão Singleton com `DontDestroyOnLoad`, garantindo que nenhuma métrica clínica seja perdida durante transições de tela ou engasgos do sistema.

### No Django (Python)
*   **Service Layer Pattern (Skinny Views):** Evitamos o terrível anti-pattern de *Fat Views*. Toda a lógica pesada de integração com a API da OpenAI e regras de negócio foi extraída para a camada `services.py`. As Views atuam apenas como rotas limpas, seguras por JWT.
*   **Custom User Model:** Modernizamos a autenticação. O Django padrão exige `username`, mas nós sobrescrevemos a arquitetura base (`AbstractBaseUser`) para utilizar **E-mail como chave primária**, o padrão real de sistemas SaaS B2B.
*   **Provisionamento Automatizado (Data Migrations):** Pensando na *Developer Experience (DX)* e na avaliação da banca, injetamos um script de *Seed* diretamente na esteira de migrações (`migrations.RunPython`). **O banco de dados se auto-popula com as credenciais Master no momento em que é criado**, dispensando qualquer configuração manual via terminal.

---

## 🛠️ Como Avaliar o Projeto (Zero-Config Setup)

Preparamos o projeto para ser avaliado da forma mais rápida e sem fricção possível.

### 1. Levantando o Servidor (Backend)
Abra o terminal na pasta `/backend`:
```bash
# 1. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/Scripts/activate  # Windows
# source .venv/bin/activate    # Mac/Linux

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure as variáveis de ambiente (Crie o arquivo .env)
# SECRET_KEY=sua_chave_aqui
# GITHUB_TOKEN=seu_token_da_ia_aqui
# DEBUG=True
# ALLOWED_HOSTS=*

# 4. Construa o banco e auto-provisione o sistema
python manage.py migrate

# 5. Inicie a API
python manage.py runserver
````
<div align="center"> <i>"A tecnologia só cumpre seu papel quando se torna invisível e resolve problemas reais."</i><br> <b>Neuroclavis - 2026</b> </div>
