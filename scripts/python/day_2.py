with open('../../input/day_2_data.txt', 'r') as file:
    data = file.readlines()

def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return all(1 <= abs(diff) <= 3 for diff in differences) and (all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences))

def can_be_safe_with_removal(report):
    return any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))

def process_reports(reports):
    safe = 0
    safe_with_dampener = 0

    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe(levels):
            safe += 1
            safe_with_dampener += 1
        elif can_be_safe_with_removal(levels):
            safe_with_dampener += 1

    return safe, safe_with_dampener

safe_reports, safe_with_dampener_reports = process_reports(data)

print(f"Safe reports: {safe_reports}")
print(f"Safe reports with Problem Dampener: {safe_with_dampener_reports}")