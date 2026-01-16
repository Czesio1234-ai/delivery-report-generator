import csv
from collections import defaultdict

FILE_NAME = "deliveries.csv"


def load_deliveries(file_name):
    deliveries = []

    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            deliveries.append(
                {
                    "date": row["date"],
                    "driver": row["driver"],
                    "km": float(row["km"]),
                    "time": int(row["delivery_time_min"]),
                    "city": row["city"],
                }
            )

    return deliveries


def create_summary(deliveries):
    total_deliveries = len(deliveries)
    total_km = sum(d["km"] for d in deliveries)
    total_time = sum(d["time"] for d in deliveries)

    deliveries_by_driver = defaultdict(int)
    km_by_driver = defaultdict(float)

    for d in deliveries:
        deliveries_by_driver[d["driver"]] += 1
        km_by_driver[d["driver"]] += d["km"]

    return total_deliveries, total_km, total_time, deliveries_by_driver, km_by_driver


def save_report(report_text):
    with open("report.txt", mode="w", encoding="utf-8") as file:
        file.write(report_text)


def main():
    deliveries = load_deliveries(FILE_NAME)

    total_deliveries, total_km, total_time, deliveries_by_driver, km_by_driver = create_summary(deliveries)

    report_lines = []
    report_lines.append("DELIVERY REPORT")
    report_lines.append("=" * 30)
    report_lines.append(f"Total deliveries: {total_deliveries}")
    report_lines.append(f"Total kilometers: {total_km:.1f} km")
    report_lines.append(f"Total time: {total_time} minutes")
    report_lines.append("")
    report_lines.append("Per driver summary:")
    report_lines.append("-" * 30)

    for driver in deliveries_by_driver:
        report_lines.append(
            f"{driver}: {deliveries_by_driver[driver]} deliveries | {km_by_driver[driver]:.1f} km"
        )

    report_text = "\n".join(report_lines)

    print(report_text)
    save_report(report_text)

    print("\n✅ Report saved as report.txt")


if __name__ == "__main__":
    main()
