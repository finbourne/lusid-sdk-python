# CounterpartyRiskInformation

In the event that the legal entity is a counterparty to an OTC transaction  (as signatory to a counterparty agreement such as an ISDA 2002 Master Agreement),  this information would be needed for calculations  such as Credit-Valuation-Adjustments and Debit-Valuation-Adjustments (CVA, DVA, XVA etc).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_of_risk** | **str** | The country to which one would naturally ascribe risk, typically the legal entity&#39;s country of registration. This can be used to infer funding currency and related market data in the absence of a specific preference. | 
**credit_ratings** | [**List[CreditRating]**](CreditRating.md) |  | 
**industry_classifiers** | [**List[IndustryClassifier]**](IndustryClassifier.md) |  | 

## Example

```python
from lusid.models.counterparty_risk_information import CounterpartyRiskInformation

# TODO update the JSON string below
json = "{}"
# create an instance of CounterpartyRiskInformation from a JSON string
counterparty_risk_information_instance = CounterpartyRiskInformation.from_json(json)
# print the JSON string representation of the object
print CounterpartyRiskInformation.to_json()

# convert the object into a dict
counterparty_risk_information_dict = counterparty_risk_information_instance.to_dict()
# create an instance of CounterpartyRiskInformation from a dict
counterparty_risk_information_form_dict = counterparty_risk_information.from_dict(counterparty_risk_information_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


