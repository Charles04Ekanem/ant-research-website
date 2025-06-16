#License Wizard 

from datetime import datetime

def generate_dataset_license(name, email, dataset_name, organization=None, year=None):
    year = year or datetime.now().year
    organization_line = f"Organization: {organization}" if organization else ""
    
    content = f"""\
Dataset License Agreement
--------------------------

Dataset Name: {dataset_name}
Contributor: {name}
Contact: {email}
{organization_line}
Year: {year}

This dataset is provided under the following conditions:

1. The dataset is intended for **non-commercial**, **research**, and **educational** purposes only.
2. Redistribution, resale, or commercial use is strictly prohibited without **prior written consent** from the contributor.
3. Proper attribution to the contributor must be given in any published work using this dataset.
4. The dataset is provided "as is" without warranty of any kind.

By using this dataset, you agree to abide by these terms.

© {year} {name}. All rights reserved.
"""

    filename = f"{dataset_name}_LICENSE.txt"
    with open(filename, 'w') as f:
        f.write(content.strip())
    
    print(f"License file generated: {filename}")

# generate_dataset_license('Charles Ekanem', 'charles@example.com', 'Cropset', organization='ANT R&D')
