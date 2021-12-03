try:
while True:
data = raw_input('prompt:')
print 'READ:', data
except EOFError as e:
print e