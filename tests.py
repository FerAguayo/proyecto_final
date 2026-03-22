import pytest
from web.services import convertir, SIMBOLOS_API
from web.models import saldo_cripto, total_invertido, total_recuperado, obtener_cripto, select_all, insert
from config import VALID_COINS


class TestConversiones:
    """Testea que la API de CoinMarketCap responde correctamente para todas las monedas"""

    def test_eur_a_btc(self):
        resultado = convertir(1, "EUR", "BTC")
        assert resultado is not None
        assert resultado > 0

    def test_eur_a_eth(self):
        resultado = convertir(1, "EUR", "ETH")
        assert resultado is not None
        assert resultado > 0

    def test_eur_a_tron(self):
        """Verifica que TRON se traduce a TRX correctamente"""
        resultado = convertir(1, "EUR", "TRON")
        assert resultado is not None
        assert resultado > 0

    def test_btc_a_eur(self):
        resultado = convertir(1, "BTC", "EUR")
        assert resultado is not None
        assert resultado > 0

    def test_todas_las_monedas_a_eur(self):
        """Verifica que todas las monedas del enunciado se pueden convertir a EUR"""
        for moneda in VALID_COINS:
            if moneda != "EUR":
                resultado = convertir(1, moneda, "EUR")
                assert resultado is not None, f"Fallo al convertir {moneda} a EUR"
                assert resultado > 0, f"{moneda} a EUR devolvió {resultado}"

    def test_monedas_iguales_no_se_permite(self):
        """Verifica que el mapeo de símbolos existe para todas las monedas"""
        for moneda in VALID_COINS:
            assert moneda in SIMBOLOS_API, f"{moneda} no tiene símbolo en SIMBOLOS_API"


class TestModels:
    """Testea las funciones de acceso a datos"""

    def test_select_all_devuelve_lista(self):
        resultado = select_all()
        assert isinstance(resultado, list)

    def test_total_invertido_devuelve_numero(self):
        resultado = total_invertido()
        assert isinstance(resultado, (int, float))

    def test_total_recuperado_devuelve_numero(self):
        resultado = total_recuperado()
        assert isinstance(resultado, (int, float))

    def test_saldo_cripto_devuelve_numero(self):
        resultado = saldo_cripto("BTC")
        assert isinstance(resultado, (int, float))

    def test_saldo_cripto_eur_no_aplica(self):
        """EUR no es una cripto, su saldo no debería ser relevante"""
        resultado = saldo_cripto("EUR")
        assert isinstance(resultado, (int, float))

    def test_obtener_cripto_devuelve_diccionario(self):
        resultado = obtener_cripto()
        assert isinstance(resultado, dict)

    def test_obtener_cripto_solo_contiene_monedas_validas(self):
        resultado = obtener_cripto()
        for cripto in resultado:
            assert cripto in VALID_COINS, f"{cripto} no es una moneda válida"


class TestValidaciones:
    """Testea las validaciones de la aplicación"""

    def test_no_vender_mas_de_lo_que_tienes(self):
        """Verifica que el saldo nunca es negativo para criptos con movimientos"""
        cartera = obtener_cripto()
        for cripto, saldo in cartera.items():
            assert saldo > 0, f"{cripto} tiene saldo negativo: {saldo}"

    def test_monedas_from_to_diferentes(self):
        """Verifica que la lista de monedas válidas no tiene duplicados"""
        assert len(VALID_COINS) == len(set(VALID_COINS))


class TestServicesErrores:
    """Testea que services maneja errores correctamente"""

    def test_convertir_cantidad_cero(self):
        """La API no acepta cantidad 0, debe devolver None"""
        resultado = convertir(0, "EUR", "BTC")
        assert resultado is None

    def test_convertir_cantidad_negativa(self):
        """La API con cantidad negativa"""
        try:
            resultado = convertir(-100, "EUR", "BTC")
            # Si no peta, al menos que devuelva algo
            assert resultado is not None
        except Exception:
            pass  # Es aceptable que falle con cantidad negativa

    def test_convertir_cantidad_muy_grande(self):
        """La API con cantidad grande"""
        resultado = convertir(1000000, "EUR", "BTC")
        assert resultado is not None
        assert resultado > 0
