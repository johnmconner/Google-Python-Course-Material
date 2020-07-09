import re
def show_time_of_pid(line):
  pattern = r"([\D]{3} [\d]{1,2} [\d]{2}:[\d]{2}:[\d]{2}) [\D]+(\[[\d]+\])"
  result = re.search(pattern, line)
  return result.group(1) + ' pid:' + result.group(2)

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440