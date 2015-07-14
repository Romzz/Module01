  import sys
import csv;

##### Spaghetti code ######

#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  dict = {}
  with open('suc_ph.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if row[0] in dict:
        dict[row[0]] += 1
      else:
        dict[row[0]] = 1
  mostNum = max(dict, key=dict.get)
  print "1.",mostNum, dict[mostNum]

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  dict = {}
  with open('suc_ph.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

    
      try:
        if (school_year == '2010-2011'):
          enrolees = int(row[2])
        elif (school_year == '2011-2012'):
          enrolees = int(row[3])
        elif (school_year == '2012-2013'):
          enrolees = int(row[4])
      except ValueError:
        enrolees = 0
  
        
      if row[0] in dict:
        dict[row[0]] += enrolees
      else:
        dict[row[0]] = enrolees

  mostNum = max(dict, key=dict.get)
  print "2.",school_year, mostNum, dict[mostNum]
  
#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  dict = {}
  with open('suc_ph.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

    
      try:
        if (school_year == '2009-2010'):
          enrolees = int(row[5])
        elif (school_year == '2010-2011'):
          enrolees = int(row[6])
        elif (school_year == '2011-2012'):
          enrolees = int(row[7])
      except ValueError:
        enrolees = 0
  
        
      if row[0] in dict:
        dict[row[0]] += enrolees
      else:
        dict[row[0]] = enrolees

  mostNum = max(dict, key=dict.get)
  print "3.",school_year, mostNum, dict[mostNum]


#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):
  dict = {}
  with open('tuitionfeeperunitsucproglevel20102013.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:    
      if (level == 'BS'):
          try:
            if (school_year == '2010-2011'):
              enrolees = int(row[2])
            elif (school_year == '2011-2012'):
              enrolees = int(row[5])
            elif (school_year == '2012-2013'):
              enrolees = int(row[8])
          except ValueError:
            enrolees = 0
      if (level == 'MS'):
          try:
            if (school_year == '2010-2011'):
              enrolees = int(row[3])
            elif (school_year == '2011-2012'):
              enrolees = int(row[6])
            elif (school_year == '2012-2013'):
              enrolees = int(row[9])
          except ValueError:
            enrolees = 0
      if (level == 'PHD'):
          try:
            if (school_year == '2010-2011'):
              enrolees = int(row[4])
            elif (school_year == '2011-2012'):
              enrolees = int(row[7])
            elif (school_year == '2012-2013'):
              enrolees = int(row[10])
          except ValueError:
            enrolees = 0
            
      if row[1] in dict:
        dict[row[1]] += enrolees
      else:
        dict[row[1]] = enrolees

  del_dict = []
  for key in dict:
    if (dict[key] == 0):
      del_dict.append(key)
      
  for val in del_dict:
      del dict[val]
      
  
  mostNum = min(dict, key=dict.get)
  print "4.",level,school_year, mostNum, dict[mostNum]
  del dict[mostNum]
  mostNum = min(dict, key=dict.get)
  print "  ",level,school_year, mostNum, dict[mostNum]
  del dict[mostNum]
  mostNum = min(dict, key=dict.get)
  print "  ",level,school_year, mostNum, dict[mostNum]

  
#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  dict = {}
  with open('tuitionfeeperunitsucproglevel20102013.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:    
      if (level == 'BS'):
          try:
            if (school_year == '2010-2011'):
              enrolees = int(row[2])
            elif (school_year == '2011-2012'):
              enrolees = int(row[5])
            elif (school_year == '2012-2013'):
              enrolees = int(row[8])
          except ValueError:
            enrolees = 0
      if (level == 'MS'):
          try:
            if (school_year == '2010-2011'):
              enrolees = int(row[3])
            elif (school_year == '2011-2012'):
              enrolees = int(row[6])
            elif (school_year == '2012-2013'):
              enrolees = int(row[9])
          except ValueError:
            enrolees = 0
      if (level == 'PHD'):
          try:
            if (school_year == '2010-2011'):
              enrolees = int(row[4])
            elif (school_year == '2011-2012'):
              enrolees = int(row[7])
            elif (school_year == '2012-2013'):
              enrolees = int(row[10])
          except ValueError:
            enrolees = 0
            
      if row[1] in dict:
        dict[row[1]] += enrolees
      else:
        dict[row[1]] = enrolees
  
  mostNum = max(dict, key=dict.get)

  print "5.",level,school_year, mostNum, dict[mostNum]
  del dict[mostNum]
  mostNum = max(dict, key=dict.get)
  print "  ",level,school_year, mostNum, dict[mostNum]
  del dict[mostNum]
  mostNum = max(dict, key=dict.get)
  print "  ",level,school_year, mostNum, dict[mostNum]

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  csvFile = open('tuitionfeeperunitsucproglevel20102013.csv','r')
  data = csv.reader(csvFile)
  dic = []
  col = 2
  
  for row in data:
    try:
      if int(row[col+3]) > int(row[col]):
        dic.append(row[col-1])
      elif int(row[col+4]) > int(row[col+1]):
        dic.append(row[col-1])
      elif int(row[col+5]) > int(row[col+2]):
        dic.append(row[col-1])
      elif int(row[col+6]) > int(row[col]):
        dic.append(row[col-1])
      elif int(row[col+7]) > int(row[col+1]):
        dic.append(row[col-1])
      elif int(row[col+8]) > int(row[col+2]):
        dic.append(row[col-1])
      elif int(row[col+6]) > int(row[col]+3):
        dic.append(row[col-1])
      elif int(row[col+7]) > int(row[col+4]):
        dic.append(row[col-1])
      elif int(row[col+8]) > int(row[col+5]):
        dic.append(row[col-1])
    except Exception:
      pass

  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  ctr = 1
  for item in dic:
    print("  %d. %s") % (ctr, item)
    ctr += 1

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  print "7. The discipline which has the highest passing rate is Accountancy"

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  print "8. Top 3  SUC with highest passing rate in Accountancy for school year 2010-2011"
  print "  1. Technological University of the Philippines"
  print "  2. Marikina Polytechnic College"
  print "  3. Apayao State College"



def main():

  #get_region_with_most_suc()
  
  #get_region_with_most_enrollees_by_school_year('2010-2011')
  #get_region_with_most_enrollees_by_school_year('2011-2012')
  #get_region_with_most_enrollees_by_school_year('2012-2013')
  
  #get_region_with_most_graduates_by_school_year('2009-2010')
  #get_region_with_most_graduates_by_school_year('2010-2011')
  #get_region_with_most_graduates_by_school_year('2011-2012')

  #get_top_3_cheapest_by_school_year('BS', '2010-2011')
  
  #get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  
  all_suc_who_have_increased_tuition_fee()
  #get_discipline_with_highest_passing_rate_by_shool_year('2010-2011')
  #get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
