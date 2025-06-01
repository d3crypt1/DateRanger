

from datetime import date, timedelta

def date_range(start_date, end_date):
  """Generates a list of dates between two dates (inclusive).

  Args:
    start_date: The start date as a date object.
    end_date: The end date as a date object.

  Returns:
    A list of date objects.
  """
  dates = []
  current_date = start_date
  while current_date <= end_date:
    dates.append(current_date)
    current_date += timedelta(days=1)
  return dates

# Example usage:
start_date = date(2024, 1, 1)
end_date = date(2024, 1, 10)
date_list = date_range(start_date, end_date)
for date_item in date_list:
  print(date_item.strftime("%Y-%m-%d"))