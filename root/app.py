# Example 1
import telegram
import time
import requests
from bs4 import BeautifulSoup
from candlestick import candlestick
import pandas as pd
import threading

from binance.client import Client

client = Client(api_key='Enter Your Binance api_key here',
                api_secret='Enter Your Binance api_secret here')

bot = telegram.Bot(token="Enter Your Telegram token here")

lst = [('BTCUSDT', 'BTC_USDT'), ('ETHUSDT', 'ETH_USDT'), ('TRXUSDT', 'TRX_USDT'), ('BCHUSDT', 'BCH_USDT'),
       ('ETCUSDT', 'ETC_USDT'), ('EOSUSDT', 'EOS_USDT'), ('ETHBTC', 'ETH_BTC'), ('BNBUSDT', 'BNB_USDT'),
       ('TOMOBTC', 'TOMO_BTC'), ('BTCUSDC', 'BTC_USDC'), ('LTCUSDT', 'LTC_USDT'), ('XRPUSDT', 'XRP_USDT'),
       ('TROYUSDT', 'TROY_USDT'), ('BNBBTC', 'BNB_BTC'), ('ATOMUSDT', 'ATOM_USDT'), ('MATICBTC', 'MATIC_BTC'),
       ('LINKUSDT', 'LINK_USDT'), ('BCHBTC', 'BCH_BTC'), ('ADAUSDT', 'ADA_USDT'), ('MATICUSDT', 'MATIC_USDT'),
       ('WINUSDT', 'WIN_USDT'), ('LINKBTC', 'LINK_BTC'), ('USDCUSDT', 'USDC_USDT'), ('XRPBTC', 'XRP_BTC'),
       ('VETUSDT', 'VET_USDT'), ('ETCBTC', 'ETC_BTC'), ('ATOMBTC', 'ATOM_BTC'), ('WAVESBTC', 'WAVES_BTC'),
       ('XMRBTC', 'XMR_BTC'), ('ADABTC', 'ADA_BTC'), ('BTTUSDT', 'BTT_USDT'), ('TOMOUSDT', 'TOMO_USDT'),
       ('VETBTC', 'VET_BTC'), ('BTCTUSD', 'BTC_TUSD'), ('EOSBTC', 'EOS_BTC'), ('LTCBTC', 'LTC_BTC'),
       ('TUSDUSDT', 'TUSD_USDT'), ('BTCBUSD', 'BTC_BUSD'), ('BTCPAX', 'BTC_PAX'), ('XMRUSDT', 'XMR_USDT'),
       ('NEOUSDT', 'NEO_USDT'), ('PAXUSDT', 'PAX_USDT'), ('BUSDUSDT', 'BUSD_USDT'), ('WAVESUSDT', 'WAVES_USDT'),
       ('XTZBTC', 'XTZ_BTC'), ('XTZUSDT', 'XTZ_USDT'),
       ('MANABTC', 'MANA_BTC'), ('DASHUSDT', 'DASH_USDT'), ('ONTUSDT', 'ONT_USDT'), ('TRXBTC', 'TRX_BTC'),
       ('TROYBTC', 'TROY_BTC'), ('IOSTUSDT', 'IOST_USDT'), ('ETHUSDC', 'ETH_USDC'), ('KAVABTC', 'KAVA_BTC'),
       ('DASHBTC', 'DASH_BTC'), ('XLMUSDT', 'XLM_USDT'), ('KAVAUSDT', 'KAVA_USDT'), ('VITEBTC', 'VITE_BTC'),
       ('QTUMUSDT', 'QTUM_USDT'), ('FETBTC', 'FET_BTC'), ('AIONBTC', 'AION_BTC'), ('NULSBTC', 'NULS_BTC'),
       ('RVNBTC', 'RVN_BTC'), ('IOTABTC', 'IOTA_BTC'), ('IOTAUSDT', 'IOTA_USDT'), ('DUSKBTC', 'DUSK_BTC'),
       ('ALGOBTC', 'ALGO_BTC'), ('ALGOUSDT', 'ALGO_USDT'), ('ENJBTC', 'ENJ_BTC'), ('FETUSDT', 'FET_USDT'),
       ('LOOMBTC', 'LOOM_BTC'), ('CDTBTC', 'CDT_BTC'), ('BNBETH', 'BNB_ETH'), ('ZECUSDT', 'ZEC_USDT'),
       ('BATBTC', 'BAT_BTC'), ('FTMBTC', 'FTM_BTC'), ('LINKETH', 'LINK_ETH'), ('XRPETH', 'XRP_ETH'),
       ('NEOBTC', 'NEO_BTC'), ('DOCKBTC', 'DOCK_BTC'), ('NULSUSDT', 'NULS_USDT'), ('PIVXBTC', 'PIVX_BTC'),
       ('MTLBTC', 'MTL_BTC'), ('HBARBTC', 'HBAR_BTC'), ('CHZBTC', 'CHZ_BTC'), ('TRXETH', 'TRX_ETH'),
       ('ZECBTC', 'ZEC_BTC'), ('BATUSDT', 'BAT_USDT'), ('XLMBTC', 'XLM_BTC'), ('TROYBNB', 'TROY_BNB'),
       ('ARPABTC', 'ARPA_BTC'), ('FTTUSDT', 'FTT_USDT'), ('ICXBTC', 'ICX_BTC'),
       ('BRDBTC', 'BRD_BTC'), ('KAVABNB', 'KAVA_BNB'), ('DLTBTC', 'DLT_BTC'), ('CMTBTC', 'CMT_BTC'),
       ('QTUMBTC', 'QTUM_BTC'), ('THETABTC', 'THETA_BTC'), ('DUSKUSDT', 'DUSK_USDT'), ('RVNUSDT', 'RVN_USDT'),
       ('ARNBTC', 'ARN_BTC'), ('ATOMUSDC', 'ATOM_USDC'), ('OAXBTC', 'OAX_BTC'), ('FTTBTC', 'FTT_BTC'),
       ('ARPAUSDT', 'ARPA_USDT'), ('HBARUSDT', 'HBAR_USDT'), ('VIBBTC', 'VIB_BTC'), ('SNGLSBTC', 'SNGLS_BTC'),
       ('STXBTC', 'STX_BTC'), ('BEAMBTC', 'BEAM_BTC'), ('BTTBNB', 'BTT_BNB'), ('WAVESETH', 'WAVES_ETH'),
       ('RENBTC', 'REN_BTC'), ('ETHTUSD', 'ETH_TUSD'), ('ONEBTC', 'ONE_BTC'), ('ERDUSDT', 'ERD_USDT'),
       ('MITHBTC', 'MITH_BTC'), ('ADAETH', 'ADA_ETH'), ('EOSETH', 'EOS_ETH'), ('ENGBTC', 'ENG_BTC'),
       ('DGDBTC', 'DGD_BTC'), ('DATABTC', 'DATA_BTC'), ('ENJUSDT', 'ENJ_USDT'), ('COCOSUSDT', 'COCOS_USDT'),
       ('IOSTBTC', 'IOST_BTC'), ('BEAMUSDT', 'BEAM_USDT'), ('LTCUSDC', 'LTC_USDC'),
       ('AGIBTC', 'AGI_BTC'), ('XVGBTC', 'XVG_BTC'), ('VETETH', 'VET_ETH'), ('WTCBTC', 'WTC_BTC'),
       ('ZRXBTC', 'ZRX_BTC'), ('XRPUSDC', 'XRP_USDC'), ('BTTTRX', 'BTT_TRX'), ('PPTBTC', 'PPT_BTC'),
       ('DOGEBTC', 'DOGE_BTC'), ('LTCETH', 'LTC_ETH'), ('STXUSDT', 'STX_USDT'), ('VITEUSDT', 'VITE_USDT'),
       ('ZILBTC', 'ZIL_BTC'), ('TRXBNB', 'TRX_BNB'), ('POLYBTC', 'POLY_BTC'), ('ONTBTC', 'ONT_BTC'),
       ('GRSBTC', 'GRS_BTC'), ('FTTBNB', 'FTT_BNB'), ('DOGEUSDT', 'DOGE_USDT'), ('PERLBTC', 'PERL_BTC'),
       ('FTMUSDT', 'FTM_USDT'), ('BCHTUSD', 'BCH_TUSD'), ('TOMOBNB', 'TOMO_BNB'), ('XRPBNB', 'XRP_BNB'),
       ('KEYBTC', 'KEY_BTC'), ('TRXUSDC', 'TRX_USDC'), ('XEMBTC', 'XEM_BTC'), ('STRATBTC', 'STRAT_BTC'),
       ('LTCBNB', 'LTC_BNB'), ('BCHUSDC', 'BCH_USDC'), ('ZENBTC', 'ZEN_BTC'), ('TRXBUSD', 'TRX_BUSD'),
       ('INSBTC', 'INS_BTC'), ('ONEUSDT', 'ONE_USDT'), ('ETCETH', 'ETC_ETH'), ('WINBNB', 'WIN_BNB'),
       ('ICXUSDT', 'ICX_USDT'), ('LTCTUSD', 'LTC_TUSD'),
       ('MATICBNB', 'MATIC_BNB'), ('ZRXUSDT', 'ZRX_USDT'), ('ZILUSDT', 'ZIL_USDT'), ('ERDBTC', 'ERD_BTC'),
       ('HOTUSDT', 'HOT_USDT'), ('MTLUSDT', 'MTL_USDT'), ('NKNBTC', 'NKN_BTC'), ('CTXCBTC', 'CTXC_BTC'),
       ('HCBTC', 'HC_BTC'), ('BANDBTC', 'BAND_BTC'), ('AMBBTC', 'AMB_BTC'), ('THETAUSDT', 'THETA_USDT'),
       ('STORMBTC', 'STORM_BTC'), ('BTTUSDC', 'BTT_USDC'), ('QKCBTC', 'QKC_BTC'), ('LSKBTC', 'LSK_BTC'),
       ('RCNBTC', 'RCN_BTC'), ('BNBUSDC', 'BNB_USDC'), ('EOSUSDC', 'EOS_USDC'), ('TRXXRP', 'TRX_XRP'),
       ('BQXBTC', 'BQX_BTC'), ('XMRETH', 'XMR_ETH'), ('STEEMBTC', 'STEEM_BTC'), ('VIABTC', 'VIA_BTC'),
       ('ETHPAX', 'ETH_PAX'), ('TRXTUSD', 'TRX_TUSD'), ('WABIBTC', 'WABI_BTC'), ('WANBTC', 'WAN_BTC'),
       ('LENDBTC', 'LEND_BTC'), ('MCOBTC', 'MCO_BTC'), ('MCOUSDT', 'MCO_USDT'), ('TRXPAX', 'TRX_PAX'),
       ('BTTTUSD', 'BTT_TUSD'), ('ADABNB', 'ADA_BNB'), ('EVXBTC', 'EVX_BTC'), ('BNBTUSD', 'BNB_TUSD'),
       ('OMGBTC', 'OMG_BTC'), ('NANOBTC', 'NANO_BTC'),
       ('BANDUSDT', 'BAND_USDT'), ('NEOETH', 'NEO_ETH'), ('WINTRX', 'WIN_TRX'), ('IOTAETH', 'IOTA_ETH'),
       ('MITHUSDT', 'MITH_USDT'), ('CHZUSDT', 'CHZ_USDT'), ('FUELBTC', 'FUEL_BTC'), ('BTSBTC', 'BTS_BTC'),
       ('CVCBTC', 'CVC_BTC'), ('CMTETH', 'CMT_ETH'), ('EOSBNB', 'EOS_BNB'), ('GOBTC', 'GO_BTC'), ('ELFBTC', 'ELF_BTC'),
       ('MTHBTC', 'MTH_BTC'), ('ALGOTUSD', 'ALGO_TUSD'), ('QSPBTC', 'QSP_BTC'), ('PERLUSDT', 'PERL_USDT'),
       ('LINKUSDC', 'LINK_USDC'), ('RLCBTC', 'RLC_BTC'), ('BTGBTC', 'BTG_BTC'), ('AIONETH', 'AION_ETH'),
       ('MANAETH', 'MANA_ETH'), ('TNTBTC', 'TNT_BTC'), ('BLZBTC', 'BLZ_BTC'), ('LOOMETH', 'LOOM_ETH'),
       ('TFUELBTC', 'TFUEL_BTC'), ('OMGUSDT', 'OMG_USDT'), ('PIVXETH', 'PIVX_ETH'), ('CNDBTC', 'CND_BTC'),
       ('WINUSDC', 'WIN_USDC'),
       ('NPXSUSDT', 'NPXS_USDT'), ('BCDBTC', 'BCD_BTC'), ('FUNBTC', 'FUN_BTC'), ('NAVBTC', 'NAV_BTC'),
       ('DOCKUSDT', 'DOCK_USDT'), ('XZCBTC', 'XZC_BTC'), ('ZILETH', 'ZIL_ETH'), ('DCRBTC', 'DCR_BTC'),
       ('BRDBNB', 'BRD_BNB'), ('NULSETH', 'NULS_ETH'), ('ALGOBNB', 'ALGO_BNB'), ('SNMBTC', 'SNM_BTC'),
       ('KNCBTC', 'KNC_BTC'), ('BNTBTC', 'BNT_BTC'), ('CELRBTC', 'CELR_BTC'), ('WANUSDT', 'WAN_USDT'),
       ('DGDETH', 'DGD_ETH'), ('ETCBNB', 'ETC_BNB'), ('MDABTC', 'MDA_BTC'), ('VETBNB', 'VET_BNB'),
       ('ETHBUSD', 'ETH_BUSD'), ('IOTXBTC', 'IOTX_BTC'), ('ONTETH', 'ONT_ETH'), ('GVTBTC', 'GVT_BTC'),
       ('ATOMBNB', 'ATOM_BNB'), ('ADATUSD', 'ADA_TUSD'), ('RENUSDT', 'REN_USDT'), ('DASHETH', 'DASH_ETH'),
       ('BRDETH', 'BRD_ETH'), ('HCUSDT', 'HC_USDT'), ('EDOBTC', 'EDO_BTC'), ('XRPTUSD', 'XRP_TUSD'),
       ('KEYUSDT', 'KEY_USDT'), ('POEBTC', 'POE_BTC'), ('WPRBTC', 'WPR_BTC'), ('HOTETH', 'HOT_ETH'),
       ('STORJBTC', 'STORJ_BTC'), ('NKNUSDT', 'NKN_USDT'), ('EOSPAX', 'EOS_PAX'), ('BTCRUB', 'BTC_RUB'),
       ('POABTC', 'POA_BTC'), ('PAXTUSD', 'PAX_TUSD'), ('USDCTUSD', 'USDC_TUSD'), ('COSBTC', 'COS_BTC'),
       ('ENJETH', 'ENJ_ETH'),
       ('REPBTC', 'REP_BTC'), ('STXBNB', 'STX_BNB'), ('HOTBTC', 'HOT_BTC'), ('BCHBUSD', 'BCH_BUSD'),
       ('XLMETH', 'XLM_ETH'), ('MTLETH', 'MTL_ETH'), ('KMDBTC', 'KMD_BTC'), ('NASBTC', 'NAS_BTC'),
       ('ZENETH', 'ZEN_ETH'), ('ONTBNB', 'ONT_BNB'), ('ETCBUSD', 'ETC_BUSD'), ('NPXSETH', 'NPXS_ETH'),
       ('CELRUSDT', 'CELR_USDT'), ('RVNBNB', 'RVN_BNB'), ('GNTBTC', 'GNT_BTC'), ('GTOBTC', 'GTO_BTC'),
       ('NANOUSDT', 'NANO_USDT'), ('WAVESBNB', 'WAVES_BNB'), ('AEBTC', 'AE_BTC'), ('ADAUSDC', 'ADA_USDC'),
       ('IOTABNB', 'IOTA_BNB'), ('KNCETH', 'KNC_ETH'), ('LENDETH', 'LEND_ETH'), ('BCHPAX', 'BCH_PAX'),
       ('NULSBNB', 'NULS_BNB'), ('BCHBNB', 'BCH_BNB'), ('ADXBTC', 'ADX_BTC'), ('VIBETH', 'VIB_ETH'),
       ('PHBBTC', 'PHB_BTC'), ('LTCBUSD', 'LTC_BUSD'), ('BCPTBTC', 'BCPT_BTC'), ('DENTETH', 'DENT_ETH'),
       ('CDTETH', 'CDT_ETH'), ('TNBBTC', 'TNB_BTC'), ('XMRBNB', 'XMR_BNB'), ('ANKRUSDT', 'ANKR_USDT'),
       ('VIBEBTC', 'VIBE_BTC'), ('ANKRBTC', 'ANKR_BTC'), ('EVXETH', 'EVX_ETH'), ('ZRXETH', 'ZRX_ETH'),
       ('XRPPAX', 'XRP_PAX'), ('DASHBNB', 'DASH_BNB'), ('DENTUSDT', 'DENT_USDT'),
       ('RLCUSDT', 'RLC_USDT'), ('SNTBTC', 'SNT_BTC'), ('STORMUSDT', 'STORM_USDT'), ('BNBPAX', 'BNB_PAX'),
       ('ARNETH', 'ARN_ETH'), ('BATETH', 'BAT_ETH'), ('OSTBTC', 'OST_BTC'), ('ONGBTC', 'ONG_BTC'),
       ('SKYBTC', 'SKY_BTC'), ('LINKTUSD', 'LINK_TUSD'), ('COSUSDT', 'COS_USDT'), ('LUNBTC', 'LUN_BTC'),
       ('ASTBTC', 'AST_BTC'), ('DATAETH', 'DATA_ETH'), ('LRCBTC', 'LRC_BTC'), ('WAVESUSDC', 'WAVES_USDC'),
       ('ENGETH', 'ENG_ETH'), ('GXSBTC', 'GXS_BTC'), ('CTXCUSDT', 'CTXC_USDT'), ('ICXETH', 'ICX_ETH'),
       ('ADABUSD', 'ADA_BUSD'), ('TFUELUSDT', 'TFUEL_USDT'), ('FUNUSDT', 'FUN_USDT'), ('POWRBTC', 'POWR_BTC'),
       ('VETBUSD', 'VET_BUSD'), ('GASBTC', 'GAS_BTC'), ('BNBBUSD', 'BNB_BUSD'), ('BUSDNGN', 'BUSD_NGN'),
       ('ONGUSDT', 'ONG_USDT'), ('QTUMBNB', 'QTUM_BNB'), ('ZECETH', 'ZEC_ETH'), ('KEYETH', 'KEY_ETH'),
       ('BANDBNB', 'BAND_BNB'), ('REQBTC', 'REQ_BTC'), ('VITEBNB', 'VITE_BNB'), ('EOSBUSD', 'EOS_BUSD'),
       ('CELRBNB', 'CELR_BNB'), ('THETAETH', 'THETA_ETH'), ('OMGETH', 'OMG_ETH'), ('BTTPAX', 'BTT_PAX'),
       ('BATBNB', 'BAT_BNB'), ('PERLBNB', 'PERL_BNB'), ('BCDETH', 'BCD_ETH'), ('ARKBTC', 'ARK_BTC'),
       ('PPTETH', 'PPT_ETH'), ('QTUMETH', 'QTUM_ETH'), ('BTCNGN', 'BTC_NGN'), ('XTZBNB', 'XTZ_BNB'),
       ('AGIETH', 'AGI_ETH'), ('IOSTETH', 'IOST_ETH'), ('MCOETH', 'MCO_ETH'), ('AIONBNB', 'AION_BNB'),
       ('YOYOBTC', 'YOYO_BTC'), ('QLCBTC', 'QLC_BTC'), ('RLCETH', 'RLC_ETH'), ('CVCUSDT', 'CVC_USDT'),
       ('HOTBNB', 'HOT_BNB'), ('XRPBUSD', 'XRP_BUSD'), ('APPCBTC', 'APPC_BTC'), ('GRSETH', 'GRS_ETH'),
       ('ONEBNB', 'ONE_BNB'), ('EOSTUSD', 'EOS_TUSD'), ('ARPABNB', 'ARPA_BNB'), ('RDNBTC', 'RDN_BTC'),
       ('BNTETH', 'BNT_ETH'), ('DUSKBNB', 'DUSK_BNB'), ('WAVESTUSD', 'WAVES_TUSD'), ('XVGETH', 'XVG_ETH'),
       ('DUSKPAX', 'DUSK_PAX'), ('FETBNB', 'FET_BNB'), ('BLZETH', 'BLZ_ETH'), ('DUSKUSDC', 'DUSK_USDC'),
       ('NXSBTC', 'NXS_BTC'), ('NEOBNB', 'NEO_BNB'), ('DNTBTC', 'DNT_BTC'), ('USDSUSDT', 'USDS_USDT'),
       ('FUNETH', 'FUN_ETH'), ('FTMBNB', 'FTM_BNB')]


def func(t):
    '''
    t in minute and int {5:'5m',(15:15),(30:30),(1h:60),(4h:240),(12h:720),(1d:1440)]
    lst not defined inside the function define ir out side

    '''
    D = {5: '5m', 15: '15m', 30: '30m', 60: '1h', 240: '4h', 720: '12h', 1440: '1d'}
    S = {5: '5 MIN', 15: '15 MIN', 30: '30 MIN', 60: '1 HOUR', 240: '4 HOUR', 720: '12 HOUR', 1440: '1 DAY'}
    P = {5: 1, 15: 2.5, 30: 4, 60: 5, 240: 5, 720: 6, 1440: 6}
    lp1 = '1lp_' + D[t]
    lp2 = '2lp_' + D[t]
    p_c = 'p_c_' + D[t]
    pct = P[t]
    T = t * 60

    while True:
        try:
            tickers = client.get_ticker()
            tickers = pd.DataFrame(tickers)
            tickers[lp1] = tickers['lastPrice']

            time.sleep(T)

            tickers2 = client.get_ticker()
            tickers2 = pd.DataFrame(tickers2)

            tickers[lp2] = tickers2['lastPrice']

            tickers[[lp1, lp2]] = tickers[[lp1, lp2]].astype(float)

            tickers[p_c] = tickers[[lp1, lp2]].pct_change(axis='columns')[lp2] * 100

            x = tickers[['symbol', p_c]][tickers[p_c] > pct]
            y = tickers[['symbol', p_c]][tickers[p_c] < -pct]

            postive = x.values.tolist()
            negtive = y.values.tolist()

            s = "<code>👉LAST </code>" + "<b>" + S[
                t] + "</b>" + "<code> PRICE CHANGE👈\n</code>" + "<b>\n% Increase ✅ ✅ ✅ ✅\n</b>"
            for a1, b1 in postive:
                for a2, b2 in lst:
                    if a1 == a2:
                        s1 = "<a href='https://www.binance.com/indexSpa.html#/trade/index?symbol=" + b2 + "'>" + b2 + ":" + "</a>" + "<b>" + " " * (
                                    11 - len(b2)) + "+ " + str(round(b1, 3)) + " %" + "</b>" + '\n'
                        s = s + s1

            s1 = "\n<b>% Decrease 🔻🔻🔻🔻</b>\n"
            s = s + s1

            for a1, b1 in negtive:
                for a2, b2 in lst:
                    if a1 == a2:
                        s1 = "<a href='https://www.binance.com/indexSpa.html#/trade/index?symbol=" + b2 + "'>" + b2 + ":" + "</a>" + "<b>" + " " * (
                                    11 - len(b2)) + "  " + str(round(b1, 3)) + " %" + "</b>" + '\n'
                        s = s + s1

            st = "<code>👉LAST </code>" + "<b>" + S[
                t] + "</b>" + "<code> PRICE CHANGE👈\n</code>" + "<b>\n% Increase ✅ ✅ ✅ ✅\n</b>" + "\n<b>% Decrease 🔻🔻🔻🔻</b>\n"
            if s != st:
                bot.sendMessage(chat_id='@sample11123', text=s, parse_mode='HTML', disable_notification=True)

        except Exception:
            time.sleep(60)


def candalstick_patter_finder(candles_df, symbol, t, b):
    lst_cand = list()
    target = 'InvertedHammers'
    candles_df = candlestick.inverted_hammer(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'DojiStar'
    candles_df = candlestick.doji_star(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'DragonflyDoji'
    candles_df = candlestick.dragonfly_doji(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'HangingMan'
    candles_df = candlestick.hanging_man(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'GravestoneDoji'
    candles_df = candlestick.gravestone_doji(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'BearishEngulfing'
    candles_df = candlestick.bearish_engulfing(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'BullishEngulfing'
    candles_df = candlestick.bullish_engulfing(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'Hammer'
    candles_df = candlestick.hammer(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'MorningStar'
    candles_df = candlestick.morning_star(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'MorningStarDoji'
    candles_df = candlestick.morning_star_doji(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'PiercingPattern'
    candles_df = candlestick.piercing_pattern(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'RainDrop'
    candles_df = candlestick.rain_drop(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'RainDropDoji'
    candles_df = candlestick.rain_drop_doji(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'Star'
    candles_df = candlestick.star(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    target = 'ShootingStar'
    candles_df = candlestick.shooting_star(candles_df, target=target)
    if candles_df.iloc[-1, :][target] == True:
        w = ((target, symbol, t), b)
        lst_cand.append(w)

    return lst_cand


def coinmarketcap_lst():
    res = requests.get("https://coinmarketcap.com/exchanges/binance/")
    soup = BeautifulSoup(res.content, "xml")

    name = soup.find_all('a', {'rel': "noopener nofollow noreferrer", 'class': 'cmc-link'}, limit=400)
    lst_name = [tr.text for tr in name]

    # convert '/' to '_'
    lst1 = ["".join([x if x.isalpha() == True else "_" for x in s]) for s in lst_name]

    # convert / to ""
    lst2 = [''.join([x for x in s if x != '/']) for s in lst_name]
    i = 1
    return (list(zip(lst2, lst1)))


x = coinmarketcap_lst()


# put time t as str
# x is zip list file define it before ( "", "_")
# time in code candlstick_chart_interval = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
def cand_pp(t):
    D = {'30m': 38, '1h': 104, '2h': 166, '6h': 389, '12h': 607, '1d': 784, '1w': 888}
    P = {'30m': "30 MIN", '1h': "1 HOUR", '2h': "2 HOUR", '6h': "6 HOUR", '12h': "12 HOUR", '1d': "1 DAY",
         '1w': "1 WEEK"}
    T = D[t] * 60
    while True:
        try:

            time.sleep(T)
            res = list()
            for a, b in x[0:150]:
                symbol = a
                st = "https://api.binance.com/api/v1/klines?symbol=" + symbol + "&interval=" + t + "&limit=3"
                candles = requests.get(st)
                candles_dict = candles.json()
                candles_df = pd.DataFrame(candles_dict,
                                          columns=['T', 'open', 'high', 'low', 'close', 'V', 'CT', 'QV', 'N', 'TB',
                                                   'TQ', 'I'])

                if len(candles_df) == 3:
                    w = (candalstick_patter_finder(candles_df, symbol, t, b))
                else:
                    pass

                res = res + w

            res2 = [num for num in res if num[0] != None]

            s = ''

            for a, b in res2:
                s1 = "<a href='https://www.binance.com/indexSpa.html#/trade/index?symbol=" + b + "'>" + b + "</a>" + " " * (
                            10 - len(b)) + "<code>" + a[0] + "</code>\n"
                s = s + s1

            s = "🤖 <code>Candlestick Pattern detected on </code>" + "<b>" + P[
                t] + "</b>" + "<code> chart</code>👉\n" + "<b>\n" + "🔸Symbol🔸" + "  " + "</b> <b>🔹Pattern🔹</b>\n" + s

            bot.sendMessage(chat_id='@sample11123', text=s, parse_mode='HTML', disable_notification=True)

        except:
            print('Iam here')
            time.sleep(60)


def binance_announcements():
    while True:
        try:
            res = requests.get("https://www.binance.com/en/support/categories/115000056351")
            q = soup.find_all('a', {'class': 'article-list-link'})
            lst_topic_1 = [tr.text for tr in q]
            lst_link_1 = [tr.get('href') for tr in q]

            time.sleep(300)

            res = requests.get("https://www.binance.com/en/support/categories/115000056351")
            q = soup.find_all('a', {'class': 'article-list-link'})
            lst_topic_2 = [tr.text for tr in q]
            lst_link_2 = [tr.get('href') for tr in q]

            for i in range(len(lst_link_1)):
                if lst_link_1[i] != lst_link_2[i]:
                    s = "<b>⚠️Binance Announcements</b>\n" + "<a href='https://www.binance.com" + lst_link_2[i] + "'>" + \
                        lst_topic_2[i] + "</a>"
                    bot.sendMessage(chat_id='@sample11123', text=s, parse_mode='HTML', disable_notification=False,
                                    disable_web_page_preview=False)

        except:
            time.sleep(60)


if __name__ == "__main__":
    t1 = threading.Thread(target=func, args=(5,))
    t2 = threading.Thread(target=func, args=(15,))
    t3 = threading.Thread(target=func, args=(30,))
    t4 = threading.Thread(target=func, args=(60,))
    t5 = threading.Thread(target=func, args=(240,))
    t6 = threading.Thread(target=func, args=(720,))
    t7 = threading.Thread(target=func, args=(1440,))
    t8 = threading.Thread(target=cand_pp, args=('30m',))
    t9 = threading.Thread(target=cand_pp, args=('1h',))
    t10 = threading.Thread(target=cand_pp, args=('2h',))
    t11 = threading.Thread(target=cand_pp, args=('6h',))
    t12 = threading.Thread(target=cand_pp, args=('12h',))
    t13 = threading.Thread(target=cand_pp, args=('1d',))
    t14 = threading.Thread(target=cand_pp, args=('1w',))
    t15 = threading.Thread(target=binance_announcements)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
