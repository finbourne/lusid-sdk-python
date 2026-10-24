# PartnershipAccountingConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**config_pack** | [**ResourceId**](ResourceId.md) |  | [optional] 
**commitment_currency_policy** | **str** | Available values: FundCurrencyOnly, AllowLineCurrency. | [optional] 
**register_portfolio_group** | [**ResourceId**](ResourceId.md) |  | [optional] 
**capital_model** | **str** | Available values: PartnershipCapitalAccounts, SeriesUnitised. | [optional] 
**capability_overrides** | [**List[CapabilityOverride]**](CapabilityOverride.md) |  | [optional] 
**series** | [**SeriesConfiguration**](SeriesConfiguration.md) |  | [optional] 
**effective_capabilities** | **Dict[str, Optional[str]]** | Derived on the way out; ignored on the way in. | [optional] 
**presentation** | [**PresentationConfiguration**](PresentationConfiguration.md) |  | [optional] 
**allocation_bases** | [**List[AllocationBasisRule]**](AllocationBasisRule.md) |  | [optional] 
## Example

```python
from lusid.models.partnership_accounting_configuration import PartnershipAccountingConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

enabled: StrictBool
enabled:StrictBool = True
config_pack: Optional[ResourceId] = # Replace with your value
commitment_currency_policy: Optional[StrictStr] = "example_commitment_currency_policy"
register_portfolio_group: Optional[ResourceId] = # Replace with your value
capital_model: Optional[StrictStr] = "example_capital_model"
capability_overrides: Optional[List[CapabilityOverride]] = # Replace with your value
series: Optional[SeriesConfiguration] = None
effective_capabilities: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
presentation: Optional[PresentationConfiguration] = None
allocation_bases: Optional[List[AllocationBasisRule]] = # Replace with your value
partnership_accounting_configuration_instance = PartnershipAccountingConfiguration(enabled=enabled, config_pack=config_pack, commitment_currency_policy=commitment_currency_policy, register_portfolio_group=register_portfolio_group, capital_model=capital_model, capability_overrides=capability_overrides, series=series, effective_capabilities=effective_capabilities, presentation=presentation, allocation_bases=allocation_bases)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

