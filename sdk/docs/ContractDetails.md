# ContractDetails

Set of identifiers of an existing FlexibleLoan contract.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **Dict[str, str]** | Unique instrument identifiers. | 
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier - readonly field, resolved from the instrument identifiers. | [optional] [readonly] 
**instrument_scope** | **str** | The scope in which the FlexibleLoan instrument lies - readonly field, resolved from the instrument identifiers. | [optional] [readonly] 
**instrument_name** | **str** | The name of the FlexibleLoan instrument - readonly field, resolved from the instrument identifiers. | [optional] [readonly] 
**dom_ccy** | **str** | The domestic currency of the instrument - readonly field, resolved from the instrument identifiers. | [optional] [readonly] 
## Example

```python
from lusid.models.contract_details import ContractDetails
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

identifiers: Dict[str, StrictStr] = # Replace with your value
lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_name: Optional[StrictStr] = "example_instrument_name"
dom_ccy: Optional[StrictStr] = "example_dom_ccy"
contract_details_instance = ContractDetails(identifiers=identifiers, lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, instrument_name=instrument_name, dom_ccy=dom_ccy)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

