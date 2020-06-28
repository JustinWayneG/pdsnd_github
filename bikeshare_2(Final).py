import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the monh to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to look at data for Chicago, New York City, or Washington?: ").lower()
        cities = ['chicago', 'new york city', 'washington']
        if city in cities:
            break
        else:
            print("Invalid input - please enter Chicago, New York City, or Washington.")

    while True:
        time_filter = input("Would you like to filter the data by month, day, or not at all? Type 'none' for no time filter: ").lower()
        time_filters = ['month', 'day', 'none']
        month='all'
        day='all'
        if time_filter in time_filters:
            break
        else:
            print("Invalid input - please enter month, day, or none.")

    # TO DO: get user input for month (all, january, february, ... , june)
    if time_filter == 'month':
        while True:
            month = input("Which month would you like to filter by? Please type one of the following - January, February, March, April, May, or June: ").lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month in months:
                break
            else:
                print("Invalid input - please enter January, February, March, April, May, or June.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif time_filter == 'day':
        while True:
            day = input("Which day of the week would you like to filter by? (e.g., Sunday): ").lower()
            days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
            if day in days:
                break
            else:
                print("Invalid input - please enter a day of the week (e.g., Sunday, Monday, etc.)")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print("The most common month is:", most_common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of the week is:", most_common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common start hour is:", most_common_hour)

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print("The most commonly used start station is:", most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print("The most comonly used end station is:", most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Start to End Station'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combination = df['Combined Start to End Station'].mode()[0]
    print("The most frequent combination of start station and end station trip is:", most_common_combination)

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is", mean_travel)

    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("The following is a count of user types:\n", count_user_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        print("The oldest user was born in:", earliest_birth)
        most_recent_birth = df['Birth Year'].max()
        print("The youngest user was born in:", most_recent_birth)
        most_common_birth = df['Birth Year'].mode()[0]
        print("The most common year of birth is:", most_common_birth)
    else:
        print("There is no birth year information for this city.")

    print('-'*40)

def raw_data(df):
    """Asks user if they would like to see raw data.

    Returns:
        5 rows of raw data and asks the user if they would like to see the next 5 rows of data.
    """
    raw_data = np.array([0, 1, 2, 3, 4])
    while True:
        answer = input("Would you want to see the first 5 rows of raw data? Yes or No?").lower()
        if answer == 'yes':
            print(df.iloc[raw_data])
            while True:
                next_answer = input("Would you like to see 5 more rows of raw data? Yes or No?").lower()
                raw_data += 5
                if next_answer == 'yes':
                    print(df.iloc[raw_data])
                if next_answer == 'no':
                    break
                if next_answer not in ['yes', 'no']:
                    print("Invalid input - please enter yes or no.")
        if answer or next_answer == 'no':
            break
        if answer not in ['yes', 'no']:
            print("Invalid input - please enter yes or no.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
