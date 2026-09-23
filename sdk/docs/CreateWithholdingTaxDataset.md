# CreateWithholdingTaxDataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the relational dataset definition. | 
**code** | **str** | The code of the relational dataset definition. Together with the scope this uniquely identifies the definition. | 
**dimensions** | [**List[CreateSeriesIdentifierField]**](CreateSeriesIdentifierField.md) | The dimensions, over and above the mandatory core, that this dataset is matched on. Fully customer-defined with no platform-enforced set; each is created as a series identifier, and each requires a value source declaration on the Withholding Tax Configuration naming where the engine reads its value from. May be empty, in which case matching proceeds on tax identity alone. A dimension whose name collides with a mandatory core field is rejected. The two datasets need not carry the same dimensions - one present on only a single dataset is simply not matched on when the other is queried, an ISIN dimension on the anomaly dataset alone being the usual case. | [optional] 
## Example

```python
from lusid.models.create_withholding_tax_dataset import CreateWithholdingTaxDataset
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
dimensions: Optional[List[CreateSeriesIdentifierField]] = # Replace with your value
create_withholding_tax_dataset_instance = CreateWithholdingTaxDataset(scope=scope, code=code, dimensions=dimensions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

