# Estimador CAG

Proyecto FastAPI para estimaciones usando CAG desde `app/context/doctora.json` y OpenAI.

## Estructura

```text
estimador-cag/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── estimations.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── llm_service.py
│   └── context/
│       ├── __init__.py
│       ├── examples.py
│       └── doctora.json
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Requisitos

- Python 3.11+
- `uv`
- Una API key de OpenAI

Dependencias principales:

- `fastapi`
- `uvicorn[standard]`
- `pydantic-settings`
- `openai`

## Setup en Windows

Desde PowerShell:

```powershell
cd D:\InstallAnywhere\estimador-cag
uv sync
```

Edita `.env` y coloca tu API key:

```env
OPENAI_API_KEY=tu_api_key_aqui
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o-mini
APP_ENV=development
LOG_LEVEL=DEBUG
CAG_CONTEXT_JSON=app/context/doctora.json
```

## Ejecutar API

```powershell
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Abre la documentación interactiva:

```text
http://127.0.0.1:8000/docs
```

Health check:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/health"
```

Ver contexto CAG activo:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/estimations/context"
```

Crear una estimación:

```powershell
$body = @{
  procedimiento = "consulta_inicial"
  descripcion = "Necesito una primera cita virtual para revisar mi caso."
  variables = @{
    modalidad = "virtual"
    urgencia = "normal"
  }
} | ConvertTo-Json -Depth 5

Invoke-RestMethod `
  -Method Post `
  -Uri "http://127.0.0.1:8000/api/estimations/" `
  -ContentType "application/json" `
  -Body $body
```

## Notas

`doctora.json` contiene el contexto CAG inicial. Ajusta el catálogo, reglas, rangos y ejemplos según tus datos reales.

No subas `.env` a Git. `.gitignore` ya lo excluye.
