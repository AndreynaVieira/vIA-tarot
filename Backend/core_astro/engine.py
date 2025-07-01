from flatlib import const 
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart

class AstroEngine:
    TRADUCAO_SIGNOS = {
        "Aries": "Áries",
        "Taurus": "Touro",
        "Gemini": "Gêmeos",
        "Cancer": "Câncer",
        "Leo": "Leão",
        "Virgo": "Virgem",
        "Libra": "Libra",
        "Scorpio": "Escorpião",
        "Sagittarius": "Sagitário",
        "Capricorn": "Capricórnio",
        "Aquarius": "Aquário",
        "Pisces": "Peixes"
    }
    
    def __init__(self, ano, mes, dia, hora_nasc, lat, lon, fuso_horario):
        """Inicializa o motor com os dados de nascimento usando a biblioteca FLATLIB."""
        
        data_formatada = f"{ano}/{mes}/{dia}"
        
        fuso_str = f"{int(fuso_horario):+03d}:00"
        self.date = Datetime(data_formatada, hora_nasc, fuso_str)
        self.pos = GeoPos(lat, lon)
        self.chart = Chart(self.date, self.pos)

    def _get_signo(self, obj_planeta):
        signo_em_ingles = obj_planeta.sign
        return self.TRADUCAO_SIGNOS.get(signo_em_ingles, signo_em_ingles)

    def _calcular_planeta(self, obj_id, nome_objeto):
        """Função genérica para planetas, usando o método correto para casas."""
        obj = self.chart.get(obj_id)
        
        casa_obj = self.chart.houses.getObjectHouse(obj)
        return {
            "planeta": nome_objeto,
            "signo": self._get_signo(obj),
            "casa": casa_obj.id
        }

    def calcular_ascendente(self):
        """O Ascendente é um caso especial, ele define a Casa 1."""
        asc_obj = self.chart.get(const.ASC)
        return {
            "planeta": "Ascendente",
            "signo": self._get_signo(asc_obj),
            "casa": 1  
        }

    def calcular_sol(self): return self._calcular_planeta(const.SUN, "Sol")
    def calcular_lua(self): return self._calcular_planeta(const.MOON, "Lua")
    def calcular_mercurio(self): return self._calcular_planeta(const.MERCURY, "Mercúrio")
    def calcular_venus(self): return self._calcular_planeta(const.VENUS, "Vênus")
    def calcular_marte(self): return self._calcular_planeta(const.MARS, "Marte")
    def calcular_jupiter(self): return self._calcular_planeta(const.JUPITER, "Júpiter")
    def calcular_saturno(self): return self._calcular_planeta(const.SATURN, "Saturno")
    
    def gerar_mapa_completo(self):
        """Gera um dicionário com todos os principais dados do mapa."""
        mapa = {
            "sol": self.calcular_sol(),
            "ascendente": self.calcular_ascendente(),
            "lua": self.calcular_lua(),
            "mercurio": self.calcular_mercurio(),
            "venus": self.calcular_venus(),
            "marte": self.calcular_marte(),
            "jupiter": self.calcular_jupiter(),
            "saturno": self.calcular_saturno(),
        }
        return mapa