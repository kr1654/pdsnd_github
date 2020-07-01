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
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_city_responses = ['chicago, new york city, washington']
    city = input('Enter city name for analysis\n').lower()
    while city in CITY_DATA:
        print('You selected'+ city +'Please, Select month')
        break

    # get user input for month (all, january, february, ... , june)

    valid_month_responses = ['all','january','february','march','april','may','june']
    month = input('Which month would you like to view data for? Please enter: January, February, March, April, May, June, or All\n').lower()
    while month in valid_month_responses:
        print('You selected'+ month +'Go for the day of week')
        break
    # get user input for day of week (all, monday, tuesday, ... sunday)

    valid_day_responses = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day= input('Which day would you like to view data for? Please enter: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All.\n').lower()
    while day in valid_day_responses:
        print('You selected'+ day +'thanks\n Wait for the data to be loaded ')
        break
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
    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
    # filter by month to create the new dataframe
    df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
         df = df[df['day_of_week']== day.title()]
    return df
    print(df)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] =df['Start Time'].dt.month
    dh['day_of_week'] = df['Start Time'].dt.weekday_name
    # display the most common month
    common_month = df['month'].mode()[0]
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    common_hour= df['hour'].mode()[0]

    print('The most common month is : ' + common_month)
    print('The most common day of week is : ' + common_day)
    print('The most common hour is : ' + common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start= df['Start Station'].mode()[0]

    # display most commonly used end station
    common_end= df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df['comb_station'] = df['Start Station'] + df['End Station']
    frequent_comb = df['comb_station'].mode()[0]
    print('The most popular start station is : ' + common_start)
    print('The most popular end station is : ' + common_end)
    print('The most frequent station trip is : ' + frequent_comb)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = (df['Trip Duration'].sum()) /60

    # display mean travel time
    mean_travel = (df['Trip Duration'].mean())/60
    print('Total travel time: ' + total_travel)
    print('Mean travel time' + mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count= df['User Types'].count_values()

    # Display counts of gender
    try:
        gender_count = df['Gender'].count_values()
    except:
        print('No such data is available. Try another input')

    # Display earliest, most recent, and most common year of birth
    try:
        common_birth = df['Birth Year'].mode()[0]
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
    except:
        print('No such data available. Try another input')
        print('Total user types: ' + user_count)
        print('Total gender count: '+ gender_count)
        print('Common year of birth: ' + common_birth)
        print('Earliest year of birth: ' + earliest_birth)
        print('Most recent year of birth: ' + recent_birth)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
    while True:
        proceed = input('\nDo you want to view data? Please enter yes or no, \n')
        if proceed.lower() == 'yes' :
            df += df[df.iloc[5, :]]
        continue
        if proceed.lower() == 'no' :
            break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
