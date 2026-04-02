<div align="center">
  
# 🧠 NeuroClavis
**As chaves digitais para decodificar a mente da criança.**

![Unity](https://img.shields.io/badge/Unity-6-black?style=for-the-badge&logo=unity)
![C#](https://img.shields.io/badge/C%23-Arquitetura_Orientada_a_Eventos-239120?style=for-the-badge&logo=c-sharp)
![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django)
![Database](https://img.shields.io/badge/Banco_de_Dados-3NF_Normalizado-blue?style=for-the-badge&logo=sqlite)
![OpenAI](https://img.shields.io/badge/AI_Co--Pilot-GPT--4o--mini-412991?style=for-the-badge&logo=openai)
![Status](https://img.shields.io/badge/Status-MVP_Completo-success?style=for-the-badge)

*Plataforma de Digital Therapeutics (DTx) que transforma avaliações neuropsicológicas em experiências lúdicas, utilizando telemetria invisível de alta precisão e Inteligência Artificial para gerar laudos clínicos baseados em evidências.*

</div>

---

## 🎯 O Impacto: Por que o NeuroClavis Existe?
O processo de rastreio de transtornos do neurodesenvolvimento (como **TDAH, TEA e Transtornos Motores - TDC**) depende de avaliações clínicas demoradas que frequentemente geram "ansiedade de performance" nas crianças. Testes tradicionais de papel e caneta falham em capturar a latência motora e a frustração real.

**A Solução NeuroClavis:** Construímos um "microscópio comportamental" travestido de jogo 2D. Enquanto a criança monta um puzzle lúdico (Drag & Drop), nosso motor de telemetria captura cada hesitação, falha motora e pico de impulsividade em milissegundos. Esses *inputs* são processados por um **Co-Piloto Clínico de IA (GPT-4o-mini)**, que entrega ao profissional de saúde um pré-laudo detalhado com as hipóteses diagnósticas, revolucionando a triagem infantil para o Terceiro Setor e clínicas especializadas.

---

## 📐 Arquitetura de Software e Engenharia de Dados
Este projeto vai muito além de um CRUD. Ele foi desenhado com foco em robustez, escalabilidade e integridade, aplicando Padrões de Projeto consolidados na indústria.

### 🗄️ Backend (Django REST Framework & Modelagem)
- **Arquitetura Estendida (MVT + Services):** O projeto adota o padrão arquitetural nativo do Django, o **MVT (Model-View-Template)**, utilizando o Django Admin como a camada de visualização (Template) B2B. No entanto, para garantir a escalabilidade e a separação de responsabilidades (SoC), implementamos o **Service Layer Pattern**. Toda a regra de negócio pesada — como a engenharia de prompts médicos e a integração assíncrona com o GPT-4o-mini via OpenAI SDK — foi extraída para o módulo isolado `services.py`. As *Views* HTTP atuam estritamente como controladoras enxutas e blindadas por JWT (*Skinny Views*).
- **Normalização de Banco de Dados (3NF):** A estrutura relacional foi rigorosamente projetada e normalizada até a **3ª Forma Normal (3NF)**. Eliminamos anomalias de inserção e atualização, garantindo zero redundância de dados entre *Pacientes, Sessões e Telemetrias*. O banco reflete integridade referencial absoluta para suportar o volume de dados do jogo.
- **Service Layer Pattern (Skinny Views):** Evitamos o anti-pattern de *Fat Views*. Toda a complexidade da integração assíncrona com o OpenAI SDK (engenharia de prompts médicos) foi extraída para o módulo `services.py`. As rotas HTTP permanecem limpas, seguras e testáveis.
- **Custom User Model (Email as PK):** Sobrescrevemos o `AbstractBaseUser` padrão do Django para utilizar **E-mail** como chave primária de autenticação, alinhando a plataforma aos padrões de sistemas B2B SaaS modernos.
- **Developer Experience (Automated Seeding via Migrations):** O ambiente é "Zero-Config". Injetamos o script de criação do usuário *Super Admin* diretamente na esteira de *migrations* (`migrations.RunPython`). Forçamos o bypass seguro dos validadores de senha usando `make_password`. Ao rodar o banco, o sistema já nasce provisionado.

### 🎮 Frontend (Unity 6 & C#)
- **Data Transfer Objects (DTOs):** A engine possui hierarquias complexas de `GameObjects`. Para proteger a API de dados sujos, aplicamos o padrão **DTO** (ex: `DjangoPayload`). A Unity extrai os dados brutos, empacota em um objeto limpo e o serializa em JSON, garantindo um cumprimento estrito e isolado do contrato da API.
- **Singleton & Persistência de Dados:** O sistema vital de coleta (`PlayerTelemetryCollector`) e de disparo de dados (`TelemetryApiSender`) utiliza o padrão Singleton com `DontDestroyOnLoad`, garantindo que nenhuma métrica clínica seja perdida por transições de cena ou engasgos.
- **Física Clínica de Alta Precisão:** Rejeitamos colisões físicas simples baseadas em *Triggers* (que falham em frames rápidos). A movimentação das peças usa interpolação matemática (`Vector3.SmoothDamp`) para registrar o tempo motor puro. A validação de área é feita por `Physics2D.OverlapBoxAll` com *LayerMasks*, garantindo um *Snap* cirúrgico das peças.
- **Filosofia do "Soft Fail":** Não há tela de "Game Over". Erros apenas fazem a peça retornar suavemente à origem. O paciente permanece no estado de *Flow*, permitindo que o sistema meça a tolerância à frustração sem gerar picos irreais de cortisol.

---

## 📊 Matriz de Telemetria Clínica (O Core Loop)

Nosso sistema capta dados invisíveis a olho nu e os traduz em psicologia:

| Variável Técnica (JSON) | Representação Cognitiva / Marcador Clínico |
| :--- | :--- |
| `tempo_primeira_acao` | **Latência de Resposta:** Velocidade de processamento visual inicial e ideação. |
| `tempo_total` | **Vigilância:** Capacidade de atenção sustentada na tarefa central. |
| `cliques_falsos` | **Controle Inibitório:** Marcador primário de impulsividade ou hiperatividade (TDAH). |
| `tempo_segurando_peca` | **Ideação Motora:** Tempo de planejamento de rota e execução. |
| `cliques_frustracao` | **Desregulação Emocional:** Cliques repetitivos indicando baixa tolerância à frustração sob estresse. |
| `qtd_quedas` | **Praxia Visuoespacial:** Falhas na coordenação motora fina (TDC). |
| `tempo_congelado_pos_erro` | **Tempo Refratário:** Bloqueio cognitivo e recuperação mental pós-falha. |

---

## 🚀 Como Executar o Projeto (Avaliação Zero-Fricção)

Projetamos o repositório para ser testado e avaliado pela banca sem dores de cabeça (*Frictionless Setup*). A autenticação ponta-a-ponta é feita por JSON Web Tokens (JWT).

### 1. Levantando o Servidor (Backend API)
Abra o terminal na pasta `/backend`:
```bash
# 1. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate

# 2. Instale as dependências (ambiente limpo, pycache bloqueado no .gitignore)
python -m pip install -r requirements.txt

# 3. Configure o arquivo .env (Variáveis de Ambiente)
# SECRET_KEY=sua_chave_secreta_aqui
# GITHUB_TOKEN=seu_token_da_api_openai_aqui
# DEBUG=True
# ALLOWED_HOSTS=*

# 4. Construa o Banco Normalizado (3NF) e auto-provisione
python manage.py migrate

# 5. Inicie o Serviço
python manage.py runserver
```

> 🚨 **Acesso ao Painel Clínico (B2B):**
> Devido à nossa arquitetura de *Data Migrations*, o sistema provisiona as tabelas, permissões e o usuário Master automaticamente. Para ler os relatórios da IA e gerenciar pacientes, acesse o painel em `http://127.0.0.1:8000/admin/`:
> - **E-mail:** `admin@gmail.com`
> - **Senha:** `Clavis`

### 2. Testando a Avaliação Clínica (Frontend Game)
Não é necessário ter a Unity instalada para validar o projeto.
1. Mantenha o servidor Django rodando no terminal em segundo plano.
2. Navegue até a pasta `/build/` no repositório.
3. Execute o aplicativo **`Guiando_Ovelhinha.exe`**.

---
<div align="center">
  <i>"A tecnologia só cumpre seu papel quando se torna invisível e resolve problemas reais."</i><br>
  <b>Desenvolvido com excelência técnica e propósito social.</b>
</div>
