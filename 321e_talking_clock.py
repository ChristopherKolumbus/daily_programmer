import argparse


def convert_time(input_time):
    numbers = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    tens = ['twenty', 'thirty', 'forty', 'fifty']
    hours_input, minutes_input = map(int, input_time.split(':'))
    # Convert hours to string:
    if hours_input == 0:
        hours_output = numbers[11]
    elif hours_input > 12:
        hours_output = numbers[hours_input - 13]
    else:
        hours_output = numbers[hours_input - 1]
    # Insert "oh" if necessary:
    if 0 < minutes_input < 10:
        oh = 'oh '
    else:
        oh = ''
    # Convert minutes to string:
    if minutes_input == 0:
        minutes_output = ''
    elif 0 < minutes_input < 20:
        minutes_output = numbers[minutes_input - 1] + ' '
    else:
        minutes_output = tens[int(minutes_input / 10) - 2]
        if minutes_input % 10 != 0:
            minutes_output += ' ' + numbers[minutes_input % 10 - 1]
        minutes_output += ' '
    # Add "am" or "pm":
    if hours_input < 12:
        am_or_pm = 'am'
    else:
        am_or_pm = 'pm'
    # Put it all together and return it:
    output_time = f'It\'s {hours_output} {oh}{minutes_output}{am_or_pm}'
    return output_time


def test():
    for hour in range(24):
        input_hour = str(hour)
        if len(input_hour) < 2:
            input_hour = '0' + input_hour
        for minute in range(60):
            input_minute = str(minute)
            if len(input_minute) < 2:
                input_minute = '0' + input_minute
            input_time = f'{input_hour}:{input_minute}'
            output_time = convert_time(input_time)
            return output_time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_time', type=str, help='Time like "12:47"')
    args = parser.parse_args()
    input_time = args.input_time
    output_time = convert_time(input_time)
    print(output_time)


if __name__ == '__main__':
    main()
