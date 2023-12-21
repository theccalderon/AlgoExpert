# This is a sample Python script.
import math


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def trunc(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d + '0' * n)[:n]])

def get_mean(input_list):
    mean = 0
    for i in input_list:
        mean += i
    mean = mean / len(input_list)
    return round(mean, 4)


def get_median(input_list):
    input_list = sorted(input_list)
    if len(input_list) % 2 == 0:
        return round((input_list[int(len(input_list) / 2)] + input_list[int(len(input_list) / 2) - 1]) / 2, 4)
    return round(input_list[int(len(input_list) / 2)], 4)


def get_mode(input_list):
    input_list = sorted(input_list)
    final_mode = input_list[0]
    max_rep_count = 1
    current_rep_count = 1
    for i in range(1, len(input_list)):
        if input_list[i] == input_list[i - 1]:
            current_rep_count += 1
        else:
            if current_rep_count > max_rep_count:
                max_rep_count = current_rep_count
                final_mode = input_list[i - 1]
            current_rep_count = 1
    return round(final_mode,4)

def get_mode_elegant(input_list):
    sorted_input = sorted(input_list)
    number_counts = {x: sorted_input.count(x) for x in set(sorted_input)}
    mode = max(number_counts.keys(), key= lambda unique_number: number_counts[unique_number])
    return mode

def get_sample_variance(input_list):
    # https://www.cuemath.com/sample-variance-formula/
    mean = get_mean(input_list)
    input_list = [n - mean for n in input_list]
    input_list = [n * n for n in input_list]
    sqr_diff = sum(input_list)
    return round(sqr_diff/(len(input_list)-1), 4)



def get_sample_standard_deviation(input_list):
    # https://www.thoughtco.com/calculate-a-sample-standard-deviation-3126345
    sample_variance = get_sample_variance(input_list)
    return round(math.sqrt(sample_variance), 4)


def get_mean_confidence_interval(input_list):
    mean = get_mean(input_list)
    sample_size = len(input_list)
    sample_deviation = get_sample_standard_deviation(input_list)
    return [trunc(mean - 1.96 * (sample_deviation/sample_size**0.5), 4),
            round(mean + 1.96 * (sample_deviation/math.sqrt(sample_size)), 4)]

def get_statistics(input_list):
    mean = get_mean(input_list)
    median = get_median(input_list)
    mode = get_mode_elegant(input_list)
    sample_variance = get_sample_variance(input_list)
    sample_standard_deviation = get_sample_standard_deviation(input_list)
    mean_confidence_interval = get_mean_confidence_interval(input_list)

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_statistics([19, 14, 0, 8, 10, 13, 1, 5, 1, 9, 14, 3, 10, 4, 0, 2, 20, 3, 8, 19, 14, 11, 4, 10, 18, 19, 6, 16, 9, 2, 7, 2, 1, 18, 0, 3, 1, 6, 20, 15, 14, 10, 5]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
