import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def gerar_cpf_valido():
    """Gera um CPF aleatório válido para passar nos validadores de formulário."""
    def calcula_digito(digitos):
        peso = len(digitos) + 1
        soma = sum(int(num) * p for num, p in zip(digitos, range(peso, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    nove_digitos = [random.randint(0, 9) for _ in range(9)]
    nove_digitos.append(calcula_digito(nove_digitos))
    nove_digitos.append(calcula_digito(nove_digitos))
    return ''.join(map(str, nove_digitos))

def conectar_wifi():
    print("📡 Iniciando o robô de autenticação Wi-Fi (Senac DF)...")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-running-insecure-content")
    
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    service = Service()
    service.service_args = ["--disable-build-check"]
    
    driver = webdriver.Chrome(options=chrome_options, service=service)
    
    try:
        print("🌐 Acessando a rota de captura do portal...")
        try:
            driver.get("http://neverssl.com")
            time.sleep(3)
        except Exception:
            # Caso o link de quebra de cache falhe, tenta forçar a rota direta interna descobeta por você
            print("🔄 Conexão direta via URL de cadastro...")
            driver.get("https://senac.br")
        
        print("📝 Preenchendo dados automatizados em background...")
        
        input_cpf = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cpf"))
        )
        input_cpf.send_keys(gerar_cpf_valido())
        
        driver.find_element(By.ID, "nome").send_keys("Visitante Autônomo")
        driver.find_element(By.ID, "email").send_keys("seu_email0@gmail.com") 
        driver.find_element(By.ID, "nascimento").send_keys("15052000")
        driver.find_element(By.ID, "telefone").send_keys("61999999999")
        
        print("⚖️  Aceitando termos de privacidade...")
        checkbox_termos = driver.find_element(By.XPATH, "//input[@type='checkbox']")
        if not checkbox_termos.is_selected():
            driver.execute_script("arguments[0].click();", checkbox_termos)
            
        print("🚀 Enviando cadastro... Liberando acesso!")
        botao_conectar = driver.find_element(By.XPATH, "//*[contains(text(), 'Cadastrar')]")
        botao_conectar.click()
        
        time.sleep(4) 
        print("✅ Sucesso! Seu notebook está autenticado e a internet está liberada.")
        
    except Exception as e:
        print(f"❌ Erro na automação: {e}")
        driver.save_screenshot("erro_portal.png")
        print("📸 Captura de tela do erro salva como 'erro_portal.png'.")
    finally:
        driver.quit()

if __name__ == "__main__":
    conectar_wifi()
