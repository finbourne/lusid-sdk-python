# CreditRating

Object describing a credit rating,  which assesses the stability and credit worthiness of a legal entity  and hence its likelihood of defaulting on its outstanding obligations (typically debt).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating_source** | **str** | The provider of the credit rating, which will typically be an agency such as Moody&#39;s or Standard and Poor. | 
**rating** | **str** | The credit rating provided by the rating source. This would expected to be consistent with the rating scheme of that agency/source. | 
## Example

```python
from lusid.models.credit_rating import CreditRating
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

rating_source: StrictStr = "example_rating_source"
rating: StrictStr = "example_rating"
credit_rating_instance = CreditRating(rating_source=rating_source, rating=rating)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

