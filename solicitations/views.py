from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView
from .models import Solicitations
from .serializers import SolicitationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError

# Create your views here.
class SolicitationView(ListCreateAPIView):
    queryset = Solicitations.objects.all()
    serializer_class = SolicitationSerializer

class ConsultInstallmentsView(APIView):
    def post(self, request):
        try:
            
            desired_value = request.data.get('desired_value', 0)

            if desired_value > 10000:
                raise ValidationError("O valor deve ser menor ou igual a 10000.")
            if desired_value < 300:
                raise ValidationError("O valor deve ser maior ou igual a 300.")

            number_of_installment = 24
            installments_default_table = []
            installments_partner_table = []
            for i in range(number_of_installment):
                interest_per_installment = (i + 1) * 2.5
                comission = (3 / 100) * desired_value
                interest = (interest_per_installment / 100) * desired_value
                total_value = desired_value + interest + comission
                installment_value = total_value / (i + 1)
                installments_default_table.append({
                    "interest": interest_per_installment,
                    "comission": round(comission, 2),
                    "total_value": round(total_value, 2),
                    "installment_value": round(installment_value, 2),
                    "number_of_installments": i + 1,
                    "table": "Default"
                })
            for i in range(number_of_installment):
                interest_per_installment = (i + 1) * 1.5
                comission = (7 / 100) * desired_value
                interest = (interest_per_installment / 100) * desired_value
                total_value = desired_value + interest + comission
                installment_value = total_value / (i + 1)
                installments_partner_table.append({
                    "interest": interest_per_installment,
                    "comission": round(comission, 2),
                    "total_value": round(total_value, 2),
                    "installment_value": round(installment_value, 2),
                    "number_of_installments": i + 1,
                    "table": "Partner"
                })
                
 

            return Response({'installments_default_table': installments_default_table, 'installments_partner_table': installments_partner_table})
        except (TypeError):
            return Response({'mensagem': 'Esta rota só aceita números'})
        except (ValidationError):
            return Response({"mensagem": "O valor solicitado deve estar entre R$300,00 e R$10000,00."})