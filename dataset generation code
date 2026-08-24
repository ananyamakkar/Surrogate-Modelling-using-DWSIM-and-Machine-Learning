import System

print("=== GENERATING 100 UNIQUE SUCCESSFUL CASES ===")

column = Flowsheet.GetFlowsheetSimulationObject("DCOL-1")
feed = Flowsheet.GetFlowsheetSimulationObject("FEED")
distillate = Flowsheet.GetFlowsheetSimulationObject("DISTILLATE")
bottoms = Flowsheet.GetFlowsheetSimulationObject("BOTTOMS")

file_path = r"C:\Users\anany\DWSIM Surrogate Model\dwsim_dataset_final_100_unique.csv"

file = open(file_path, "w")

file.write(
    "Feed Temperature,Feed Pressure,Feed Benzene Mole Fraction,"
    "Number of Stages,Feed Stage,Reflux Ratio,"
    "Bottoms Withdrawal Rate,Distillate Purity,Bottoms Purity,"
    "Condenser Heat Duty,Reboiler Heat Duty\n"
)

temperatures = [
    351.15,
    351.40,
    351.65,
    351.90,
    352.15,
    352.40,
    352.65,
    352.90,
    353.15,
    353.40,
    353.65,
    353.90,
    354.15,
    354.40,
    354.65,
    354.90,
    355.15,
    355.40,
    355.65,
    355.90
]

pressures = [
    99000.0,
    100000.0,
    101000.0,
    101325.0,
    102000.0
]

reflux_ratios = [
    3.0,
    3.15,
    3.30,
    3.45,
    3.60,
    3.75,
    3.90,
    4.05,
    4.20,
    4.35
]

bottoms_rates = [
    13.70,
    13.73,
    13.76,
    13.79,
    13.82,
    13.85,
    13.88,
    13.91,
    13.94,
    13.97
]

benzene_fraction = 0.50
number_of_stages = 10
feed_stage = 5

successful_cases = 0
attempted_cases = 0
max_attempts = 130

while successful_cases < 100 and attempted_cases < max_attempts:

    attempted_cases += 1

    i = successful_cases

    temperature = temperatures[i % 20]
    pressure = pressures[i // 20]

    reflux_ratio = reflux_ratios[
        (i * 3) % 10
    ]

    bottoms_rate = bottoms_rates[
        (i * 7) % 10
    ]

    print("")
    print("========================================")
    print("ATTEMPT " + str(attempted_cases))
    print("SUCCESSFUL: " + str(successful_cases) + " / 100")
    print("========================================")

    print("Temperature: " + str(temperature))
    print("Pressure: " + str(pressure))
    print("Reflux Ratio: " + str(reflux_ratio))
    print("Bottoms Rate: " + str(bottoms_rate))

    try:

        feed.SetTemperature(
            float(temperature)
        )

        feed.SetPressure(
            float(pressure)
        )

        composition = System.Array[float]([
            float(benzene_fraction),
            float(1.0 - benzene_fraction)
        ])

        feed.SetOverallMolarComposition(
            composition
        )

        try:
            feed.Calculate(True, True)
        except:
            pass

        try:
            column.SetTopPressure(
                float(pressure)
            )
        except:
            pass

        column.SetNumberOfStages(
            int(number_of_stages)
        )

        column.SetStreamFeedStage(
            feed,
            int(feed_stage)
        )

        column.SetCondenserSpec(
            "Reflux Ratio",
            float(reflux_ratio),
            ""
        )

        column.SetReboilerSpec(
            "Product Molar Flow",
            float(bottoms_rate),
            "mol/s"
        )

        print("Running calculation...")

        column.Solve()

        print("Calculation finished.")

        distillate_purity = float(
            distillate.GetOverallComposition()[0]
        )

        bottoms_purity = float(
            bottoms.GetOverallComposition()[1]
        )

        condenser_heat_duty = abs(
            float(column.CondenserDuty)
        )

        reboiler_heat_duty = abs(
            float(column.ReboilerDuty)
        )

        if distillate_purity <= 0.0 or distillate_purity >= 1.0:
            raise Exception("Invalid distillate purity")

        if bottoms_purity <= 0.0 or bottoms_purity >= 1.0:
            raise Exception("Invalid bottoms purity")

        if condenser_heat_duty <= 0.0:
            raise Exception("Invalid condenser duty")

        if reboiler_heat_duty <= 0.0:
            raise Exception("Invalid reboiler duty")

        file.write(
            str(temperature) + "," +
            str(pressure) + "," +
            str(benzene_fraction) + "," +
            str(number_of_stages) + "," +
            str(feed_stage) + "," +
            str(reflux_ratio) + "," +
            str(bottoms_rate) + "," +
            str(distillate_purity) + "," +
            str(bottoms_purity) + "," +
            str(condenser_heat_duty) + "," +
            str(reboiler_heat_duty) +
            "\n"
        )

        file.flush()

        successful_cases += 1

        print("")
        print("SUCCESSFUL CASE")
        print("xD = " + str(distillate_purity))
        print("xB = " + str(bottoms_purity))
        print("QC = " + str(condenser_heat_duty))
        print("QR = " + str(reboiler_heat_duty))

    except Exception as error:

        print("")
        print("CASE FAILED")
        print(str(error))
        print("Skipping this case...")

file.close()

print("")
print("========================================")
print("DATASET GENERATION COMPLETE")
print("========================================")
print("")
print("Successful cases: " + str(successful_cases))
print("Attempts made: " + str(attempted_cases))
print("")
print("CSV:")
print(file_path)
print("")
print("=== DONE ===")
