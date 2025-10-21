import streamlit as st
from Back_banco import SistemaBancario

# Configuração da página
st.set_page_config(
    page_title="Sistema Bancário",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Customizado - Tema Nubank (Dark/Purple/Blue)
st.markdown("""
<style>
    /* Importar fontes modernas */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Tema Dark Global */
    .stApp {
        background: linear-gradient(135deg, #0a1929 0%, #1e3a5f 50%, #0d47a1 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1b2a 0%, #1b263b 100%);
border-right: 2px solid rgba(59, 130, 246, 0.3);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Títulos */
    h1, h2, h3 {
        color: white !important;
        font-weight: 700 !important;
        text-shadow: 0 2px 10px rgba(138, 43, 226, 0.3);
    }
    
    h1 {
        font-size: 2.5rem !important;
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Texto */
    p, label, span, div {
        color: #e0e0e0 !important;
    }
    
    /* Botões */
    .stButton>button {
        width: 100%;
        height: 55px;
        border-radius: 12px;
        border: none;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
    }
    
    /* Botão Primary */
    .stButton>button[kind="primary"] {
       background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
       box-shadow: 0 4px 15px rgba(37, 99, 235, 0.5);
    }
    
    .stButton>button[kind="primary"]:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
box-shadow: 0 6px 25px rgba(37, 99, 235, 0.7);
    }
    
    /* Inputs */
    .stTextInput>div>div>input,
    .stNumberInput>div>div>input,
    .stTextArea>div>div>textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid rgba(59, 130, 246, 0.3) !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 12px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput>div>div>input:focus,
    .stNumberInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: #3b82f6 !important;
box-shadow: 0 0 20px rgba(59, 130, 246, 0.4) !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }
    
    /* SelectBox */
    .stSelectbox>div>div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid rgba(59, 130, 246, 0.3) !important;
        border-radius: 12px !important;
        color: white !important;
    }
    
    /* Cards/Containers */
    .element-container {
        backdrop-filter: blur(10px);
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #3b82f6 !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #b0b0b0 !important;
        font-weight: 600 !important;
    }
    
    /* Info boxes */
    .stAlert {
        background: rgba(102, 126, 234, 0.1) !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: 12px !important;
        color: white !important;
    }
    
    /* Success messages */
    .stSuccess {
        background: rgba(34, 197, 94, 0.15) !important;
        border-left: 4px solid #22c55e !important;
        color: #4ade80 !important;
    }
    
    /* Error messages */
    .stError {
        background: rgba(239, 68, 68, 0.15) !important;
        border-left: 4px solid #ef4444 !important;
        color: #f87171 !important;
    }
    
    /* Warning messages */
    .stWarning {
        background: rgba(251, 191, 36, 0.15) !important;
        border-left: 4px solid #fbbf24 !important;
        color: #fcd34d !important;
    }
    
    /* Cards personalizados */
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 12px 40px rgba(59, 130, 246, 0.4);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(138, 43, 226, 0.4);
        border-color: rgba(59, 130, 246, 0.5);
    }
    
    /* Glassmorphism effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }
    
    /* Divider */
    hr {
        border-color: rgba(59, 130, 246, 0.3) !important;
        margin: 30px 0 !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.2);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
    }
    
    /* Animação de entrada */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .main > div {
        animation: fadeIn 0.5s ease-out;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar o sistema bancário
if 'sistema' not in st.session_state:
    st.session_state.sistema = SistemaBancario()
if 'conta_selecionada' not in st.session_state:
    st.session_state.conta_selecionada = None

sistema = st.session_state.sistema

# Header com logo e título
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="70" height="70">
            <defs>
                <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#3b82f6;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#1e40af;stop-opacity:1" />
                </linearGradient>
                <linearGradient id="lightBlue" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:#60a5fa;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#3b82f6;stop-opacity:1" />
                </linearGradient>
            </defs>
            <circle cx="100" cy="100" r="95" fill="url(#blueGrad)" opacity="0.15"/>
            <path d="M 40 90 L 100 60 L 160 90 Z" fill="url(#lightBlue)" stroke="#1e40af" stroke-width="2.5"/>
            <rect x="45" y="88" width="110" height="70" fill="#3b82f6" stroke="#1e40af" stroke-width="2.5" rx="3" opacity="0.9"/>
            <rect x="55" y="95" width="12" height="55" fill="#1e40af" opacity="0.6" rx="2"/>
            <rect x="80" y="95" width="12" height="55" fill="#1e40af" opacity="0.6" rx="2"/>
            <rect x="108" y="95" width="12" height="55" fill="#1e40af" opacity="0.6" rx="2"/>
            <rect x="133" y="95" width="12" height="55" fill="#1e40af" opacity="0.6" rx="2"/>
            <rect x="40" y="158" width="120" height="8" fill="#1e40af" rx="2"/>
            <circle cx="100" cy="125" r="20" fill="#60a5fa" stroke="#1e40af" stroke-width="2.5"/>
            <text x="100" y="138" font-family="Arial" font-size="28" font-weight="bold" fill="#1e40af" text-anchor="middle">$</text>
            <path d="M 30 50 Q 45 45 55 50" fill="none" stroke="#60a5fa" stroke-width="6" stroke-linecap="round"/>
            <ellipse cx="55" cy="50" rx="8" ry="10" fill="#93c5fd" stroke="#3b82f6" stroke-width="2"/>
            <path d="M 57 45 L 60 42 M 57 50 L 61 50 M 57 55 L 60 58" stroke="#3b82f6" stroke-width="2" stroke-linecap="round"/>
            <path d="M 170 50 Q 155 45 145 50" fill="none" stroke="#60a5fa" stroke-width="6" stroke-linecap="round"/>
            <ellipse cx="145" cy="50" rx="8" ry="10" fill="#93c5fd" stroke="#3b82f6" stroke-width="2"/>
            <path d="M 143 45 L 140 42 M 143 50 L 139 50 M 143 55 L 140 58" stroke="#3b82f6" stroke-width="2" stroke-linecap="round"/>
            <ellipse cx="100" cy="50" rx="15" ry="12" fill="#a5f3fc" opacity="0.8" stroke="#3b82f6" stroke-width="2.5"/>
            <path d="M 95 45 Q 100 35 105 45" fill="none" stroke="#3b82f6" stroke-width="2" opacity="0.7" stroke-linecap="round"/>
            <circle cx="90" cy="48" r="2.5" fill="#60a5fa"/>
            <circle cx="110" cy="48" r="2.5" fill="#60a5fa"/>
            <circle cx="100" cy="40" r="2.5" fill="#60a5fa"/>
            <circle cx="100" cy="70" r="3" fill="#93c5fd" opacity="0.7"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("# Sistema Bancário Digital")
    st.markdown("### *Simples, moderno e feito para você*")

st.markdown("---")

# Sidebar - Informações da conta
with st.sidebar:
    st.markdown("### 📊 Sua Conta")
    
    if st.session_state.conta_selecionada:
        conta = st.session_state.conta_selecionada
        
        # Card da conta no sidebar
        st.markdown(f"""
        <div class="glass-card">
            <h4 style="color: #8a2be2; margin-bottom: 10px;">💳 Conta Ativa</h4>
            <p style="font-size: 14px; margin: 5px 0;"><b>👤</b> {conta.usuario.nome}</p>
            <p style="font-size: 14px; margin: 5px 0;"><b>🏦</b> Ag: {conta.agencia}</p>
            <p style="font-size: 14px; margin: 5px 0;"><b>💳</b> C/C: {conta.numero_conta}</p>
            <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(138, 43, 226, 0.3);">
                <p style="font-size: 12px; color: #b0b0b0;">Saldo disponível</p>
                <h2 style="color: #8a2be2; margin: 5px 0;">R$ {conta.consultar_saldo():.2f}</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🔄 Trocar de Conta", use_container_width=True):
            st.session_state.conta_selecionada = None
            st.rerun()
    else:
        st.info("💡 Selecione ou crie uma conta para começar")
    
    st.markdown("---")
    st.markdown("### 📈 Estatísticas")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("👥 Usuários", len(sistema.listar_usuarios()))
    with col2:
        st.metric("💳 Contas", len(sistema.listar_contas()))

# Menu Principal
st.markdown("### 🎯 O que você deseja fazer hoje?")

menu = st.selectbox(
    "Selecione uma operação:",
    ["🏠 Início", "💰 Depositar", "💸 Sacar", "📊 Extrato", 
     "👤 Novo Usuário", "🏦 Nova Conta", "📋 Minhas Contas"],
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

# Tela: Início
if menu == "🏠 Início":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="color: #22c55e;">💰 Depósitos</h3>
            <p style="font-size: 14px;">Deposite seu dinheiro de forma rápida e segura</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="color: #8a2be2;">💸 Saques</h3>
            <p style="font-size: 14px;">Saque quando precisar, sem complicação</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3 style="color: #667eea;">📊 Extratos</h3>
            <p style="font-size: 14px;">Acompanhe todas as suas movimentações</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: white;">🚀 Como começar:</h3>
        <ol style="font-size: 16px; line-height: 2;">
            <li>Cadastre-se em <b>Novo Usuário</b></li>
            <li>Crie sua conta em <b>Nova Conta</b></li>
            <li>Selecione a conta em <b>Minhas Contas</b></li>
            <li>Comece a usar! 💜</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# Tela: Depositar
elif menu == "💰 Depositar":
    st.markdown("## 💰 Realizar Depósito")
    
    if not st.session_state.conta_selecionada:
        st.warning("⚠️ Selecione uma conta em 'Minhas Contas' primeiro!")
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        
        valor = st.number_input(
            "💵 Quanto você quer depositar?",
            min_value=0.01,
            format="%.2f",
            step=50.0,
            help="Digite o valor que deseja depositar"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("✅ Confirmar Depósito", type="primary", use_container_width=True):
                sucesso, mensagem = st.session_state.conta_selecionada.depositar(valor)
                if sucesso:
                    st.success(mensagem)
                    st.balloons()
                else:
                    st.error(mensagem)

# Tela: Sacar
elif menu == "💸 Sacar":
    st.markdown("## 💸 Realizar Saque")
    
    if not st.session_state.conta_selecionada:
        st.warning("⚠️ Selecione uma conta em 'Minhas Contas' primeiro!")
    else:
        conta = st.session_state.conta_selecionada
        
        st.info(f"💡 Limite por saque: R$ {conta.LIMITE_SAQUE:.2f} | Limite diário: {conta.LIMITE_SAQUES_DIA} saques")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        valor = st.number_input(
            "💵 Quanto você quer sacar?",
            min_value=0.01,
            max_value=float(conta.consultar_saldo()),
            format="%.2f",
            step=50.0,
            help="Digite o valor que deseja sacar"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("✅ Confirmar Saque", type="primary", use_container_width=True):
                sucesso, mensagem = conta.sacar(valor)
                if sucesso:
                    st.success(mensagem)
                else:
                    st.error(mensagem)

# Tela: Extrato
elif menu == "📊 Extrato":
    st.markdown("## 📊 Extrato Bancário")
    
    if not st.session_state.conta_selecionada:
        st.warning("⚠️ Selecione uma conta em 'Minhas Contas' primeiro!")
    else:
        conta = st.session_state.conta_selecionada
        extrato = conta.ver_extrato()
        
        # Card com info da conta
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("👤 Titular", conta.usuario.nome[:15] + "..." if len(conta.usuario.nome) > 15 else conta.usuario.nome)
        with col2:
            st.metric("🏦 Agência", conta.agencia)
        with col3:
            st.metric("💳 Conta", conta.numero_conta)
        
        st.markdown("---")
        
        # Extrato
        if not extrato:
            st.info("📭 Nenhuma movimentação realizada ainda.")
        else:
            st.markdown("### 📜 Suas Transações")
            st.markdown("<br>", unsafe_allow_html=True)
            
            for item in reversed(extrato):
                tipo_emoji = "📥" if item['tipo'] == 'Depósito' else "📤"
                cor = "#22c55e" if item['tipo'] == 'Depósito' else "#ef4444"
                sinal = "+" if item['tipo'] == 'Depósito' else "-"
                
                st.markdown(f"""
                <div class="card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h4 style="color: white; margin: 0;">{tipo_emoji} {item['tipo']}</h4>
                            <p style="color: #b0b0b0; margin: 5px 0; font-size: 14px;">🕒 {item['data']}</p>
                        </div>
                        <div>
                            <h2 style="color: {cor}; margin: 0;">{sinal} R$ {item['valor']:.2f}</h2>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Saldo final
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <p style="font-size: 16px; color: #b0b0b0; margin-bottom: 10px;">Saldo Disponível</p>
            <h1 style="color: #8a2be2; margin: 0;">R$ {conta.consultar_saldo():.2f}</h1>
        </div>
        """, unsafe_allow_html=True)

# Tela: Novo Usuário
elif menu == "👤 Novo Usuário":
    st.markdown("## 👤 Cadastro de Usuário")
    st.markdown("### *Preencha seus dados para começar*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.form("form_usuario", clear_on_submit=True):
        nome = st.text_input("📝 Nome Completo*", placeholder="Digite seu nome completo")
        cpf = st.text_input("🆔 CPF*", placeholder="Apenas números", max_chars=11)
        data_nascimento = st.text_input("📅 Data de Nascimento*", placeholder="DD/MM/AAAA")
        endereco = st.text_area("📍 Endereço Completo*", placeholder="Rua, número, bairro, cidade - UF")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button("✅ Cadastrar", use_container_width=True, type="primary")
        
        if submitted:
            if nome and cpf and data_nascimento and endereco:
                sucesso, mensagem = sistema.criar_usuario(nome, cpf, data_nascimento, endereco)
                if sucesso:
                    st.success(mensagem)
                    st.balloons()
                else:
                    st.error(mensagem)
            else:
                st.error("❌ Por favor, preencha todos os campos!")

# Tela: Nova Conta
elif menu == "🏦 Nova Conta":
    st.markdown("## 🏦 Abrir Nova Conta")
    st.markdown("### *Sua conta digital em segundos*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if len(sistema.listar_usuarios()) == 0:
        st.warning("⚠️ Você precisa cadastrar um usuário primeiro!")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➕ Cadastrar Agora", use_container_width=True):
            st.session_state.menu = "👤 Novo Usuário"
            st.rerun()
    else:
        cpf = st.text_input("🆔 Digite seu CPF*", placeholder="Apenas números", max_chars=11)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("✅ Criar Conta", type="primary", use_container_width=True):
                if cpf:
                    sucesso, mensagem = sistema.criar_conta(cpf)
                    if sucesso:
                        st.success(mensagem)
                        st.balloons()
                    else:
                        st.error(mensagem)
                else:
                    st.error("❌ Por favor, informe o CPF!")

# Tela: Minhas Contas
elif menu == "📋 Minhas Contas":
    st.markdown("## 📋 Suas Contas")
    
    contas = sistema.listar_contas()
    
    if not contas:
        st.info("📭 Você ainda não possui contas cadastradas.")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➕ Criar Minha Primeira Conta", use_container_width=True):
            st.session_state.menu = "🏦 Nova Conta"
            st.rerun()
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        
        for conta in contas:
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"""
                <div class="card">
                    <h3 style="color: white; margin-bottom: 10px;">💳 {conta.usuario.nome}</h3>
                    <p style="font-size: 14px; margin: 3px 0;"><b>🏦 Agência:</b> {conta.agencia} | <b>C/C:</b> {conta.numero_conta}</p>
                    <p style="font-size: 14px; margin: 3px 0;"><b>🆔 CPF:</b> {conta.usuario.cpf}</p>
                    <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(138, 43, 226, 0.3);">
                        <h2 style="color: #22c55e; margin: 0;">💰 R$ {conta.consultar_saldo():.2f}</h2>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("<br><br>", unsafe_allow_html=True)
                if st.button("Selecionar", key=f"btn_{conta.numero_conta}", use_container_width=True):
                    st.session_state.conta_selecionada = conta
                    st.success(f"✅ Conta {conta.numero_conta} selecionada!")
                    st.rerun()

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #b0b0b0; padding: 20px;'>
    <p style='font-size: 14px;'>💜 Sistema Bancário Digital</p>
    <p style='font-size: 12px;'>Desenvolvido com Python & Streamlit | Projeto Portfólio</p>
</div>
""", unsafe_allow_html=True)