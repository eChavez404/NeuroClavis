<div align="center">

# 🧠 NeuroClavis
### *As chaves digitais para decodificar a mente da criança.*

[![Unity](https://img.shields.io/badge/Unity-6-black?style=for-the-badge&logo=unity)](https://unity.com/)
[![C#](https://img.shields.io/badge/C%23-Orientado_a_Eventos-239120?style=for-the-badge&logo=c-sharp)](https://learn.microsoft.com/dotnet/csharp/)
[![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/AI_Co--Pilot-GPT--4o--mini-412991?style=for-the-badge&logo=openai)](https://openai.com/)
[![Google AI](https://img.shields.io/badge/Google_Gemini-SDK_Integrado-4285F4?style=for-the-badge&logo=google)](https://ai.google.dev/)
[![JWT](https://img.shields.io/badge/Auth-JWT_Bearer-000000?style=for-the-badge&logo=jsonwebtokens)](https://jwt.io/)
[![Status](https://img.shields.io/badge/Status-MVP_Completo-28a745?style=for-the-badge)](https://github.com/eChavez404/NeuroClavis)

<br>

> *Uma plataforma de **Digital Therapeutics (DTx)** que transforma avaliações neuropsicológicas infantis em experiências lúdicas, combinando um motor gráfico 2D, telemetria comportamental invisível e Inteligência Artificial Generativa para gerar laudos clínicos baseados em evidências — sem que a criança perceba que está sendo avaliada.*

</div>

---

## 🎯 O Problema e a Nossa Solução

O processo tradicional de diagnóstico de transtornos do neurodesenvolvimento — como **TDAH, TEA e Transtornos Motores** — é moroso, caro e emocionalmente pesado. Crianças submetidas a baterias de testes clássicos frequentemente desenvolvem **"ansiedade de performance"**, que mascara seus reais comportamentos cognitivos e invalida os resultados.

**O NeuroClavis inverte essa lógica.**

Enquanto a criança joga um puzzle de encaixe de peças aparentemente simples, o sistema atua como um **microscópio comportamental invisível**: captura cada milissegundo de hesitação, cada clique impulsivo, cada gesto de frustração e cada falha motora — sem jamais interromper o estado de *flow* da criança. Ao término da sessão, um modelo de IA analisa esses padrões e entrega ao profissional de saúde um relatório pré-clínico detalhado, em linguagem natural, em questão de segundos.

---

## 🏗️ Visão Geral da Arquitetura

O ecossistema é composto por três camadas integradas:

```
┌─────────────────────────────────────────────────────────────────┐
│  🎮  FRONTEND  (Unity 6 / C#)                                   │
│  Guiando Ovelhinha — Game Engine com Motor de Telemetria        │
│  └─► Physics2D · SmoothDamp · PlayerTelemetryCollector          │
│  └─► Singleton TelemetryApiSender · DTO DjangoPayload           │
└───────────────────────────────┬─────────────────────────────────┘
                                │  HTTP POST · JWT Bearer
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│  ⚙️  BACKEND  (Django 6.0.3 / Python 3.11 / DRF)               │
│  API REST segura por JSON Web Tokens                            │
│  └─► View (Skinny) · Serializer · Service Layer (services.py)  │
│  └─► Integração OpenAI (GPT-4o-mini) + Google Gemini SDK        │
└───────────────────────────────┬─────────────────────────────────┘
                                │  ORM Django
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│  🗄️  BANCO DE DADOS  (SQLite → MySQL-ready)                     │
│  Schema normalizado até a 3ª Forma Normal (3FN)                 │
│  └─► Usuario · Diagnostico · Paciente · SessaoJogo · Log        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 O Motor da Inovação — O que construímos, de verdade

### 🎮 1. Game Design Focado em Psicologia (Frontend — Unity 6)

Este não é apenas um jogo. Cada decisão de design esconde uma intenção clínica:

- **Física Clínica com `Vector3.SmoothDamp`:** A movimentação das peças é matematicamente suavizada via interpolação vetorial. Isso elimina qualquer rigidez artificial do motor gráfico da resposta do mouse, garantindo que a medição da **coordenação visomotora fina** da criança seja pura, sem ruído tecnológico.

- **Filosofia do "Soft Fail" (Falha Silenciosa):** Telas de *Game Over* causam picos de cortisol e invalidam clinicamente o teste. No NeuroClavis, quando a criança erra o encaixe, a peça simplesmente retorna suavemente à posição original. O jogo **nunca pune**, mas o sistema registra o erro silenciosamente, com precisão cirúrgica.

- **Detecção de Área com `Physics2D.OverlapBoxAll` + LayerMasks:** Rejeitamos o uso de simples *Colliders Trigger*, que falham em movimentos rápidos (bug de *tunneling*). Construímos um sistema de validação de área matemática usando varredura de caixas de colisão (`OverlapBoxAll`) filtradas por máscaras de camada (`LayerMask`). Isso garante **100% de precisão na detecção de acertos e erros**, sem falsos positivos.

- **Mecânica de Drag & Drop com Snap:** A interação é natural e intuitiva para crianças. A peça "gruda" no alvo correto com feedback visual, recompensando a conclusão sem criar pistas que eliminariam o valor do teste.

---

### 🧠 2. O Cérebro Invisível — Telemetria Clínica de Alta Precisão

Enquanto a criança joga, o componente `PlayerTelemetryCollector` opera silenciosamente em *background*, traduzindo cada interação bruta da engine em um marcador clínico estruturado. Ao final da sessão, esses **8 marcadores** são empacotados pelo DTO `DjangoPayload` e enviados em um único `HTTP POST` autenticado para a API.

| Campo no Banco (`SessaoJogo`) | Ação Capturada no Jogo | Marcador Clínico |
| :--- | :--- | :--- |
| `tempo_primeira_acao` | Segundos até o 1º clique na peça | **Latência de Resposta** — velocidade de processamento visual inicial e planejamento de ação. |
| `tempo_total` | Duração total da sessão (segundos) | **Vigilância Sustentada** — capacidade de manter o foco durante toda a tarefa. |
| `cliques_falsos` | Cliques em áreas inativas da tela | **Controle Inibitório** — marcador primário de impulsividade, associado ao TDAH. |
| `solturas_erradas` | Peça solta sobre alvo incorreto | **Praxia Visuoespacial** — falha no planejamento espacial vs. tentativa & erro impulsivo. |
| `qtd_quedas` | Peça saiu do cursor durante o arraste | **Destreza Motora Fina** — coordenação visomotora e precisão do movimento de pinça. |
| `tempo_segurando_peca` | Segundos com a peça "presa" no cursor | **Tempo de Ideação** — planejamento de rota cognitiva antes de executar o movimento. |
| `cliques_frustracao` | Cliques rápidos e repetitivos em <500ms | **Regulação Emocional** — baixa tolerância à frustração sob pressão. |
| `tempo_congelado_pos_erro` | Inatividade imediatamente após um erro | **Tempo Refratário** — bloqueio cognitivo pós-falha e velocidade de recuperação. |

---

### 🤖 3. Co-Piloto Clínico — Inteligência Artificial Generativa

O backend vai muito além de um simples CRUD. Ao receber a telemetria, aciona imediatamente o módulo `services.py`, que se comunica com modelos de linguagem avançados:

**Configuração da IA (`gerar_laudo_com_ia`):**
| Parâmetro | Valor |
| :--- | :--- |
| **Provedor** | OpenAI SDK via GitHub Models (Azure AI Endpoint) |
| **Modelo** | `gpt-4o-mini` |
| **Temperatura** | `0.2` (baixíssima — saída determinística, sem "alucinações") |
| **Max Tokens** | `250` (laudos precisos e sem verbosidade clínica excessiva) |
| **Endpoint** | `https://models.inference.ai.azure.com` |
| **SDK Adicional** | `google-genai` (Google Gemini SDK também integrado) |

**Engenharia de Prompt (Prompt Engineering):**
O sistema usa um *role* de "Doutor em Neurociência Cognitiva" com uma **diretiva crítica anti-viés**: o modelo é explicitamente instruído a reconhecer e reportar padrões **NEUROTÍPICOS (desenvolvimento normativo)**, evitando superdiagnosticar transtornos onde a criança apresentou desempenho preservado.

**Perfis Reconhecidos pela IA:**
1. 🟢 **PADRÃO PRESERVADO (NEUROTÍPICO):** Poucos erros, latências adequadas → funções executivas preservadas.
2. 🟡 **PERFIL ANSIOSO / RIGIDEZ COGNITIVA:** Alta latência inicial + alto tempo de ideação + alto tempo congelado → possível ansiedade ou dificuldade de transição.
3. 🔵 **PERFIL DISPRÁXICO / MOTOR:** Muitas quedas + muitas solturas erradas + baixa impulsividade → possível transtorno da coordenação motora.
4. 🔴 **PERFIL IMPULSIVO / HIPERATIVO:** Muitos cliques falsos + cliques de frustração → falha no controle inibitório (marcador central do TDAH).

O laudo gerado é salvo no campo `laudo_ia` da `SessaoJogo` e fica imediatamente disponível no painel administrativo do médico.

---

## 📐 Engenharia de Software Avançada — Design Patterns

O código foi desenhado para ser **escalável, manutenível e blindado contra falhas**, utilizando padrões consolidados da indústria de software:

### 🎮 No Unity (C#)

- **Data Transfer Object (DTO) — `DjangoPayload`:**
  A engine Unity gerencia seus dados internamente com estruturas pesadas e incompatíveis com JSON (`GameObjects`, `Transforms`, `Vector3`, `Collider2D`). Em vez de expor essa complexidade à API, criamos a classe `DjangoPayload`: um objeto simples, plano e serializável, que contém **apenas os 8 floats/ints** que a API Django precisa. Essa separação cria um contrato explícito e protege o sistema de jogo contra qualquer mudança no contrato da API, e vice-versa.

- **Singleton Pattern + `DontDestroyOnLoad` — `TelemetryApiSender`:**
  O sistema de coleta e envio de telemetria é um `Singleton`: existe **uma única instância** em toda a execução do jogo. Ao ser instanciado na primeira cena, o objeto é marcado com `DontDestroyOnLoad`, tornando-o imune à destruição durante as transições de cena. Isso garante que nenhuma métrica clínica seja perdida por engasgos ou recarregamentos de cena.

- **Component-Based Architecture & Event-Driven Design:**
  A lógica de física, a interface do usuário e a telemetria são componentes totalmente desacoplados. A UI nunca sabe como a física funciona; ela apenas reage a eventos (`C# Delegates`). Isso torna o sistema facilmente extensível para novas fases e mecânicas.

### ⚙️ No Django (Python)

- **Service Layer Pattern (Skinny Views):**
  Aplicamos rigorosamente o princípio de *Separação de Preocupações*. As `Views` (`views.py`) são enxutas: validam o JWT, desserializam o corpo da requisição e chamam a camada de serviço. Toda a inteligência — a comunicação com a OpenAI, a construção do prompt, o tratamento de exceções da API de IA — vive em `services.py`. O resultado: Views com menos de 30 linhas, serviços testáveis em isolamento.

- **Custom User Model — `AbstractUser` com autenticação por E-mail:**
  O Django padrão usa `username` como chave de autenticação. Sobrescrevemos essa arquitetura base herdando de `AbstractUser` e definindo `email` como `USERNAME_FIELD`. O `UsuarioManager` customizado encapsula a lógica de `create_user` e `create_superuser`, garantindo que o sistema seja **à prova de alterações futuras** na estratégia de autenticação.

- **`TimeStampedModel` (Abstract Base Model — DRY):**
  Para garantir rastreabilidade em todos os registros sem duplicar código, criamos o model abstrato `TimeStampedModel`, que injeta automaticamente os campos `created_at` e `updated_at` em qualquer model que o herde (`Diagnostico`, `Paciente`, `SessaoJogo`, `RegistroLog`). Alteração em um único lugar; efeito em todo o banco.

- **Automated Data Migration (Seeding via `migrations.RunPython`):**
  Em vez de exigir que o avaliador execute um `createsuperuser` interativo no terminal, injetamos um script de *seed* diretamente na esteira de migrations do Django (`0002_auto_20260401_2028.py`). A função `criar_usuario_master` é chamada automaticamente pelo `python manage.py migrate`. **O banco nasce provisionado.** A função `reverter_seed` garante que a migration seja reversível (`migrate --unapply`), seguindo as boas práticas do Django.

- **`RegistroLog` — Trilha de Auditoria (Audit Trail):**
  Toda ação de registro de sessão de jogo gera um `RegistroLog` com o nível (`INFO`, `WARNING`, `ERROR`), a ação realizada, os detalhes e o IP de origem. O model é configurado como **somente leitura no admin** (sem permissão de adicionar, alterar ou deletar via interface), garantindo a integridade da trilha de auditoria. Essa é uma prática essencial para sistemas de saúde em conformidade com a LGPD.

---

## 🗄️ Banco de Dados Normalizado até a 3ª Forma Normal (3FN)

O schema foi projetado com rigor acadêmico. Cada tabela obedece às três primeiras formas normais, eliminando redundâncias e dependências transitivas:

**Por que 3FN?**
- **1FN:** Todos os atributos são atômicos. Nenhum campo armazena listas ou grupos repetitivos.
- **2FN:** Todas as tabelas têm chaves primárias simples (UUID ou BigInt). Não existem dependências parciais.
- **3FN:** Nenhum atributo não-chave depende de outro atributo não-chave. Por exemplo, o `nome` do diagnóstico não está dentro de `Paciente` — ele vive em sua própria tabela `Diagnostico` e é referenciado via chave estrangeira.

**Diagrama de Entidade-Relacionamento:**

```
┌──────────────┐        ┌──────────────────┐        ┌──────────────────────────────┐
│  Diagnostico │        │     Paciente     │        │         SessaoJogo           │
│──────────────│        │──────────────────│        │──────────────────────────────│
│ id (UUID) PK │◄──┐    │ id (UUID) PK     │◄──┐    │ id (UUID) PK                 │
│ nome (unique)│   └────│ diagnostico_id FK│   └────│ paciente_id FK               │
│ created_at   │        │ nome             │        │ tempo_primeira_acao (float)   │
│ updated_at   │        │ data_nascimento  │        │ tempo_total (float)           │
└──────────────┘        │ created_at       │        │ cliques_falsos (int)          │
                        │ updated_at       │        │ solturas_erradas (int)        │
                        └──────────────────┘        │ qtd_quedas (int)             │
                                                    │ tempo_segurando_peca (float) │
┌──────────────┐                                    │ cliques_frustracao (int)     │
│   Usuario    │        ┌──────────────────┐        │ tempo_congelado_pos_erro (f.) │
│──────────────│        │   RegistroLog    │        │ laudo_ia (text)              │
│ id (BigInt)PK│        │──────────────────│        │ created_at                   │
│ email(unique)│        │ id (UUID) PK     │        │ updated_at                   │
│ password     │        │ nivel (choices)  │        └──────────────────────────────┘
│ is_staff     │        │ acao             │
│ is_superuser │        │ detalhes         │
│ date_joined  │        │ ip_origem        │
└──────────────┘        │ created_at       │
                        │ updated_at       │
                        └──────────────────┘
```

**Decisões de Design Notáveis:**
- **UUIDs como Chaves Primárias** em `Diagnostico`, `Paciente`, `SessaoJogo` e `RegistroLog`: proteção contra enumeração de IDs e conformidade com a **LGPD** (anonimização de pacientes).
- **Separação de `Diagnostico`:** o diagnóstico não é um simples `CharField` em `Paciente`. É uma entidade própria com ciclo de vida independente, permitindo que futuras categorias (CID-10, DSM-5) sejam adicionadas sem alterar a estrutura de `Paciente`.
- **`laudo_ia` em `SessaoJogo`:** o laudo é um atributo funcional da sessão, não uma entidade separada. Ele nasce `blank` e é preenchido atomicamente pela IA na mesma transação de criação da sessão.

---

## 🛠️ Stack Tecnológica Completa

### Backend
| Categoria | Tecnologia | Versão |
| :--- | :--- | :--- |
| Framework Web | Django + Django REST Framework | 6.0.3 / 3.17.1 |
| Autenticação | djangorestframework-simplejwt | 5.5.1 |
| IA (OpenAI) | openai SDK | 2.30.0 |
| IA (Google) | google-genai | 1.69.0 |
| Banco de Dados | SQLite (dev) / MySQL-ready | mysqlclient 2.2.8 |
| Variáveis de Ambiente | python-dotenv | 1.2.2 |
| HTTP Client | httpx + requests | 0.28.1 / 2.33.1 |
| Serialização | pydantic | 2.12.5 |
| Segurança | cryptography + PyJWT | 46.0.6 / 2.12.1 |
| Retry Logic | tenacity | 9.1.4 |
| Async / WSGI | asgiref | 3.11.1 |

### Frontend
| Categoria | Tecnologia |
| :--- | :--- |
| Motor Gráfico | Unity 6 (LTS) |
| Linguagem | C# (.NET) |
| Comunicação HTTP | `UnityWebRequest` + Coroutines |
| Física 2D | `Physics2D.OverlapBoxAll` + `Vector3.SmoothDamp` |
| Build | Windows x86-64 PE32+ (`.exe`) |

### DevOps & Qualidade
| Área | Decisão |
| :--- | :--- |
| Versionamento | Git + GitHub |
| Timezone | America/Sao_Paulo (`pt-br`) |
| Token JWT | 365 dias (sessões de jogo persistentes) |
| Proteção CSRF | Global + desativada pontualmente na API do jogo (trust JWT) |
| Conformidade | LGPD (UUIDs, sem PII exposta na API) |

---

## 🔌 Mapa de Endpoints da API

| Método | Endpoint | Autenticação | Descrição |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/token/` | Público | Obtém os tokens JWT (access + refresh). Entrada: `email` + `password`. |
| `POST` | `/api/token/refresh/` | Público | Renova o access token a partir do refresh token. |
| `POST` | `/api/sessoes/` | `Bearer <JWT>` | Recebe o payload de telemetria do jogo, cria a sessão e aciona a IA para gerar o laudo. |
| `GET` | `/` | Staff Django | Acesso ao painel administrativo (médicos e gestores). |

**Exemplo de Payload enviado pelo Jogo:**
```json
{
  "paciente": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "tempo_primeira_acao": 3.812,
  "tempo_total": 124.5,
  "cliques_falsos": 7,
  "solturas_erradas": 3,
  "qtd_quedas": 5,
  "tempo_segurando_peca": 8.24,
  "cliques_frustracao": 12,
  "tempo_congelado_pos_erro": 2.1
}
```

**Resposta da API (incluindo laudo da IA):**
```json
{
  "mensagem": "Sessão registrada com sucesso.",
  "laudo_ia": "A sessão revela um perfil de atenção seletiva com possível comprometimento do controle inibitório. O número elevado de cliques falsos (7) e cliques de frustração (12), combinado com um tempo de reação preservado, sugere dificuldade na inibição de respostas motoras impulsivas, padrão frequentemente observado no TDAH-I. Recomenda-se avaliação clínica complementar com instrumentos específicos de rastreio de atenção."
}
```

---

## ⚙️ Como Executar o Projeto (Zero-Config Setup)

O projeto foi preparado para ser avaliado da forma mais rápida e sem fricção possível.

### 1. Backend (Servidor Django)

```bash
# Clone o repositório
git clone https://github.com/eChavez404/NeuroClavis.git
cd NeuroClavis

# Crie e ative o ambiente virtual
python -m venv .venv

# Windows (PowerShell)
python -m pip install --upgrade pip
.venv\Scripts\Activate.ps1

# Linux / Mac
# source .venv/bin/activate

# Instale as dependências
python -m pip install -r requirements.txt

# Configure as variáveis de ambiente
# Copie o arquivo de exemplo e preencha com seus tokens:
# cp env.example .env
#
# Conteúdo do .env:
# SECRET_KEY=uma-chave-secreta-longa-e-aleatoria
# GITHUB_TOKEN=seu_token_do_github_models_aqui
# DEBUG=True
# ALLOWED_HOSTS=*

# Construa o banco de dados (o Super Admin é criado automaticamente)
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

> 🔑 **Credenciais de Acesso (Provisionadas Automaticamente pelo Seed):**
>
> Graças à nossa arquitetura de *Data Migrations* com `RunPython`, o usuário Master é criado no momento em que o banco é inicializado — sem necessidade de nenhum comando adicional.
>
> Acesse o painel em **`http://127.0.0.1:8000/`** com:
> | Campo | Valor |
> | :--- | :--- |
> | **E-mail** | `admin@gmail.com` |
> | **Senha** | `Clavis` |

### 2. Frontend (Jogo — Sem necessidade de instalar a Unity)

Para facilitar a avaliação sem precisar da engine, disponibilizamos o *build* executável:

1. Certifique-se de que o servidor Django está **rodando em background**.
2. Navegue até a pasta `/build/` no repositório.
3. Execute **`Guiando_Ovelhinha.exe`**.
4. Jogue a fase. Tente propositalmente:
   - Clicar várias vezes fora das peças (teste o controle inibitório 🔴)
   - Soltar a peça no lugar errado (teste a praxia visuoespacial 🔵)
   - Ficar parado após um erro (teste o tempo refratário 🟡)
5. Ao finalizar a fase, o jogo enviará silenciosamente a telemetria via `HTTP POST + JWT Bearer` para a API.
6. A IA gerará o laudo e ele aparecerá no painel do Django em segundos.

---

## 📁 Estrutura do Repositório

```
NeuroClavis/
│
├── 📁 build/
│   └── Guiando_Ovelhinha.exe       # Build executável do jogo (Windows x86-64)
│
├── 📁 core/                        # Configurações do projeto Django
│   ├── settings.py                 # Configurações globais (JWT, DB, Apps, LGPD)
│   ├── urls.py                     # Roteamento principal (admin + api/)
│   ├── asgi.py / wsgi.py           # Interfaces de servidor
│
├── 📁 neuroclavis/                 # App principal
│   ├── models.py                   # 5 modelos: Usuario, Diagnostico, Paciente,
│   │                               #            SessaoJogo, RegistroLog
│   ├── views.py                    # View enxuta (Skinny View)
│   ├── serializers.py              # Contrato da API (DRF ModelSerializer)
│   ├── services.py                 # Service Layer: integração com IA Generativa
│   ├── admin.py                    # Painel admin configurado (inlines, readonly)
│   ├── urls.py                     # Rotas da app
│   └── 📁 migrations/
│       ├── 0001_initial.py         # Criação completa do schema (3FN)
│       └── 0002_auto_20260401_2028.py  # Data Migration: Seed do Super Admin
│
├── manage.py                       # Entry point do Django
├── requirements.txt                # 48 dependências Python
├── env.example                     # Template de variáveis de ambiente
└── README.md                       # Este documento
```

---

## 🔒 Segurança e Conformidade (LGPD)

| Medida | Implementação |
| :--- | :--- |
| **Autenticação Stateless** | JWT Bearer com 365 dias de validade para sessões de jogo persistentes |
| **Anonimização de Pacientes** | UUIDs como PKs — IDs sequenciais nunca são expostos na API |
| **Proteção CSRF** | Habilitada globalmente; desativada cirurgicamente apenas no endpoint de telemetria |
| **Variáveis Sensíveis** | `SECRET_KEY` e `GITHUB_TOKEN` carregados de `.env` (nunca no código-fonte) |
| **Trilha de Auditoria** | `RegistroLog` registra toda ação com IP de origem, somente leitura no admin |
| **Senha Hashada** | Django `AbstractUser` + `make_password` — nenhuma senha armazenada em texto plano |

---

<div align="center">

---

*"A tecnologia só cumpre seu papel quando se torna invisível e resolve problemas reais."*

**NeuroClavis — 2026**

*Desenvolvido com excelência técnica e propósito social.*

</div>
