import numpy as np

from ej_2.base_models.risk_request import RiskRequest
from ej_2.base_models.risk_response import RiskResponse
from ej_2.enums.status_enum import StatusEnum


class Ferretero(RiskRequest):
    max_level = 5

    @staticmethod
    def compute_amount(last_bought: list, level: int, max_level: int, score: float) -> int:
        return int(np.average(last_bought) * (1 + level / max_level + score))

    def risk_analysis(self) -> RiskResponse:
        self.max_level = 5
        status, amount = StatusEnum('rejected'), 0
        last_bought, bought_mix, level = self.input_data['last_bought'], self.input_data['bought_mix'],\
                                         self.input_data['level']

        if bought_mix & level < 3:
            status = StatusEnum('approved')
            amount = self.compute_amount(last_bought, level, self.max_level, 0.2)
        elif not bought_mix & level >= 3:
            status = StatusEnum('approved')
            amount = self.compute_amount(last_bought, level, self.max_level, 0.3)
        elif bought_mix:
            status = StatusEnum('approved')
            amount = self.compute_amount(last_bought, level, self.max_level, 0.1)

        response = RiskResponse(user_id=self.user_id,
                                product_name=self.product_name,
                                status=status,
                                amount=amount)
        return response
