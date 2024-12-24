# NANPA API Client

<p align="center">
  <img src="./.screens/nanpa.png">
</p>

A Python client for interacting with the North American Numbering Plan Administration (NANPA) public API system.

## Overview
The North American Numbering Plan *(NANP)* is the unified telephone numbering system used by the United States, Canada, and many Caribbean territories. Established in 1997, NANPA serves as the administrator for this system, managing the allocation and assignment of area codes, central office codes, and other numbering resources to ensure efficient telecommunications routing and prevent number exhaustion.

This client provides a simple interface to NANPA's public API endpoints, allowing developers to programmatically access critical numbering plan data and network information.

## Installation
```bash
pip install nanpa
```

or...

```bash
git clone https://github.com/acidvegas/nanpa
cd nanpa
python setup.py install
```

## API Documentation

### State & Area Code Information
The foundation of the NANP system revolves around geographic numbering assignments. The `get_states()` method returns all participating regions in the NANP, including US states and territories, Canadian provinces, and Caribbean nations. For more granular information, `get_area_codes_by_state(state)` provides all area codes assigned to a specific region, while `get_area_code_info(npa)` delivers detailed information about individual area codes including their service boundaries, implementation dates, and relief planning status.

### Rate Center Operations
Rate centers form the geographic backbone of telephone billing and routing. Using `get_rate_centers(state)`, you can retrieve information about these fundamental units within any state, including their coordinates, associated area codes, and operating companies. The `get_rate_center_changes(start_date, end_date)` method tracks modifications to these configurations over time, such as consolidations, splits, and boundary adjustments.

### Number Block Management
The NANP manages telephone numbers in blocks of 1,000 consecutive numbers. The `get_thousands_blocks(state, npa, report_type)` method provides information about these blocks, including carrier assignments and availability. For future planning, `get_pooling_forecast(state, npa)` projects number utilization and exhaust dates, while `get_current_pool_tracking(state, npa)` monitors active pool sizes and carrier participation.

### Network Infrastructure
Location Routing Numbers *(LRNs)* are crucial for number portability in modern networks. The `get_lrn_forecast(state, npa)` method helps plan for routing efficiency and port capacity. Central office code assignments can be monitored through `get_co_code_forecast(state, npa)`, while `get_pstn_activation(state)` provides status updates on Public Switched Telephone Network readiness.

### Specialty Number Resources
Beyond geographic numbers, NANPA manages special purpose codes. The 5XX NPA code family, accessed through various methods like `get_specialty_codes_available()`, `get_specialty_codes_assigned()`, and `get_specialty_codes_aging()`, serves non-geographic services. The 9YY codes, retrieved via `get_9yy_codes()`, are reserved for premium services, emergency preparedness, and network testing.

## Usage Example
```python
from nanpa import NanpaAPI

client = NanpaAPI()

# Get rate centers in Florida
fl_centers = client.get_rate_centers('FL')

# Check thousands blocks for area code 239
blocks = client.get_thousands_blocks('FL', '239')

# Monitor rate center changes
changes = client.get_rate_center_changes(
    '2024-12-01T00:00:00.000-05:00',
    '2024-12-31T23:59:59.999-05:00'
)
```

---

###### Mirrors: [acid.vegas](https://git.acid.vegas/nanpa) • [SuperNETs](https://git.supernets.org/acidvegas/nanpa) • [GitHub](https://github.com/acidvegas/nanpa) • [GitLab](https://gitlab.com/acidvegas/nanpa) • [Codeberg](https://codeberg.org/acidvegas/nanpa)
