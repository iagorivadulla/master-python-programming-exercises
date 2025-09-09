# Complete the function to return how many hours and minutes are displayed on the 24h digital clock
def digital_clock(n):
  hour = (n // 60) % 24
  minutes = n % 60
  return (hour, minutes)

# Invoke the function with any integer (minutes after midnight)
print(digital_clock(150))
