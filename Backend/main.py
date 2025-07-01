# main.py
from core_astro.engine import AstroEngine
from core_ai.generator import gerar_analise_ia
from utils.converters import get_coords_from_city
import config

def main():
    """Função principal que executa a aplicação."""
    print("--- Bem-vinda ao seu Hub Astrológico com IA ---")
    
    data_nasc = input("Digite sua data de nascimento (AAAA/MM/DD):\n ")
    hora_nasc = input("Digite sua hora de nascimento (HH:MM):\n ")
    cidade_nasc = input("Digite a cidade em que você nasceu (cidade, UF):\n ")
    fuso = input("Digite o fuso horário do local (ex: -3 para São Paulo, 0 para Londres):\n ")
    
    coords = get_coords_from_city(cidade_nasc)
    
    if not coords:
        print("\nNão foi possível continuar sem as coordenadas do local de nascimento.")
        return
        
    lat, lon = coords
    
    try:
        motor_astrologico = AstroEngine(data_nasc, hora_nasc, lat, lon, fuso)
        mapa_completo = motor_astrologico.gerar_mapa_completo()
        
        print("Gerando sua análise com IA...")
        
        analise_texto = gerar_analise_ia(mapa_completo)
        
        print("-" * 40)
        print(analise_texto)
        print("-" * 40)
    
    except Exception as e:
        print(f"\nOcorreu um erro no cálculo. Verifique os dados. Detalhe: {e}")
        
if __name__ == "__main__":
    main()