# 🧠 Neuroclavis

**Neuroclavis** é uma plataforma inovadora de *Digital Therapeutics (DTx)* focada na avaliação neuropsicológica e psicopedagógica infantil. O ecossistema une a capacidade de engajamento dos videogames (Frontend), a precisão matemática da telemetria digital (Backend) e o poder de síntese da Inteligência Artificial Generativa para auxiliar profissionais de saúde no rastreio de transtornos do neurodesenvolvimento (como TDAH, TEA, e Transtornos Motores).

Atuando como um "microscópio comportamental", o jogo coleta dados invisíveis a olho nu e os traduz em relatórios clínicos preliminares baseados em evidências.

---

## 🚀 Principais Funcionalidades

- **Telemetria de Alta Precisão:** Coleta dados comportamentais em milissegundos durante a gameplay, sem interromper o estado de *flow* do paciente (mecânicas de *Soft Fail*).
- **AI Co-Pilot Clínico:** Integração assíncrona com LLMs (GPT-4o-mini via GitHub Models) configurados com *prompts* de alto rigor científico (baseados no DSM-5-TR e teorias de Funções Executivas) para gerar uma pré-análise clínica da sessão.
- **Painel Administrativo (B2B):** Interface web segura para médicos e psicopedagogos gerenciarem pacientes, cadastrarem diagnósticos formais e acessarem o histórico de laudos gerados pela IA.
- **Arquitetura Segura:** Proteção de rotas via JSON Web Tokens (JWT) e anonimização de pacientes utilizando UUIDs, garantindo conformidade com leis de proteção de dados de saúde (LGPD).

---

## 🏗️ Arquitetura do Sistema

O projeto é dividido em três grandes camadas:

1. **Frontend (O Jogo - Unity 2D / C#):** 
   Interface interativa onde a criança realiza tarefas visuoespaciais. Responsável por rodar a física do jogo, registrar as métricas comportamentais invisíveis e enviar o *payload* final via REST API.
2. **Backend (A API - Python / Django REST Framework):** 
   O servidor central. Gerencia a autenticação, valida a integridade dos dados, persiste o histórico no banco de dados e serve o Painel Admin.
3. **Processamento de Linguagem Natural (IA):** 
   Módulo isolado (`services.py`) que processa as métricas matemáticas, cruza as variáveis de acordo com a literatura neurocientífica e devolve um texto estruturado para a API.

---

## 📊 Métricas Coletadas (O *Payload*)

A ponte entre a Engenharia de Software e a Neurociência. O jogo exporta um JSON contendo:

| Variável Técnica | Representação Cognitiva / Clínica |
| :--- | :--- |
| `tempo_primeira_acao` | **Latência de Resposta:** Processamento visual inicial e iniciativa. |
| `tempo_total` | **Vigilância:** Atenção sustentada e foco na tarefa. |
| `cliques_falsos` | **Controle Inibitório:** Marcador de impulsividade e hiperatividade. |
| `solturas_erradas` | **Praxia Visuoespacial:** Planejamento espacial vs. Tentativa e Erro. |
| `qtd_quedas` | **Destreza Fina:** Coordenação visomotora e mecânica de precisão. |
| `tempo_segurando_peca` | **Ideação:** Tempo de planejamento de rota e tomada de decisão. |
| `cliques_frustracao` | **Regulação Emocional:** Tolerância à frustração sob estresse. |
| `tempo_congelado_pos_erro` | **Tempo Refratário:** Bloqueio cognitivo e recuperação pós-falha. |

---

## 🛠️ Tecnologias Utilizadas

**Motor Gráfico:**
- Unity (C#)
- Sistema nativo de Coroutines e `UnityWebRequest` para requisições assíncronas.
- Arquitetura baseada em Singletons para *Managers* (Telemetria, Transição de Cena, API).

**Servidor & API:**
- Python 3.11+
- Django & Django REST Framework
- Simple JWT (Autenticação)
- SQLite (Desenvolvimento) / PostgreSQL (Produção)

**Inteligência Artificial:**
- OpenAI Python SDK
- GitHub Models / Azure AI Inference (`gpt-4o-mini`)

---

## ⚙️ Como Executar o Projeto Localmente

### 1. Configurando o Backend (Django)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/neuroclavis.git
cd neuroclavis/backend

# Crie e ative um ambiente virtual
python -m venv venv
source venv/Scripts/activate  # (No Windows)
# source venv/bin/activate    # (No Linux/Mac)

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
# Crie um arquivo .env na raiz do backend com as seguintes chaves:
# SECRET_KEY=sua_chave_secreta_do_django
# GITHUB_TOKEN=seu_token_do_github_models

# Execute as migrações do banco de dados
python manage.py migrate

# Crie um superusuário para acessar o Painel Admin
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
````
*Neuroclavis - As chaves para entender a mente da criança.*
