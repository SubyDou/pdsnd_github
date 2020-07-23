import time
import pandas as pd


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
    
    cities=['chicago','new york city','washington']
    
    while True:
        user_city=input('Would you like to see data for Chicago, New York City, or Washington?')
        user_city=user_city.lower()
        if user_city in cities:
            city=user_city
            break
        else:
            print('Opps!Somthing is wrong.Please choose only one city from Chicago, New York City, or Washington.')
       

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    while True:
        user_month=input('Which month do you like to explore: January, February, March, April, May, June, or All?')
        user_month=user_month.title()
        if user_month in months:
            month=user_month
            break
        elif user_month == 'All':
            month='All'
            break
        else:
            print('Opps!Somthing is wrong.Please choose a month from January, February, March, April, May,June or All.')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    while True:
        user_day=input('Which day do you like to explore: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday,or All?')
        user_day=user_day.title()
        if  user_day in days:
            day=user_day
            break
        elif user_day == 'All':
            day='All'
            break
        else:
            print('Opps!Somthing is wrong.Please choose a day from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday,or All.')

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
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all'and month != 'All' :
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower())+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] ==month]

    # filter by day of week if applicable
    if day != 'all'and day != 'All':
    
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most common month is {}'.format(months[df['month'].mode()[0]-1]))


    # TO DO: display the most common day of week
    print('The most common day of week is {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is {}'.format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print('The most common end station is {}'.format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    df['station_combination'] = 'Start at: '+df['Start Station']+' End at: '+ df['End Station']
    print('The most frequent combination of start station and end station trip is {}'.format(df['station_combination'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is {} seconds'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The average travel time is {} seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    for i in user_types.index:
        print('The count of user type {} is {}'.format(i, user_types[i]))

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    ## For Chicago and New york city, display counts of gender . For washington, I display no gender or birth year information
    if city in ['chicago', 'new york city']:
        gender_cou = df['Gender'].value_counts()
        for i in gender_cou.index:
            print('The count of gender {} is {}'.format(i, gender_cou[i]))
        print('The earliest year of birth is {}'.format(df['Birth Year'].min()))
        print('The most recent year of birth is {}'.format(df['Birth Year'].max()))
        print('The most common year of birth is {}'.format(df['Birth Year'].mode()[0]))
    else:
        print('No gender or birth year information for Washington.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        
        
        ## if the user input is yes, then print data
        ## it shows the original data 10 entries every time until user input no.
        data = input('Would you like to see your original data \n')
        
        if data.lower()=='yes':
            df.drop(columns = ['station_combination', 'month', 'day_of_week','hour'], inplace = True)
            i = 10
            print(df.iloc[i-10:i])
            i+=10
            while i<=len(df):
                more_data = input('Would you like to see more data?\n')
                if more_data.lower()!='no':
                    print(df.iloc[i-10:i])
                    i+=10
                else:
                    break
            ## print the last piece of data that is not part of the 10 segment
            print(df.iloc[i-10:])

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
 	main()
   
