import re

with open("locale/pt_BR/LC_MESSAGES/django.po", "r") as f:
    lines = f.readlines()

translations = {
    "FinGen": "FinGen",
    "Dirb-like — Web Directory Scanner": "Dirb-like — Scanner de Diretórios Web",
    "CV-Spammer — Automated Job Application Bot": "CV-Spammer — Bot Automatizado de Vagas",
    "CambioMatic — ERP for Auto Shops": "CambioMatic — ERP para Oficinas",
    "Django SaaS Boilerplate": "Django SaaS Boilerplate",
    "Security Research & Offensive Tooling": "Pesquisa de Segurança e Ferramentas Ofensivas",
    "CourierIQ — Logistics Microservices": "CourierIQ — Microsserviços de Logística",
    "Most people manage money reactively — they notice problems after they happen. FinGen changes that. Upload a bank statement PDF and the system parses your real transaction history, feeds it to an AI financial advisor, and returns concrete recommendations: where you're bleeding money, how your cash flow compares month-over-month, and where to invest based on current market data scraped live. Built with Spring Boot on the backend, Thymeleaf + HTMX on the front, and a Three.js animated currency visualization on the landing page.": "A maioria das pessoas gerencia dinheiro de forma reativa — elas percebem os problemas depois que eles acontecem. O FinGen muda isso. Faça o upload de um extrato bancário em PDF e o sistema analisa seu histórico real de transações, envia para um consultor financeiro com IA e retorna recomendações concretas: onde você está perdendo dinheiro, como seu fluxo de caixa se compara mês a mês e onde investir com base em dados de mercado atuais extraídos em tempo real. Construído com Spring Boot no backend, Thymeleaf + HTMX no front-end, e uma visualização de moeda animada em Three.js na página inicial.",
    "A brute-force web directory scanner built entirely in pure Python — no external libraries, no requests, no shortcuts. HTTP and HTTPS handlers written from scratch against the RFC spec. The point wasn't to reinvent the wheel; it was to understand exactly what tools like DIRB are doing under the hood before trusting them blindly. Concurrent scanning, configurable wordlists, and clean output formatting.": "Um scanner de diretórios web por força bruta construído inteiramente em Python puro — sem bibliotecas externas, sem requests, sem atalhos. Handlers HTTP e HTTPS escritos do zero seguindo a especificação RFC. O objetivo não era reinventar a roda; era entender exatamente o que ferramentas como o DIRB estão fazendo por baixo dos panos antes de confiar nelas cegamente. Escaneamento concorrente, wordlists configuráveis e formatação limpa de saída.",
    "Job hunting at scale is a numbers game. CV-Spammer is a web scraper and automation tool that searches job boards, filters listings by role and location, and fires off tailored application emails — automatically. Built to solve a real problem (sending hundreds of applications manually is brutal), and as a practical exercise in scraping, browser automation, and SMTP handling.": "Procurar emprego em escala é um jogo de números. CV-Spammer é um web scraper e ferramenta de automação que pesquisa em painéis de empregos, filtra as vagas por função e localização, e dispara e-mails de candidatura personalizados — automaticamente. Construído para resolver um problema real (enviar centenas de candidaturas manualmente é brutal), e como um exercício prático de scraping, automação de navegador e manipulação SMTP.",
    "Small auto repair shops run on paper, WhatsApp messages, and memory. CambioMatic replaces that with a full ERP: service orders from open to invoiced, inventory tracking, customer records, and billing — all in one place. Built for non-technical operators who need something that just works, without training or IT support. Currently live and in use.": "Pequenas oficinas mecânicas funcionam com papel, mensagens de WhatsApp e memória. O CambioMatic substitui isso por um ERP completo: ordens de serviço do início ao faturamento, controle de estoque, registros de clientes e cobrança — tudo em um só lugar. Construído para operadores não técnicos que precisam de algo que simplesmente funcione, sem treinamento ou suporte de TI. Atualmente em produção e uso.",
    "Starting a SaaS from scratch means solving the same problems every time: auth, subscriptions, async tasks, database. This boilerplate eliminates that. Stripe subscription billing, OAuth2 via Google and GitHub, Celery for background jobs, and Postgres on Neon — production-ready architecture with proper separation of concerns. Designed to be the foundation you actually want to build on.": "Começar um SaaS do zero significa resolver os mesmos problemas todas as vezes: autenticação, assinaturas, tarefas assíncronas, banco de dados. Este boilerplate elimina isso. Faturamento de assinaturas via Stripe, OAuth2 via Google e GitHub, Celery para tarefas em segundo plano e Postgres no Neon — arquitetura pronta para produção com separação adequada de responsabilidades. Projetado para ser a base sobre a qual você realmente quer construir.",
    "A collection of self-directed security research done alongside formal ethical hacking coursework at university. Areas covered: network-layer attack analysis (understanding how DoS/DDoS traffic behaves at the protocol level, studied in isolated lab environments); Android security research (APK structure, static analysis, and payload behavior in sandboxed VMs); physical access testing with a Raspberry Pi Pico flashed as a USB HID device (Rubber Ducky-style keystroke injection); and web recon automation. All conducted in controlled environments — VMs, local labs, or with explicit permission. The goal: understand how attacks work before trying to defend against them.": "Uma coleção de pesquisas de segurança autodirecionadas feitas em paralelo ao curso formal de ethical hacking na universidade. Áreas abordadas: análise de ataques na camada de rede (entendendo como o tráfego DoS/DDoS se comporta no nível do protocolo, estudado em ambientes de laboratório isolados); pesquisa de segurança Android (estrutura do APK, análise estática e comportamento de payload em VMs isoladas); testes de acesso físico com um Raspberry Pi Pico modificado como um dispositivo USB HID (injeção de teclas no estilo Rubber Ducky); e automação de reconhecimento web. Tudo conduzido em ambientes controlados — VMs, laboratórios locais, ou com permissão explícita. O objetivo: entender como os ataques funcionam antes de tentar defender-se contra eles.",
    "Real-time package tracking system designed for throughput. Microservices architecture with FastAPI, event streams via Redis, live WebSocket dashboards, and dynamic ETA recalculation as shipments move. Built to explore async patterns, clean architecture, and production-grade error handling under concurrent load.": "Sistema de rastreamento de pacotes em tempo real projetado para alto rendimento. Arquitetura de microsserviços com FastAPI, fluxos de eventos via Redis, dashboards ao vivo em WebSocket e recálculo dinâmico de ETA conforme as remessas se movem. Construído para explorar padrões assíncronos, arquitetura limpa e tratamento de erros de nível de produção sob carga concorrente.",
    "// AI financial advisor": "// Consultor financeiro de IA",
    "POST /api/chat/analyze": "POST /api/chat/analyze",
    "→ Parsing statement...": "→ Analisando extrato...",
    "→ Monthly spend: R$ 3.240": "→ Gasto mensal: R$ 3.240",
    "→ Savings rate: 18.4%": "→ Taxa de poupança: 18,4%",
    "→ Recommendation ready ✓": "→ Recomendação pronta ✓"
}

out_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith('msgid '):
        msgid = line[6:].strip().strip('"')
        
        # handle multiline msgid
        j = i + 1
        while j < len(lines) and lines[j].startswith('"'):
            msgid += lines[j].strip().strip('"')
            j += 1
        
        if msgid in translations:
            out_lines.append(line)
            # append remaining msgid lines if any
            for k in range(i+1, j):
                out_lines.append(lines[k])
                
            out_lines.append(f'msgstr "{translations[msgid]}"\n')
            
            # skip the original msgstr block
            while j < len(lines) and (lines[j].startswith('msgstr ') or lines[j].startswith('"')):
                j += 1
            i = j - 1
        else:
            out_lines.append(line)
    else:
        out_lines.append(line)
    i += 1

with open("locale/pt_BR/LC_MESSAGES/django.po", "w") as f:
    f.writelines(out_lines)

print("Translation applied.")
