import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def graph(rows, column_names, name, title1, title2, drop_columns, color, color_reg, regression, size, output):
    # Create DataFrame with rows and provided column names
    Dataframe = pd.DataFrame(rows, columns=column_names)

    # Debugging: Check column names
    print("Columns in DataFrame:", Dataframe.columns)

    # Drop specified columns if they exist
    for col in drop_columns:
        if col in Dataframe.columns:
            Dataframe = Dataframe.drop(columns=[col])

    # Convert 'date' column to datetime and set as index
    if 'date' in Dataframe.columns:
        Dataframe['date'] = pd.to_datetime(Dataframe['date'])
        Dataframe.set_index('date', inplace=True)
    else:
        raise KeyError("'date' column is missing in the DataFrame")

    # Plot the data
    Dataframe.plot(style='o', markersize=size, color=color)

    # Add regression line if enabled
    if regression:
        if name in Dataframe.columns:
            X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
            y = Dataframe[name]
            model = LinearRegression()
            model.fit(X, y)
            y_pred = model.predict(X)
            plt.plot(Dataframe.index, y_pred, color=color_reg)
        else:
            raise KeyError(
                f"'{name}' column is missing in the DataFrame for regression")

    # Customize plot labels and title
    plt.xlabel("Date")
    plt.ylabel("")
    legend = [{title1, "Regression Line"}] if regression else [title1]
    plt.legend([title1, "Regression Line"])
    plt.title(title2)
    plt.savefig(output)

    plt.close()
