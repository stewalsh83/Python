import time
# from sys import stdout

i = 0

while i <= 50000:
    print(f'\r{i}', end='', flush=True)
    # time.sleep(1)
    i += 1
print("\n")

s = 'Hello World!'
for i in range(1, len(s) + 1):
    print(f'\r{s[:i]}', end='', flush=True)
    time.sleep(1)

# stdout.write("\r Time %s" % t)
# stdout.flush()
