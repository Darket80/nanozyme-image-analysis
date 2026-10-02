import pandas as pd
from src.analysis.fit_curve import fit_linear_curve

def calculate_error(data, group_column, value_column):

    result = data.groupby(group_column)[value_column].agg(
        ['mean', 'std']
    )

    return result



if __name__ == "__main__":

    # 假数据
    data = pd.DataFrame({

        "concentration":[
            10,10,10,
            50,50,50,
            100,100,100
        ],

        "rate":[

            0.001800,
            0.001830,
            0.001800,

            0.004240,
            0.004180,
            0.004230,

            0.006530,
            0.006550,
            0.006500
        ]

    })


    result = calculate_error(
        data,
        "concentration",
        "rate"
    )

    x = result.index.to_numpy()

    y = result["mean"].to_numpy()

    yerr = result["std"].to_numpy()

    slope, intercept, r2 = fit_linear_curve(
        x,
        y
    )

    y_fit = slope * x + intercept

    print()
    print("====================")
    print("Linear fitting")
    print("====================")

    print(f"Slope     = {slope:.8f}")
    print(f"Intercept = {intercept:.8f}")
    print(f"R²        = {r2:.6f}")

    print(
        f"Equation  = y = {slope:.8f}x + {intercept:.8f}"
    )
    print(result)

    from plot_curve import plot_activity_curve
    x =result.index.to_numpy()
    y =result["mean"].to_numpy()
    yerr =result["std"].to_numpy()
    plot_activity_curve(
        x=x,
        y=y,
        y_fit=y_fit,
        title="CuMnZnS Nanozyme Activity",
        xlabel="Concentration (μg/mL)",
        ylabel="Initial rate (Abs/s)",
        save_path="../../results/figures/activity_errorbar.png",
        yerr=yerr
    )

