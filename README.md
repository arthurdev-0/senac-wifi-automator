# 📡 Senac Wi-Fi Automator (Background Login)

[![Python Version](https://shields.io)](https://python.org)
[![Selenium](https://shields.io)](https://selenium.dev)
[![Platform](https://shields.io)](https://microsoft.com)

Um script de automação leve e invisível construído em Python com **Selenium** para realizar o login automático na rede cativa de Wi-Fi corporativa `Senac VISITANTES` (Senac DF).

## 💡 A Dor Resolvida
Telas de login de Wi-Fi públicos (*captive portals*) que não salvam dados e expiram a sessão constantemente quebram o fluxo de trabalho e estudos. Este script elimina a necessidade de abrir o navegador, preencher cadastros repetitivos ou inventar dados falsos manualmente a cada conexão. O robô faz tudo isso em **background** em menos de 3 segundos.

---

## 🛠️ Como o Script Funciona

1. **Acesso Direto**: O script ignora os redirecionamentos lentos e acessa diretamente a URL interna de autenticação (`https://senac.br`).
2. **Dados Inteligentes (Massa de Teste)**: Utiliza um algoritmo interno para gerar um **CPF válido aleatório** em tempo real, contornando travas de segurança e máscaras de validação do portal, mantendo a privacidade do desenvolvedor.
3. **Execução Headless**: O Google Chrome é inicializado em modo oculto (`--headless`). Nenhuma janela é aberta e o consumo de memória é mínimo.
4. **Resiliência a Erros**: Caso o portal mude de interface, o script tira uma captura de tela automática (`erro_portal.png`) para fins de debug.

---

## 🚀 Como Configurar no seu Notebook

### 1. Clonar e Instalar Dependências
Dentro de uma pasta segura no seu Windows, execute:
```bash
git clone https://github.com
cd senac-wifi-automator
pip install selenium
```

### 2. Configurar seu E-mail
Abra o arquivo `wifi_senac_df.py` e mude o campo de e-mail para o de sua preferência:
```python
driver.find_element(By.ID, "email").send_keys("seu_email_real@gmail.com")
```

---

## 🔄 Como Automatizar 100% no Windows (Modo Invisível)

Para fazer o script rodar sozinho **sempre que você se conectar ao Wi-Fi**, usaremos o Agendador de Tarefas do Windows atrelado aos logs de eventos de rede:

1. Pressione `Win + R`, digite **`taskschd.msc`** e dê Enter.
2. No menu direito, clique em **Criar Tarefa Básica...**
3. Dê o nome de `Autologin Senac` e avance.
4. Em **Disparador**, escolha a opção **Quando um evento específico for registrado** e avance.
5. Configure o evento exatamente assim:
   * **Log:** `Microsoft-Windows-NetworkProfile/Operational`
   * **Origem:** `NetworkProfile`
   * **ID do Evento:** `10000` *(Este ID significa: Conectado com sucesso a uma rede)*
6. Na ação, escolha **Iniciar um programa**.
7. No campo **Programa/script**, digite: `pythonw` *(O 'w' final garante que o Python rode sem abrir a tela preta do terminal)*.
8. No campo **Adicione argumentos**, coloque o caminho completo do seu arquivo, exemplo:
   `C:\Users\arthu\Documents\Projetos\wifi-autologin-senac\wifi_senac_df.py`
9. Avance e clique em **Concluir**.

Pronto! Agora, o Windows vai vigiar a sua placa de rede. Sempre que você conectar no Wi-Fi de visitantes, o robô acorda em background, injeta o CPF gerado e te dá internet de forma totalmente invisível.

---

## ⚡ Tecnologias Dominadas neste Projeto
* **Automação de Sistemas:** Web Scraping Avançado / Selenium WebDriver
* **Segurança de Dados:** Algoritmos de validação matemática (Cálculo de dígitos verificadores de CPF)
* **Engenharia de Infraestrutura:** Windows Event Triggering / Automação de Sistemas Operacionais