# 🏦 Dashboard Focus — Banco Central do Brasil

Visualização interativa dos dados históricos do Relatório Focus, consumindo diretamente a [API pública do BCB](https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/).

## Indicadores disponíveis
- IPCA, IGP-M, Taxa Selic, PIB Total, Câmbio (USD), Balança Comercial, Produção Industrial

## Funcionalidades
- 📊 Gráficos interativos com zoom, pan e múltiplas séries
- 🃏 Cards de resumo com variação semanal
- 📋 Tabela ordenável + exportação CSV
- 🎛️ Filtros por período, ano de referência e suavização
- 🌓 Tema claro/escuro

---

## 🚀 Deploy no Streamlit Cloud (passo a passo)

### 1. Suba o repositório para o GitHub
```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/focus-bcb-dashboard.git
git push -u origin main
```

### 2. Acesse o Streamlit Cloud
1. Vá para [share.streamlit.io](https://share.streamlit.io)
2. Clique em **"New app"**
3. Conecte sua conta do GitHub
4. Selecione o repositório `focus-bcb-dashboard`
5. Defina **Main file path** como `app.py`
6. Clique em **Deploy!**

---

## ▶️ Rodar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura do projeto
```
focus-bcb-dashboard/
├── app.py               # Wrapper Streamlit
├── dashboard.html       # Dashboard completo (HTML/CSS/JS)
├── requirements.txt     # Dependências Python
├── .streamlit/
│   └── config.toml      # Configurações do Streamlit
├── .gitignore
└── README.md
```
