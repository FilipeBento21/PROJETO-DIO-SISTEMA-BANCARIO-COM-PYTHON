import streamlit as st
from Back_banco import SistemaBancario

# Configuração da página
st.set_page_config(
    page_title="Sistema Bancário",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Customizado
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-weight: bold;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar o sistema bancário
if 'sistema' not in st.session_state:
    st.session_state.sistema = SistemaBancario()
if 'conta_selecionada' not in st.session_state:
    st.session_state.conta_selecionada = None

sistema = st.session_state.sistema

# Header
st.title("🏦 Sistema Bancário Digital")
st.markdown("### Gerencie suas finanças com segurança e praticidade")
st.markdown("---")

# Sidebar - Informações
with st.sidebar:
    st.header("📊 Painel de Controle")
    
    if st.session_state.conta_selecionada:
        conta = st.session_state.conta_selecionada
        st.success("Conta Ativa")
        st.markdown(f"""
        **👤 Titular:** {conta.usuario.nome}  
        **🏦 Agência:** {conta.agencia}  
        **💳 C/C:** {conta.numero_conta}  
        """)
        st.metric("💰 Saldo", f"R$ {conta.consultar_saldo():.2f}")
        
        if st.button("🔄 Trocar de Conta", use_container_width=True):
            st.session_state.conta_selecionada = None
            st.rerun()
    else:
        st.info("ℹ️ Nenhuma conta selecionada")
    
    st.markdown("---")
    st.markdown("### 📈 Estatísticas")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("👥 Usuários", len(sistema.listar_usuarios()))
    with col2:
        st.metric("💳 Contas", len(sistema.listar_contas()))

# Menu Principal
menu = st.selectbox(
    "🎯 Selecione uma operação:",
    ["🏠 Início", "💰 Depositar", "💸 Sacar", "📊 Ver Extrato", 
     "👤 Novo Usuário", "🏦 Nova Conta", "📋 Listar Contas"],
    index=0
)

st.markdown("---")

# Tela: Início
if menu == "🏠 Início":
    st.header("Bem-vindo ao Sistema Bancário! 👋")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### 💰 Depósitos\nRealize depósitos de forma rápida e segura")
    with col2:
        st.warning("### 💸 Saques\nSaque seu dinheiro quando precisar")
    with col3:
        st.success("### 📊 Extratos\nAcompanhe todas as movimentações")
    
    st.markdown("---")
    st.markdown("""
    ### 🚀 Como começar:
    1. **Cadastre um usuário** em "Novo Usuário"
    2. **Crie uma conta** em "Nova Conta"
    3. **Selecione a conta** em "Listar Contas"
    4. **Comece a usar!** Deposite, saque e consulte seu extrato
    """)

# Tela: Depositar
elif menu == "💰 Depositar":
    st.header("💰 Realizar Depósito")
    
    if not st.session_state.conta_selecionada:
        st.warning("⚠️ Selecione uma conta em 'Listar Contas' primeiro!")
    else:
        valor = st.number_input(
            "Valor do depósito (R$):",
            min_value=0.01,
            format="%.2f",
            step=10.0
        )
        
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("✅ Confirmar Depósito", type="primary", use_container_width=True):
                sucesso, mensagem = st.session_state.conta_selecionada.depositar(valor)
                if sucesso:
                    st.success(mensagem)
                    st.balloons()
                else:
                    st.error(mensagem)

# Tela: Sacar
elif menu == "💸 Sacar":
    st.header("💸 Realizar Saque")
    
    if not st.session_state.conta_selecionada:
        st.warning("⚠️ Selecione uma conta em 'Listar Contas' primeiro!")
    else:
        conta = st.session_state.conta_selecionada
        
        st.info(f"💡 Limite por saque: R$ {conta.LIMITE_SAQUE:.2f} | Limite diário: {conta.LIMITE_SAQUES_DIA} saques")
        
        valor = st.number_input(
            "Valor do saque (R$):",
            min_value=0.01,
            max_value=float(conta.consultar_saldo()),
            format="%.2f",
            step=10.0
        )
        
        if st.button("✅ Confirmar Saque", type="primary", use_container_width=True):
            sucesso, mensagem = conta.sacar(valor)
            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)

# Tela: Ver Extrato
elif menu == "📊 Ver Extrato":
    st.header("📊 Extrato Bancário")
    
    if not st.session_state.conta_selecionada:
        st.warning("⚠️ Selecione uma conta em 'Listar Contas' primeiro!")
    else:
        conta = st.session_state.conta_selecionada
        extrato = conta.ver_extrato()
        
        # Informações da conta
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("👤 Titular", conta.usuario.nome)
        with col2:
            st.metric("🏦 Agência", conta.agencia)
        with col3:
            st.metric("💳 Conta", conta.numero_conta)
        
        st.markdown("---")
        
        # Extrato
        if not extrato:
            st.info("📭 Nenhuma movimentação realizada ainda.")
        else:
            st.subheader("📜 Histórico de Transações")
            for item in reversed(extrato):  # Mais recente primeiro
                tipo_emoji = "📥" if item['tipo'] == 'Depósito' else "📤"
                cor = "green" if item['tipo'] == 'Depósito' else "red"
                sinal = "+" if item['tipo'] == 'Depósito' else "-"
                
                with st.container():
                    col1, col2, col3 = st.columns([2, 2, 1])
                    with col1:
                        st.write(f"{tipo_emoji} **{item['tipo']}**")
                    with col2:
                        st.write(f"🕒 {item['data']}")
                    with col3:
                        st.markdown(f"<p style='color:{cor}; font-weight:bold; font-size:18px;'>{sinal} R$ {item['valor']:.2f}</p>", 
                                  unsafe_allow_html=True)
                    st.markdown("---")
        
        # Saldo final
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 15px; text-align: center;'>
            <h2 style='color: white; margin: 0;'>💰 Saldo Atual: R$ {conta.consultar_saldo():.2f}</h2>
        </div>
        """, unsafe_allow_html=True)

# Tela: Novo Usuário
elif menu == "👤 Novo Usuário":
    st.header("👤 Cadastrar Novo Usuário")
    
    with st.form("form_usuario"):
        nome = st.text_input("Nome Completo*")
        cpf = st.text_input("CPF (apenas números)*")
        data_nascimento = st.text_input("Data de Nascimento (DD/MM/AAAA)*")
        endereco = st.text_area("Endereço Completo*")
        
        submitted = st.form_submit_button("✅ Cadastrar Usuário", use_container_width=True, type="primary")
        
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
    st.header("🏦 Criar Nova Conta Bancária")
    
    if len(sistema.listar_usuarios()) == 0:
        st.warning("⚠️ Cadastre um usuário primeiro em 'Novo Usuário'!")
    else:
        cpf = st.text_input("CPF do Titular*")
        
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

# Tela: Listar Contas
elif menu == "📋 Listar Contas":
    st.header("📋 Contas Cadastradas")
    
    contas = sistema.listar_contas()
    
    if not contas:
        st.info("📭 Nenhuma conta cadastrada ainda. Crie uma em 'Nova Conta'!")
    else:
        for conta in contas:
            with st.container():
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    st.markdown(f"""
                    **👤 {conta.usuario.nome}**  
                    🏦 Agência: {conta.agencia} | 💳 C/C: {conta.numero_conta}  
                    📄 CPF: {conta.usuario.cpf}  
                    💰 **Saldo: R$ {conta.consultar_saldo():.2f}**
                    """)
                
                with col2:
                    if st.button("Selecionar", key=f"btn_{conta.numero_conta}", use_container_width=True):
                        st.session_state.conta_selecionada = conta
                        st.success(f"Conta {conta.numero_conta} selecionada!")
                        st.rerun()
                
                st.markdown("---")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    💡 Sistema Bancário desenvolvido com Python e Streamlit<br>
    🚀 Projeto para Portfólio
</div>
""", unsafe_allow_html=True)