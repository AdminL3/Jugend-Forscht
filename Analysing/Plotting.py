import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyparsing import col
from sklearn.linear_model import LinearRegression


def graph(rows, column_names, name, title1, title2, drop_columns, color, color_reg, regression, size, output):
    Dataframe = pd.DataFrame(rows, columns=column_names)

    # Drop specified columns if they exist
    for col in drop_columns:
        if col in Dataframe.columns:
            Dataframe = Dataframe.drop(columns=[col])

    # Convert 'date' column to datetime and set as index
    if 'date' in Dataframe.columns:
        Dataframe['date'] = pd.to_datetime(Dataframe['date'])
        Dataframe.set_index('date', inplace=True)
    else:
        Dataframe['date'] = pd.to_datetime(
            Dataframe[['year', 'month']].assign(day=1))

    # Plot the data
    plt.plot(Dataframe.index,
             Dataframe[name], 'o', markersize=size, color=color)

    # Add regression line if enabled
    if regression:
        name_lower = name.lower()
        if name_lower in Dataframe.columns:
            X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
            y = Dataframe[name_lower]
            model = LinearRegression()
            try:
                model.fit(X, y)
                y_pred = model.predict(X)
                plt.plot(Dataframe.index, y_pred, color=color_reg)
            except:
                print("Could not fit regression model")
        else:
            raise KeyError(
                f"'{name}' column is missing in the DataFrame for regression")

    # Customize plot labels and title
    plt.xlabel("Date")
    plt.ylabel(name.capitalize())
    legend = [title1, "Regression Line"] if regression else [title1]
    plt.legend(legend)
    plt.title(title2)
    plt.savefig(output)

    plt.close()


def multiple(all_rows, all_columns, name, all_titles, drop_columns, colors, colors_reg, regression, size, output):
    for i, rows in enumerate(all_rows):
        color = colors[i]

        # Create DataFrame for the current dataset
        Dataframe = pd.DataFrame(rows, columns=all_columns[i])

        # Drop specified columns if they exist
        for column in drop_columns:
            if column in Dataframe.columns:
                Dataframe = Dataframe.drop(columns=[column])

        # Handle the 'date' column
        if 'date' not in Dataframe.columns:
            try:
                Dataframe['date'] = pd.to_datetime(
                    Dataframe[['year', 'month']].assign(day=1)
                )
            except KeyError as e:
                print(f"Could not create 'date' column: {e}")
                continue

        # Ensure 'date' column is a datetime and set as index
        Dataframe['date'] = pd.to_datetime(Dataframe['date'])
        Dataframe.set_index('date', inplace=True)

        # Plot the data points
        if name.lower() in Dataframe.columns:
            plt.plot(Dataframe.index, Dataframe[name.lower()],
                     'o', markersize=size, color=color)
        else:
            print(f"'{name}' column is missing in the DataFrame for dataset {
                  all_titles[i]}")

    # Add regression lines if enabled
    if regression:
        for i, rows in enumerate(all_rows):
            Dataframe = pd.DataFrame(rows, columns=all_columns[i])

            for column in drop_columns:
                if column in Dataframe.columns:
                    Dataframe = Dataframe.drop(columns=[column])

            if 'date' not in Dataframe.columns:
                try:
                    Dataframe['date'] = pd.to_datetime(
                        Dataframe[['year', 'month']].assign(day=1)
                    )
                except KeyError as e:
                    print(f"Could not create 'date' column: {e}")
                    continue

            Dataframe['date'] = pd.to_datetime(Dataframe['date'])
            Dataframe.set_index('date', inplace=True)

            if name.lower() in Dataframe.columns:
                # Prepare data for regression
                X = Dataframe.index.astype(np.int64).values.reshape(-1, 1)
                y = Dataframe[name.lower()]
                model = LinearRegression()
                try:
                    model.fit(X, y)
                    y_pred = model.predict(X)
                    plt.plot(Dataframe.index, y_pred, color=colors_reg[i])
                except:
                    print("Could not fit regression model")
            else:
                print(f"'{name}' column is missing in the DataFrame for regression in dataset {
                      all_titles[i]}")

    # Create legends for the plot
    legend1 = [f"{name.capitalize()} for {topic}" for topic in all_titles]
    legend2 = [f"Regression Line for {topic}" for topic in all_titles]
    plt.xlabel("Date")
    plt.ylabel(name.capitalize())
    plt.legend(legend1 + legend2 if regression else legend1)
    plt.title(f"{name.capitalize()} Analysis")

    # Save the plot to the specified output file
    plt.savefig(output)
    plt.close()
