import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def graph(rows, column_names, name, legend_title, title, drop_columns, color, color_reg, regression, size, output):
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
        Dataframe.set_index('date', inplace=True)

    # Plot the data
    plt.plot(Dataframe.index,
             Dataframe[name], 'o', markersize=size, color=color)

    # Add regression line if enabled
    corr_coefficient = None
    slope = None
    if regression:
        name_lower = name.lower()
        if name_lower in Dataframe.columns:

            # Prepare data for regression and correlation
            # Convert dates to a numeric scale in years instead of nanoseconds
            X = (Dataframe.index.astype(np.int64) / 1e9 / (60 * 60 * 24 * 365)
                 ).values.reshape(-1, 1)  # Convert to years

            y = Dataframe[name_lower]

            # Calculate correlation coefficient
            corr_coefficient = np.corrcoef(X.flatten(), y)[0, 1]

            # Fit regression model
            model = LinearRegression()
            try:
                model.fit(X, y)
                y_pred = model.predict(X)
                plt.plot(Dataframe.index, y_pred, color=color_reg)
                slope = model.coef_[0]  # Extract the slope
            except:
                print("Could not fit regression model")
        else:
            raise KeyError(
                f"'{name}' column is missing in the DataFrame for regression")

    # Customize plot labels and title
    plt.xticks(rotation=25)
    plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.2)

    plt.xlabel("Date")
    plt.ylabel(name.capitalize())
    legend = [legend_title, "Regression Line"] if regression else [legend_title]
    plt.legend(legend)

    # Display correlation coefficient and slope on the plot (if calculated)
    if corr_coefficient is not None:
        plt.gcf().text(0.93, 0.94, f'Slope: {
            slope:.0f} (words per year)', fontsize=12, verticalalignment='top', horizontalalignment='right')
        plt.gcf().text(0.93, 0.98, f"Correlation: {round(
            corr_coefficient*100, 2)}%", fontsize=12, verticalalignment='top', horizontalalignment='right')

    plt.text(0, 1.07, title, fontsize=14, verticalalignment='top',
             horizontalalignment='left', transform=plt.gca().transAxes)
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

    # Customize plot labels and title
    plt.xticks(rotation=25)
    plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.2)
    legend1 = [f"{name.capitalize()} for {topic}" for topic in all_titles]
    legend2 = [f"Regression Line for {topic}" for topic in all_titles]
    plt.xlabel("Date")
    plt.ylabel(name.capitalize())
    plt.legend(legend1 + legend2 if regression else legend1)
    plt.title(f"{name.capitalize()} Analysis")

    # Save the plot to the specified output file
    plt.savefig(output)
    plt.close()
