"""
IMPORTANT NOTE TO ADD TO ALL TEST FILES WITH ADDRESSES/TRANSACTIONS

DO NOT use personal addresses/transactions for tests.  Instead, choose relatively random
addresses/transactions.  For example, choose recent transactions from mintscan explorer for a
validator or contract.  This is to ensure good faith in maintaining privacy.

"""
import logging
import unittest
from unittest.mock import patch

from tests.mock_lcd import MockLcdAPI_v1, MockLcdAPI_v2
from tests.mock_mintscan import MockMintscanAPI
import staketaxcsv
import staketaxcsv.settings_csv as co
from tests.mock_osmo import mock_get_symbol, mock_get_exponent


@patch("staketaxcsv.common.ibc.denoms.LcdAPI_v1", new=MockLcdAPI_v1)
@patch("staketaxcsv.common.ibc.api_lcd_v1.LcdAPI_v1", new=MockLcdAPI_v1)
@patch("staketaxcsv.common.ibc.api_lcd_v2.LcdAPI_v2", new=MockLcdAPI_v2)
@patch("staketaxcsv.common.ibc.api_mintscan_v1.MintscanAPI", new=MockMintscanAPI)
@patch("staketaxcsv.settings_csv.DB_CACHE", False)
@patch("staketaxcsv.osmo.denoms._symbol", mock_get_symbol)
@patch("staketaxcsv.osmo.denoms._exponent", mock_get_exponent)
def run_test(ticker, wallet_address, start_date, end_date):
    return staketaxcsv.historical_balances(
        ticker,
        wallet_address,
        path=None,
        options={"start_date": start_date, "end_date": end_date},
        logs="test"
    )


class TestBalHistoryMintscan(unittest.TestCase):

    def test_arch_balhistory(self):
        result = run_test(co.TICKER_ARCH, "archway1rv52shjza8lv7pv4avr24nqpqmq4z90yhywwrc", "2023-12-10", "2024-01-20")
        correct_result = """
-------------------  ------------------  ----
timestamp            ARCH                ATOM
2024-01-12 00:43:52  151.23277649512175  0.01
2024-01-10 18:35:55  151.44536274882475  0.01
2023-12-24 22:15:24  150.66872906168328  0.01
2023-12-18 18:19:26  150.37992819835836  0.01
2023-12-11 11:47:26  150.08812354586183  0.01
-------------------  ------------------  ----
        """
        self.assertEqual(result, correct_result.strip(), result)

    def test_akt_balhistory(self):
        result = run_test(co.TICKER_AKT, "akash10vx09tg27lg4dtkv4r09s2glz3mme62u4wzxrz", "2024-01-18", "2024-01-20")
        correct_result = """
-------------------  ------------------
timestamp            AKT
2024-01-20 23:53:14  2145.7468305304283
2024-01-18 16:56:42  2144.166230264817
-------------------  ------------------
        """
        self.assertEqual(result, correct_result.strip(), result)

    def test_atom_balhistory(self):
        result = run_test(co.TICKER_ATOM, "cosmos1ma02nlc7lchu7caufyrrqt4r6v2mpsj92s3mw7", "2023-11-27", "2024-01-17")
        correct_result = """
-------------------  -----------------  -----------  ------------------  ------------------  -------  ------------------  -----------------  ------------------  -----------------  -------------------  -----------------  ------------------  ------------------  ------------------  ------------------  -----------------
timestamp            ATOM               BTSG         NTRN                STRD                UMEE     USDC                stATOM             stCMDX              stEVMOS            stINJ                stJUNO             stLUNA              stOSMO              stSOMM              stSTARS             stUMEE
2024-01-16 08:04:45  645587.5604237274  1382.791038  37.29834            131.800189          1.7e-05  7.697574            9.870068           16.950794           74.43844923827035  0.47640626177690193  8.763815           1.049824            26.099742           1.272302            105.052738          92.835653
2024-01-15 02:10:27  645256.8842767094  1382.791038  37.09327494009525   131.11389868366896  1.7e-05  7.50699591472509    9.81701033873099   16.898084275800414  74.24495457818173  0.4006398617881348   8.721080310968784  1.0143139645468093  25.719000999553845  1.260339505043984   104.57815233764288  92.43150236429139
2024-01-07 01:29:23  643104.3713835382  1382.791038  29.116451374442963  126.30640748694893  1.7e-05  5.883956814917527   9.412456104895998  16.40314815256433   72.50213309641471  0.3956149651697037   8.391734210100582  0.9900733946744065  24.00861711565929   1.1663956867021     100.87117321644175  89.41751654731141
2023-12-29 08:19:06  640759.0063969037  1382.791038  20.711487318260335  121.15829188293705  1.7e-05  3.0076143131418034  9.029566373657172  15.824059330512615  70.07781492448792  0.3907953917873278   8.090281304027645  0.970064440543445   22.29827111741325   1.0799312504198264  96.9185793751954    86.75687791089992
2023-12-19 05:31:27  638024.8807858278  1382.791038  12.825914512397263  114.88421458574571  1.7e-05                      8.588467491978314  15.163544452316856  66.7537016455758   0.38556581418111946  7.745272136836037  0.9483520726419106  20.17911254954916   0.9796286520294986  91.3613085020682    83.84183748870413
2023-11-29 00:35:26  634636.4170006958  1382.791038  9.242006915723106   106.80159873858581  1.7e-05                      7.873015331795951  13.890148788837195  59.48950727332251  0.3678271786795163   7.084151293303326  0.9123391613325417  16.115498500361205  0.8150632133821581  82.25130160865952   76.10753088361868
-------------------  -----------------  -----------  ------------------  ------------------  -------  ------------------  -----------------  ------------------  -----------------  -------------------  -----------------  ------------------  ------------------  ------------------  ------------------  -----------------
        """
        self.assertEqual(result, correct_result.strip(), result)

    def test_evmos_balhistory(self):
        result = run_test(co.TICKER_EVMOS, "evmos15jtys3wy27lcvmjzewxr636uke6t0lk9qj7c6p", "2023-09-18", "2023-09-19")
        correct_result = """
-------------------  ------------------
timestamp            EVMOS
2023-09-18 14:13:19  2326191.1317405747
2023-09-18 13:54:18  1958119.1238164378
2023-09-18 13:53:38  1832507.3035661578
2023-09-18 13:53:05  945580.1320218776
2023-09-18 13:52:21  880226.8710715958
2023-09-18 13:50:03  465299.2387272407
-------------------  ------------------
        """
        self.assertEqual(result, correct_result.strip(), result)

    def test_juno_balhistory(self):
        result = run_test(co.TICKER_JUNO, "juno1enu0aefq33q8re7vawpsrla43du4zgp5x533zs", "2024-01-14", "2024-01-21")
        correct_result = """
-------------------  --------  ------------
timestamp            ATOM      JUNO
2024-01-21 07:24:20  0.000533  0.705386
2024-01-21 07:23:52  0.000533  0.705386
2024-01-20 16:57:37  0.000533  13990.713462
2024-01-14 16:49:44  0.000533  13990.713462
2024-01-14 16:49:32  0.000533  13990.713462
-------------------  --------  ------------
        """
        self.assertEqual(result, correct_result.strip(), result)

    def test_osmo_balhistory(self):
        result = run_test(co.TICKER_OSMO, "osmo1af5tyfjgrjycv5zu3asnh4u3hruqu8xknqk7fl", "2024-01-01", "2024-01-20")
        correct_result = """
 -------------------  ------------------  --------  -----------------------------------------------------------------
timestamp            OSMO                SCRT      unknown_factory/osmo1pfyxruwvtwk00y8z06dh2lqjdj82ldvy74wzm3/WOSMO
2024-01-20 19:44:22  2128545.4282873776  1.061529  2000000.0
2024-01-20 19:18:22  2128544.4486946524  1.061529
2024-01-09 09:33:38  2120884.823966269   1.061529
-------------------  ------------------  --------  -----------------------------------------------------------------
        """
        self.assertEqual(result, correct_result.strip(), result)

    def test_strd_balhistory(self):
        logging.basicConfig(level=logging.INFO)

        result = run_test(co.TICKER_STRD, "stride1sjl5mhsxhxyxe3ael6qawu7m2qkaahdu4ymv47", "2024-01-01", "2024-01-20")
        correct_result = """
-------------------  --------  ------------------  --------  --------  -----------------  --------------------  -------  --------  --------  --------  --------  -------
timestamp            OSMO      STRD                stATOM    stCMDX    stEVMOS            stINJ                 stJUNO   stLUNA    stOSMO    stSOMM    stSTARS   stUMEE
2024-01-20 06:24:00  0.000126  20760.029817        0.558149  0.998682  5.365600965291225  0.007355770766691136  0.46622  0.030243  2.935948  0.137119  7.640569  4.91202
2024-01-17 06:23:50  0.000126  20760.029817        0.558149  0.998682  5.365600965291225  0.007355770766691136  0.46622  0.030243  2.935948  0.137119  7.640569  4.91202
2024-01-14 06:23:35  0.000126  20760.029817        0.558149  0.998682  5.365600965291225  0.007355770766691136  0.46622  0.030243  2.935948  0.137119  7.640569  4.91202
2024-01-11 06:23:01  0.000126  20760.029817        0.558149  0.998682  5.365600965291225  0.007355770766691136  0.46622  0.030243  2.935948  0.137119  7.640569  4.91202
2024-01-08 06:22:37  0.000126  20760.029817        0.558149  0.998682  5.365600965291225  0.007355770766691136  0.46622  0.030243  2.935948  0.137119  7.640569  4.91202
2024-01-05 06:22:11  0.000126  20760.029817        0.558149  0.998682  5.365600965291225  0.007355770766691136  0.46622  0.030243  2.935948  0.137119  7.640569  4.91202
2024-01-02 06:21:22  0.000126  20760.029817000002  0.558149  0.998682  5.365600965291225  0.007355770766691136  0.46622  0.030243  2.935948  0.137119  7.640569  4.91202
-------------------  --------  ------------------  --------  --------  -----------------  --------------------  -------  --------  --------  --------  --------  -------
        """
        self.assertEqual(result, correct_result.strip(), result)

    def test_tia_balhistory(self):
        logging.basicConfig(level=logging.INFO)

        result = run_test(co.TICKER_TIA, "celestia1jass7yq2juz2rsyf56lte3h2e4vyvwt5gztjts", "2023-11-01", "2023-12-01")
        correct_result = """
-------------------  -----------------
timestamp            TIA
2023-11-06 13:17:12  2415238.881058599
2023-11-03 18:00:11  2415060.970515274
2023-11-03 17:41:52  2380952.380001
-------------------  -----------------
        """
        self.assertEqual(result, correct_result.strip(), result)
