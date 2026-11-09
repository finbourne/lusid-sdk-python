# TaxClassificationInputs

The instrument static the decision tree reads. A missing flag is a missing input, not a false.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_relationship_asset** | **bool** | Whether the instrument is a loan relationship asset. | [optional] 
**index_linked_gilt** | **bool** | Whether the instrument is an index-linked gilt. | [optional] 
**chargeable_asset** | **bool** | Whether disposals of the instrument give rise to chargeable gains. | [optional] 
**cis_non_transparent** | **bool** | Whether the instrument is a non-transparent collective investment scheme. | [optional] 
**cis_transparent** | **bool** | Whether the instrument is a transparent collective investment scheme. | [optional] 
**derivative** | **bool** | Whether the instrument is a derivative contract. | [optional] 
**derivative_financial_future** | **bool** | Whether the derivative is a financial future or option within the chargeable gains rules. | [optional] 
**derivative_pooled_security** | **bool** | Whether the derivative is pooled as a security. | [optional] 
**private_equity** | **bool** | Whether the instrument is a private equity holding. | [optional] 
**real_estate** | **bool** | Whether the instrument is a real estate holding. | [optional] 
**qualifying_investments_percent** | **float** | The percentage of the scheme&#39;s assets that are qualifying (non-equity) investments; more than 60 percent makes the scheme a bond fund. | [optional] 
## Example

```python
from lusid.models.tax_classification_inputs import TaxClassificationInputs
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

loan_relationship_asset: Optional[StrictBool] = # Replace with your value
loan_relationship_asset:Optional[StrictBool] = None
index_linked_gilt: Optional[StrictBool] = # Replace with your value
index_linked_gilt:Optional[StrictBool] = None
chargeable_asset: Optional[StrictBool] = # Replace with your value
chargeable_asset:Optional[StrictBool] = None
cis_non_transparent: Optional[StrictBool] = # Replace with your value
cis_non_transparent:Optional[StrictBool] = None
cis_transparent: Optional[StrictBool] = # Replace with your value
cis_transparent:Optional[StrictBool] = None
derivative: Optional[StrictBool] = # Replace with your value
derivative:Optional[StrictBool] = None
derivative_financial_future: Optional[StrictBool] = # Replace with your value
derivative_financial_future:Optional[StrictBool] = None
derivative_pooled_security: Optional[StrictBool] = # Replace with your value
derivative_pooled_security:Optional[StrictBool] = None
private_equity: Optional[StrictBool] = # Replace with your value
private_equity:Optional[StrictBool] = None
real_estate: Optional[StrictBool] = # Replace with your value
real_estate:Optional[StrictBool] = None
qualifying_investments_percent: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_classification_inputs_instance = TaxClassificationInputs(loan_relationship_asset=loan_relationship_asset, index_linked_gilt=index_linked_gilt, chargeable_asset=chargeable_asset, cis_non_transparent=cis_non_transparent, cis_transparent=cis_transparent, derivative=derivative, derivative_financial_future=derivative_financial_future, derivative_pooled_security=derivative_pooled_security, private_equity=private_equity, real_estate=real_estate, qualifying_investments_percent=qualifying_investments_percent)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

