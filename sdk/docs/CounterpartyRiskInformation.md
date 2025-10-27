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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

country_of_risk: StrictStr = "example_country_of_risk"
credit_ratings: List[CreditRating] = # Replace with your value
industry_classifiers: List[IndustryClassifier] = # Replace with your value
counterparty_risk_information_instance = CounterpartyRiskInformation(country_of_risk=country_of_risk, credit_ratings=credit_ratings, industry_classifiers=industry_classifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

