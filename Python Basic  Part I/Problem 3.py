from datetime import datetime

current = datetime.now()
print('Current date and time:')
# strftime use to format date to string
print(current.strftime('%Y-%m-%d %H:%M:%S'))
