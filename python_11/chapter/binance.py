from binance.client import Client
import os
import ta  # 기술적 분석 라이브러리 (선택 사항)
import time

# API 키 및 시크릿 키 설정 (환경 변수 사용 권장)
api_key = os.environ.get('D1TSfV9MbrwWqD03ykzMnOtuRVZtwOTJMdZsL9uYkS2q5Z7zXfQBbDb1SxVTYZN5')
secret_key = os.environ.get('8juE7ouTrMavzLWVsHbFiJDFBKsiwYq21W0bveBEsr4KOkvBhh0uWsf0cH3PJpay')
client = Client(api_key, secret_key)

def calculate_ma(data, period):
    # 이동 평균선 계산 로직
    return data['close'].rolling(window=period).mean()

def calculate_bollinger_bands(data, period, std_dev):
    # 볼린저 밴드 계산 로직
    ma = calculate_ma(data, period)
    upper_band = ma + data['close'].rolling(window=period).std() * std_dev
    lower_band = ma - data['close'].rolling(window=period).std() * std_dev
    return upper_band, ma, lower_band

# (다른 기술적 지표 계산 함수들...)

def check_buy_condition(data):
    # 매수 조건 확인 로직 (이동 평균선 교차, 볼린저 밴드, 가격 돌파 등)
    # ...
    return should_buy

def check_sell_condition(data):
    # 매도 조건 확인 로직
    # ...
    return should_sell

from binance.client import Client
import os
import ta
import time
import pandas as pd

# API 키 및 시크릿 키 설정 (사용자 제공)
api_key = 'D1TSfV9MbrwWqD03ykzMnOtuRVZtwOTJMdZsL9uYkS2q5Z7zXfQBbDb1SxVTYZN5'
secret_key = '8juE7ouTrMavzLWVsHbFiJDFBKsiwYq21W0bveBEsr4KOkvBhh0uWsf0cH3PJpay'
client = Client(api_key, secret_key)

def check_buy_condition(df):
    # 단기 이동 평균선이 장기 이동 평균선 위로 골든 크로스 발생 시 매수 신호
    if (df['ma_short'].iloc[-1] > df['ma_long'].iloc[-1]) and (df['ma_short'].iloc[-2] <= df['ma_long'].iloc[-2]):
        return True
    return False

def check_sell_condition(df):
    # 단기 이동 평균선이 장기 이동 평균선 아래로 데드 크로스 발생 시 매도 신호
    if (df['ma_short'].iloc[-1] < df['ma_long'].iloc[-1]) and (df['ma_short'].iloc[-2] >= df['ma_long'].iloc[-2]):
        return True
    return False

def place_order(side, symbol, quantity):
    # 시장가 주문 실행 로직 (오류 처리 포함)
    try:
        order = client.order_market(symbol=symbol, side=side, quantity=quantity)
        print(f"{side} 주문 실행 완료: {order}")
        return True
    except Exception as e:
        print(f"{side} 주문 실행 실패: {e}")
        print(e)
        return False

if __name__ == "__main__":
    symbol = 'BTCUSDT'  # 거래 쌍
    interval = '1h'     # 캔들 데이터 간격
    ma_short_period = 20
    ma_long_period = 50
    quantity = 0.001     # 매수/매도 수량 (본인 자금 상황에 맞게 조정!)
    sleep_interval = 60   # 매매 조건 확인 주기 (초)

    while True:
        try:
            # 과거 캔들 데이터 가져오기 (최근 500개)
            klines = client.get_historical_klines(symbol, interval, "500 hours ago")

            if not klines:
                print("캔들 데이터가 없습니다.")
                time.sleep(sleep_interval)
                continue

            # 데이터프레임으로 변환
            df = pd.DataFrame(klines, columns=['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
            df['close'] = pd.to_numeric(df['close'])

            # 이동 평균선 계산 (ta 라이브러리 사용)
            df['ma_short'] = ta.trend.sma_indicator(df['close'], window=ma_short_period)
            df['ma_long'] = ta.trend.sma_indicator(df['close'], window=ma_long_period)

            # 매수 조건 확인 및 주문 실행
            if check_buy_condition(df):
                print(f"{time.ctime()} - 매수 신호 발생")
                place_order('BUY', symbol, quantity)

            # 매도 조건 확인 및 주문 실행
            elif check_sell_condition(df):
                print(f"{time.ctime()} - 매도 신호 발생")
                place_order('SELL', symbol, quantity)

            else:
                print(f"{time.ctime()} - 매수/매도 신호 없음")

            time.sleep(sleep_interval)

        except Exception as e:
            print(f"오류 발생: {e}")
            time.sleep(sleep_interval)