# WithholdingTaxValueSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** | The name of the matching dimension this declaration populates, as it appears in the dataset field schema. A declaration naming a dimension neither dataset has is rejected. | 
**source** | **str** | The LUSID field the engine reads the dimension&#39;s value from, addressed in the same syntax used to filter results: a property key in the form Properties[{domain}/{scope}/{code}], such as Properties[Instrument/WithholdingTax/AssetClass] or Properties[Transaction/WithholdingTax/Custodian]; or the name of a field on the entity itself, such as Transaction.SettlementCurrency. | 
## Example

```python
from lusid.models.withholding_tax_value_source import WithholdingTaxValueSource
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

dimension: StrictStr = "example_dimension"
source: StrictStr = "example_source"
withholding_tax_value_source_instance = WithholdingTaxValueSource(dimension=dimension, source=source)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

