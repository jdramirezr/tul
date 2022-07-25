from ej_2.base_models.risk_response import RiskResponse
from ej_2.base_models.risk_request import RiskRequest
from ej_2.enums.status_enum import StatusEnum


class Tuler(RiskRequest):

    @staticmethod
    def compute_amount(salary: int, fees: int) -> int:
        return int(salary * fees * 0.3)

    def risk_analysis(self) -> RiskResponse:
        response = RiskResponse(
            user_id=self.user_id,
            product_name=self.product_name)

        if self.input_data['months_worked'] < 3:
            
            response.status = StatusEnum('rejected')
            response.amount = 0
            pass
        else:
            response.status = StatusEnum('approved')
            response.amount = self.compute_amount(self.input_data['salary'], self.input_data['fees'])
        return response
