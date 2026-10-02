def calculate_activity(
    rate_abs_per_min,
    total_volume_ml,
    extinction_coefficient,
    path_length_cm,
    enzyme_mass_mg
):
    """
    根据吸光度变化速率计算纳米酶活性

    参数
    ----
    rate_abs_per_min : float
        吸光度变化速率，Abs/min

    total_volume_ml : float
        反应体系总体积，mL

    extinction_coefficient : float
        摩尔消光系数，M^-1 cm^-1

    path_length_cm : float
        光程，cm

    enzyme_mass_mg : float
        纳米酶质量，mg

    返回
    ----
    activity : float
        纳米酶活性，U/mg
    """

    # mL → L
    total_volume_L = total_volume_ml / 1000

    # Abs/min → mol/L/min
    concentration_rate = (
        rate_abs_per_min
        / (extinction_coefficient * path_length_cm)
    )

    # mol/min
    reaction_rate = (
        concentration_rate
        * total_volume_L
    )

    # 1 U = 1 μmol/min
    activity = (
        reaction_rate
        * 1_000_000
        / enzyme_mass_mg
    )

    return activity
if __name__ == "__main__":

    # 模拟测试
    rate = 0.003

    volume = 1.0

    epsilon = 39000

    path_length = 1.0

    enzyme_mass = 0.1


    activity = calculate_activity(
        rate,
        volume,
        epsilon,
        path_length,
        enzyme_mass
    )


    print("====================")
    print("Enzyme activity")
    print("====================")

    print(
        f"Activity = {activity:.6f} U/mg"
    )