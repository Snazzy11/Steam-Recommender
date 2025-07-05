print('hello world!')

import numpy as np
import pandas as pd

# Create a simple NumPy array
numpy_array = np.array([1, 2, 3, 4, 5])
print("Successfully created a NumPy array:")
print(numpy_array)
print("-" * 30)

# Create a simple Pandas DataFrame
data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=data)
print("Successfully created a Pandas DataFrame:")
print(df)
print("-" * 30)

print("🎉 Conda is working correctly!")