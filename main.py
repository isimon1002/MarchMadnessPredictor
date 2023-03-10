import csv


def algorithm(q1_wins, q1_losses, q2_wins, q2_losses, q3_wins, q3_losses, q4_wins, q4_losses):
    total_q1_games = q1_wins + q1_losses
    total_q2_games = q2_wins + q2_losses
    total_q3_games = q3_wins + q3_losses
    total_q4_games = q4_wins + q4_losses

    q1_winning_percentage = q1_wins / total_q1_games if total_q1_games > 0 else 0
    q2_winning_percentage = q2_wins / total_q2_games if total_q2_games > 0 else 0
    q3_winning_percentage = q3_wins / total_q3_games if total_q3_games > 0 else 0
    q4_winning_percentage = q4_wins / total_q4_games if total_q4_games > 0 else 0

    return ((q1_winning_percentage * q1_wins) * 4) + ((q2_winning_percentage * q2_wins) * 3) + (
                (q3_winning_percentage * q3_wins) * 2) + (q4_winning_percentage * q4_wins)


def convert_dict_to_list_of_dicts(dict):
    list_from_dictionary = []
    for k, v in dict.items():
        list_from_dictionary .append({"Team": k, "Rating": v})
    return list_from_dictionary


resultsList = []
results = {}
with open('TeamQuadTracker20230310.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for stats in reader:
        team = stats["Team"]
        results[team] = algorithm(int(stats["Q1_W"]), int(stats["Q1_L"]), int(stats["Q2_W"]), int(stats["Q2_L"]),
                                  int(stats["Q3_W"]), int(stats["Q3_L"]), int(stats["Q4_W"]), int(stats["Q4_L"]))

resultsList = convert_dict_to_list_of_dicts(results)


with open('NCAA_predictions.csv', 'w') as file:
    writer = csv.DictWriter(file, ('Team', 'Rating'))
    writer.writeheader()
    writer.writerows(resultsList)

