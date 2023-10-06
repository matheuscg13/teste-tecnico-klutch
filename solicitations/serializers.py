from rest_framework import serializers
from .models import Solicitations

class SolicitationSerializer(serializers.ModelSerializer):
    installment_value = serializers.SerializerMethodField()
    interest_per_installment = serializers.SerializerMethodField()
    total_value = serializers.SerializerMethodField()
    comission = serializers.SerializerMethodField()
    
    class Meta:
        model = Solicitations
        fields = ['client', 'interest_per_installment', 'number_of_installments', 'installment_value', 'total_value', 'comission', 'card_number', 'card_cvc', 'card_validity', 'desired_value', 'table']
        

    def get_interest_per_installment(self, obj):
        
        if obj.table == "Partner":
            return obj.number_of_installments * 1.5
        else:
            return obj.number_of_installments * 2.5
    
    def get_comission(self, obj):
        if obj.table == "Partner":
           return (7 / 100) * obj.desired_value
        else:
            return (3 / 100) * obj.desired_value

    def get_total_value(self, obj):
        interest = (obj.interest_per_installment / 100) * obj.desired_value
        return obj.desired_value + interest + obj.comission

    def get_installment_value(self, obj):
        return obj.total_value / obj.number_of_installments
    
    def create(self, validated_data: dict):
        print("=" * 1000)
        solicitation = Solicitations(**validated_data)

        if solicitation.table == "Partner":
            solicitation.interest_per_installment = solicitation.number_of_installments * 1.5
            solicitation.comission = (7 / 100) * solicitation.desired_value


        else:
            solicitation.interest_per_installment = solicitation.number_of_installments * 2.5
            solicitation.comission = (3 / 100) * solicitation.desired_value
        
        solicitation.total_value = (solicitation.interest_per_installment / 100) * solicitation.desired_value + solicitation.comission + solicitation.desired_value
        solicitation.installment_value = solicitation.total_value / solicitation.number_of_installments

        
        solicitation.save()
  

        return solicitation