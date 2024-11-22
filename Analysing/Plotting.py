import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyparsing import col
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
        print("DataFrame columns:", Dataframe.columns)
        name_lower = name.lower()
        if name_lower in Dataframe.columns:
            X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
            y = Dataframe[name_lower]
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
    legend = [title1, "Regression Line"] if regression else [title1]
    plt.legend(legend)
    plt.title(title2)
    plt.savefig(output)

    plt.close()


def multiple(all_rows, all_columns, name, all_titles, drop_columns, colors, colors_reg, regression, size, output):
    for i, rows in enumerate(all_rows):
        color = colors[i]

        Dataframe = pd.DataFrame(
            rows, columns=all_columns[i])

        for column in drop_columns:
            Dataframe = Dataframe.drop(columns=[f'{column}'])

        Dataframe['date'] = pd.to_datetime(Dataframe['date'])
        Dataframe.set_index('date', inplace=True)

        plt.plot(Dataframe.index,
                 Dataframe[f"{name.lower()}"], 'o', markersize=size, color=color)

    if regression:
        for i, rows in enumerate(all_rows):
            Dataframe = pd.DataFrame(
                rows, columns=all_columns[i])
            for column in drop_columns:
                Dataframe = Dataframe.drop(columns=[f'{column}'])

            Dataframe['date'] = pd.to_datetime(Dataframe['date'])
            Dataframe.set_index('date', inplace=True)

            X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
            y = Dataframe[f'{name}']
            model = LinearRegression()
            model.fit(X, y)
            y_pred = model.predict(X)
            plt.plot(Dataframe.index, y_pred, color=colors_reg[i])

        legend1 = [f"Word Count for {topic}" for topic in all_titles]
        legend2 = [f"Regression Line for {topic}" for topic in all_titles]
        plt.xlabel("Date")
        plt.ylabel(name.capitalize())
        plt.legend(legend1 + legend2 if regression else legend1)
        plt.title("Word Count Analysis")

        plt.savefig(output)
        plt.close()
