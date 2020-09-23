# Asymmetric_distributions

Code to draw samples from an asymmetric distribution, defined by a mean value, plus asymmetric uncertainties. 
This will create an skewnormal distribution using the mean value plus the uncertainties, and will later draw random samples from that distribution.

Useful for working with quantities with asymmetric uncertainties.

# Usage

The module `asymmetric_distribution.asymmetric_samples` takes four arguments: (`mean`, `plus`, `minus`, `size=5000`).

Let's say you have a quantity `a=100` with asymmetric uncertainties (`upper_error=10` and `lower_error=8`), then we can create a skewnormal distribution that matches the mean and 1sigma levels for `a`, and draw 1000 samples from it by doing the following:

```python
from asymmetric_distribution import asymmetric_samples

samples = asymmetric_samples(200, 10, 8, size=1000):
```
