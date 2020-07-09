import re
import csv

def check_and_replace_domain(address, new_domain, old_domain):
  """Returns address with new domain if the pattern matches; otherwise, it returns the original domain"""
  pattern = r"^([\w\.\-\+]+@)([\w]+.[\D]+$)"
  result = re.search(pattern, address)
  if result.group(2) == old_domain:
      address = result.group(1) + new_domain
      return address
  return address


def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  list = []
  counter = 0
  csv_file_name = "list.csv"
  csv_file_location = "C:\\Users\\John\\Desktop\\python\\random\\" + csv_file_name
  new_file_location = "C:\\Users\\John\\Desktop\\python\\random\\new_list.csv"
  old_domain, new_domain = "abc.edu", "xyz.edu"
  field_names = ['Full Name', ' Email Address']

  csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
  reader = csv.DictReader(open(csv_file_location, "r"), dialect="empDialect")
  writer = csv.writer(open(new_file_location, 'w'), lineterminator='\n')
  for row in reader:
      if counter == 0:
        writer.writerow(field_names)
        counter += 1
      else:
        list.append(row['Full Name']) 
        list.append(' ' + check_and_replace_domain(row['Email Address'], new_domain, old_domain))
        writer.writerow(list)
        list = []

main()