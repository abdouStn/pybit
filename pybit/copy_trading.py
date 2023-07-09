from enum import Enum


class CopyTrading(str, Enum):
    # https://api2.bybit.com/fapi/beehive/public/v1/common/leaderboard-info?timeStamp=1686475454753

    # https://api2.bybit.com/fapi/beehive/private/v1/common/recommend-leaders?timeStamp=1686475454762&language=en-US

    # https://api2.bybit.com/fapi/beehive/public/v1/common/dynamic-leader-list?timeStamp=1686475454764&pageNo=1&pageSize=16&dataDuration=DATA_DURATION_SEVEN_DAY&leaderTag=&code=&leaderLevel=&userTag=

    # https://api2.bybit.com/fapi/beehive/public/v1/common/trader-leaderboard?timeStamp=1686475455358&rankingForm=RANKING_FORM_TRADERS_PNL&period=LEADERBOARD_PERIOD_WEEK&endTimeE3=1686268800000

    # https://api2.bybit.com/fapi/beehive/private/v1/pub-leader/info?timeStamp=1686480986366&leaderMark=C83kHVKD%2BVxaIxuYRwxFew%3D%3D

    # https://api2.bybit.com/fapi/beehive/public/v1/common/position/list?timeStamp=1686480507956&leaderMark=C83kHVKD%2BVxaIxuYRwxFew%3D%3D

    GET_LEADERBOARD_TRADER = "/fapi/beehive/public/v1/common/trader-leaderboard"
    GET_LEADER_INFO = "/fapi/beehive/private/v1/pub-leader/info"
    GET_LEADER_POSITION = "/fapi/beehive/public/v1/common/position/list"

    def __str__(self) -> str:
        return self.value
