import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Ian Vaughn",
            "John Doe",
            "Allan Smith"
        ],
        "Age": [22,35,58],
        "Sex": ["Male","Male","Female"]
    }
)

print(df["Age"])