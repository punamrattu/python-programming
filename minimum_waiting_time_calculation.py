"""

In a hospital's A&E department, patients with varying medical needs await their turn to be seen by the one doctor available. Each patient's session duration depends on their medical issue.

Given an array of positive integers representing the time each patient's session takes, create a function to determine the minimum total waiting time for all patients. The waiting time for each patient is the cumulative duration of previous patients' sessions before they are seen by the doctor.

For example, if the session durations in minutes are [1, 4, 5], the optimal arragment will result in the following waiting times:
- The first patient with duration 5 min would be attended to immediately, so their waiting time would be 0
- The second patient of duration 1 min would have to wait 5 min (the duration of the first patient) to be attended by medical staff.
- The last patient would have to wait the duration of the first two patient before they get to see a doctor. 
Total waiting time: (0) + (5) + (5 +1) = 11 minutes.

"""


# List containing patients' appointment durations
patients = [ 3, 2, 1, 2, 6]

def min_waiting_time(patients):
    """
    Calculates the minimum amount of total waiting time for patients.

    Args:
        patients (list): A list of positive integers representing the time it takes to attend each patient.

    Returns:
        int: The minimum total waiting time for all patients.
    """
    patients.sort()  # Sort the list of patients in ascending order of their session durations
    total_waiting_time = 0  # Initialize the total waiting time

    for i in range(len(patients)):
        # Calculate the waiting time for each patient by summing the durations of previous patients
        waiting_time = sum(patients[:i])
        total_waiting_time += waiting_time  # Update the total waiting time

    return total_waiting_time  # Return the minimum total waiting time


print(min_waiting_time(patients))
