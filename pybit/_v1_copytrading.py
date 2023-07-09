from ._http_manager import _V5HTTPManager
from .copy_trading import CopyTrading


class CopyTradingHTTP(_V5HTTPManager):
    def get_leader_board(self, **kwargs):
        """Get leaderboard top traders."""
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{CopyTrading.GET_LEADERBOARD_TRADER}",
            query=kwargs,
            auth=True,
        )

    def get_leader_info(self, **kwargs):
        """Get a leader info."""
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{CopyTrading.GET_LEADER_INFO}",
            query=kwargs,
            auth=True,
        )

    def get_leader_positions(self, **kwargs):
        """Get leader current positions."""
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{CopyTrading.GET_LEADER_POSITION}",
            query=kwargs,
            auth=True,
        )
